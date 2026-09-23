#!/usr/bin/env python3
"""Secret-safe heuristic review of client-commercial artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".csv"}
COMMERCIAL_TERMS = {
    "client", "lead", "opportunity", "pipeline", "crm", "outreach", "proposal",
    "quote", "estimate", "pricing", "sow", "scope", "agreement", "contract",
    "meeting", "call", "follow-up", "followup", "handoff", "closeout", "invoice",
    "клиент", "лид", "сделк", "воронк", "предлож", "оценк", "смет", "договор",
}
SKIP_DIRS = {
    ".git", ".next", ".idea", ".vscode", "node_modules", "bin", "obj", "dist",
    "build", "coverage", "artifacts",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".age"}


@dataclass(frozen=True)
class Finding:
    id: str
    severity: str
    message: str
    file: str | None = None


def allowed(path: Path) -> bool:
    """Filter paths before reading; never inspect environment or credential files."""
    name = path.name.lower()
    parts = {part.lower() for part in path.parts}
    if parts & SKIP_DIRS:
        return False
    if name.startswith(".env") or name.startswith("appsettings"):
        return False
    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        return False
    if name.endswith((".enc.json", ".enc.yaml", ".enc.yml")):
        return False
    if any(term in name for term in (
        "secret", "credential", "service-account", "service_account", "identity",
        "keychain", "vault",
    )):
        return False
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return False
    stem = path.stem.lower()
    return any(term in stem for term in COMMERCIAL_TERMS)


def collect(target: Path) -> list[tuple[Path, str]]:
    candidates = [target] if target.is_file() else target.rglob("*")
    result: list[tuple[Path, str]] = []
    for path in candidates:
        if not path.is_file() or not allowed(path):
            continue
        try:
            if path.stat().st_size > 2_000_000:
                continue
            result.append((path, path.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            continue
    return result


def contains(text: str, pattern: str) -> bool:
    return re.search(pattern, text, re.IGNORECASE | re.MULTILINE) is not None


def audit(target: Path, files: list[tuple[Path, str]]) -> list[Finding]:
    root = target if target.is_dir() else target.parent
    findings: list[Finding] = []

    def add(finding_id: str, severity: str, message: str, path: Path | None = None) -> None:
        location = str(path.relative_to(root)) if path else None
        findings.append(Finding(finding_id, severity, message, location))

    if not files:
        add(
            "no-commercial-artifacts",
            "info",
            "No explicitly named client-commercial artifacts were found; unrelated files were not read.",
        )
        return findings

    for path, text in files:
        name = path.name.lower()

        if contains(text, r"\b(TODO|TBD|FIXME|fill this|placeholder)\b"):
            add("unresolved-placeholder", "high", "Unresolved placeholder language remains.", path)

        if contains(text, r"\b(password|passwd|api.?key|private.?key|access.?token|refresh.?token|recovery.?code|cvv|cvc)\b"):
            add(
                "possible-sensitive-field",
                "critical",
                "Potential secret or highly sensitive field name found; remove values and keep credentials outside commercial artifacts.",
                path,
            )

        if contains(text, r"\b(guarantee[ds]?|guaranteed|100%\s*(secure|success)|гарантир\w*\s+(доход|результат|безопас))\b"):
            add("absolute-claim", "high", "Potentially uncontrollable or absolute outcome claim found.", path)

        if any(term in name for term in ("estimate", "pricing", "quote", "оценк", "смет")):
            checks = (
                ("estimate-range-missing", r"range|optimistic|most likely|pessimistic|диапазон|оптимист|вероятн|пессимист", "An effort or scenario range was not found."),
                ("estimate-assumptions-missing", r"assumption|допущ|предполож", "Estimate assumptions were not found."),
                ("estimate-exclusions-missing", r"out.?of.?scope|exclusion|не входит|исключ", "Estimate exclusions were not found."),
                ("estimate-dependencies-missing", r"dependenc|client input|зависим|со стороны клиента", "Dependencies or client inputs were not found."),
                ("estimate-confidence-missing", r"confidence|certainty|уверенн|неопредел", "Confidence or uncertainty was not found."),
                ("calendar-separation-missing", r"calendar|elapsed|календар|срок", "Calendar duration was not distinguished from effort."),
                ("estimate-change-trigger-missing", r"re.?estimate|change request|change trigger|переоцен|изменени.{0,12}(срок|цен|оцен)", "A re-estimation or change trigger was not found."),
            )
            for finding_id, pattern, message in checks:
                if not contains(text, pattern):
                    add(finding_id, "high" if "range" in finding_id else "medium", message, path)

        if any(term in name for term in ("proposal", "sow", "предлож")):
            checks = (
                ("proposal-deliverables-missing", r"deliverable|результат|поставк", "Observable deliverables were not found."),
                ("proposal-exclusions-missing", r"out.?of.?scope|exclusion|не входит|исключ", "Explicit exclusions were not found."),
                ("proposal-acceptance-missing", r"acceptance|accept|приемк|приёмк", "Acceptance mechanism was not found."),
                ("proposal-client-inputs-missing", r"client (input|responsib|provide)|заказчик.{0,20}(предостав|ответ)", "Client responsibilities or inputs were not found."),
                ("proposal-change-missing", r"change request|scope change|изменени.{0,10}(объем|объём|состав)", "Scope-change handling was not found."),
                ("proposal-validity-missing", r"valid until|validity|действител.{0,12}(до|дней)", "Proposal validity or review trigger was not found."),
            )
            for finding_id, pattern, message in checks:
                if not contains(text, pattern):
                    add(finding_id, "high" if "acceptance" in finding_id else "medium", message, path)

        if any(term in name for term in ("agreement", "contract", "договор")):
            checks = (
                ("agreement-payment-missing", r"payment|invoice|оплат|счет|счёт", "Payment mechanism was not found."),
                ("agreement-acceptance-missing", r"acceptance|accept|приемк|приёмк", "Acceptance mechanism was not found."),
                ("agreement-change-missing", r"change|amend|изменен", "Change/amendment handling was not found."),
                ("agreement-ip-missing", r"intellectual property|copyright|\bIP\b|интеллектуаль|авторск", "IP and reusable-material treatment was not found."),
                ("agreement-exit-missing", r"termination|suspension|расторж|приостанов", "Suspension or termination handling was not found."),
                ("agreement-support-missing", r"warranty|support|maintenance|гаранти|поддерж|сопровожд", "Warranty/support boundary was not found."),
            )
            for finding_id, pattern, message in checks:
                if not contains(text, pattern):
                    add(finding_id, "high" if "payment" in finding_id or "acceptance" in finding_id else "medium", message, path)

        if any(term in name for term in ("crm", "pipeline", "lead", "opportunity", "воронк", "лид", "сделк")):
            for finding_id, pattern, message in (
                ("crm-stage-missing", r"stage|стади|этап", "Pipeline stage was not found."),
                ("crm-next-action-missing", r"next action|next step|следующ", "A concrete next action was not found."),
                ("crm-owner-missing", r"owner|ответствен|владелец", "Next-action owner was not found."),
                ("crm-date-missing", r"date|deadline|due|дата|срок", "A next-action date was not found."),
                ("crm-source-missing", r"source|источник|канал", "Lead source/provenance was not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "medium", message, path)

        if any(term in name for term in ("meeting", "call", "follow-up", "followup", "встреч", "звон")):
            for finding_id, pattern, message in (
                ("communication-decisions-missing", r"decision|решен", "Decisions were not found."),
                ("communication-actions-missing", r"action|next step|задач|следующ", "Actions or next steps were not found."),
                ("communication-owners-missing", r"owner|ответствен|владелец", "Action owners were not found."),
                ("communication-dates-missing", r"date|deadline|due|дата|срок", "Action dates were not found."),
                ("communication-unknowns-missing", r"unknown|open question|неизвест|открыт.{0,8}вопрос", "Open questions or unknowns were not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "medium", message, path)

    return findings


def self_test() -> int:
    assert not allowed(Path("/tmp/.env"))
    assert not allowed(Path("/tmp/.env.example"))
    assert not allowed(Path("/tmp/client-secrets.md"))
    assert not allowed(Path("/tmp/appsettings.Production.json"))
    assert not allowed(Path("/tmp/proposal.enc.yaml"))
    assert allowed(Path("/tmp/client-proposal.md"))
    assert allowed(Path("/tmp/project-estimate.json"))

    sample = [(
        Path("/tmp/client-proposal.md"),
        "# Proposal\n## Deliverables\nWorking site\nTODO\npassword: [redacted]",
    )]
    finding_ids = {item.id for item in audit(Path("/tmp"), sample)}
    assert "unresolved-placeholder" in finding_ids
    assert "possible-sensitive-field" in finding_ids
    assert "proposal-acceptance-missing" in finding_ids

    complete = [(
        Path("/tmp/client-proposal.md"),
        """
# Proposal
## Deliverables
Working booking flow.
## Exclusions
Native applications are out of scope.
## Assumptions and client responsibilities
The client provides approved content.
## Acceptance
The named approver verifies the agreed scenarios.
## Scope changes
A written change request updates scope, price, and calendar time.
## Validity
Valid until 2030-01-31.
""",
    )]
    assert not audit(Path("/tmp"), complete)
    print("self-test: ok")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.path is None or not args.path.exists():
        parser.error("path must be an existing commercial artifact or directory")

    target = args.path.resolve()
    findings = audit(target, collect(target))
    if args.format == "json":
        print(json.dumps(
            {"status": "review" if findings else "pass", "findings": [asdict(item) for item in findings]},
            ensure_ascii=False,
            indent=2,
        ))
    elif not findings:
        print("PASS: no heuristic commercial-artifact blockers found. This is not legal advice or deal validation.")
    else:
        print(f"REVIEW: {len(findings)} finding(s). No document excerpts or sensitive values are shown.")
        for item in findings:
            location = f" ({item.file})" if item.file else ""
            print(f"- [{item.severity}] {item.id}{location}: {item.message}")
    return 1 if any(item.severity in {"high", "critical"} for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())

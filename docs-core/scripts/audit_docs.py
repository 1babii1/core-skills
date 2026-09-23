#!/usr/bin/env python3
"""Secret-safe heuristic review of project documentation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".mdx", ".rst", ".adoc", ".txt", ".json", ".yaml", ".yml"}
DOC_NAMES = {
    "readme", "contributing", "changelog", "architecture", "onboarding", "handoff",
    "runbook", "playbook", "operations", "api", "openapi", "swagger", "adr",
    "troubleshooting", "quickstart", "quick-start", "getting-started", "release-notes",
}
DOC_DIRS = {"docs", "doc", "documentation", "wiki", "runbooks", "adr", "adrs", "handbook"}
SKIP_DIRS = {
    ".git", ".next", ".idea", ".vscode", "node_modules", "bin", "obj", "dist",
    "build", "coverage", "artifacts", "vendor", "generated",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".age"}


@dataclass(frozen=True)
class Finding:
    id: str
    severity: str
    message: str
    file: str | None = None


def allowed(path: Path) -> bool:
    """Filter before reading; never inspect environment, vault, or credential files."""
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
    suffix = path.suffix.lower()
    if suffix not in ALLOWED_SUFFIXES:
        return False
    stem = path.stem.lower()
    doc_named = stem in DOC_NAMES or any(
        stem.startswith(f"{prefix}-") or stem.endswith(f"-{prefix}") for prefix in DOC_NAMES
    )
    if suffix in {".json", ".yaml", ".yml"}:
        return doc_named
    return bool(parts & DOC_DIRS) or doc_named


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


def local_markdown_links(path: Path, text: str) -> list[str]:
    links: list[str] = []
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        raw = target.strip().split(maxsplit=1)[0].strip("<>")
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
            continue
        links.append(raw.split("#", 1)[0])
    return links


def audit(target: Path, files: list[tuple[Path, str]]) -> list[Finding]:
    root = target if target.is_dir() else target.parent
    findings: list[Finding] = []

    def add(finding_id: str, severity: str, message: str, path: Path | None = None) -> None:
        location = str(path.relative_to(root)) if path else None
        findings.append(Finding(finding_id, severity, message, location))

    if not files:
        add(
            "no-documentation-artifacts",
            "info",
            "No explicitly named documentation artifacts were found; unrelated files were not read.",
        )
        return findings

    for path, text in files:
        stem = path.stem.lower()

        if contains(text, r"\b(TODO|TBD|FIXME|fill this|placeholder|lorem ipsum)\b"):
            add("unresolved-placeholder", "high", "Unresolved placeholder language remains.", path)

        if contains(
            text,
            r"\b(password|passwd|api.?key|private.?key|access.?token|refresh.?token|recovery.?code|client.?secret)\b\s*[:=]\s*[\"']?[A-Za-z0-9+/_.-]{12,}",
        ):
            add(
                "possible-secret-value",
                "critical",
                "A potential secret assignment was found; use a visibly non-secret placeholder and safe external transfer.",
                path,
            )

        for link in local_markdown_links(path, text):
            candidate = (path.parent / link).resolve()
            if not candidate.exists():
                add("broken-local-link", "high", "A local documentation link target does not exist.", path)

        if stem == "readme":
            for finding_id, pattern, message in (
                ("readme-purpose-missing", r"purpose|overview|about|what .{0,20}(is|does)|назнач|о проекте|что это", "Project purpose or overview was not found."),
                ("readme-start-missing", r"quick.?start|getting.?started|install|setup|запуск|установ", "A setup or quick-start path was not found."),
                ("readme-verify-missing", r"verify|expected|health|test|провер|ожида", "An observable verification step was not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "high" if "start" in finding_id else "medium", message, path)

        if "onboarding" in stem or "getting-started" in stem or "quickstart" in stem:
            for finding_id, pattern, message in (
                ("onboarding-audience-missing", r"audience|for .{0,20}(developer|maintainer|operator)|для кого|аудитор", "The onboarding audience was not found."),
                ("onboarding-prerequisites-missing", r"prerequisite|requirements|требован|предвар", "Prerequisites were not found."),
                ("onboarding-success-missing", r"expected|verify|first .{0,12}(success|task|change)|ожида|провер|перв", "A first-success outcome or verification was not found."),
                ("onboarding-troubleshooting-missing", r"troubleshoot|common (issue|error)|ошиб|неполад", "Troubleshooting guidance was not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "medium", message, path)

        if "runbook" in stem or "playbook" in stem or stem == "operations":
            checks = (
                ("runbook-owner-missing", r"owner|владелец|ответствен", "Runbook owner was not found."),
                ("runbook-verification-date-missing", r"last verified|verified on|последн.{0,12}провер", "Last verified state/date was not found."),
                ("runbook-trigger-missing", r"trigger|when to use|когда использ|услови.{0,8}запуск", "Trigger or usage scope was not found."),
                ("runbook-prerequisites-missing", r"prerequisite|permission|access|требован|доступ", "Prerequisites or permissions were not found."),
                ("runbook-expected-missing", r"expected result|expected output|ожидаем", "Expected results for steps were not found."),
                ("runbook-verification-missing", r"verification|verify|провер", "Outcome verification was not found."),
                ("runbook-recovery-missing", r"rollback|roll.?forward|recovery|откат|восстанов", "Rollback, roll-forward, or recovery handling was not found."),
                ("runbook-escalation-missing", r"escalat|эскалац|обратит", "Escalation conditions were not found."),
            )
            for finding_id, pattern, message in checks:
                if not contains(text, pattern):
                    add(finding_id, "high" if "verification" in finding_id or "recovery" in finding_id else "medium", message, path)

        if "handoff" in stem:
            checks = (
                ("handoff-scope-missing", r"deliverable|scope|accepted|поставк|объем|объём|принят", "Delivered scope and acceptance were not found."),
                ("handoff-ownership-missing", r"owner|ownership|владелец|принадлеж", "Account or asset ownership was not found."),
                ("handoff-environments-missing", r"environment|deploy|hosting|среда|развер|хостинг", "Environment or deployment ownership was not found."),
                ("handoff-data-missing", r"data|backup|restore|retention|данн|резерв|восстанов", "Data, backup, or recovery state was not found."),
                ("handoff-support-missing", r"support|warranty|maintenance|поддерж|гарант|сопровожд", "Support or warranty boundary was not found."),
                ("handoff-risk-missing", r"risk|known issue|limitation|риск|огранич|известн.{0,8}проблем", "Known risks or limitations were not found."),
            )
            for finding_id, pattern, message in checks:
                if not contains(text, pattern):
                    add(finding_id, "high" if "scope" in finding_id or "ownership" in finding_id else "medium", message, path)

        if stem in {"api", "openapi", "swagger"} or "api-" in stem or stem.endswith("-api"):
            for finding_id, pattern, message in (
                ("api-version-missing", r"version|openapi|верси", "API or contract version was not found."),
                ("api-auth-missing", r"auth|security|авторизац|аутентиф", "Authentication/authorization behavior was not found."),
                ("api-example-missing", r"example|curl|request|response|пример|запрос|ответ", "A request/response example was not found."),
                ("api-errors-missing", r"error|problem details|status code|ошиб|код состоян", "Error semantics were not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "high" if "errors" in finding_id else "medium", message, path)

        if stem == "architecture" or stem.startswith("adr-"):
            for finding_id, pattern, message in (
                ("architecture-boundaries-missing", r"boundary|scope|owns|границ|ответствен", "System or decision boundaries were not found."),
                ("architecture-tradeoffs-missing", r"trade.?off|alternative|consequence|компромисс|альтернатив|последств", "Tradeoffs, alternatives, or consequences were not found."),
                ("architecture-unknowns-missing", r"unknown|open question|limitation|неизвест|открыт.{0,8}вопрос|огранич", "Unknowns or limitations were not found."),
            ):
                if not contains(text, pattern):
                    add(finding_id, "medium", message, path)

    return findings


def self_test() -> int:
    assert not allowed(Path("/tmp/.env"))
    assert not allowed(Path("/tmp/.env.example"))
    assert not allowed(Path("/tmp/docs/credentials.md"))
    assert not allowed(Path("/tmp/appsettings.Production.json"))
    assert not allowed(Path("/tmp/docs.enc.yaml"))
    assert allowed(Path("/tmp/README.md"))
    assert allowed(Path("/tmp/docs/onboarding.md"))
    assert allowed(Path("/tmp/openapi.yaml"))
    assert not allowed(Path("/tmp/src/config.json"))

    incomplete = [(
        Path("/tmp/docs/runbook.md"),
        "# Runbook\nTODO\npassword = \"this-looks-like-a-secret-value\"\n[Missing](missing.md)",
    )]
    finding_ids = {item.id for item in audit(Path("/tmp"), incomplete)}
    assert "unresolved-placeholder" in finding_ids
    assert "possible-secret-value" in finding_ids
    assert "broken-local-link" in finding_ids
    assert "runbook-verification-missing" in finding_ids

    complete = [(
        Path("/tmp/docs/runbook.md"),
        """
# Runbook
Owner: Platform team
Last verified: 2030-01-01 in staging
When to use: on the stated alert
Prerequisites and access: read-only operator role
## Steps
Run the documented inspection.
Expected result: service reports healthy.
## Verification
Verify the critical journey.
## Rollback and recovery
Use the approved recovery procedure.
## Escalation
Escalate to the on-call role if verification fails.
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
        parser.error("path must be an existing documentation artifact or directory")

    target = args.path.resolve()
    findings = audit(target, collect(target))
    if args.format == "json":
        print(json.dumps(
            {"status": "review" if findings else "pass", "findings": [asdict(item) for item in findings]},
            ensure_ascii=False,
            indent=2,
        ))
    elif not findings:
        print("PASS: no heuristic documentation blockers found. This does not prove technical accuracy.")
    else:
        print(f"REVIEW: {len(findings)} finding(s). No excerpts or sensitive values are shown.")
        for item in findings:
            location = f" ({item.file})" if item.file else ""
            print(f"- [{item.severity}] {item.id}{location}: {item.message}")
    return 1 if any(item.severity in {"high", "critical"} for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())

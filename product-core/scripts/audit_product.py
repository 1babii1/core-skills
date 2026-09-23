#!/usr/bin/env python3
"""Secret-safe heuristic review of product artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".csv"}
PRODUCT_TERMS = {
    "prd", "product", "brief", "requirement", "scope", "hypothesis", "experiment",
    "metric", "analytics", "instrumentation", "decision", "research", "interview",
    "jtbd", "canvas", "opportunity", "assumption", "discovery", "validation",
}
SKIP_DIRS = {
    ".git", ".next", ".idea", ".vscode", "node_modules", "bin", "obj", "dist",
    "build", "coverage", "artifacts",
}
FORBIDDEN_SUFFIXES = {
    ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".age",
}


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
    if any(term in name for term in ("secret", "credential", "service-account", "service_account")):
        return False
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return False
    stem = path.stem.lower()
    return any(term in stem for term in PRODUCT_TERMS)


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
            "no-product-artifacts",
            "info",
            "No product-looking artifact names were found; only explicitly named product documents are read.",
        )
        return findings

    for path, text in files:
        name = path.name.lower()

        if contains(text, r"\b(TODO|TBD|FIXME|fill this|placeholder)\b"):
            add("unresolved-placeholder", "medium", "Unresolved placeholder language remains.", path)

        if any(term in name for term in ("prd", "requirement", "brief", "scope")):
            if not contains(text, r"out.?of.?scope|не входит|исключ"):
                add("scope-exclusions-missing", "high", "Explicit out-of-scope boundaries were not found.", path)
            if not contains(text, r"acceptance|given.+when.+then|критери.{0,8}при"):
                add("acceptance-missing", "high", "Observable acceptance criteria were not found.", path)
            if not contains(text, r"success metric|metric|метрик|критери.{0,8}успех"):
                add("success-measure-missing", "high", "A success measure was not found.", path)
            if not contains(text, r"assumption|unknown|open question|допущ|неизвест|открыт.{0,8}вопрос"):
                add("unknowns-missing", "medium", "Assumptions or open questions were not found.", path)

        if "hypothesis" in name or "гипот" in name:
            if not contains(text, r"we believe|мы считаем|если.+то|believe that"):
                add("hypothesis-structure-missing", "high", "No explicit falsifiable hypothesis structure was found.", path)
            if not contains(text, r"pass|fail|inconclusive|успех|провал|неопредел"):
                add("hypothesis-decision-rule-missing", "high", "Pass/fail/inconclusive rules were not found.", path)
            if not contains(text, r"segment|target user|сегмент|пользовател"):
                add("hypothesis-segment-missing", "medium", "The target segment was not found.", path)

        if any(term in name for term in ("metric", "analytics", "instrumentation")):
            for key, pattern, message in (
                ("metric-formula-missing", r"formula|numerator|denominator|формул|числител|знаменател", "Metric formula/denominator definition was not found."),
                ("metric-baseline-missing", r"baseline|базов", "A baseline or baseline collection plan was not found."),
                ("metric-threshold-missing", r"target|threshold|порог|целе", "A target or decision threshold was not found."),
                ("metric-window-missing", r"time window|window|period|окно|период", "A measurement window was not found."),
                ("metric-guardrail-missing", r"guardrail|counter.?metric|огранич|защитн", "Guardrail/counter-metrics were not found."),
            ):
                if not contains(text, pattern):
                    add(key, "high" if "formula" in key else "medium", message, path)

        if "instrumentation" in name:
            if not contains(text, r"trigger|fires?|срабаты"):
                add("event-trigger-missing", "high", "Precise event trigger semantics were not found.", path)
            if contains(text, r"\b(email|phone|full.?name|message.?body|address)\b") and not contains(
                text, r"PII|privacy|exclude|hash|персональ|приват"
            ):
                add("analytics-pii-review", "high", "Potential personal-data properties need an explicit privacy decision.", path)

        if "experiment" in name or "validation" in name:
            if not contains(text, r"hypothesis|гипотез"):
                add("experiment-hypothesis-missing", "high", "The tested hypothesis was not found.", path)
            if not contains(text, r"decision|ship|iterate|stop|kill|решен|запуск|останов"):
                add("experiment-action-missing", "high", "Outcome-to-decision actions were not found.", path)
            if not contains(text, r"sample|traffic|participant|выборк|трафик|участник"):
                add("experiment-sample-limit-missing", "medium", "Sample/traffic limitations were not found.", path)

        if "decision" in name:
            for key, pattern, message in (
                ("decision-owner-missing", r"owner|владелец|ответствен", "Decision owner was not found."),
                ("decision-options-missing", r"option|alternative|вариант|альтернатив", "Alternatives considered were not found."),
                ("decision-evidence-missing", r"evidence|fact|metric|доказ|факт|метрик", "Decision evidence was not found."),
                ("decision-revisit-missing", r"revisit|review date|пересмотр|дата проверки", "A revisit condition/date was not found."),
            ):
                if not contains(text, pattern):
                    add(key, "medium", message, path)

    return findings


def self_test() -> int:
    assert not allowed(Path("/tmp/.env"))
    assert not allowed(Path("/tmp/.env.example"))
    assert not allowed(Path("/tmp/product-secrets.md"))
    assert not allowed(Path("/tmp/appsettings.Production.json"))
    assert not allowed(Path("/tmp/product.enc.yaml"))
    assert allowed(Path("/tmp/product-brief.md"))
    assert allowed(Path("/tmp/experiment-results.json"))
    sample = [(Path("/tmp/product-brief.md"), "# Product brief\n## In scope\nTODO")]
    finding_ids = {item.id for item in audit(Path("/tmp"), sample)}
    assert "scope-exclusions-missing" in finding_ids
    assert "acceptance-missing" in finding_ids
    assert "unresolved-placeholder" in finding_ids
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
        parser.error("path must be an existing product artifact or directory")

    target = args.path.resolve()
    findings = audit(target, collect(target))
    if args.format == "json":
        print(json.dumps({"status": "review" if findings else "pass", "findings": [asdict(item) for item in findings]}, ensure_ascii=False, indent=2))
    elif not findings:
        print("PASS: no heuristic product-artifact blockers found. This does not prove product value.")
    else:
        print(f"REVIEW: {len(findings)} finding(s). No document excerpts or sensitive values are shown.")
        for item in findings:
            location = f" ({item.file})" if item.file else ""
            print(f"- [{item.severity}] {item.id}{location}: {item.message}")
    return 1 if any(item.severity in {"high", "critical"} for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())

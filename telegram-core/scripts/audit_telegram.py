#!/usr/bin/env python3
"""Secret-safe heuristic audit for Telegram bot and Mini App source code."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

TEXT_SUFFIXES = {
    ".cs", ".csproj", ".props", ".targets", ".ts", ".tsx", ".js", ".jsx",
    ".mjs", ".md", ".yaml", ".yml", ".toml", ".config", ".html", ".css",
}
IGNORED_DIRS = {
    ".git", ".next", ".turbo", ".idea", ".vscode", "bin", "obj", "node_modules",
    "dist", "build", "coverage", "artifacts",
}
FORBIDDEN_SUFFIXES = {
    ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".age",
}
FORBIDDEN_NAMES = {
    "secrets.json", "credentials.json", "service-account.json",
    "service_account.json", "id_rsa", "id_ed25519",
}


@dataclass(frozen=True)
class Finding:
    id: str
    severity: str
    message: str
    file: str | None = None
    line: int | None = None


def is_allowed(path: Path) -> bool:
    """Decide before opening a file; secret-bearing files are never read."""
    lower_name = path.name.lower()
    lower_parts = {part.lower() for part in path.parts}
    if lower_parts & IGNORED_DIRS:
        return False
    if lower_name.startswith(".env"):
        return lower_name == ".env.example"
    if lower_name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
        return False
    if lower_name.endswith((".enc.json", ".enc.yaml", ".enc.yml")):
        return False
    if lower_name.startswith(("credentials.", "service-account.", "service_account.")):
        return False
    if lower_name.startswith("appsettings") and lower_name.endswith(".json"):
        return False
    return path.suffix.lower() in TEXT_SUFFIXES


def collect(root: Path) -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for path in root.rglob("*"):
        if not path.is_file() or not is_allowed(path):
            continue
        try:
            if path.stat().st_size > 2_000_000:
                continue
            files.append((path, path.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            continue
    return files


def first_match(
    files: list[tuple[Path, str]], pattern: str, flags: int = re.IGNORECASE
) -> tuple[Path, int] | None:
    regex = re.compile(pattern, flags)
    for path, text in files:
        match = regex.search(text)
        if match:
            return path, text.count("\n", 0, match.start()) + 1
    return None


def has(files: list[tuple[Path, str]], pattern: str, flags: int = re.IGNORECASE) -> bool:
    return first_match(files, pattern, flags) is not None


def audit(root: Path, files: list[tuple[Path, str]]) -> list[Finding]:
    findings: list[Finding] = []

    def add(
        finding_id: str,
        severity: str,
        message: str,
        location: tuple[Path, int] | None = None,
    ) -> None:
        relative = str(location[0].relative_to(root)) if location else None
        findings.append(
            Finding(finding_id, severity, message, relative, location[1] if location else None)
        )

    webhook = has(files, r"setwebhook|webhook")
    if webhook and not has(files, r"X-Telegram-Bot-Api-Secret-Token"):
        add(
            "webhook-secret-header-missing",
            "high",
            "Webhook code was found without the Telegram secret-header name.",
        )
    if webhook and has(files, r"X-Telegram-Bot-Api-Secret-Token") and not has(
        files, r"FixedTimeEquals|CryptographicOperations|constant.?time|timingSafeEqual"
    ):
        add(
            "webhook-secret-comparison-review",
            "medium",
            "Confirm that webhook secret comparison is constant-time.",
        )

    init_location = first_match(files, r"initDataUnsafe")
    if init_location:
        add(
            "initdataunsafe-trust-risk",
            "high",
            "initDataUnsafe is present; ensure it is display-only and never a trust source.",
            init_location,
        )
    init_flow = has(files, r"initData|WebAppData")
    if init_flow and not has(files, r"HMACSHA256|Ed25519|ValidateInit|VerifyInit"):
        add(
            "initdata-server-validation-missing",
            "high",
            "Mini App init data appears present without recognizable server-side validation.",
        )
    if init_flow and not has(
        files, r"FixedTimeEquals|CryptographicOperations|constant.?time|timingSafeEqual"
    ):
        add(
            "initdata-constant-time-missing",
            "high",
            "Confirm constant-time comparison for init-data authentication material.",
        )
    if init_flow and not has(files, r"auth_date|AuthDate|MaxAge|ClockSkew|Fresh"):
        add(
            "initdata-freshness-missing",
            "high",
            "No recognizable init-data freshness check was found.",
        )

    update_flow = has(files, r"\bUpdate(Id)?\b|update_id")
    if update_flow and not has(
        files, r"dedup|idempoten|unique|HasIndex|offset|processed.?update"
    ):
        add(
            "update-dedup-missing",
            "high",
            "Update handling appears present without recognizable deduplication/idempotency.",
        )

    payment_flow = has(files, r"sendInvoice|PreCheckout|SuccessfulPayment|currency.{0,20}XTR")
    if payment_flow and not has(files, r"PreCheckout"):
        add("precheckout-missing", "high", "Payment flow lacks a recognizable pre-checkout handler.")
    if payment_flow and not has(files, r"SuccessfulPayment"):
        add(
            "payment-successful-event-missing",
            "critical",
            "Payment flow lacks a recognizable successful-payment fulfillment event.",
        )
    if payment_flow and not has(
        files, r"TelegramPaymentChargeId|ProviderPaymentChargeId|idempoten|unique|HasIndex"
    ):
        add(
            "payment-idempotency-missing",
            "critical",
            "No recognizable unique charge/idempotent fulfillment protection was found.",
        )

    memory_state = first_match(
        files,
        r"(Dictionary|ConcurrentDictionary|MemoryCache|Map)\s*[<(].{0,80}(chat|user|conversation|state)",
    )
    if memory_state:
        add(
            "inmemory-conversation-state",
            "medium",
            "Conversation-like state may be process-local and lost on restart.",
            memory_state,
        )

    cors = first_match(files, r"AllowAnyOrigin|\borigins?\s*:\s*\[\s*['\"]\*")
    if cors:
        add("cors-wildcard", "high", "Wildcard CORS configuration was found.", cors)

    raw_log = first_match(
        files,
        r"(Log|WriteLine|console\.log).{0,100}(initData|authorization|bot.?token|payment.?payload)",
    )
    if raw_log:
        add(
            "raw-sensitive-logging",
            "high",
            "Potential sensitive Telegram/auth/payment logging was found; no source snippet is shown.",
            raw_log,
        )

    token = first_match(files, r"\b\d{7,12}:[A-Za-z0-9_-]{25,}\b")
    if token:
        add(
            "possible-hardcoded-telegram-token",
            "critical",
            "A token-shaped literal may be hardcoded; rotate if real. Its value is intentionally hidden.",
            token,
        )

    return findings


def self_test() -> int:
    assert is_allowed(Path("/tmp/project/.env.example"))
    assert not is_allowed(Path("/tmp/project/.env"))
    assert not is_allowed(Path("/tmp/project/.env.production"))
    assert not is_allowed(Path("/tmp/project/appsettings.Production.json"))
    assert not is_allowed(Path("/tmp/project/private.enc.yaml"))
    assert is_allowed(Path("/tmp/project/Handler.cs"))
    print("self-test: ok")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.project is None or not args.project.is_dir():
        parser.error("project must be an existing directory")

    root = args.project.resolve()
    findings = audit(root, collect(root))
    if args.format == "json":
        print(json.dumps({"status": "review" if findings else "pass", "findings": [asdict(x) for x in findings]}, indent=2))
    elif not findings:
        print("PASS: no heuristic Telegram blockers found. This is not proof of security.")
    else:
        print(f"REVIEW: {len(findings)} heuristic finding(s). No secret values or source snippets are shown.")
        for item in findings:
            location = f" ({item.file}:{item.line})" if item.file else ""
            print(f"- [{item.severity}] {item.id}{location}: {item.message}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

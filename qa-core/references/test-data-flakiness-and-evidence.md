# Test data, flakiness, and evidence

## Test data

- Generate synthetic, minimal, non-sensitive data.
- Do not copy production personal data into tests without an approved anonymization process.
- Allocate unique tenants, users, records, ports, schemas, and object prefixes per run or worker.
- Make setup and cleanup explicit and idempotent.
- Prefer APIs or fixtures for setup over slow UI setup, while keeping the user-visible action under test.
- Freeze clocks and random seeds when behavior depends on them.
- Ensure parallel tests do not share mutable state.
- Keep required variable names and safe placeholders in `.env.example`; never inspect other env files.

## Environment

Record:

- build/commit;
- service and dependency versions;
- migration version;
- browser/OS/container image;
- feature flags and non-secret configuration;
- test-data seed/version;
- known infrastructure limitations.

Environment drift makes results inconclusive until explained.

## Flaky-test handling

Classify a test as flaky when the same build and relevant environment produce fail-then-pass without an intentional product change.

For each flake:

- keep the original failure artifact;
- reproduce with repeat and concurrency settings;
- identify owner and tracking item;
- quarantine only when necessary to restore signal;
- add an expiry and visible reporting;
- keep the critical behavior covered by a lower-level test or manual gate;
- remove quarantine after a stability run.

Do not:

- add sleeps;
- increase all timeouts;
- loosen assertions;
- silently exclude the test;
- treat retry success as a pass.

## Failure classification

Use one of:

- product regression;
- test defect;
- environment/infrastructure failure;
- known baseline failure;
- unsupported target;
- inconclusive.

Include the first actionable cause, not pages of raw logs.

## Artifact policy

Keep artifacts proportionate to the gate:

- unit/integration reports and coverage when requested;
- OpenAPI candidate and compatibility diff;
- Playwright trace, screenshot, video, console, and network diagnostics on failure;
- visual expected/actual/diff;
- accessibility report plus manual notes;
- k6 summary and observability links;
- UAT acceptance record;
- final requirement-to-evidence matrix.

Redact or prevent collection of secrets, auth tokens, cookies, personal data, and private payloads.

## Verification record

For every claimed gate, record:

```text
Gate:
Environment/build:
Command:
Exit code:
Result:
Counts/thresholds:
Artifacts:
Known gaps or waiver:
```

Fresh command output is required for a current success claim.

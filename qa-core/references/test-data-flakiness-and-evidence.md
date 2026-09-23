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

## Prove the test can fail

A regression test that passes against the bug it was written for is theater, and worse than no test because it reports safety that is not there. Before counting a test as evidence for a fix, break the fix (or the guarded behavior) and watch that specific test fail, then restore it. Green after the break means the test is wrong, not the code. Record the mutation and the failure.

Assertions that cannot tell the two cases apart:

- a cap or limit asserted with less data than the cap (a clamp to 200 and no clamp return the same rows when three exist): seed past the boundary;
- a filter asserted with only matching rows present: seed a row that must be excluded;
- an ownership or tenant rule asserted with one owner's data: seed a second owner;
- a race test seeded against a brand-new aggregate can pass by accident because the aggregate's own primary key masks the missing constraint: seed it against one that already has related rows;
- only a status code asserted where the defect changes the body, or the reverse.

State in the test what makes the boundary observable so nobody "simplifies" the seed and hollows the test out. A probabilistic race test is honest only if you report how often the mutant failed (for example 3 of 6 runs), not "proven".

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

## Fails only in the full run: broken, not flaky

"Passes alone, fails in the full run" is a defect with a cause. Do not retry it away and do not touch the assertion first. Check in this order:

- a background service the test host starts that the tests do not need, competing for the same resources and retrying against infrastructure that does not exist in tests;
- one container per test class where one per assembly would do;
- shared state reset by one class while another is mid-run.

A suite that is both slow and load-sensitive is usually waiting on something it should never have started; if the fix does not also make it markedly faster, suspect a different cause. When one project's test setup differs from its siblings', start there.

## Shared fixtures and reset tools

The reset between tests is test infrastructure and fails confusingly. A "wipe every table" reset (Respawn, TRUNCATE loops, snapshot restore) also wipes rows the host needs to boot: seeded roles, OAuth clients and scopes, signing keys, reference data. Exclude them explicitly and have any class that mutates shared state restore it in its own setup. Startup seeders may run lazily on first host access, so a wipe before that first touch races the seeder. The signature of wiped bootstrap data is an error from deep in the framework ("no signing key registered", "client not found") in tests that never touched that feature: suspect the reset before the feature.

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

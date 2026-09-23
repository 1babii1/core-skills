# CI quality gates

Coordinate pipeline mechanics with `delivery-core`. Keep QA responsible for required evidence and verdicts.

## PR gate

Optimize for fast feedback:

- repository lint/typecheck/build checks;
- changed unit and component tests;
- focused integration tests;
- OpenAPI validation and breaking-change detection;
- critical changed-flow Chromium E2E;
- automated accessibility smoke;
- secret/security checks owned by the security and delivery cores.

Target a predictable suite budget. Do not make every expensive test a PR blocker.

## Mainline gate

Run:

- full relevant unit/integration suite;
- critical E2E;
- Chromium, Firefox, and WebKit;
- approved visual regression;
- migration/startup smoke;
- complete failure artifacts.

Do not promote an artifact built from a different commit than the one tested.

## Staging/release gate

Require as applicable:

- deployed artifact identity;
- forward migration and rollback/restore evidence;
- UAT acceptance;
- supported browser/device matrix;
- manual accessibility review of critical flows;
- safe smoke or average-load profile;
- monitoring and rollback readiness;
- explicit waivers for non-critical gaps.

## Scheduled gates

Move expensive or long-running work here:

- stress, spike, soak, and capacity experiments;
- extended browser/device/locale matrix;
- repeated tests for flake detection;
- deep accessibility audit;
- mutation or property-based testing where it adds value;
- resilience and dependency-failure exercises.

## Post-deploy

Run safe checks against the exact deployed version:

- health and readiness;
- read-only critical journey or synthetic probe;
- dependency and error-rate signals;
- deployment-specific contract/version check;
- rollback trigger observation.

Do not perform destructive production actions without explicit authorization.

## Gate behavior

- Stop dependent stages when an earlier required gate fails.
- Allow retries for infrastructure diagnostics, not to erase the original failure.
- Publish machine-readable and human-readable results.
- Preserve artifacts long enough for triage and release audit.
- Require owner and expiry for quarantines and waivers.
- Distinguish merge-blocking and deploy-blocking failures.

## Release report

Summarize:

| Gate | Required | Result | Evidence | Owner/gap |
|---|---:|---|---|---|

Conclude with exactly one verdict:

- `PASS`
- `CONDITIONAL`
- `BLOCKED`
- `INCONCLUSIVE`

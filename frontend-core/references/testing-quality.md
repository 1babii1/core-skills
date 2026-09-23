# Testing and quality

Read this reference for test strategy, adding coverage, audits, or release verification.

## Select the cheapest strong boundary

| Risk | Preferred test |
| --- | --- |
| Pure transformation, parser, schema, reducer | Vitest unit test |
| Hook or component behavior | Testing Library with Vitest |
| HTTP success/error/latency scenario | MSW-backed component/integration test |
| Router/server/client integration | Framework integration test |
| Critical user journey | Playwright |
| Visual hierarchy/polish | `design-core` browser iteration |
| Accessibility | semantic/component checks plus browser audit |

Test observable behavior rather than implementation trivia. Avoid snapshots that hide meaningful changes.

## Minimum risk coverage

For changed critical behavior, cover:

- success;
- validation/rejection;
- permission failure;
- backend/network failure;
- retry or recovery when applicable;
- duplicate action/concurrency when applicable;
- mobile/keyboard behavior for user-facing flows.

Use MSW handlers grouped by domain and reset test overrides after each test. Do not mock the unit under test or every internal module.

## Critical E2E candidates

- login/logout and protected navigation;
- the product's primary value-producing action;
- checkout/payment or destructive operations;
- a critical form with server validation;
- permission boundaries;
- deployed smoke flow.

Keep E2E few, independent, deterministic, and based on stable user-facing locators.

## Gate

Run repository-native:

1. dependency restore/install using the lockfile;
2. formatting/lint;
3. typecheck;
4. unit/component tests;
5. relevant integration/E2E;
6. production build;
7. accessibility/security/performance checks proportional to risk.

Coverage is navigation for locating untested risk, not a completion score.

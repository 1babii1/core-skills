# E2E, cross-browser, and visual regression

Use `playwright-best-practices` for implementation details and this reference for qa-core policy.

## E2E scope

Define one or more critical journeys per product area, for example:

- sign in and recover access;
- create, edit, and complete the primary business object;
- purchase, booking, submission, or other money path;
- permission-sensitive administrator action;
- file upload/download;
- real-time or multi-user update;
- error recovery after a failed dependency.

Do not reproduce every validation permutation in E2E. Prove rules lower in the test stack.

## Browser tiers

- PR: Chromium for changed critical paths.
- Mainline: Chromium, Firefox, and WebKit for critical paths.
- Release: supported branded channels and mobile emulation derived from policy or analytics.
- Scheduled: extended locale, viewport, device, and browser-version matrix.

Document unsupported combinations instead of silently skipping them.

## Determinism

- Use accessible roles, names, labels, and stable test IDs.
- Wait for observable state, not arbitrary time.
- Isolate accounts, tenants, and records by worker/run.
- Freeze or control clocks, randomness, locale, timezone, and network where relevant.
- Mock only external systems that should not be tested; keep owned services real when the journey claims full-stack evidence.
- Capture trace, screenshot, video, console, and network evidence on failure according to artifact-retention policy.

## Visual regression policy

Choose stable pages and component states. Cover:

- default, loading, empty, error, and populated states;
- responsive breakpoints;
- focus, hover, selected, disabled, and validation states when visually contractual;
- themes and supported locales when they affect layout.

Stabilize:

- container image/OS and browser version;
- fonts and rendering dependencies;
- viewport and device scale;
- clock, animations, caret, skeletons, random data, and dynamic ads;
- test data and network responses.

Review every baseline change:

1. Inspect expected, actual, and diff.
2. Link the product/design change that justifies it.
3. Confirm cross-browser or platform scope.
4. Approve intentionally.
5. Keep the diff artifact.

Never raise thresholds globally to hide a regression. Mask only truly non-contractual dynamic regions and document why.

## Flake check

For a new or repaired critical test:

- run it focused;
- run it repeatedly;
- run it with the intended worker count;
- run the relevant browser matrix;
- confirm failure artifacts are sufficient to diagnose the next incident.

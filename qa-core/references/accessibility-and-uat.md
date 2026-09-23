# Accessibility and UAT

Accessibility and UAT answer different questions:

- accessibility asks whether people with disabilities can operate and understand the product;
- UAT asks whether the delivered behavior satisfies the business need.

Neither replaces functional regression testing.

## Accessibility layers

### Automated

Use `accessibility`, `web-quality-audit`, and Playwright/axe where configured to check:

- semantic structure and landmarks;
- accessible names and roles;
- common ARIA misuse;
- form labels and errors;
- contrast detectable by tooling;
- document language and page title;
- duplicate IDs and structural violations.

Automation cannot prove full WCAG conformance.

### Manual critical-flow review

Verify:

- keyboard-only completion without traps;
- visible and logical focus order;
- skip navigation and landmark navigation;
- dialog, menu, disclosure, tab, and combobox behavior;
- error announcement and recovery;
- zoom/reflow and text spacing;
- reduced motion;
- screen-reader name, role, state, and meaningful reading order;
- media alternatives when applicable.

Test the supported desktop/mobile modes and critical journeys, not only isolated components.

## Accessibility evidence

Record:

- WCAG version and target level;
- pages/journeys and browsers reviewed;
- automated tool/version and rules;
- manual input/assistive-technology method;
- violations with severity, reproduction, affected users, and remediation;
- accepted exceptions with owner and expiry.

## UAT preparation

For each requirement, define:

- business outcome;
- preconditions and role;
- scenario in Given/When/Then or equivalent form;
- observable acceptance result;
- required data and environment;
- owner who can accept the result.

Avoid implementation details in acceptance criteria.

## UAT execution

- Use `gsd-verify-work` for conversational acceptance.
- Use `gsd-audit-uat` to find unresolved UAT across phases.
- Use `gsd-add-tests` to convert confirmed regressions and stable acceptance rules into automation.
- Preserve screenshots or records needed for acceptance, excluding secrets and sensitive personal data.
- Distinguish rejection, defect, scope change, environment issue, and clarification.

## Traceability matrix

| Requirement | Acceptance criterion | Risk | Evidence | Result | Owner |
|---|---|---|---|---|---|

Critical requirements without direct evidence block release. Product decisions that change acceptance criteria must be recorded rather than silently changing the test.

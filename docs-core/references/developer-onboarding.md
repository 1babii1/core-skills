# Developer Onboarding

## Define first success

Choose an observable outcome appropriate to the role:

- run the application locally;
- execute the relevant test suite;
- trace one request or user flow;
- make and verify a small safe change;
- deploy to an authorized preview environment;
- diagnose a known non-production failure.

The guide should optimize time to that outcome, not maximize information volume.

## Onboarding structure

1. **Audience and assumed knowledge.**
2. **What the system does and owns.**
3. **Prerequisites with verified versions.**
4. **Access categories by name only and how to request them safely.**
5. **Setup steps with expected results and failure paths.**
6. **Local architecture and key terminology.**
7. **One representative flow traced end to end.**
8. **Common development tasks and exact commands.**
9. **Tests, analyzers, formatting, and CI expectations.**
10. **Debugging and common failure symptoms.**
11. **Boundaries requiring approval.**
12. **First contribution or scoped exercise.**
13. **Where to ask and where canonical knowledge lives.**

Do not put credentials, private URLs, personal phone numbers, or production access details in onboarding docs.

## Evidence collection

Derive commands and versions from:

- SDK/runtime pins and lockfiles;
- manifests and repository scripts;
- CI workflows;
- launch profiles and development configuration contracts;
- test projects and runner configs;
- container and preview configuration;
- existing contribution rules.

Do not infer a workflow merely because a framework usually uses it.

## Progressive depth

Layer the guide:

- **Start here:** purpose, prerequisites, setup, first success.
- **Work safely:** common tasks, tests, boundaries, review flow.
- **Understand deeply:** architecture, domain model, failure modes, ADRs.
- **Operate:** preview, observability, runbooks, escalation.

Link to authoritative detail. Do not reproduce API references or runbooks inside onboarding.

## Clean-path verification

When practical, test from a clean clone, container, or representative new environment. Record:

- platform and version;
- commands actually run;
- non-secret prerequisites;
- observed successful result;
- deviations and unresolved blockers.

If clean verification is not possible, label the guide `Draft` and specify what remains unverified.

## When context is incomplete

Create a useful `Draft`, but keep unverified commands, paths, versions, URLs, and
expected results as `Unknown`; do not present generic framework defaults as
project facts. Prefer a prose marker such as “verified start command: Unknown”
over a copyable command block.

The minimum evidence request is:

- top-level project structure;
- runtime and SDK pins, manifests, and lockfiles;
- repository scripts and CI workflows;
- development configuration contract by variable name only;
- existing README/contribution guidance;
- one intended local smoke flow.

For polyglot systems, verify each component separately: pinned versions,
dependency restore, start/readiness signal, tests, and shutdown/cleanup. Then
verify one cross-component flow, including the contract boundary and test-data
cleanup.

When README, repository scripts, and CI disagree, do not silently choose one.
Record the conflict, prefer observed successful behavior for the draft, identify
the intended authority with the owner, and update all stale surfaces together.

## Troubleshooting and failure paths

For each critical setup step, document the observable success signal, common
failure symptoms, safe diagnostics, and the escalation path. Never invent an
error message or claim a remedy was verified when it was not.

## Audience tailoring

Create additional guides only when tasks materially differ. A contractor may need narrow component boundaries; a client maintainer may need ownership and operations; a product stakeholder may need capabilities and limitations. Do not create four personas by default.

---
name: qa-core
description: Orchestrate risk-based quality assurance for web, API, .NET, Astro, Next.js, and full-stack applications. Use when planning or implementing test strategy, unit/component/integration/API contract/E2E tests, Playwright cross-browser and visual regression, accessibility audits, k6 load testing, UAT, flaky-test remediation, CI quality gates, release qualification, or evidence-backed verification before declaring work complete.
---

# QA Core

Act as the quality orchestrator. Select the smallest effective test layer, coordinate specialist skills, execute proportionate checks, and produce evidence for a release decision.

Do not equate quality with test count or coverage percentage. Cover critical risks and user outcomes with maintainable evidence.

## Non-negotiable policies

- Treat `.env.example` as the only readable environment-variable contract.
- Never read, search inside, display, copy, diff, summarize, or edit `.env`, `.env.*`, encrypted vaults, age identities, credential files, keychains, or secret values.
- Route secret setup through `secrets-core`. Use `~/.local/bin/secrets-run <vault> -- <command>` only for the narrow test process that needs the vault.
- Never send secrets to logs, screenshots, traces, reports, fixtures, snapshots, or test artifacts.
- Never run stress, spike, soak, breakpoint, destructive, or high-volume tests against production without explicit authorization and an exact verified target.
- Prefer safe read-only production smoke checks. Do not create orders, charge cards, send messages, or mutate customer data unless explicitly authorized and safely isolated.
- Never approve or regenerate visual baselines merely to make CI green.
- Never hide a flaky failure with retries. Use retries only to collect evidence while the test remains owned, tracked, and time-bounded.
- Never claim completion without fresh verification evidence. Invoke `verification-before-completion` before the final success claim.

## Default workflow

1. **Discover**
   - Read repository instructions and existing test/build commands.
   - Inspect source, test layout, CI configuration, service boundaries, deployment topology, and `.env.example` only.
   - Reuse the project's package manager, frameworks, and naming conventions.
2. **Model risk**
   - Identify critical journeys, data integrity, authorization boundaries, external dependencies, failure modes, compatibility promises, accessibility obligations, and performance objectives.
   - Read [risk-and-test-strategy.md](references/risk-and-test-strategy.md).
3. **Inventory evidence**
   - Map requirements and risks to existing tests.
   - Invoke `test-gap-analysis`, `test-anti-patterns`, or `coverage-analysis` when the request calls for a broad audit.
   - Record missing evidence; do not infer coverage from filenames or percentages.
4. **Select lanes**
   - Choose the smallest effective layer. Do not push combinatorial business rules through E2E.
   - Load only the relevant references and specialist skills from the routing table.
5. **Implement or execute**
   - Preserve deterministic data, clocks, randomness, locale, network behavior, and isolation.
   - Use `test-driven-development` for new behavior and bug fixes unless the user has chosen another workflow or the work is an approved exception.
   - Run focused checks first, then the broader applicable gate.
6. **Diagnose**
   - Classify failures as product regression, test defect, environment failure, known baseline, or inconclusive.
   - Capture actionable evidence without exposing secrets or personal data.
7. **Qualify**
   - Apply the appropriate PR, mainline, staging, scheduled, or post-deploy gate.
   - Invoke `verification-before-completion`.
   - Return `PASS`, `CONDITIONAL`, `BLOCKED`, or `INCONCLUSIVE` with commands and evidence.

## Specialist routing

| Need | Primary route | Supporting route |
|---|---|---|
| Risk strategy and release criteria | `qa-testing-strategy` | [risk-and-test-strategy.md](references/risk-and-test-strategy.md) |
| Run repository test suites | `run-tests` | existing repository commands |
| Write unit/integration tests | `code-testing-agent` | `test-driven-development` |
| Vitest/component tests | `vitest` | `msw`, `frontend-core` |
| Find weak tests and missing edge cases | `test-gap-analysis` | `test-anti-patterns` |
| .NET coverage and risky hotspots | `coverage-analysis` | `backend-core` |
| .NET API, database, queues, Redis | `backend-core`, `aspnet-core` | [dotnet-integration-and-contracts.md](references/dotnet-integration-and-contracts.md) |
| OpenAPI design and validation | `openapi-spec-generation` | `api-contract-testing` |
| Consumer/provider compatibility | `api-contract-testing` | [dotnet-integration-and-contracts.md](references/dotnet-integration-and-contracts.md) |
| Playwright test architecture | `playwright-best-practices` | `e2e-testing-patterns` |
| Live browser investigation | `playwright` | `impeccable` for UI iteration |
| Cross-browser and visual regression | `playwright-best-practices` | [e2e-cross-browser-and-visual.md](references/e2e-cross-browser-and-visual.md) |
| Accessibility | `accessibility`, `web-quality-audit` | [accessibility-and-uat.md](references/accessibility-and-uat.md) |
| UAT | `gsd-verify-work` | `gsd-audit-uat`, `gsd-add-tests` |
| Load and capacity | [load-and-performance.md](references/load-and-performance.md) | `monitoring-expert`, `sre-engineer`, `backend-core` |
| CI gates and deployment smoke | `delivery-core` | [ci-quality-gates.md](references/ci-quality-gates.md) |
| Authentication and authorization cases | `auth-core` | `security-best-practices` |
| Threat-driven security verification | `security-threat-model` | `security-best-practices` |

## Test-layer selection

- Use **unit tests** for pure rules, invariants, transformations, validators, and edge cases.
- Use **component tests** for UI states, forms, validation, interactions, and error rendering.
- Use **integration tests** for real databases, caches, queues, filesystem adapters, serialization, and application hosting.
- Use **contract tests** for compatibility between independently changing consumers and providers.
- Use **E2E tests** for complete critical journeys and integration risks that lower layers cannot prove.
- Use **visual tests** for stable pages/components where layout and rendering are part of the contract.
- Use **accessibility automation** as a fast signal, then add keyboard and assistive-technology review for critical flows.
- Use **load tests** only with a workload model, thresholds, representative infrastructure, and observability.
- Use **UAT** to validate business acceptance, not to replace technical regression tests.

## Gate profiles

- **PR fast gate:** lint/typecheck/build as applicable, changed unit/component/integration tests, contract compatibility, focused Chromium E2E, accessibility smoke.
- **Mainline gate:** broad integration suite, critical E2E, Chromium/Firefox/WebKit, approved visual comparisons, artifacts.
- **Staging/release gate:** migrations and rollback evidence, UAT, full supported browser matrix, manual accessibility checks, smoke or average-load test when justified.
- **Scheduled gate:** stress/spike/soak, extended compatibility matrix, deep accessibility review, mutation/property-based checks when useful, flaky-test detection.
- **Post-deploy gate:** safe synthetic/read-only smoke, health and critical dependency signals, rollback readiness.

Read [ci-quality-gates.md](references/ci-quality-gates.md) before authoring or changing CI.

## Evidence contract

Always report:

- scope and environment;
- commit/build/version when available;
- commands executed and exit codes;
- pass/fail/skip counts where available;
- requirements and critical journeys covered;
- artifacts created and their paths;
- for each fix or regression test counted as evidence, the mutation that made it fail (see [test-data-flakiness-and-evidence.md](references/test-data-flakiness-and-evidence.md)), or an explicit statement that it was not proven;
- failures classified with first actionable cause;
- known gaps, waivers, owner, and expiry;
- final verdict: `PASS`, `CONDITIONAL`, `BLOCKED`, or `INCONCLUSIVE`.

Do not call a release `PASS` when a required gate was skipped, a regression test was never shown to fail without its fix, the target was ambiguous, evidence is stale, or critical requirements have no direct evidence.

Read [test-data-flakiness-and-evidence.md](references/test-data-flakiness-and-evidence.md) for isolation, artifact, and quarantine rules.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), report verification with its vocabulary: PASS / FAIL / NOT RUN, never a skipped gate as PASS; use `.harness/scripts/verify.sh` for the change-scoped check and `.pi/laws/proof-obligations.md` to decide which property each test must prove. This skill owns the release-quality verdict; the harness `testing` and `verification` skills own the defect-derived rules above, so extend them rather than copying.

## Cross-core ownership

- Let `frontend-core` own frontend architecture and testability.
- Let `backend-core` own service architecture and production behavior.
- Let `auth-core` own authentication and authorization design.
- Let `design-core` own intended UX and visual language.
- Let `delivery-core` own environments, pipeline mechanics, deploy, rollback, and backups.
- Let `qa-core` own risk coverage, test evidence, acceptance traceability, and the release-quality verdict.

Do not silently redesign another core's area. Report the quality gap and route the required change.

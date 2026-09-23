---
name: frontend-core
description: Orchestrate end-to-end architecture, implementation, review, repair, testing, security, performance, resilience, accessibility, observability, state management, data fetching, forms, validation, and production readiness for Astro, React, and Next.js frontends. Use for new or existing websites, dashboards, SaaS products, Telegram Mini Apps, and web applications when asked to build, structure, improve, audit, refactor, debug, optimize, or prepare them for release.
---

# Frontend Core

Own the frontend outcome from stack selection to verified user journeys. Assemble the smallest relevant train from installed specialist skills; do not require the user to invoke cars manually.

## Non-negotiable defaults

- Detect repository instructions, framework and library versions, rendering mode, package manager, lockfile, test stack, browser targets, deployment shape, and existing conventions before advising or editing.
- Default to Astro for content-first and mostly static sites, and Next.js App Router for application-heavy products. Preserve an existing suitable framework; never migrate for fashion.
- Prefer route colocation for small projects, feature-first boundaries as complexity grows, and bounded domain modules only when domain/team complexity justifies them. DDD is not a folder template.
- Use TypeScript in strict mode for new work. Preserve compatibility in existing projects and tighten incrementally when a full switch would be disruptive.
- Classify state before choosing a library: local UI, URL/navigation, form, server, shared client, or persisted client. Never mirror TanStack Query data into Zustand.
- Use native/framework capabilities before adding a dependency. Do not install TanStack Query, Zustand, React Hook Form, Zod, nuqs, Tailwind, or another package unless the problem and repository justify it.
- Keep server and client boundaries narrow. Do not move secrets, privileged logic, or authorization decisions into browser code.
- Never read `.env`, `.env.*`, secret stores, credentials, tokens, or key files. Read `.env.example` only and use `secrets-core` for secret workflows.
- Preserve unrelated user changes. Keep changes cohesive and verify observable behavior.

## Resolve guidance conflicts

Apply guidance in this order:

1. explicit user requirements and repository-scoped instructions;
2. behavior of the versions actually installed, verified against current primary documentation when unstable;
3. this skill's ownership, architecture, state, and safety rules;
4. specialist-skill recommendations.

Treat specialist words such as “always”, “never”, fixed thresholds, and universal cache durations as hypotheses unless they express a real correctness or security invariant. Measure performance and derive freshness, retry, and persistence policies from product requirements.

## Select the operating mode

- **Create:** choose the stack and architecture, implement the requested product, add proportional tests, and verify a production build.
- **Improve/fix:** establish a baseline, make the smallest effective change, and prove the regression is resolved.
- **Audit:** inspect and report evidence without modifying files or external systems.
- **Audit and repair:** prioritize findings, repair authorized issues, and re-run the quality gate.
- **Debug:** reproduce and explain the cause; implement only when the user asks for a fix.
- **Production readiness:** verify security, performance, accessibility, telemetry, browser behavior, build output, and critical journeys.

## Mandatory baseline

Read each selected skill's `SKILL.md` before applying it.

| Area | Skill or reference | Requirement |
| --- | --- | --- |
| Type safety | `typescript` | Apply to TypeScript implementation and configuration |
| Secrets | `secrets-core` | Enforce the `.env.example`-only boundary |
| Security | `security-best-practices`, [error-resilience-security.md](references/error-resilience-security.md) | Review browser trust boundaries and changed attack surface |
| Verification | `run-tests` plus repository commands | Run proportional typecheck, lint, tests, and production build |
| UX implementation | `design-core` | Use for user-facing visual or interaction work; preserve its no-generated-SVG policy |

For public indexable pages, include `seo-core`. For login, sessions, permissions, or protected navigation, include `auth-core`. For API contract changes, include `backend-core`. For hosting, CI/CD, release, or production checks, include `delivery-core`.

## Route by framework and architecture

- Read [stack-and-architecture.md](references/stack-and-architecture.md) for new projects, structural changes, module-boundary problems, or uncertain stack selection.
- For Astro, read [astro.md](references/astro.md). Use Astro components and zero client JavaScript by default; add React islands only for actual interaction.
- For Next.js, use `nextjs`, `react-best-practices`, and `composition-patterns`. Detect the installed Next.js version before applying version-specific cache, routing, proxy, or Server Action rules.
- Use `feature-arch` for architecture design, migration blueprints, import-boundary audits, or a codebase that has outgrown route colocation. Do not generate a large architecture document for routine feature work.
- For React component APIs or boolean-prop proliferation, use `composition-patterns`.

## Route by concern

| Concern | Skills or references | Include when |
| --- | --- | --- |
| State and URL | [state-and-url.md](references/state-and-url.md), `nuqs` | Shared client state, filters, pagination, search parameters, persistence |
| Server data/cache | `tanstack-query`, [data-and-api-contracts.md](references/data-and-api-contracts.md) | Client refetch, polling, mutations, optimistic UI, infinite data, client cache |
| .NET API contract | [data-and-api-contracts.md](references/data-and-api-contracts.md), `backend-core` | ASP.NET OpenAPI, generated TypeScript clients, Problem Details, compatibility |
| Forms/validation | `react-hook-form`, `zod`, [forms-and-validation.md](references/forms-and-validation.md) | Non-trivial forms, runtime validation, field arrays, server errors |
| Form audit | `react-hook-form-audit` | Explicit form audit or material RHF-heavy review |
| Styling | `tailwind`, `design-core` | Tailwind v4 projects; use scoped CSS/CSS Modules without this car |
| Expressive public website | `craft-distinctive-websites`, `design-core`, `motion-core` | Reference-driven, cinematic, tactile, typographic, experimental, Canvas, WebGL, or 3D presentation |
| Unit/component tests | `vitest`, [testing-quality.md](references/testing-quality.md) | TypeScript logic, hooks, components, test setup |
| HTTP mocking | `msw` | Deterministic API scenarios in tests or development |
| Browser journeys | `playwright`, `e2e-testing-patterns` | Critical flows, responsive/browser behavior, release smoke tests |
| Performance | `performance`, `core-web-vitals`, `react-best-practices`, [performance-observability.md](references/performance-observability.md) | Broad audit, measured regression, production readiness |
| Accessibility | `accessibility`, `web-quality-audit` | User-facing implementation, audit, or release readiness |
| Observability | `sentry-react-sdk`, `sentry-nextjs-sdk`, [performance-observability.md](references/performance-observability.md) | Existing/selected Sentry, error monitoring, traces, release correlation |
| Internationalization | [i18n-and-dependencies.md](references/i18n-and-dependencies.md) | Multiple locales, currency/time-zone behavior, locale routing, future-ready formatting |

Sentry is optional. Do not introduce a provider solely because its skill is installed.

## Execute the workflow

### 1. Inventory the real application

Map:

- public routes, protected routes, layouts, rendering boundaries, interactive islands/components, and critical user journeys;
- feature/domain ownership, import direction, shared code, generated code, styling system, and design tokens;
- each state value's owner and lifetime;
- API clients, server reads, browser reads, query keys, cache layers, mutations, validation, and error contracts;
- tests, CI gates, bundle analysis, accessibility checks, telemetry, supported browsers, and deployment assumptions.

Separate confirmed evidence from assumptions. Establish existing failures before editing.

### 2. Select the simplest sustainable structure

Apply [stack-and-architecture.md](references/stack-and-architecture.md). Keep one-off code close to its route. Extract a feature only when cohesion, reuse, ownership, or testing improves. Introduce domains/bounded contexts because business boundaries demand them, not because the repository crossed an arbitrary size.

Enforce public module APIs and unidirectional dependencies. Avoid top-level dumping grounds such as generic `components`, `hooks`, `services`, `utils`, or `types` when business behavior becomes fragmented.

### 3. Place rendering and interaction boundaries

Keep Astro static and Next.js Server Components as the default where applicable. Hydrate or mark client code only when state, events, effects, or browser APIs require it. Keep client providers as deep as practical and minimize serialized server-to-client data.

Use composition for flexible component APIs. Preserve semantic HTML, keyboard behavior, focus management, responsive behavior, and all meaningful UI states.

For expressive reference-driven sites, keep semantic content as the base layer and art direction as progressive enhancement. Recompose wide layouts for narrow screens instead of scaling or clipping the desktop canvas. Isolate optional motion/Canvas/3D in leaf boundaries with a meaningful poster, bounded loader, and static failure path.

### 4. Assign state and data ownership

Apply [state-and-url.md](references/state-and-url.md) before adding or extending a store. Keep server data in the server/framework cache or TanStack Query, shareable navigation state in the URL, form state in the form, and ephemeral state locally.

Apply [data-and-api-contracts.md](references/data-and-api-contracts.md). Generate clients from a trustworthy OpenAPI contract when available. Define cache freshness, invalidation, cancellation, pagination, retries, and optimistic behavior from business semantics.

### 5. Implement forms and complete UI states

Apply [forms-and-validation.md](references/forms-and-validation.md). Use native forms for simple cases and RHF for justified complexity. Validate untrusted input at the appropriate runtime boundary; client validation improves UX but never replaces server validation.

Cover applicable loading, success, empty, stale, offline, validation, unauthorized, forbidden, not-found, rate-limited, partial-success, and unexpected-error states.

### 6. Engineer resilience and browser security

Apply [error-resilience-security.md](references/error-resilience-security.md). Cancel obsolete work, prevent duplicate submissions, bound retries, preserve idempotency, isolate failures, sanitize untrusted content, minimize browser storage, and keep authorization server-side.

### 7. Test by risk

Apply [testing-quality.md](references/testing-quality.md). Prefer deterministic logic tests, behavior-oriented component tests, MSW-backed API scenarios, and Playwright for the few journeys whose end-to-end failure would materially harm the product.

Do not optimize for a vanity coverage number. Include negative, permission, error, and mobile cases proportional to risk.

### 8. Measure and instrument

Apply [performance-observability.md](references/performance-observability.md). Run a production build and measure before optimizing. Inspect bundle size, hydration, waterfalls, images, fonts, third-party scripts, long tasks, subscriptions, and Core Web Vitals.

Capture unexpected errors and useful performance signals with release correlation and request IDs while excluding secrets and unnecessary personal data.

### 9. Re-run the full gate

Run repository-native formatting, lint, typecheck, unit/component tests, affected E2E journeys, accessibility checks, production build, and relevant security/performance checks. State exact commands and unavailable checks.

## Completion gate

Do not call frontend work complete until applicable statements are true:

- framework, versions, rendering model, architecture, and module ownership are explicit;
- state and cache ownership have no avoidable duplication;
- server/client and trust boundaries are correct;
- API contracts, validation, cancellation, errors, retries, and mutations are coherent;
- meaningful loading, empty, error, permission, offline, and responsive states work;
- no secret values were inspected or exposed and browser storage contains no inappropriate credentials;
- typecheck, lint, relevant tests, production build, and critical browser journeys pass or exact failures are reported;
- accessibility and performance were verified proportionally rather than assumed;
- telemetry is useful, privacy-aware, and release-correlated when production observability is in scope;
- integration with design, SEO, auth, backend, and delivery cores has no silent gap.

## Completion response

Lead with the frontend outcome. Report material architectural or implementation changes, user journeys verified, checks actually run, and remaining risk or deployment assumptions. Do not dump internal skill invocations unless asked.

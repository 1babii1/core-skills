---
name: backend-core
description: Orchestrate end-to-end architecture, implementation, audit, repair, testing, security, performance, resilience, observability, data access, API design, and production readiness for .NET and ASP.NET Core backends. Use for new or existing APIs, services, monoliths, modular monoliths, microservices, workers, integrations, and backend libraries when asked to build, improve, review, harden, optimize, debug, or prepare them for deployment.
---

# Backend Core

Own the .NET backend outcome from architecture to verified production readiness. Assemble the smallest relevant train from installed specialist skills, make authorized changes, and return one evidence-based result. Do not require the user to invoke cars manually.

## Scope and defaults

- Optimize for modern supported .NET and ASP.NET Core. Detect the repository's actual SDK, target frameworks, package versions, test platform, architecture, and deployment shape before advising.
- Consult current primary documentation when framework APIs, security guidance, compatibility, support status, or package behavior may have changed.
- Preserve working project conventions unless they create a demonstrated risk. Avoid architecture rewrites for style alone.
- Prefer the simplest architecture that satisfies current scale and reliability requirements. Do not introduce microservices, queues, Redis, distributed transactions, or extra abstraction without a concrete need.
- Treat correctness, security, operability, maintainability, and performance as one system. Do not optimize benchmark numbers while weakening another property.
- Never read `.env`, `.env.*`, secret stores, key files, tokens, or credentials. Read `.env.example` only and use `secrets-core` for secret workflows.
- Preserve unrelated user changes. Keep edits small, cohesive, and verifiable.

## Establish the operating mode

Infer the narrowest mode that fulfills the request:

- **Create:** design and implement a new backend or capability with tests and operational foundations.
- **Improve/fix:** diagnose, modify, and verify a scoped existing system.
- **Audit:** inspect and report evidence; do not modify files or external systems.
- **Audit and repair:** establish a baseline, prioritize findings, fix authorized issues, and prove improvements.
- **Debug:** reproduce and explain the cause; implement only when the user asks for a fix.
- **Production readiness:** validate deployment, failure behavior, telemetry, security, migrations, and rollback assumptions.

For broad requests, cover the entire lifecycle. For focused requests, run only the affected deep-dive cars while still applying mandatory baselines.

## Mandatory baseline cars

Read each named skill's `SKILL.md` before applying it.

| Car | Skill | Required behavior |
| --- | --- | --- |
| Platform | `aspnet-core` | Always inspect hosting, middleware, DI, configuration, framework conventions, and supported-version behavior |
| Authentication boundary | `auth-core` | Always inventory authentication and authorization; if none exists, verify that public/trusted access is deliberate and documented |
| Secrets | `secrets-core` | Always enforce `.env.example`-only agent inspection and production-safe secret handling |
| Verification | `run-tests` plus repository commands | Always run proportional build/test checks and report what was not exercised |

`auth-core` is part of the core, never a Duende-conditional wagon. Duende-specific skills are not part of `backend-core`. If an existing client project already uses Duende, preserve it and use its official documentation only for that project.

## Specialist cars

| Area | Skills or references | Include when |
| --- | --- | --- |
| HTTP API | `dotnet-webapi`, [api-and-data.md](references/api-and-data.md) | REST/HTTP endpoints, contracts, OpenAPI, validation, errors, pagination, compatibility |
| Architecture/code | [architecture-and-code.md](references/architecture-and-code.md) | New services, material refactors, boundary or dependency problems |
| EF Core/data | `optimizing-ef-core-queries`, [api-and-data.md](references/api-and-data.md) | EF Core, SQL, transactions, migrations, concurrency, query performance |
| Data layer | `data-core` | Schema design, index and plan work, migration operations, caching policy, PII/retention, backup and restore readiness |
| Tests | `code-testing-agent`, `test-gap-analysis`, `test-anti-patterns`, `coverage-analysis` | Add tests, assess strength, locate risk, or audit an existing suite |
| Security | `security-threat-model`, [security-and-supply-chain.md](references/security-and-supply-chain.md) | New trust boundaries, exposed services, security review, material flow changes |
| Static analysis | Semgrep CLI or official container | Always attempt for create/audit/repair when available; use C#/.NET-relevant trusted rules and report unavailable tooling |
| Observability | `configuring-opentelemetry-dotnet`, [production-readiness.md](references/production-readiness.md) | Services, distributed calls, diagnostics, production readiness |
| Performance | `analyzing-dotnet-performance`, [performance.md](references/performance.md) | Hot paths, resource pressure, latency/throughput concerns, broad audit |
| Reliability | [reliability.md](references/reliability.md) | Remote calls, queues, workers, concurrency, retries, idempotency, graceful degradation |
| Redis | `redis-core`, `redis-connections`, `redis-security`, `redis-observability` | Only when repository dependencies or requirements actually use Redis |
| Runtime E2E | `playwright` | Browser-backed flows, deployed smoke tests, or UI-to-API journeys |

Grafana MCP is an operational adapter, not a core skill. Use it only when a real Grafana instance and approved read-only credentials are available through the secret workflow.

## Execute the workflow

### 1. Inventory before judging

Read repository instructions and map:

- solution/projects, target frameworks, SDK pinning, central package management, analyzers, nullable settings, and warnings policy;
- entry points, middleware order, endpoint surfaces, background workers, service boundaries, and dependency direction;
- databases, caches, queues, object stores, external APIs, scheduled jobs, and consistency boundaries;
- configuration contracts from tracked examples, deployment manifests, proxy/load-balancer assumptions, and documented commands;
- tests, coverage artifacts, CI gates, telemetry, health checks, and operational documentation.

Build a compact request/data/failure map. Distinguish confirmed repository evidence from assumptions. Do not recommend a pattern before identifying the problem it solves.

### 2. Establish a baseline

Use the repository's documented restore, build, format/analyzer, and test commands. Capture existing failures before editing. For a runnable service, exercise representative endpoints and observe logs/metrics/traces when available.

Run package vulnerability and outdated-package checks supported by the repository/SDK. Run Semgrep when available. Never silently upgrade dependencies or apply broad autofixes; evaluate compatibility and scope first.

### 3. Design or review boundaries

Apply [architecture-and-code.md](references/architecture-and-code.md). Keep domain rules independent from transport and infrastructure where that reduces coupling. Define ownership of data, transactions, side effects, external calls, and failure recovery. Prefer vertical slices or cohesive modules over ceremonial layers.

Use `auth-core` to establish the auth boundary even for internally exposed services. Mark every public endpoint and privileged operation intentionally.

### 4. Implement contracts and data behavior

Apply `dotnet-webapi` and [api-and-data.md](references/api-and-data.md) for HTTP work. Validate at trust boundaries, use correct status semantics, return safe structured errors, document contracts, bound collections/uploads, propagate cancellation, and preserve compatibility.

For data work, make transaction and concurrency semantics explicit. Inspect generated SQL and query shape before optimizing. Treat schema/data migrations as deployment operations with forward/rollback or roll-forward consequences.

### 5. Engineer failure behavior

Apply [reliability.md](references/reliability.md). Set explicit timeouts, propagate cancellation, bound concurrency and queues, retry only safe transient operations, add jitter where appropriate, and prevent retry amplification. Make duplicate delivery and partial failure safe through idempotency, transactional boundaries, outbox/inbox patterns, or reconciliation when justified.

Define behavior for database, cache, queue, external provider, DNS, storage, and dependency outages. Do not turn a cache miss or telemetry failure into a full outage unless requirements demand it.

### 6. Secure the system

Apply [security-and-supply-chain.md](references/security-and-supply-chain.md) and `auth-core`. Threat-model material trust-boundary changes. Review input/output handling, authorization, tenant/resource isolation, SSRF, injection, deserialization, uploads, secret exposure, dependency risk, debug endpoints, unsafe logging, rate limits, and denial-of-service amplification.

Treat LLM review and Semgrep as complementary. Never claim Semgrep proves security, and never replace deterministic analysis with a prose review.

### 7. Test behavior, not implementation trivia

Run existing tests first. Add the cheapest test at the strongest useful boundary:

- unit tests for dense deterministic domain rules;
- integration tests for database behavior, middleware, serialization, auth, queues, and external adapters;
- contract tests for published or consumed interfaces;
- E2E/smoke tests for critical deployed journeys.

Use `test-gap-analysis` for high-risk changed paths, `test-anti-patterns` for suspicious suites, and coverage/CRAP as navigation rather than a vanity target. Require negative and failure-path tests proportional to risk.

### 8. Measure performance

Apply [performance.md](references/performance.md). Establish a representative workload and baseline before optimizing. Inspect database round trips, allocations, serialization, networking, contention, thread-pool starvation, GC, caching, payload size, and downstream latency. Re-measure with the same method after changes.

### 9. Establish observability and production readiness

Apply `configuring-opentelemetry-dotnet` and [production-readiness.md](references/production-readiness.md). Provide correlated structured logs, metrics, and traces without sensitive data. Define useful health/readiness behavior, graceful shutdown, resource limits, deployment ordering, migration strategy, rollback/roll-forward, alerts, dashboards, and runbook-worthy failure signals.

Do not confuse “container starts” with production readiness.

### 10. Re-run the full gate

Re-run formatting/analyzers, build, tests, vulnerability checks, Semgrep, representative integration/E2E flows, and any performance comparison affected by the change. Compare against the baseline. If a gate is unavailable, state the exact missing tool/environment and provide the next executable check.

## Prioritization

Order broad audit work by expected damage and dependency:

1. data loss/corruption, authentication bypass, authorization failure, secret/key exposure, critical injection or remote execution;
2. broken contracts, migrations, concurrency, idempotency, and outage amplification;
3. unbounded resource use, severe query/latency issues, missing operational visibility;
4. weak tests around high-risk behavior and maintainability hazards;
5. low-impact style, speculative abstraction, and micro-optimization.

Use severity, evidence, affected scope, exploit/failure path, recommended change, risk, and verification. Avoid one opaque quality score.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), public contracts, concurrency, migrations, and authentication changes are high-risk there: derive proof obligations from `.pi/laws/proof-obligations.md`, use `.harness/scripts/verify.sh` for the change-scoped check (PASS / FAIL / NOT RUN; a green build proves compilation only), and run the `independent-verifier` before completion. An idempotency check backed only by a prior read is check-then-act: prove it with a concurrent test seeded against an aggregate that already has related rows. A new package needs a known-vulnerability check (`dotnet list package --vulnerable --include-transitive`), not just a successful build. This skill owns the backend domain; the harness owns the evidence bar.

## Completion gate

Do not call work complete until applicable statements are true:

- architecture, trust boundaries, public surface, data ownership, and failure semantics are explicit;
- `auth-core` baseline has been applied and privileged access defaults closed;
- configuration and secrets are production-safe and no secret values were inspected or exposed;
- HTTP/data contracts, migrations, concurrency, cancellation, timeouts, and idempotency are correct for the changed scope;
- build, analyzers, relevant tests, vulnerability checks, and static analysis pass or failures are clearly reported;
- changed critical paths have positive, negative, and failure-mode coverage;
- performance claims have comparable measurements;
- telemetry, health behavior, shutdown, deployment, migration, and recovery assumptions are addressed;
- implemented fixes are re-verified from observable behavior, not code inspection alone.

## Completion response

Lead with the backend outcome. Report material changes/findings, evidence and checks actually run, remaining risk or deployment assumptions, and the single most valuable next step only when one remains. Do not dump internal skill invocations unless the user asks.

---
name: delivery-core
description: Orchestrate safe end-to-end delivery of .NET, ASP.NET Core, Next.js, Astro, static web, worker, and Telegram applications from CI through production verification and operations. Use when asked to containerize, configure CI/CD, publish, deploy, host, release, migrate, operate, monitor, roll back, recover, or assess production readiness on a PaaS, VPS, container platform, or static host.
---

# Delivery Core

Own the delivery outcome from a reproducible build to a verified, observable, recoverable release. Assemble the smallest relevant train from installed specialist skills; do not require the user to invoke cars manually.

## Non-negotiable boundaries

- Detect repository instructions, stack, runtime, package manager, deployment target, environments, data stores, background work, and existing delivery conventions before proposing changes.
- Prefer the simplest target that meets the actual availability, scale, latency, legal, geographic, and budget constraints. Do not introduce Kubernetes, Terraform, service meshes, or multi-region infrastructure without a demonstrated need.
- Treat production deployment, DNS cutover, database mutation, resource creation, and destructive rollback as external state changes. Execute them only when the user's request authorizes that scope and the exact target is resolved.
- Default vendor deployment skills to preview or staging. Deploy production only when production is explicit.
- Never read, search, display, copy, diff, summarize, or edit `.env`, `.env.*`, SOPS vaults, age identities, credential files, keychains, or secret values. Read `.env.example` only.
- Use names and placeholders from `.env.example`. Direct interactive secret creation or rotation through `~/.local/bin/secrets-edit <vault>`. Use `~/.local/bin/secrets-run <vault> -- <command>` only for the narrow application process that requires the vault.
- Never place a credential in a command argument, generated file, log, artifact, image layer, CI output, patch, commit, or response.
- Build an immutable artifact once and promote the same artifact between environments. Do not rebuild source independently for production.
- Preserve unrelated user changes and existing working infrastructure.

## Select an operating mode

Infer the narrowest mode that fulfills the request:

- **Design:** produce a deployment architecture, target choice, release sequence, risk analysis, and executable validation plan without changing external systems.
- **Prepare:** create or repair containers, workflows, manifests, health checks, observability, runbooks, and configuration contracts.
- **Preview/staging:** deploy to a non-production target, verify it, and return evidence.
- **Production release:** run approved gates, deploy the resolved artifact to the resolved target, verify behavior and telemetry, and roll back only when the defined trigger and authority permit it.
- **Audit:** inspect and report evidence without modifying files or external systems.
- **Incident/recovery:** stabilize service and data first, preserve evidence, follow the runbook, verify recovery, and document remaining risk.

## Mandatory train

Read each selected skill's `SKILL.md` before applying it.

| Car | Skill | Responsibility |
| --- | --- | --- |
| Secrets boundary | `secrets-core` | Enforce `.env.example`-only inspection and safe runtime injection |
| Delivery implementation | `devops-engineer` | Containers, delivery automation, artifacts, deployment strategies, and operational implementation |
| Pipeline architecture | `deployment-pipeline-design` | Environments, gates, promotion, rollout, health criteria, and rollback design |
| Workflow implementation | `github-actions-templates` | Create general GitHub Actions workflows when GitHub Actions is used |
| Workflow correctness | `authoring-github-workflows` | Validate Actions YAML and expressions with `actionlint` |
| CI diagnosis | `gh-fix-ci` | Diagnose and repair failed GitHub Actions checks when requested |
| Verification | `run-tests` and repository commands | Run proportional build, test, lint, and package checks |

For deployment or production-readiness work, also apply:

| Area | Skills |
| --- | --- |
| Runtime journey | `playwright`, and `e2e-testing-patterns` when establishing or repairing E2E coverage |
| Observability | `monitoring-expert`; add `configuring-opentelemetry-dotnet` for .NET |
| Reliability | `sre-engineer` |
| Incident documentation | `incident-runbook-templates` |
| Cost | `cost-optimization` when a paid or elastic platform is involved |
| Security | `security-best-practices` plus repository-native dependency, container, and static-analysis tools |

Do not duplicate a specialist's full guidance in this skill. Use the references below only for routing and stack-specific delivery gaps.

## Route by stack and target

- For ASP.NET Core or .NET workers, read [dotnet-deployment.md](references/dotnet-deployment.md) and use `aspnet-core`.
- For Next.js, read [nextjs-deployment.md](references/nextjs-deployment.md).
- For Astro, read [astro-deployment.md](references/astro-deployment.md).
- For schema changes, persistent data, backups, or recovery, read [data-and-recovery.md](references/data-and-recovery.md). Use `data-core` to design or review the migration, caching, and restore requirements this pipeline must satisfy, and `postgres-pro` only when PostgreSQL is actually present.
- After the release, hand ongoing operation, monitoring, incidents, upgrades, and support to `maintenance-core`.
- For VPS, DNS, TLS, CDN, reverse proxy, PaaS, or provider choice, read [edge-and-platforms.md](references/edge-and-platforms.md). Use `nginx` for every Nginx configuration change.
- For smoke tests, observability, rollback decisions, release evidence, or incident readiness, read [verification-and-operations.md](references/verification-and-operations.md).
- For complete pipeline ordering and artifact rules, read [pipeline-and-artifacts.md](references/pipeline-and-artifacts.md).

## Delivery workflow

### 1. Inventory the real system

Map:

- source entry points, SDK/runtime pins, lockfiles, build commands, tests, and generated artifacts;
- static, server-rendered, API, worker, scheduled, queue-consuming, WebSocket, SignalR, and Telegram processes;
- domains, proxy/CDN topology, public ports, callback URLs, trust boundaries, and health endpoints;
- databases, migrations, persistent volumes, object storage, caches, queues, backup ownership, and recovery requirements;
- environments, registries, CI permissions, deployment credentials by name only, and the `.env.example` contract;
- current release path, downtime tolerance, rollback method, RPO/RTO, traffic, geographic access, and cost ceiling.

Separate confirmed evidence from assumptions. Verify current platform availability, pricing, regional restrictions, runtime support, and framework adapters against primary documentation before choosing a provider.

### 2. Establish a baseline

Run the repository's documented restore/install, build, lint/analyzer, and test commands before editing. Inspect existing CI and manifests. Record pre-existing failures without hiding them.

Validate the planned production topology locally or in staging when feasible. A successful development server is not deployment evidence.

### 3. Design the release

Use `deployment-pipeline-design` to define:

1. source and change trigger;
2. deterministic dependency restore;
3. build, analyzers, unit/integration/E2E tests, and security gates;
4. immutable artifact or image with commit/version identity;
5. preview/staging deployment;
6. controlled schema migration ordering;
7. production rollout;
8. post-deploy health, smoke, logs, metrics, and traces;
9. automatic stop/rollback thresholds and a manual recovery path.

Prefer a single VPS with containers and Nginx for small workloads when it satisfies requirements. Prefer a PaaS when its supported features, access, pricing, data location, and lock-in are acceptable. Escalate to orchestration only when measured needs justify it.

### 4. Implement reproducible artifacts and CI

Use `devops-engineer`, `github-actions-templates`, and `authoring-github-workflows`.

- Pin the SDK/runtime and use repository lockfiles.
- Use multi-stage container builds when containers are selected.
- Keep the runtime image minimal, non-root, signal-aware, and free of build tools and secrets.
- Add `.dockerignore`, health/readiness behavior, resource expectations, and persistent-volume ownership where applicable.
- Tag artifacts immutably; never deploy mutable `latest` as the release identity.
- Grant CI jobs the minimum permissions and isolate build, deploy, and production approval authority.
- Validate workflow structure with `actionlint` and validate container/manifests with their native tools.

### 5. Prepare stateful changes

Apply [data-and-recovery.md](references/data-and-recovery.md). Never let every application replica race to apply production migrations. Test migrations against production-like data and define compatibility with both old and new application versions.

Before a destructive or hard-to-reverse change, require a verified recovery point and an explicit cutover plan. Prefer roll-forward when reversing data transformation would lose information.

### 6. Deploy progressively

Deploy preview or staging first when available. Verify the exact artifact there. For production, resolve the application, account/project, environment, region, domain, image digest/version, and migration set before changing state.

Use rolling, blue-green, or canary only when the target and application support the required health, traffic, session, cache, and version-skew semantics. Otherwise use a simple, documented maintenance deployment rather than pretending it is zero-downtime.

### 7. Prove the release

Apply [verification-and-operations.md](references/verification-and-operations.md):

- verify process/container health and readiness;
- exercise the API and critical user journey;
- validate auth callbacks, uploads, static assets, WebSocket/SignalR/streaming, workers, and scheduled jobs that are in scope;
- inspect sanitized logs, metrics, and traces for the deployed version;
- confirm migration state and data invariants without exposing records or credentials;
- test rollback or recovery in staging when the production procedure is material.

Do not mark a release successful merely because a command exited zero or a URL exists.

### 8. Operate and hand off

Use `monitoring-expert`, `sre-engineer`, `incident-runbook-templates`, and `cost-optimization` proportionally. Define actionable alerts, ownership, escalation, retention, budget thresholds, backup monitoring, certificate expiry monitoring, and a short runbook.

Report the deployed version/digest, target, checks actually run, observable result, migration state, rollback point, and any unresolved risk. Never include secret values.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), production infrastructure, migrations in the pipeline, and destructive operations are high-risk there: derive proof obligations from `.pi/laws/proof-obligations.md` (Migration, Destructive / irreversible operation), ask what is true only because exactly one instance runs and is written down nowhere, and run the `pi-independent-verifier` before declaring a production change done. This skill owns pipeline and deployment mechanics; the harness owns the evidence bar.

## Completion gate

Do not call delivery complete until applicable statements are true:

- the target, environment, domain, artifact identity, runtime topology, and data dependencies are explicit;
- `.env.example` is the only inspected environment contract and runtime secrets are injected outside agent context;
- restore/build/test/security/workflow gates pass or exact failures are reported;
- the same immutable artifact tested in staging is promoted to production;
- Nginx, TLS, proxy headers, streaming, callback URLs, and public exposure are correct for the topology;
- database migration ordering, backward compatibility, backup, restore, and rollback/roll-forward assumptions are documented and proportionally tested;
- health, critical smoke/E2E behavior, logs, metrics, traces, and background processes are verified after deployment;
- rollback/recovery triggers and authority are clear;
- cost, certificate, storage, backup, and incident ownership have no silent gap.

## Completion response

Lead with the delivery outcome. State what is live or prepared, exact non-secret target and artifact identity, evidence from checks, migration/recovery state, and remaining risk. If production was not authorized or could not be verified, say so plainly. Do not dump internal skill invocations unless asked.

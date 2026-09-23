# Verification and operations gate

Use after deployment and for production-readiness reviews. Apply `playwright`, `monitoring-expert`, `sre-engineer`, and `incident-runbook-templates` proportionally.

## Layered verification

1. **Artifact:** verify version/digest, provenance available from trusted tooling, expected contents, architecture, and vulnerability gate.
2. **Process:** verify desired replicas/processes are running, stable, non-root where intended, within resource limits, and handling termination.
3. **Network:** verify DNS, TLS, proxy routing, ports, redirects, headers, streaming, and CDN behavior.
4. **Health:** verify liveness and readiness independently and confirm failed dependencies produce intended behavior.
5. **Application:** run API smoke tests and the critical Playwright journey using non-sensitive test data.
6. **State:** verify migration version, invariants, background jobs, queues, storage, and cache behavior.
7. **Telemetry:** verify sanitized logs, metrics, traces, release/version identity, dashboards, and alerts.

Capture exact commands/checks and observable outcomes without printing environment or credential state.

## Critical journeys

Choose the smallest high-value set:

- public landing and static assets;
- sign-in, callback, sign-out, and authorization boundary;
- primary create/read/update operation;
- upload/download when present;
- payment or other irreversible integration in sandbox only;
- WebSocket, SignalR, gRPC, or streamed response;
- Telegram webhook/polling and Mini App init-data validation when present;
- worker or scheduled job completion and idempotent retry.

Do not perform a real purchase, message real users, or mutate production business data unless explicitly authorized.

## Rollback trigger

Define before release:

- health/readiness failure duration;
- error-rate and latency threshold;
- crash/restart threshold;
- failed critical journey;
- data-integrity or migration failure;
- human stop authority.

Rollback only when the prior version remains compatible and rollback is authorized. Otherwise stop traffic or new work, preserve evidence, and execute the roll-forward/recovery runbook.

## Observability minimum

- structured logs with correlation and release identity;
- request/error/latency and resource saturation metrics;
- traces across meaningful remote boundaries;
- actionable alerts tied to user impact;
- dashboard or query for the release window;
- certificate, backup, disk, queue, and job monitoring where applicable.

Avoid high-cardinality identifiers and sensitive data in telemetry.

## Incident and cost handoff

Use `sre-engineer` for SLO/error-budget decisions and `incident-runbook-templates` for actionable recovery procedures. Use `cost-optimization` to establish budget alerts, retention, rightsizing, and maximum scaling bounds on paid infrastructure.

## Release evidence

Report:

- environment and non-secret target;
- version, commit, artifact tag, and digest when available;
- migration/recovery-point identifiers without sensitive contents;
- checks run and results;
- telemetry observation window;
- rollback state;
- unresolved risks and unverified paths.

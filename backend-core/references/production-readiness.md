# .NET production readiness

Use before deployment and in full backend audits.

## Configuration and runtime

- Pin or document the supported SDK/runtime and base image; use supported patched versions.
- Validate required configuration at startup without printing secret values.
- Keep environment differences explicit and minimize production-only code paths.
- Configure trusted proxies/forwarded headers, HTTPS, ports, DNS, and external URLs correctly.
- Run containers as a non-root user where feasible, with read-only/minimal filesystem access and explicit resource limits.
- Persist only intentional state and key material outside ephemeral containers.

## Health and lifecycle

- Keep liveness cheap and local; use readiness for dependencies required to serve useful traffic.
- Avoid health probes that overload dependencies or reveal sensitive topology.
- Handle SIGTERM: stop intake, propagate cancellation, drain work within the platform grace period, and exit deterministically.
- Verify startup, shutdown, restart, rolling deployment, and dependency-unavailable behavior.

## Observability

- Use structured logs with stable event meaning and correlation/trace identifiers.
- Emit RED signals for request services and USE/saturation signals for constrained resources.
- Trace meaningful cross-service/database/queue operations while controlling sampling and cardinality.
- Exclude secrets, tokens, cookies, raw credentials, sensitive claims, and unnecessary personal data.
- Define alerts from user-impacting symptoms and actionable causes; avoid alerting on every exception.
- Make dashboards/runbooks answer: what broke, who is affected, since when, likely dependency, and safe mitigation.

## Delivery and data

- Build once and promote the same artifact/configure per environment.
- Run tests, analyzers, package audit, Semgrep, image scanning, and artifact provenance/SBOM gates as appropriate.
- Separate application rollout from risky migrations; use expand/migrate/contract for compatible rolling deployments.
- Define rollback versus roll-forward, backup/restore, and disaster-recovery objectives for stateful systems.
- Smoke-test public and privileged critical flows after deployment without exposing secrets.

## Capacity and resilience

- Set requests/limits from measurement; verify behavior under throttling and memory pressure.
- Test realistic concurrency, slow dependencies, connection exhaustion, retries, queue backlog, and cache/database failure.
- Establish latency/error/availability objectives and connect them to telemetry and alerts.
- Record ownership and escalation for production dependencies and security incidents.

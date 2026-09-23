# Load and performance testing

Use k6 OSS by default unless the repository has an established alternative.

## Safety gate

Before any non-trivial load:

- resolve the exact target and owner;
- confirm production versus staging;
- obtain explicit authorization for production;
- define allowed traffic, duration, data mutations, and abort conditions;
- verify monitoring, rollback, rate limits, and emergency contact;
- use dedicated test accounts and safe data;
- avoid third-party costs and real notifications.

If any item is unknown, restrict work to script authoring or a minimal local/staging smoke test.

## Workload model

Derive the workload from analytics, monitoring, forecasts, or explicit assumptions:

- critical scenarios and their traffic share;
- arrival rate or concurrent users;
- think time and session duration;
- payload and data distribution;
- authentication/session behavior;
- cache warm/cold state;
- geographic/network assumptions;
- expected peak and growth factor.

State assumptions when production evidence is unavailable.

## Test types

| Type | Purpose |
|---|---|
| Smoke | Validate script and minimum system behavior |
| Average load | Establish normal-load baseline |
| Stress | Validate behavior above expected peak |
| Spike | Validate sudden traffic change |
| Soak | Find leaks and degradation over time |
| Breakpoint | Find capacity limit; run only with explicit approval |

Run smoke before every larger profile.

## Thresholds

Define pass/fail criteria before running:

- request and business-operation error rate;
- latency percentiles, normally p95 and p99;
- successful throughput;
- saturation signals such as CPU, memory, connections, queues, locks, and pool exhaustion;
- domain correctness, not only HTTP status;
- recovery time after load.

Tie thresholds to SLOs or stated product requirements. Do not invent an aggressive number without labelling it as a provisional budget.

## Observability

Correlate the test run with:

- build/commit and environment;
- scenario and endpoint tags;
- application traces and logs;
- database query/lock/pool metrics;
- cache hit rate and evictions;
- queue depth and processing lag;
- host/container resources;
- dependency latency and error rate.

Route bottleneck diagnosis to `backend-core`, `analyzing-dotnet-performance`, `optimizing-ef-core-queries`, `monitoring-expert`, or `sre-engineer`.

## Result interpretation

Report:

- workload and duration;
- thresholds and result;
- latency percentiles, errors, successful throughput;
- first saturated resource;
- correctness failures;
- comparison with baseline;
- recovery behavior;
- limitations and next experiment.

Do not call a test successful because all requests completed if latency, correctness, or saturation thresholds failed.

# Reliability and failure engineering

Use when a backend performs remote I/O, background processing, messaging, concurrency, or production deployment.

## Time and cancellation

- Set explicit timeouts for database, HTTP, cache, queue, storage, and shutdown operations.
- Propagate request/host cancellation where aborting work is safe.
- Distinguish timeout, caller cancellation, dependency rejection, and internal failure in telemetry and behavior.
- Budget nested timeouts so downstream work cannot exceed the caller's useful deadline.

## Retry discipline

- Retry only classified transient failures and only idempotent/replay-safe operations.
- Use bounded exponential backoff with jitter; honor server retry hints when trustworthy.
- Cap total attempts and elapsed retry budget.
- Prevent retry multiplication across proxy, client, worker, and dependency layers.
- Do not retry validation, authentication, authorization, deterministic business rejection, or unknown write outcomes blindly.

## Load and isolation

- Bound queues, batches, concurrency, request bodies, result sets, and fan-out.
- Apply backpressure or shed load deliberately rather than consuming unlimited memory.
- Use circuit breakers/bulkheads only with measured thresholds and a defined degraded behavior.
- Treat caches as optimization unless explicitly authoritative; define stampede control, TTL, invalidation, and outage behavior.
- Make startup/readiness reflect mandatory dependencies without causing unnecessary cascading restarts.

## Messaging and workers

- Assume at-least-once delivery unless the concrete broker contract proves otherwise.
- Make consumers idempotent or deduplicate at the side-effect boundary.
- Separate transient retry from poison-message handling; use bounded redelivery and observable dead-letter/quarantine behavior.
- Commit message acknowledgement only after owned durable effects meet the consistency contract.
- Version event contracts compatibly and avoid leaking internal persistence models.
- Ensure graceful shutdown stops intake, drains within a deadline, and safely abandons remaining work for redelivery.

## Recovery evidence

For each critical dependency define:

- impact of unavailable, slow, stale, duplicated, or partially successful behavior;
- user/system-visible response;
- retry/degradation/reconciliation strategy;
- alert and diagnostic evidence;
- recovery owner and operational action;
- automated failure-path test where practical.

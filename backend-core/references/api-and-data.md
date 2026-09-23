# API and data contracts

Use for HTTP endpoints, persistence, migrations, and query reviews.

## HTTP/API

- Model resources/actions and choose HTTP semantics intentionally; do not return `200` for every outcome.
- Validate syntax and shape at the transport boundary, business invariants in the owning domain behavior, and authorization against the actual resource.
- Use safe structured errors such as Problem Details without stack traces, SQL, secrets, or internal identifiers.
- Document request/response types, required headers, auth, status codes, pagination, limits, idempotency behavior, and examples in OpenAPI where applicable.
- Bound page sizes, uploads, JSON depth/body size, query complexity, and expensive filters.
- Prefer cursor pagination for large or frequently changing ordered sets; require deterministic ordering.
- Introduce API versioning only for a real compatibility contract. Prefer additive evolution and tolerant readers.
- Propagate trace context and cancellation across outbound calls.

## EF Core/querying

- Project only required columns and avoid materializing before filtering/paging.
- Detect N+1 queries, cartesian explosion, unbounded results, client evaluation assumptions, and unnecessary tracking.
- Use `AsNoTracking` for read-only queries unless identity tracking is required.
- Inspect generated SQL and database execution plans for important/slow paths.
- Add indexes from observed query predicates/order/join patterns; account for write/storage cost and validate in the actual database engine.
- Avoid parallel operations on one `DbContext`; respect its scoped/unit-of-work lifetime.
- Use optimistic concurrency tokens where lost updates matter and define the conflict response.

## Transactions and distributed effects

- Keep local invariants within one database transaction where possible.
- Never assume a database write and message/API call commit atomically.
- Use outbox/inbox, idempotency keys, deduplication, or reconciliation only where duplicate/lost side effects are plausible and material.
- Keep transactions short; avoid remote calls while holding database locks.
- Define isolation needs from anomalies to prevent, not by selecting the strongest level automatically.

## Migrations

- Review generated migrations and SQL; never infer safety from successful generation.
- Separate schema evolution from large data backfills when necessary.
- Prefer expand/migrate/contract for zero-downtime compatibility across old and new application versions.
- Avoid destructive rename/drop/type changes without a verified data-preservation and rollout plan.
- Ensure startup does not let every replica race to apply production migrations.
- Test migrations against representative schema/data and define backup, roll-forward, or rollback handling.

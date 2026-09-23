---
name: data-core
description: "Orchestrate the data layer end to end: schema design, EF Core and SQL query performance, indexing, migrations and zero-downtime evolution, caching, Redis, connection pools, backups and restore drills, PII retention, test-data anonymization, tenant isolation. Use when designing or changing a schema, diagnosing slow queries or database load, planning or reviewing a migration, deciding what to cache, introducing Redis, preparing a restore plan, or auditing how user data is stored and deleted."
---

# Data Core

Own the data outcome: how data is shaped, queried, cached, evolved, protected, and recovered. Assemble the smallest relevant train from installed specialist skills, make authorized changes, and return one evidence-based result. Do not require the user to invoke cars manually.

## Scope boundary

- `backend-core` owns application architecture, HTTP contracts, and transaction semantics inside a service. This skill owns the store itself and the data lifecycle across the project. When a request needs both, run `backend-core` for the service boundary and this skill for the store; do not restate its references, apply them.
- `delivery-core` owns deployment mechanics. This skill defines what a migration or restore must satisfy; `delivery-core` executes it in the pipeline.
- `secrets-core` owns connection strings and credentials. Never read `.env`, `.env.*`, vaults, or credential files. `.env.example` is the only readable environment contract. Never paste a connection string into output.
- `auth-core` owns who may act. This skill owns what rows, columns, and tenants that identity can reach.

## Non-negotiable rules

- Never run destructive SQL — `DROP`, `TRUNCATE`, `DELETE` without a bounded predicate, `UPDATE` without `WHERE`, schema drops — against any database the user has not explicitly named as safe. Read-only inspection is the default.
- Never operate on a production database without explicit per-request authorization, and never as the first attempt when a local, staging, or restored copy answers the same question.
- Prove query behavior with `EXPLAIN (ANALYZE, BUFFERS)` or the engine's equivalent, not by reading ORM code. Prove index adoption with a plan captured after the change.
- Never present a migration as safe because it generated or applied cleanly on an empty local database.
- Never invent row counts, table sizes, latency figures, or cache hit ratios. Measure or label them unknown.
- Never copy production data into a development, test, or demo environment without anonymization.
- A backup is not a backup until a restore has been performed and verified.
- Preserve unrelated user changes. Keep migrations small, reviewable, and individually reversible or explicitly roll-forward-only.

## Establish the operating mode

Infer the narrowest mode that fulfills the request:

- **Design:** model a new schema, data structure, or caching strategy for a capability that does not exist yet.
- **Optimize:** diagnose and fix slow queries, excessive load, lock contention, or cache misbehavior against a measured baseline.
- **Evolve:** plan, review, and sequence a schema or data migration, including compatibility across deployed application versions.
- **Audit:** inspect and report on schema quality, indexing, query patterns, caching, PII handling, and recovery readiness; do not modify anything.
- **Protect:** classify data, define retention and deletion, verify isolation, and prove the restore path.

For broad requests, walk the full workflow. For focused requests, run only the affected cars while still applying the non-negotiable rules.

## Cars

Read each named skill's `SKILL.md` before applying it.

| Area | Skills or references | Include when |
| --- | --- | --- |
| Relational schema | [schema-and-migrations.md](references/schema-and-migrations.md) | New tables, model changes, normalization decisions, keys, constraints, data types |
| PostgreSQL depth | `postgres-pro` | EXPLAIN analysis, index choice, JSONB, extensions, VACUUM/bloat, replication, pg_stat inspection |
| ORM query layer | `optimizing-ef-core-queries`, [backend-core/api-and-data.md](../backend-core/references/api-and-data.md) | EF Core, N+1, tracking mode, projection, compiled queries, generated SQL review |
| Application hot path | `analyzing-dotnet-performance` | Allocation, serialization, or materialization cost that only looks like a database problem |
| Migrations as an operation | [schema-and-migrations.md](references/schema-and-migrations.md), `delivery-core` | Any schema or backfill change reaching a shared or production environment |
| Caching strategy | [caching-strategy.md](references/caching-strategy.md) | Deciding what to cache, TTLs, invalidation, stampede protection, staleness tolerance |
| Redis modeling | `redis-core` | Choosing a data structure, key naming, sessions, counters, leaderboards, membership sets |
| Redis client behavior | `redis-connections` | Pooling, multiplexing, pipelining, SCAN over KEYS, timeouts, client-side caching |
| Redis hardening | `redis-security` | Any Redis instance reachable beyond localhost: auth, ACL users, TLS, bind and firewall |
| Redis operations | `redis-observability` | Memory, hit ratio, rejected connections, SLOWLOG triage, metrics wiring |
| Data lifecycle | [data-lifecycle.md](references/data-lifecycle.md) | PII classification, retention, deletion requests, test data, anonymization, tenant isolation |
| Backup and recovery | [data-lifecycle.md](references/data-lifecycle.md), [delivery-core/data-and-recovery.md](../delivery-core/references/data-and-recovery.md) | Recovery readiness, restore drills, RPO/RTO, pre-migration safety |
| Telemetry | `configuring-opentelemetry-dotnet`, `monitoring-expert` | Database spans, query duration metrics, pool exhaustion signals, alert thresholds |
| Live inspection | Available Postgres MCP servers | A real database is reachable and read-only inspection beats guessing from code |
| Verification | `qa-core`, `run-tests` | Migrations, repositories, or query changes need behavioral proof |

## Execute the workflow

### 1. Inventory the store before judging it

Map from repository evidence:

- engines in use, versions, hosting shape, and who owns each store;
- schema source of truth — migrations, SQL files, or ORM model — and whether they agree;
- entities, relationships, keys, constraints, indexes, and data types actually declared;
- query entry points, repositories, raw SQL, background jobs, and reporting paths;
- caches, their keys, TTLs, and who invalidates them;
- connection configuration, pool sizes, and timeouts from tracked examples only;
- backup configuration, retention, and any evidence a restore has ever been tested.

Distinguish confirmed evidence from assumption. Where a live database is reachable and read-only inspection is authorized, prefer `pg_stat_statements`, `pg_stat_user_tables`, and index-usage views over reasoning from code.

### 2. Establish a measured baseline

Before changing anything, capture: the slow query set with call counts and mean time, the plan for each target query, table and index sizes, dead-tuple ratios, cache hit ratio, and pool saturation. Record the exact method and date. Optimization claims later compare against this, using the same method.

### 3. Design or review the schema

Apply [schema-and-migrations.md](references/schema-and-migrations.md). Model the invariants the database must enforce itself — keys, foreign keys, uniqueness, check constraints, not-null, correct types — before pushing rules into application code. Choose normalization by access pattern and write frequency, and justify every denormalization with the read it serves. Decide deliberately between a relational column, a JSONB document, and a separate store; do not let JSONB become an untyped escape hatch.

### 4. Fix queries at the right layer

Diagnose in order: plan, index, query shape, ORM behavior, then application code. Apply `optimizing-ef-core-queries` for N+1, tracking, and projection problems, and `postgres-pro` for plans, index types, and statistics. Add indexes from observed predicates, ordering, and joins — not speculatively — and account for write and storage cost. Verify with a plan captured after the change, and confirm no other query regressed.

### 5. Design caching as a policy, not a reflex

Apply [caching-strategy.md](references/caching-strategy.md). Do not introduce a cache before the underlying query has been measured and optimized. Every cached value needs a named owner, a staleness tolerance, an invalidation trigger, and defined behavior when the cache is empty, stale, or unavailable. Apply `redis-core` for structure and key naming, `redis-connections` for client behavior, and `redis-security` before any instance leaves localhost.

### 6. Treat migrations as production operations

Apply [schema-and-migrations.md](references/schema-and-migrations.md). Review the generated SQL, not just the migration class. Separate schema change from large backfill. Use expand/migrate/contract whenever old and new application versions will run concurrently. Establish a fresh verified backup before any destructive or irreversible step, state the rollback or roll-forward path explicitly, and ensure only one replica applies migrations.

### 7. Protect and prove recovery

Apply [data-lifecycle.md](references/data-lifecycle.md). Classify what personal or sensitive data the schema holds, where it is duplicated, how long it is kept, and how a deletion request is satisfied across tables, backups, logs, and caches. Verify tenant and row-level isolation with a negative test, not a code reading. Confirm backup coverage, RPO/RTO, and the date of the last successful restore drill.

### 8. Verify from behavior

Run the repository's migration, build, and test commands. Prove migrations against representative schema and data, including a rollback or roll-forward rehearsal where one is claimed. Re-measure the queries captured in step 2 with the same method. Report what was not exercised.

## Prioritization

Order broad audit work by expected damage:

1. data loss, corruption, irreversible migration, missing or unverified backup, cross-tenant leakage;
2. secrets in connection handling, unauthenticated or exposed store, over-privileged database account;
3. broken constraints and invariants the application silently depends on;
4. lock contention, pool exhaustion, unbounded result sets, and queries that degrade with data growth;
5. missing indexes, avoidable round trips, weak cache invalidation;
6. schema style, naming, and speculative optimization.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), migrations, constraints, indexes, and destructive operations are high-risk there: derive proof obligations from `.pi/laws/proof-obligations.md` (Migration, Destructive / irreversible operation, Cache, Performance claims), keep task notes in `.pi/work/`, and run the `independent-verifier` before completion. A cache without a measured problem, an owner, a staleness bound, and outage behavior is a signal, not a default. This skill owns the data domain; the harness owns the evidence bar.

## Completion gate

Do not call work complete until applicable statements are true:

- schema invariants are enforced by the database where the database can enforce them;
- every query change has a before and after plan captured by the same method;
- every added index has an observed predicate behind it and confirmed planner adoption;
- migrations have reviewed SQL, a stated compatibility window, a rollback or roll-forward path, and a fresh backup before destructive steps;
- caches have a named invalidation trigger and defined behavior when unavailable;
- personal data is classified, with retention and a working deletion path across tables, backups, logs, and caches;
- tenant and row-level isolation has a negative test;
- backup coverage, RPO/RTO, and the last verified restore are stated with dates, or the gap is named plainly;
- no secret value, connection string, or production row content appears in output;
- relevant build, migration, and test commands pass or failures are reported.

## Completion response

Lead with the data outcome. Report what changed or was found, the measurements actually taken and how, remaining risk and recovery assumptions, and the single most valuable next step only when one remains. Do not list internal skill invocations unless the user asks.

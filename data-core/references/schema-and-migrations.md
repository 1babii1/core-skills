# Schema design and migration operations

Use for new tables, model changes, and any schema or data change that reaches a shared environment. Query tuning lives in `postgres-pro` and `optimizing-ef-core-queries`; this reference covers shape and evolution.

## Let the database enforce what it can

- Every table gets a primary key. Prefer a surrogate key for identity and a separate unique constraint for the natural key when one exists.
- Declare foreign keys with a deliberate delete behavior. Choosing `RESTRICT`, `CASCADE`, or `SET NULL` is a domain decision, not a default.
- Encode invariants as `NOT NULL`, `UNIQUE`, and `CHECK` constraints. An application-only rule is a rule the next process, script, or import will break.
- Use exact types: `uuid` not `text`, `numeric` for money, `timestamptz` for instants, native enums or a lookup table instead of magic strings. Store instants in UTC and convert at the edge.
- Set defaults in the database when the value is a data fact, in the application when it is a business decision.
- Name constraints and indexes explicitly so migrations and error messages are readable.

## Choose the shape from the access pattern

- Normalize first. Denormalize only against a measured read, and record which read justified it and what keeps the copies consistent.
- Reach for JSONB when the shape is genuinely open-ended or supplied by an external system — not to avoid writing a migration. Anything queried, filtered, sorted, or constrained belongs in a column.
- Index JSONB with GIN only for the containment queries actually issued; an unfocused GIN index on a large write-heavy table is expensive.
- Model soft delete deliberately. A nullable `deleted_at` changes every query, every unique constraint, and every foreign key expectation; if only a few tables need it, do not apply it globally.
- Give history its own table when audit or point-in-time questions are real requirements, rather than overloading the live row.
- Decide multi-tenancy shape early — shared table with a tenant column, schema per tenant, or database per tenant. Changing it later is a migration of everything.

## Review the SQL, not the migration class

- Read the generated SQL for every migration. Successful generation says nothing about lock behavior, duration, or data safety.
- Identify which statements take an exclusive lock and for how long against production-scale data. On PostgreSQL, adding a column with a volatile default, changing a type, and adding a non-concurrent index all block writes.
- Use `CREATE INDEX CONCURRENTLY` on populated tables, and know it cannot run inside a transaction — the migration must be structured for it.
- Add `NOT NULL` in stages on a large table: add nullable, backfill in batches, add a validated check constraint, then set not-null.
- Never mix a schema change and a multi-million-row backfill in one migration. Backfill in bounded batches with progress that can be resumed.

## EF Core migration hazards

A migration is code that runs once against data you cannot see; treat the scaffolded file as a draft.

- A renamed property scaffolds as drop-column plus add-column and destroys the data. Replace it with `RenameColumn` (or expand/migrate/contract below) and never dismiss the scaffolder's possible-data-loss warning.
- Do not use the current `DbContext` or entity classes inside a migration; they change later and old migrations must keep compiling and behaving identically. Use `Sql` for computed values and `InsertData`/`UpdateData`/`DeleteData` for fixed rows.
- Adding a unique, foreign-key, or NOT NULL constraint to existing data: first query for rows that violate it and decide their fate. A green build and an empty local database prove nothing about this.
- `CREATE INDEX CONCURRENTLY` cannot run in a transaction (pass `suppressTransaction: true` to `migrationBuilder.Sql`), scans the table twice, and a failure leaves an INVALID index behind: check `pg_index.indisvalid`, drop it, retry.
- Never edit or delete a migration that reached a shared database, and never hand-edit the model snapshot; add a corrective migration. Write `Down` only when the original values can really be rebuilt, otherwise fail explicitly and document restore-from-backup.
- Catch a forgotten migration in CI with a test asserting `context.Database.HasPendingModelChanges()` is false (EF Core 8+).
- Prove the upgrade path on a database holding representative historical data (restored snapshot or seeded fixture), not only an empty one.

## Composite indexes and ORDER BY

A composite index lets the planner skip the sort only when column order **and each column's direction** match the ORDER BY. `ORDER BY a DESC, b ASC, c ASC` needs an index declared with those per-column directions; an all-ascending `(a, b, c)` does not serve it, and a backward scan does not help because it flips every column at once. In EF Core use `HasIndex(...).IsDescending(true, false, false)`; the default call creates every column ascending. Read the index back from the catalog (`pg_indexes.indexdef`) and check the printed direction per column, then run EXPLAIN (ANALYZE, BUFFERS) against the index the application will actually use, not a hand-written one used earlier to validate the idea: the two can differ in exactly this field and the mismatch yields a plan worse than no index.

## Expand, migrate, contract

Whenever the old and new application versions will run at the same time — which is every rolling deploy:

1. **Expand.** Add the new column, table, or index. Nothing is removed and nothing is renamed. Old code keeps working.
2. **Migrate.** Deploy code that writes both old and new, backfill existing rows in batches, then deploy code that reads the new shape.
3. **Contract.** Only after every running instance uses the new shape, drop the old column or constraint in a separate later migration.

Rename is never a rename in this model: add, dual-write, backfill, switch reads, drop.

## Safety around every migration

- Take and verify a fresh backup before any destructive or irreversible step. Note the timestamp in the change description.
- State the rollback path explicitly. Many migrations are roll-forward only — say so rather than implying a `Down` method that was never tested.
- Ensure exactly one process applies migrations. Multiple replicas racing at startup is a real outage; use a deploy step, a migration job, or an advisory lock.
- Test against a restored copy with representative volume. Duration and lock behavior on ten rows predict nothing.
- Have a kill criterion: how long the migration may run before it is aborted, and what aborting leaves behind.

## Migration review checklist

- Generated SQL read and lock behavior understood.
- Compatible with the currently deployed application version.
- Destructive steps separated into a later contract migration.
- Backfill batched, resumable, and outside the schema migration.
- Indexes created concurrently on populated tables.
- Fresh verified backup, stated rollback or roll-forward path, and abort criterion.
- Single applier guaranteed.
- Rehearsed against representative data with a recorded duration.

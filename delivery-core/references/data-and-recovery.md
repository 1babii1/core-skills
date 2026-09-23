# Data release and recovery gate

Use whenever a release changes a schema, data representation, persistent volume, object store, queue durability, or backup process. Apply `postgres-pro` only for PostgreSQL and consult the current official documentation for the actual database/provider.

## Migration gate

- Inventory every migration and its lock, rewrite, duration, disk, replication, and compatibility risk.
- Test against the same engine major version and a representative schema/data volume.
- Separate schema preparation, application rollout, backfill, and destructive cleanup when overlap is required.
- Ensure old and new application versions can coexist for the rollout window.
- Run one controlled migration job with observable logs and an explicit timeout.
- Verify schema version and application invariants after migration.
- Do not assume transactional DDL or down migrations are safe across engines and operations.

## Backup gate

Before a destructive or hard-to-reverse release:

- define protected data and dependencies;
- define RPO and RTO;
- confirm backup ownership, schedule, retention, encryption, and storage isolation;
- confirm the latest backup completed and is restorable;
- record a non-secret recovery-point identifier;
- estimate restore time and required capacity.

Do not call a backup verified merely because a file or snapshot exists.

## Restore test

Restore into an isolated non-production target using credentials supplied outside agent context. Validate:

- database/service starts cleanly;
- expected schema and migration history exist;
- critical tables/objects and integrity constraints are present;
- representative application reads and writes work;
- required extensions, users/roles, object metadata, and encryption dependencies are recoverable;
- measured RTO/RPO meet the stated requirement.

Never overwrite production as a restore test. Any production restore or destructive database action requires the exact target, recovery point, impact, and explicit authorization.

## Rollback versus roll-forward

- Roll back application code only while the prior version remains schema-compatible.
- Roll forward schema/data when reversing would lose writes or transformed data.
- Use feature flags or dual-read/write only when their operational complexity is justified and tested.
- Preserve evidence and stop automated cleanup until the release is stable.

## PostgreSQL

Use `postgres-pro` for engine-specific behavior. Verify current official guidance for logical/physical backup, WAL/PITR, replication, concurrent indexes, vacuum, and major-version compatibility. Do not copy generic community commands into production without matching the actual provider and version.

Primary reference: https://www.postgresql.org/docs/current/backup.html

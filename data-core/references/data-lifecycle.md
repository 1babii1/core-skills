# Data lifecycle: classification, retention, isolation, recovery

Use when auditing what a project stores about people, how long it keeps it, who can reach it, and whether it can be restored. Deployment mechanics live in [delivery-core/data-and-recovery.md](../../delivery-core/references/data-and-recovery.md); credential handling lives in `secrets-core`.

## Classify before protecting

Produce a table of what the schema actually holds, from the columns rather than from the product description:

| Class | Examples | Handling |
| --- | --- | --- |
| Identifying | name, email, phone, Telegram ID, address, document number | Minimize, restrict, retain by policy, deletable |
| Sensitive | payment details, health, location history, precise device data | Collect only with a stated need; encrypt; narrow access; short retention |
| Credential | password hashes, tokens, API keys, refresh tokens | Hashed or encrypted, never logged, rotatable, never in test data |
| Behavioral | events, sessions, analytics, logs | Aggregate or pseudonymize; expire on a schedule |
| Operational | non-personal business records | Ordinary retention |

Record where each class is duplicated — read replicas, backups, caches, search indexes, logs, analytics exports, error trackers, and CSV exports someone made once. Duplication is where deletion promises fail.

## Minimize and expire

- Do not collect a field because it might be useful. Every stored field is an obligation.
- Give every personal-data table a retention period expressed in time, and an automated job that enforces it. A retention policy nobody executes is documentation, not protection.
- Expire sessions, tokens, verification codes, and one-time links by construction — a TTL in the store, not a cleanup script that may be disabled.
- Truncate or pseudonymize personal data in logs and error reports at the point of writing. Scrubbing later never catches everything.

## Deletion has to actually work

When a user or a client asks for deletion, the path must cover:

- primary rows and every foreign-key dependent, including soft-deleted rows that were never purged;
- caches and sessions keyed by that identity;
- search indexes and denormalized read models;
- logs, error tracker events, and analytics that contain identifiers;
- backups — which usually cannot be edited, so state the maximum window until the last backup containing the data expires;
- third-party processors the data was sent to.

Distinguish anonymization, which keeps the row for aggregates with identifiers irreversibly removed, from deletion, which removes the row. Say which one the system performs. Test the path end to end at least once and record the result.

## Isolation is a test, not a code reading

- Verify tenant scoping with a negative test: authenticate as tenant A and attempt to read, update, and delete an object belonging to tenant B through every route that accepts an identifier.
- Verify the same for user-owned resources within a tenant, and for direct-object references in exports, file downloads, and background jobs.
- Give the application a least-privilege database account. The runtime user should not own the schema, drop tables, or read tables it never touches. Migrations run under a separate account.
- Confirm no shared connection, cache prefix, or search index merges tenants unintentionally.

## Test data must not be production data

- Never copy production rows into development, test, staging, or a demo without anonymization. "Only for a moment" is how the copy becomes permanent.
- Prefer generated or seeded fixtures over a subset of real data. When a realistic dataset is genuinely required, anonymize irreversibly: replace identifiers, randomize names and contacts, shift dates consistently, drop credential columns entirely, and preserve only the distribution that the test needs.
- Keep the anonymization script in the repository and run it as part of the copy, never as a manual step afterwards.
- Verify the result by searching the anonymized dump for a known real identifier before it leaves the secure environment.

## Recovery is proven, not configured

State for each store, with dates:

- what is backed up, how often, where it is stored, and whether that location survives losing the primary environment;
- how long backups are retained and whether that satisfies the retention policy in both directions — long enough to recover, short enough to delete;
- whether backups are encrypted, and where that key lives relative to the data;
- the RPO — how much data may be lost — and the RTO — how long recovery may take — as agreed values, not aspirations;
- the date of the last restore performed and verified, and how long it took.

Run a restore drill into an isolated environment: restore, run migrations if needed, start the application, and verify a known record. An untested backup is an assumption. Before any destructive migration, take a fresh backup and confirm it is readable — not merely that the job reported success.

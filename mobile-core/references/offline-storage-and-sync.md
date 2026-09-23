# Offline storage and synchronization

Read whenever data survives a process restart or the product must work without a reliable network.

Official baselines:

- https://docs.expo.dev/versions/latest/sdk/sqlite/
- https://docs.expo.dev/guides/local-first/
- https://docs.expo.dev/versions/latest/sdk/securestore/

## Select storage by ownership

| Need | Default |
| --- | --- |
| Small credentials or device-bound secret | SecureStore |
| Theme, onboarding flag, simple preference | key-value store |
| Persisted TanStack Query cache | dedicated query persister |
| Durable relational/domain records | Expo SQLite |
| Large files and media | filesystem plus metadata database |

SecureStore is not a database or sole source of truth for irreplaceable data. Key-value storage is not appropriate for relational queries or large evolving datasets. Query-cache persistence is not a durable local-first model.

## Database rules

- Define numbered, transactional, forward-only migrations and test upgrades from supported production versions.
- Use parameters or safe tagged SQL; never concatenate untrusted values.
- Keep database access behind feature/domain repositories.
- Use explicit transactions for atomic business changes.
- Avoid synchronous heavy queries on the JS thread.
- Plan corruption, partial migration, low-disk, interrupted write, and reset/recovery behavior.
- Encrypt only when the threat model warrants it; manage the key separately and never hard-code it.

## Synchronization model

Define before implementation:

- local and server sources of truth;
- stable record and operation identifiers;
- version, cursor, or timestamp semantics;
- deletion/tombstone behavior;
- conflict strategy per entity or field;
- attachment upload lifecycle;
- schema and protocol compatibility across app versions.

For offline mutations, persist an outbox transactionally with the local change. Each operation needs a stable ID, idempotency contract, retry classification, attempt metadata, and terminal/manual-recovery state.

## Recovery and lifecycle

- Treat connectivity as a hint, not proof that the API is reachable.
- Pause and resume deliberately around app backgrounding and foregrounding.
- Use bounded exponential backoff with jitter.
- Do not retry validation, authorization, conflict, or permanent errors blindly.
- Surface pending, failed, conflicted, and stale states honestly.
- Reset or namespace user-scoped data on logout and account switch.
- Never let cache restoration overwrite newer durable local data.

Test airplane mode, flaky connection, process kill, device restart, duplicate delivery, out-of-order responses, clock skew, account switching, token expiry, migration interruption, and server incompatibility.

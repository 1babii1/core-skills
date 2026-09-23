# Testing, Observability, and Release

## Test layers

- Unit: parsers, state transitions, authorization, callback/deep-link codecs, price rules.
- Integration: PostgreSQL/Redis/queue, idempotency, outbox, init-data validation.
- Contract: representative Update payloads and unknown optional fields.
- E2E: bot conversations and Mini App APIs with a separate test bot/environment.
- Client: real Telegram iOS/Android/Desktop plus browser SDK mock.
- Resilience/load: bursts, retries, duplicates, queue backlog, dependency failure.
- Accessibility/visual/UAT: route through `qa-core`.

Do not use production credentials for tests.

## Signals

Track update intake/processing latency, failures by handler, dedup hits, callback acknowledgement time, queue depth/age, Telegram/API rate limits, outbound delivery failures, Mini App API latency, auth rejection reasons without sensitive data, payment reconciliation, and dependency health.

Use correlation IDs that do not expose tokens, init data, payment payloads, or PII.

## Release

Use `delivery-core` for pipeline, migrations, health checks, backups, rollout, and rollback. Roll out schema changes compatibly, drain workers gracefully, verify webhook health after deployment, and keep a documented polling/webhook recovery procedure. Registration or production changes require explicit authorization.

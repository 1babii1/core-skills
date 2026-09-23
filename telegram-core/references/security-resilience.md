# Security and Resilience

Threat-model the bot token, webhook, init data, callbacks, deep links, uploads, payments, admin actions, third-party APIs, and logs.

Minimum controls:

- least-privilege admin/application authorization;
- secret rotation and redacted structured logs;
- body/file size and type limits;
- SSRF-safe remote fetch policy;
- escaped Telegram formatting and safe link handling;
- callback/deep-link schemas with expiry and replay handling;
- per-user/chat/action rate limits;
- idempotency and unique constraints for money and entitlements;
- bounded timeouts, retries, circuit breaking where justified;
- audit events for privileged or financial actions;
- retention/deletion rules for PII.

Never scan or inspect secret stores during an audit. `.env.example` is the only readable environment contract.

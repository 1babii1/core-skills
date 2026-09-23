# Webhooks and Update Pipeline

## Webhook contract

- Public HTTPS endpoint.
- Configure `secret_token`; validate `X-Telegram-Bot-Api-Secret-Token` with constant-time comparison.
- Keep the token out of the URL and logs.
- Restrict body size and accepted content type.
- Configure `allowed_updates` explicitly.

## Processing

1. Parse and minimally validate the update.
2. Authenticate the webhook.
3. Durably record/deduplicate `update_id`.
4. Enqueue or execute the idempotent handler.
5. Return success after durable acceptance.

Use a database uniqueness constraint or equivalent atomic operation for deduplication. If ordering matters, partition work by chat/conversation/business entity rather than serializing all updates globally.

## Recovery

- Bound retries with jitter; distinguish transient from permanent failures.
- Move poison work to a review/dead-letter path.
- Observe pending count, oldest-update age, processing latency, failures, retries, and dedup hits.
- During incidents inspect webhook status, TLS, secret configuration, and Telegram diagnostics.
- Switching modes requires explicit operational steps; delete the webhook before polling.

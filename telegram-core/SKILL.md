---
name: telegram-core
description: Orchestrate production Telegram bots and Mini Apps with ASP.NET Core, Telegram.Bot, React, secure init data, webhooks, Stars, deep links, state ownership, testing, and deployment. Use when planning, building, reviewing, debugging, testing, or releasing a Telegram bot, Telegram Mini App, Web App, payment flow, or related backend/frontend integration.
---

# Telegram Core

Build Telegram products as one system: bot transport, application backend, Mini App frontend, durable state, security, tests, and delivery.

## Start with discovery

1. Read repository instructions and existing architecture.
2. Inspect project and lock files for .NET, `Telegram.Bot`, React, Telegram SDK, and test versions.
3. Read `.env.example` only for environment-variable names. Never read `.env`, `.env.*`, vaults, age identities, credential files, or secret values.
4. Identify supported surfaces: private chat, groups, channels, inline mode, business, Mini App, payments, and public web.
5. Identify update delivery, storage, queueing, hosting, BotFather configuration contract, and release constraints.
6. Verify feature-specific behavior against the current official Bot API documentation and changelog. Installed package capabilities and official current docs override third-party skills.

Do not replace a suitable existing stack merely to match these defaults.

## Default architecture

- Backend: ASP.NET Core and `Telegram.Bot`.
- Mini App: React + TypeScript. Prefer Vite for a focused client-only Mini App; use Next.js when the product also needs substantial server rendering, public web routes, or Next-specific backend behavior.
- Durable data: PostgreSQL.
- Short-lived cache, distributed rate limits, locks, and coordination: Redis only when justified.
- Production ingestion: webhook by default. Polling is appropriate for local development and simple deployments.
- Never run webhook and polling simultaneously for one bot.

Read [architecture-and-dotnet.md](references/architecture-and-dotnet.md) before structural work.

## Route work through the core

Load only relevant modules:

- Updates/webhooks: `telegram-bot-api-getting-updates`, then [webhooks-and-update-pipeline.md](references/webhooks-and-update-pipeline.md).
- Messages and rich text: `telegram-bot-api-messages-and-formatting`.
- Files/media: `telegram-bot-api-media-and-files`.
- Commands and input: `telegram-bot-api-commands-keyboards-and-input`.
- Inline/callback flows: `telegram-bot-api-inline-mode-and-callbacks`.
- Mini Apps: `telegram-bot-api-mini-apps-and-attachment-menu`, [mini-app-runtime-and-ux.md](references/mini-app-runtime-and-ux.md), and `frontend-core`.
- Login/init data: `telegram-bot-api-security-privacy-and-identity`, `telegram-bot-api-web-login-and-deep-linking`, [init-data-and-auth.md](references/init-data-and-auth.md), and `auth-core`.
- Stars/payments: `telegram-bot-api-payments-stars-and-broadcasting` and [payments-and-stars.md](references/payments-and-stars.md).
- Deep links/referrals: `telegram-bot-api-web-login-and-deep-linking` and [deep-links-and-referrals.md](references/deep-links-and-referrals.md).
- API/schema drift: `telegram-bot-api-schema-and-type-modeling` and [api-version-and-capabilities.md](references/api-version-and-capabilities.md).
- Localization, testing, local Bot API: `telegram-bot-api-localization-testing-and-local-bot-api`.
- Security/release review: [security-resilience.md](references/security-resilience.md) and [testing-observability-and-release.md](references/testing-observability-and-release.md).

## State ownership

Use [state-data-and-forms.md](references/state-data-and-forms.md). In short:

- component UI: `useState`/`useReducer`;
- route and launch context: URL, `start`, or `startapp` parameters;
- forms: React Hook Form + Zod;
- remote/server state: TanStack Query;
- small shared client-only state: scoped Zustand;
- Telegram theme, viewport, buttons, and runtime capabilities: Telegram SDK;
- conversations, orders, entitlements, users, and payment records: PostgreSQL;
- transient distributed coordination: Redis when needed.

Do not mirror server state or Telegram SDK state into Zustand.

## Mandatory trust boundaries

- Treat the bot token as root access.
- Validate webhook HTTPS and the configured secret header.
- Never put a token in the webhook URL.
- Never trust `initDataUnsafe`; send raw `initData` to the backend and validate it there.
- Validate signature, freshness, and replay risk before creating a short application session.
- Authorize every action server-side; Telegram identity proves identity, not permission.
- Minimize PII and redact logs. Never log tokens, raw init data, hashes, payment payloads, or sensitive query strings.
- Use `secrets-core`; agents use `.env.example` as the only secret contract.

## Interaction and reliability rules

- Acknowledge callback queries quickly.
- Keep `callback_data` compact, versioned, and replay-safe.
- Treat updates as immutable inputs and handlers as idempotent.
- Deduplicate by `update_id` and business identifiers.
- Return webhook success only after durable acceptance when work is queued.
- Serialize only the conversation/entity streams that require ordering.
- Handle `retry_after`, bounded retries, poison messages, cancellation, and graceful shutdown.
- Validate all files, URLs, remote content, deep-link payloads, and user-controlled formatting.

## Payments

For digital goods and services sold inside Telegram, use Telegram Stars (`XTR`) when Telegram requires it. Answer pre-checkout promptly, fulfill only from a verified successful-payment update, persist charge IDs uniquely, and make fulfillment/refunds/reconciliation idempotent. Keep billing, entitlement, and delivery separate.

## UI and assets

Use `design-core` for visual work and `motion-core` only when animation improves comprehension. Do not generate ad-hoc SVG artwork. Prefer a coherent icon library for interface icons and raster/generated image assets for illustration, following the project's design rules.

## Quality and delivery

- Use `backend-core` for ASP.NET architecture, data, performance, and observability.
- Use `frontend-core` and `design-core` for Mini Apps.
- Use `qa-core` for unit, integration, contract, E2E, accessibility, cross-client, visual, load, and UAT coverage.
- Use `delivery-core` for Docker, CI/CD, DNS, TLS, Nginx, migrations, backups, health checks, rollback, and deployment.
- Use `seo-core` only for a public crawlable landing site, never for the in-Telegram surface itself.

Run `python3 scripts/audit_telegram.py <project>` for a secret-safe static preflight. Treat its result as a heuristic review, not proof of security.

## External-change boundary

Planning and local implementation do not authorize BotFather changes, webhook registration, production deployment, sending messages/invoices, purchases, refunds, broadcasts, or other actions affecting real users. Obtain explicit authorization before those external changes.

## Definition of done

1. Current API/package capability assumptions are documented.
2. Update ingestion is authenticated, idempotent, observable, and recoverable.
3. State ownership is explicit and durable state survives restarts.
4. Mini App auth is validated server-side with freshness controls.
5. Payment fulfillment is event-driven and idempotent when applicable.
6. Real Telegram clients and failure paths are tested.
7. Secrets policy, migrations, health checks, backups, and rollback are ready.
8. Relevant core audits pass or remaining risks are documented.

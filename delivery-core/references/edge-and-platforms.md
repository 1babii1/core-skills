# Edge and platform routing

Use for provider selection, VPS/PaaS deployment, DNS, TLS, CDN, and reverse proxies.

## Select a target

Evaluate current primary documentation and the user's actual constraints:

- framework/runtime and feature support;
- static versus long-running server/worker needs;
- WebSocket, streaming, background jobs, cron, storage, and database connectivity;
- supported regions, network access, account/payment availability, data location, and legal requirements;
- pricing, egress, build minutes, log retention, scaling limits, backups, support, and lock-in;
- preview environments, custom domains, certificates, observability, and rollback behavior.

For users operating from Russia, verify current signup, billing, sanctions/terms, network reachability, and support before recommending any foreign service. Do not claim that a provider is available based on old experience.

## Default independent VPS route

For a small application when no PaaS clearly wins:

1. supported Linux host;
2. firewall exposing only required management and public ports;
3. rootless/non-root application containers managed with current Docker Compose;
4. Nginx reverse proxy and static delivery;
5. ACME-managed TLS;
6. external or separately protected persistent data and backups;
7. centralized logs/metrics and uptime checks;
8. immutable image promotion and documented rollback.

Avoid manual source builds on the production server.

## Nginx

Use the `nginx` skill for every configuration change.

- Verify directive syntax against current official Nginx documentation.
- Validate configuration before reload.
- Prefer reload over restart when safe.
- Configure trusted proxy headers explicitly.
- Verify upstream keepalive, timeouts, request/body limits, buffering, WebSocket upgrades, gRPC/HTTP2, streaming, static caching, compression, and error behavior as applicable.
- Do not add broad CORS, unsafe TLS, arbitrary `if` rules, or unverified copied snippets.
- Ensure the previous known-good configuration and rollback command are available before reload.

## DNS and TLS

- Resolve the exact zone and record before changing it.
- Lower TTL ahead of a planned cutover when the provider and schedule permit it.
- Verify apex, `www`, API, callback, email-related, and validation records independently.
- Preserve unrelated records.
- Validate certificate issuance, chain, hostname coverage, automatic renewal, renewal monitoring, and HTTP-to-HTTPS redirects.
- Test the final domain from an external network when possible.

## Provider skills

Use official provider skills only when installed and the provider is selected:

- `vercel-deploy` for Vercel preview/production actions;
- `cloudflare-deploy` for Cloudflare Pages/Workers and related services;
- `netlify-deploy` for Netlify;
- `render-deploy` for Render.

These execute provider actions; they do not replace the framework-specific adapters or the delivery completion gate.

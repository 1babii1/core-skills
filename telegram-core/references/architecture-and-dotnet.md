# Architecture and .NET

## Recommended boundaries

- `BotTransport`: Telegram client, update adapters, webhook/polling hosting.
- `Application`: commands/use cases, authorization, idempotency, transaction boundaries.
- `Domain`: business rules independent of Telegram types.
- `Infrastructure`: EF Core/PostgreSQL, Redis, queues, external services.
- `MiniApp`: React client and its API contract.

Keep Telegram DTOs at the edge. Normalize them into application events; retain a safely redacted raw-payload path only when schema-drift diagnostics require it.

## ASP.NET Core guidance

- Bind options from configuration names documented in `.env.example`; never inspect real secret files.
- Register `Telegram.Bot` clients through dependency injection and `HttpClientFactory`-compatible patterns supported by the installed version.
- Propagate cancellation tokens through handlers and I/O.
- Use typed results/problem details for Mini App APIs.
- Put validation at transport boundaries and business invariants in the domain/application layer.
- Use EF Core migrations intentionally; do not auto-migrate uncontrolled production instances.
- Add readiness checks for required dependencies and a lightweight liveness check.

## Scale gradually

Start as a modular monolith. Introduce a durable queue when webhook work exceeds the response budget, bursts must be absorbed, or retries need isolation. Split services only when independent scaling, security isolation, or ownership makes the operational cost worthwhile.

Use an outbox for database state changes that must reliably trigger notifications. Do not attempt distributed exactly-once delivery; combine at-least-once delivery with idempotent consumers.

# Data fetching and .NET API contracts

Read this reference for remote data, caching, generated clients, or ASP.NET integration.

## Choose the data path

- Astro static content: fetch at build time or use a content loader.
- Next.js initial/read-heavy page data: fetch in Server Components near the source.
- Client-heavy interaction, polling, optimistic mutation, or infinite data: use TanStack Query.
- Do not route a server read through an internal HTTP endpoint when direct trusted server access is simpler and preserves the intended boundary.

## OpenAPI pipeline

Prefer a generated client when the ASP.NET backend publishes a trustworthy OpenAPI contract:

```text
ASP.NET OpenAPI
    -> generated TypeScript client and DTOs
    -> small application adapter/query options
    -> feature/domain UI
```

Select the existing project tool when present. For new work, evaluate NSwag, Kiota, Orval, or OpenAPI Generator against the actual contract and desired TanStack integration.

Keep generated output isolated, reproducible, and unedited. Pin the generator, document the command, and fail CI when regeneration produces an unexpected diff.

Do not create a second hand-written DTO hierarchy that drifts from generated contracts. Application/domain models may adapt transport DTOs when the UI needs different semantics.

## Errors and validation

- Align backend failures with ASP.NET Problem Details where practical.
- Map transport failures into a small typed frontend error model.
- Preserve correlation/request IDs for support and tracing.
- Distinguish validation, authentication, authorization, not-found, conflict, rate-limit, transient, cancellation, and unexpected failures.
- Validate data at trust boundaries. Do not pay for redundant runtime parsing of every trusted internally generated response without a risk-based reason.
- Never render server error details that may expose internals.

## Requests and mutations

- Propagate `AbortSignal`.
- Bound pagination and payload sizes.
- Prevent duplicate submissions.
- Retry safe transient reads with bounded backoff and jitter.
- Do not automatically retry unsafe mutations unless the operation has an idempotency guarantee.
- Model concurrency conflicts explicitly.
- Keep authorization decisions on the backend even when UI controls are hidden.

## Cache ownership

Document for each important resource:

- authoritative owner;
- cache layers;
- freshness requirement;
- invalidation/update event;
- mutation consistency;
- offline/stale behavior;
- user/tenant isolation.

Avoid layering Next.js cache, HTTP cache, TanStack Query, service worker cache, and browser persistence by accident.

Coordinate backend contract changes with `backend-core` and delivery/version compatibility with `delivery-core`.

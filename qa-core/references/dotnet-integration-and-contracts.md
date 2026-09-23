# .NET integration and API contracts

Use this reference for ASP.NET Core services, PostgreSQL, Redis, queues, and OpenAPI consumers.

## Test portfolio

- Keep domain and application rules in fast unit tests.
- Host the real ASP.NET Core pipeline for endpoint integration tests.
- Prefer real disposable dependencies through Testcontainers for PostgreSQL, Redis, and brokers when boundary behavior matters.
- Mock third-party systems at the network boundary, not repositories or EF Core when persistence semantics are under test.
- Verify cancellation, timeouts, idempotency, concurrency, transactions, unique constraints, pagination, filtering, and error responses.
- Test migrations both forward and, when the delivery policy requires it, rollback or restore behavior.
- Keep each test isolated. Use a database per run, schema per worker, transaction rollback, or explicit deterministic cleanup.

## ASP.NET Core integration checks

Verify:

- middleware order and exception handling;
- authentication and authorization policies through `auth-core`;
- RFC Problem Details shape and content types;
- model binding and validation;
- headers, caching, compression, rate limits, and CORS when contractual;
- database transaction and concurrency behavior;
- health endpoints without treating them as full dependency tests;
- structured telemetry and correlation without leaking sensitive data.

Use the test framework already selected by the repository. Do not introduce a second assertion or mocking library without a clear benefit.

## OpenAPI compatibility pipeline

1. Generate the OpenAPI document from the same build being tested.
2. Validate syntax and unresolved references.
3. Lint the contract using the repository's configured rules.
4. Compare the candidate document with the released baseline using `oasdiff` or the repository's equivalent.
5. Classify additions, behavioral changes, deprecations, and breaking changes.
6. Exercise provider responses against the schema.
7. Regenerate the TypeScript/client SDK when the project uses one.
8. Compile consumers and run their focused integration tests.
9. Publish the candidate contract and diff as artifacts.

Do not update the released baseline before compatibility review.

## When to use Pact

Use consumer-driven contracts when:

- consumers and providers deploy independently;
- multiple consumers need different provider behavior;
- coordinating a shared test environment is expensive;
- consumer expectations cannot be represented sufficiently by schema compatibility alone.

Avoid Pact for a single jointly deployed frontend/backend when OpenAPI diff, provider integration tests, and client compilation provide adequate evidence.

When using Pact:

- define expectations from the consumer;
- use matchers instead of brittle example equality;
- verify provider states deterministically;
- version contracts and provider builds;
- require provider verification before deployment;
- keep business logic out of contract tests.

## Failure scenarios

Cover applicable cases:

- malformed and semantically invalid input;
- 401 versus 403 behavior;
- missing resource and conflict;
- duplicate request/idempotency key;
- downstream timeout and cancellation;
- database deadlock/concurrency conflict;
- cache miss and unavailable cache;
- queue redelivery and poison message;
- incompatible enum or nullable-field evolution;
- large payload and pagination boundaries.

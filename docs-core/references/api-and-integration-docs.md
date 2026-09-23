# API and Integration Documentation

## Determine authority

Choose explicitly:

- **Design-first:** the reviewed API contract is authoritative; implementation must conform.
- **Code-first:** a generated contract reflects implementation; generation and drift checks are authoritative.
- **Hybrid:** define which elements come from code and which are curated, plus merge/regeneration rules.

Avoid two independently edited sources for the same endpoint or schema.

## Consumer journey

API documentation should let a consumer:

1. understand the capability and supported version;
2. obtain access through a safe process;
3. authenticate without seeing real secrets;
4. make a minimal successful request;
5. understand response and error semantics;
6. handle pagination, retries, idempotency, limits, and asynchronous behavior when applicable;
7. test in an appropriate environment;
8. migrate across a breaking or deprecated version;
9. know where to get support.

## Reference completeness

For each operation or message document as applicable:

- method/event and path/topic;
- purpose and authorization;
- parameters, headers, body, types, constraints, defaults, and nullability;
- response/status variants and schema;
- stable error code, meaning, recoverability, and consumer action;
- idempotency and concurrency behavior;
- pagination/filter/sort semantics;
- rate or size limits with authoritative source;
- side effects and consistency guarantees;
- webhook signature, retry, ordering, duplicate, and timeout semantics;
- deprecation and versioning.

Do not add a requirement merely because another API commonly has it. State `Not applicable` only after verification.

## Examples

Examples must be:

- syntactically and semantically valid for the documented version;
- executable where feasible;
- deterministic or explicit about variable output;
- sanitized and clearly non-production;
- consistent across curl, C#, TypeScript, or other supported clients;
- paired with expected status and relevant response shape.

Use names such as `YOUR_API_TOKEN` or environment variable references from `.env.example`. Never include a token-shaped value, private hostname, customer data, production ID, or real webhook secret.

## Errors and safety

Document what consumers can act on. Separate:

- validation and business-rule errors;
- authentication and authorization;
- conflicts/idempotency;
- rate limiting and temporary unavailability;
- dependency failures;
- internal failures without leaking sensitive detail.

Do not promise retry safety without verifying idempotency. Do not expose stack traces, internal topology, queries, or security-sensitive implementation detail.

## Contract quality

Use `openapi-spec-generation` and validate:

- OpenAPI version and schema dialect;
- unique operation identifiers;
- reusable components without circular confusion;
- security requirements by operation;
- representative success and failure examples;
- breaking-change detection;
- implementation contract tests;
- rendered developer experience.

SDK generation is downstream of a correct contract, not proof that the contract is correct.

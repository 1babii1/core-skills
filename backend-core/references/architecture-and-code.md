# .NET backend architecture and code

Use for new services, material refactors, or audits of dependency and ownership boundaries.

## Architecture choices

- Start with a modular monolith unless independent deployment, scaling, ownership, isolation, or regulatory requirements justify distributed services.
- Organize around cohesive capabilities/vertical slices when it keeps behavior, validation, data access, and tests discoverable.
- Add layers only when they enforce a real dependency rule. Avoid pass-through services, repositories wrapping EF Core without added semantics, and interfaces with one implementation created solely for mocking.
- Keep domain/business decisions separate from HTTP, serialization, database, queue, clock, filesystem, and third-party SDK mechanics when those dependencies would otherwise make rules difficult to test or reuse.
- Keep the composition root explicit. Prefer constructor injection, narrow lifetimes, and visible dependencies over service location or global mutable state.

## Correctness rules

- Enable nullable reference types and honor annotations at boundaries.
- Prefer immutable request/value models where mutation is unnecessary.
- Propagate `CancellationToken` through async I/O; do not use `Task.Run` to disguise blocking server work.
- Avoid sync-over-async, fire-and-forget tasks without ownership, swallowed exceptions, and broad catches that convert failure into false success.
- Make time, randomness, identifiers, and external I/O replaceable only where deterministic behavior/testing needs it.
- Use UTC instants for machine timestamps and explicit time zones for user/calendar rules.
- Define equality, money/decimal behavior, rounding, ordering, nullability, and boundary semantics deliberately.

## Boundary ownership

For every operation identify:

- input validation and authorization owner;
- transaction boundary and authoritative data store;
- side effects and their ordering;
- retry/idempotency behavior;
- concurrency expectation;
- emitted integration events and compatibility contract;
- failure observation and recovery owner.

## Review smells

- shared database tables written by unrelated modules/services;
- controllers/endpoints containing business transactions;
- domain code referencing HTTP or vendor SDK types;
- cyclic project references or feature dependencies;
- singleton services holding scoped dependencies or request/user state;
- generic `Result<T>`/repository/event abstractions that erase actionable error semantics;
- distributed service boundaries created only to make folders look independent;
- reflection, dynamic dispatch, or source generation without measured/operational need;
- comments describing what code does instead of why a non-obvious constraint exists.

Refactor incrementally and preserve behavior with characterization/integration tests before moving risky boundaries.

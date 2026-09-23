# Architecture and Decisions

## Architecture document

Document the system at the level needed for a real decision or change:

- context, users, and quality constraints;
- what the system owns and delegates;
- deployable units and boundaries;
- major data flows and durable state;
- external dependencies and failure behavior;
- trust boundaries and sensitive data categories;
- observability, recovery, and scaling constraints;
- known limitations and open questions;
- links to accepted decisions and deeper component docs.

Separate:

- **Current:** verified implementation and deployed reality.
- **Desired:** approved target state not yet complete.
- **Historical:** replaced design retained for decision context.

Do not draw aspirational components as if they are live.

## Diagram discipline

Use the smallest useful visualization:

- context/container diagram for ownership and dependencies;
- sequence diagram for multi-hop behavior;
- state diagram for lifecycle;
- ER diagram for important data relationships;
- flowchart for a decision or recovery path.

Every box and edge must have a source. Add a nearby source list or explanatory text when the rendering format does not support citations. A diagram without verified semantics is decoration.

## ADR structure

For a material decision record:

```markdown
# ADR-NNN: Decision title

Status: Proposed | Accepted | Superseded | Rejected
Date:
Owners:
Decision scope:

## Context and constraints
## Options considered
## Decision
## Consequences and tradeoffs
## Validation and review trigger
## Links to evidence and superseding decisions
```

Record options actually considered. Do not invent retrospective rationale or consensus. Mark missing history as unknown.

## Decision triggers

Create or update an ADR when changing:

- service or module boundaries;
- public API compatibility;
- durable data model or migration strategy;
- authentication/authorization model;
- infrastructure topology or delivery strategy;
- critical dependency or vendor;
- reliability, privacy, or security posture;
- a convention with meaningful long-term cost.

Minor implementation details do not need ceremonial ADRs.

## Verification

Trace representative paths through actual code and configuration. Check imports/calls, route registration, schemas, persistence, external clients, deployment units, and tests. Cite stable file paths and identifiers; use line links only when the repository URL and branch make them durable enough.

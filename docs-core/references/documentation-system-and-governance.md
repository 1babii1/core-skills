# Documentation System and Governance

## Start with tasks, not folders

Map the knowledge needed to complete real tasks:

- understand what the product is and whether it fits;
- set up and run it;
- contribute safely;
- integrate through a public interface;
- operate, diagnose, recover, and escalate;
- understand architecture and decisions;
- use the product or resolve a problem;
- accept and own a delivered project.

Organize documents around reader journeys. A `docs/` folder is not an information architecture.

## Minimal document register

For each document record:

| Field | Meaning |
| --- | --- |
| Title/path | Stable location or canonical URL |
| Audience | Primary reader, not “everyone” |
| Reader task | Decision or action enabled |
| Status | Draft, Verified, Published, Deprecated, Archived |
| Owner | Role responsible for truth |
| Reviewer | Required technical/product/ops/security/client review |
| Authority | Code, spec, schema, tests, platform, accepted decision |
| Last verified | Date and environment/version where relevant |
| Update trigger | Code area, API version, deployment, policy, incident, release |
| Replacement | Canonical successor when deprecated |

Use dates as evidence of verification, not automatic expiration. Event-based triggers are usually stronger than arbitrary cadence.

## Source-of-truth rules

- Maintain one canonical source for each fact.
- Link to canonical detail instead of copying it.
- Generate reference material from contracts when generation is reliable.
- Keep explanations near the reader journey; keep implementation facts near the owning component.
- Mark generated files and regeneration commands.
- Record intentional divergence, such as a design-first contract ahead of implementation.

When sources disagree, do not silently choose. State the conflict, determine authority with the responsible owner, and update or deprecate the losing source.

## Information architecture

A small project may need only:

```text
README.md
docs/
  architecture.md
  onboarding.md
  api.md
  runbooks/
  handoff/
```

Add hierarchy only when navigation or ownership needs it. Avoid empty categories, duplicate “overview” pages, and one document per internal class.

Every entry point should answer:

- What is here?
- Who is it for?
- Where do I start?
- What is authoritative?
- Where do I go next?

## Documentation lifecycle

1. **Proposed:** need and audience identified.
2. **Draft:** content exists but has not passed required review.
3. **Verified:** claims and procedures checked against named sources.
4. **Published:** available in the intended system.
5. **Needs update:** a trigger fired or contradiction was found.
6. **Deprecated:** replacement and migration path exist.
7. **Archived:** retained for history but removed from active navigation.

Publishing is not verification. A generated page is not automatically authoritative.

## Change integration

For behavior changes, ask:

- Which reader tasks changed?
- Which docs and examples reference the old behavior?
- Is the API contract or schema version affected?
- Is migration or deprecation guidance required?
- Did a runbook command, dashboard, target, or rollback path change?
- Does client handoff or support scope change?

Prefer documentation changes in the same PR or release unit as behavior changes. Use CI for deterministic checks such as links, code snippets, generated-spec drift, and site builds; retain human review for meaning and usability.

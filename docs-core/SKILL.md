---
name: docs-core
description: "Orchestrate evidence-backed project documentation across README and project overviews, developer onboarding, architecture and ADRs, API references and integration guides, operational runbooks and SOPs, user help and release notes, documentation maintenance, and complete client handoff. Use when creating, updating, auditing, organizing, or transferring documentation for a website, mobile app, Telegram bot or Mini App, .NET backend, API, infrastructure, or delivered client project."
---

# Docs Core

Create the smallest documentation system that lets its intended reader act correctly. Verify facts against the authoritative source, expose unknowns, and keep ownership and update triggers visible.

## Select the mode

Infer the narrowest mode that fulfills the request:

- **Inventory:** map existing documentation, audiences, sources, owners, duplication, gaps, and stale areas.
- **Design:** define information architecture, document types, source-of-truth boundaries, ownership, and lifecycle.
- **Create:** write a new document grounded in current evidence.
- **Update:** preserve useful authored content while correcting changed facts.
- **Verify:** compare documentation with code, contracts, tests, deployment, and current behavior without writing.
- **Onboard:** build a tested path from prerequisites to first successful contribution or operation.
- **Reference:** document stable interfaces, configuration contracts, terminology, and supported behavior.
- **Operate:** create a runbook or SOP with safe steps, verification, rollback, and escalation.
- **Handoff:** assemble the exact knowledge and ownership transfer required by a client or new maintainer.
- **Maintain:** detect drift, broken links, orphaned docs, duplication, and missing review ownership.

Do not require the user to invoke specialist skills manually. Load only the references and wagons needed for the selected mode.

## Resolve audience and authority first

Before writing, record:

- intended reader and the decision or task they must complete;
- scope and appropriate depth;
- authoritative source for each material claim;
- document owner and reviewer;
- state: `Draft`, `Verified`, `Published`, `Deprecated`, or `Archived`;
- verification date or event;
- change trigger that must update the document.

Possible sources of truth include implemented code, tests, generated API contracts, schemas/migrations, deployment manifests, production configuration contracts, accepted product requirements, ADRs, vendor documentation, and observed behavior. Authority is topic-specific: do not assume code always overrides an intentionally design-first API contract, or that a README overrides the build pipeline.

Label uncertain material as `Verified`, `Client-provided`, `Observed`, `Inferred`, `Example`, `Unknown`, or `Decision`. Never turn convention or file names into facts.

## Route by document type

### Documentation system and project entry points

Read [documentation-system-and-governance.md](references/documentation-system-and-governance.md).
Read [readme-and-project-overview.md](references/readme-and-project-overview.md) for README, contributing, setup, and navigation.

- Use `documentation` for a focused technical document.
- Use `gsd-docs-update` when project documentation should be generated or verified against the live codebase through the GSD workflow.
- Use `copy-editing` after technical truth is established, never as a substitute for verification.

### Developer onboarding

Read [developer-onboarding.md](references/developer-onboarding.md).

- Build a shortest path to first verified success, then progressive depth.
- Verify commands in a clean or representative environment when feasible.
- Do not generate fixed audience packs, huge glossaries, or mandatory diagrams without a reader need.

### Architecture and decisions

Read [architecture-and-decisions.md](references/architecture-and-decisions.md).

- Route implementation truth to the relevant engineering core.
- Use diagrams only when relationships or sequence are materially clearer than prose.
- Distinguish current architecture, desired architecture, and historical decisions.

### API and integration documentation

Read [api-and-integration-docs.md](references/api-and-integration-docs.md).

- Use `openapi-spec-generation` for REST/OpenAPI contract creation and maintenance.
- Route API implementation and contract tests to `backend-core` and `api-contract-testing`.
- Keep examples valid, deterministic, sanitized, and consistent with the documented version.

### Runbooks and SOPs

Read [runbooks-and-sops.md](references/runbooks-and-sops.md).

- Use `runbook` for a recurring operational task.
- Use `incident-runbook-templates` for outage, degradation, data, and incident response.
- Use `process-doc` for business processes, RACI, exceptions, and handoffs.
- Route deployment and production truth to `delivery-core`; route testing to `qa-core`.

### User help and releases

Read [user-help-and-release-docs.md](references/user-help-and-release-docs.md).

- Use `kb-article` for focused how-to, troubleshooting, FAQ, or known-issue content.
- Route public search surfaces to `seo-core` when discoverability is in scope.
- Do not expose internal architecture, private data, security-sensitive detail, or unpublished roadmap claims in customer docs.

### Client handoff

Read [client-handoff.md](references/client-handoff.md).

- Route acceptance, commercial support/warranty boundaries, and relationship closeout to `client-core`.
- Route production verification, ownership, backups, monitoring, and recovery to `delivery-core`.
- Route product scope and acceptance artifacts to `product-core`; route UAT evidence to `qa-core`.
- Transfer credentials only through approved secret mechanisms outside documentation and agent context.

## Documentation workflow

1. **Inventory:** find repository instructions and existing docs; identify overlapping or contradictory sources.
2. **Define:** choose audience, task, scope, document type, authority, owner, and verification method.
3. **Trace:** inspect the implementation, contract, tests, deployment, or accepted decision that supports each material section.
4. **Draft:** lead with the reader's task; use progressive disclosure, concrete examples, and explicit limits.
5. **Verify:** check every command, path, link, identifier, version, example, screenshot, diagram edge, and expected result that is in scope.
6. **Review:** obtain the appropriate technical, product, operational, security, legal, or client review.
7. **Publish:** write or publish only within the authorized local or external scope.
8. **Maintain:** attach update triggers, ownership, and drift checks; update docs in the same change as behavior where practical.

Preserve useful existing prose and project conventions. Do not replace a small accurate document with generic boilerplate.

## Truth and safety boundaries

- Never invent commands, paths, endpoints, schemas, responses, defaults, versions, owners, contacts, SLAs, costs, legal duties, support promises, architecture decisions, production state, or observed results.
- Do not claim a command or runbook is tested unless it was actually executed in the stated environment and its result verified.
- Do not copy generated API output into a second manually maintained source without defining authority and regeneration.
- Use placeholders that are visibly non-secret. Never use realistic credentials or production identifiers as examples.
- Never read, search, display, copy, diff, summarize, or edit `.env`, `.env.*`, encrypted vaults, age identities, credentials, keychains, or secret values. `.env.example` is the only readable environment contract when technically necessary.
- Never put passwords, tokens, private keys, recovery codes, connection strings containing secrets, personal data, or production access instructions in documentation, examples, commands, screenshots, logs, or responses.
- Direct secret creation or rotation to `~/.local/bin/secrets-edit <vault>` and run only the narrow application process through `~/.local/bin/secrets-run <vault> -- <command>`.
- Treat publishing to a wiki, knowledge base, repository, package portal, developer portal, or customer system as an external change requiring explicit authorization.
- Treat production commands in runbooks as instructions, not authorization to execute them.

## Completion gate

Do not call documentation complete until applicable statements are true:

1. Audience, task, scope, status, owner, authority, and update trigger are explicit.
2. Material claims are verified or clearly marked as inference, example, decision, or unknown.
3. Commands, paths, links, interfaces, examples, and expected results are checked proportionally to risk.
4. The document leads to a concrete first success or operational outcome.
5. Duplication and contradiction with existing sources are resolved.
6. Security, privacy, secrets, production, and external-publishing boundaries are safe.
7. Handoff documents cover ownership and remaining risk, not just file delivery.
8. The next verification event is visible.

Run `python3 scripts/audit_docs.py <path>` for a secret-safe heuristic review. It reads only explicitly named documentation files, checks local links without opening their targets, and reports issue identifiers without quoting content. Its result is a quality prompt, not proof that the documentation is correct or safe to execute.

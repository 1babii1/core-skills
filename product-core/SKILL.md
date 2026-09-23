---
name: product-core
description: Orchestrate evidence-based product discovery, customer research, problem framing, assumptions, value validation, requirements, scope, prioritization, analytics, experiments, and product decisions. Use when evaluating an idea, starting or rescuing a client project, preparing a PRD or MVP, deciding what to build, defining product metrics or events, validating demand, analyzing feedback, or deciding whether to ship, iterate, pivot, or stop.
---

# Product Core

Decide what is worth building, for whom, why, and how the result will be judged before routing implementation into GSD and the engineering cores.

## Begin with the product mode

Read [operating-model.md](references/operating-model.md), then classify the work:

- **Client project:** clarify the buyer's requested outcome, users, decision-maker, scope, acceptance, change process, and commercial risk.
- **New product:** validate problem, segment, switching behavior, demand, viability, distribution, and the riskiest assumptions before production engineering.
- **Existing product:** use real behavior, funnel, retention, support, revenue, and experiment data to diagnose an outcome.

Do not apply startup discovery theater to a tiny well-understood client task, and do not treat a founder's conviction as customer evidence.

## Select discovery depth

- **Fast scope:** low-cost, reversible, well-understood work. Produce a product brief, scope boundary, acceptance criteria, risks, and success check.
- **Standard discovery:** meaningful feature or client product. Add interviews/data synthesis, assumptions, alternatives, metrics, and validation.
- **Deep discovery:** high cost, strategic commitment, regulated/safety-sensitive domain, new market, or weak evidence. Add structured research, multiple validation steps, economics, and explicit product gates.

Use the cheapest depth that controls the cost of being wrong. Document why it is sufficient.

## Preserve evidence integrity

Read [evidence-and-research.md](references/evidence-and-research.md).

- Label claims as `Fact`, `Observation`, `Quote`, `Metric`, `Assumption`, `Inference`, `Decision`, or `Unknown`.
- Never invent users, quotes, sources, market size, baseline, target, conversion, sample size, confidence, or research findings.
- Distinguish reported intent from past behavior and real commitment.
- Cite current external claims near the claim using primary sources where possible.
- Protect interviewee identity and minimize personal data.
- State contradictory evidence and limitations, not only support for the favored idea.

## Route the work

### Understand the problem

- Prepare or critique interviews with `mom-test`.
- Synthesize multiple interviews with `discover-interview-synthesis`.
- Frame customer progress with `define-jtbd-canvas`.
- Frame the specific problem with `define-problem-statement`.
- Explore outcomes and opportunities with `define-opportunity-tree`.
- Use `competitors` for current competitive and alternative research.

Interview evidence is not automatically representative. Analytics shows what happened; qualitative research helps explain why. Use both when the decision warrants it.

### Surface risk and assumptions

- New product: `identify-assumptions-new`.
- Existing product or feature: `identify-assumptions-existing`.
- Rank tests: `prioritize-assumptions`.
- Write one falsifiable claim: `define-hypothesis`.
- Capture the whole business thesis when useful: `foundation-lean-canvas`.

Override any instruction to proceed directly from a low-risk score to implementation when the underlying evidence is weak. Confidence must reflect evidence, not optimism.

### Validate value

Read [value-validation.md](references/value-validation.md). Match the test to the uncertainty: problem, demand, usability, feasibility, viability, distribution, ethics, or compliance. Prefer observable behavior and progressively stronger commitments. Do not default to an A/B test when traffic is insufficient or the product does not exist.

Use `measure-experiment-design` for controlled quantitative experiments and `measure-experiment-results` for their readout.

### Specify the product

Read [requirements-and-scope.md](references/requirements-and-scope.md).

- Product handoff: `deliver-prd`.
- Story/slice verification: `deliver-acceptance-criteria`.
- Failure surface: `deliver-edge-cases`.
- Candidate ranking: `define-prioritization-framework`.

For client work, also read [client-project-discovery.md](references/client-project-discovery.md). Keep business requirements separate from implementation choices. Do not promise dates or fixed cost while material scope-driving unknowns remain hidden.

### Measure outcomes

Read [metrics-and-instrumentation.md](references/metrics-and-instrumentation.md).

- Define the decision and value moment before selecting a metric.
- Specify events with `measure-instrumentation-spec`.
- Specify decision-oriented dashboards with `measure-dashboard-requirements`.
- Use `analytics` for implementation-aware analytics work.
- Use `cro` only when conversion optimization is actually the product question.

Do not use signups, pageviews, downloads, or raw activity as proof of value without the behavior and outcome they represent.

### Decide and learn

- Record important choices using [decision-journal.md](references/decision-journal.md).
- Use `iterate-pivot-decision` for evidence-based pivot/persevere decisions after meaningful market feedback.
- Apply [product-review.md](references/product-review.md) before approving an artifact or handing work to implementation.

## Product gates

Advance only when the relevant gate has an evidence-backed answer:

1. **Problem gate:** specific actor, circumstance, pain/current alternative, evidence, and why now.
2. **Value gate:** observable behavior or commitment that justifies the next investment.
3. **Scope gate:** in/out/deferred, dependencies, acceptance, change policy, and unresolved assumptions.
4. **Measurement gate:** decision, metric formula, baseline or collection plan, target/threshold rationale, instrumentation, and guardrails.
5. **Release gate:** implementation acceptance, analytics validation, operational readiness, and a decision date after launch.

A gate may explicitly pass with risk accepted by an identified decision-maker. Never silently convert an unknown into a pass.

## Core integration

- Use `gsd-explore` or `gsd-spec-phase` after product intent is sufficiently clear; GSD owns implementation planning, not product truth.
- Route UI hypotheses and prototype work through `design-core`.
- Route architecture and implementation through `frontend-core`, `backend-core`, `mobile-core`, or `telegram-core`.
- Route test coverage and UAT through `qa-core`.
- Route launch engineering through `delivery-core`.
- Route public demand/search questions through `seo-core`.
- Route security/privacy requirements through `auth-core`, `secrets-core`, and the relevant engineering core.

## External actions

Local analysis does not authorize contacting customers, publishing surveys or landing pages, scraping restricted sources, configuring analytics, launching experiments, spending money, changing a roadmap, messaging stakeholders, or editing external product systems. Obtain explicit authorization for those actions.

## Definition of done

Produce only the artifacts justified by the chosen depth. Before handoff, ensure:

1. Mode, decision, owner, discovery depth, and constraints are explicit.
2. Facts, evidence, inferences, assumptions, and unknowns are separated.
3. The problem and value hypothesis are falsifiable.
4. The next investment is proportional to evidence strength.
5. Scope and acceptance are testable; exclusions are visible.
6. Metrics measure delivered value and include guardrails.
7. The next review/decision point and kill/iterate/ship criteria are recorded.

Run `python3 scripts/audit_product.py <path>` for a secret-safe heuristic review of product artifacts. Its result is a quality prompt, not proof that the product has value.

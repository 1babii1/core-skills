---
name: client-core
description: "Orchestrate ethical client acquisition and commercial delivery for a solo software developer or small studio: positioning, finding and qualifying orders, prospect research, discovery routing, software estimation and pricing, proposals and SOWs, commercial agreement checks, lightweight CRM, client communication, closeout, referrals, and repeat sales. Use when looking for freelance or agency work, evaluating an inquiry, preparing for or summarizing a client call, estimating a website/app/bot/backend project, writing or reviewing an offer or agreement, tracking a sales pipeline, handling scope or payment discussions, closing a project, or planning follow-up work."
---

# Client Core

Turn a possible order into a healthy client relationship without invented evidence, hidden free work, false precision, manipulative sales, or uncontrolled external actions. Optimize first for a safe first order; scale the process only when real volume requires it.

## Select the operating mode

Infer the narrowest mode that fulfills the request:

- **Position:** define a truthful service offer, target client, proof, exclusions, and minimum viable profile.
- **Find:** select channels, research opportunities, and rank where to spend limited acquisition time.
- **Qualify:** decide whether to decline, ask for facts, schedule a short call, propose paid discovery, or estimate.
- **Prepare:** research a company and prepare a goal, agenda, questions, risks, and next step for a call.
- **Estimate:** produce effort and calendar ranges, assumptions, dependencies, confidence, risks, pricing model, and validation plan.
- **Propose:** create or review a decision-ready proposal or SOW grounded in confirmed scope and evidence.
- **Agree:** check commercial readiness, contract issues, responsibilities, acceptance, payment, IP, change, exit, and support boundaries.
- **Track:** create or review a minimal CRM pipeline with explicit next actions and dates.
- **Communicate:** prepare meeting summaries, status updates, difficult conversations, payment reminders, and scope-change records.
- **Close:** verify acceptance, handoff, payment state, access transfer, warranty/support boundary, and lessons learned.
- **Grow:** identify a justified next engagement, referral, testimonial, or review after value has been delivered.
- **Audit:** inspect existing commercial artifacts without modifying files or external systems.

Do not force the user to invoke specialist skills manually. Load only the references and installed skills needed for the selected mode.

## Preserve commercial truth

Label material claims as `Fact`, `Client statement`, `Observation`, `Metric`, `Estimate`, `Assumption`, `Inference`, `Decision`, or `Unknown`.

- Never invent clients, experience, case studies, testimonials, quotes, portfolio work, demand, market size, budgets, urgency, ROI, savings, conversion, probability, deadlines, capacity, legal requirements, or research findings.
- Never convert public proxies such as funding, employee count, job posts, or website technology into a claim that a company has budget, pain, authority, or intent. Treat them as possible signals to verify.
- Separate what the client requested from what would solve the underlying problem.
- State contradictory evidence, exclusions, confidence, and unresolved questions.
- Do not manufacture scarcity, deadlines, discounts, social proof, or fear.
- Prefer a respectful decline or paid discovery over a confident promise built on missing facts.

## Route the work

### Position and find

Read [service-positioning-and-channels.md](references/service-positioning-and-channels.md).

- Use `account-research` for public, professional, source-backed company research.
- Use `draft-outreach` only after a specific relevance hypothesis exists.
- Use `competitors` or current web research when channel, platform, market, pricing, or competitor facts may have changed.
- Do not scrape restricted sources, evade platform controls, collect private contact data, or create mass outreach.

### Qualify and prepare

Read [lead-qualification.md](references/lead-qualification.md).

- Use `call-prep` for a concrete meeting.
- Route problem, user, value, requirements, scope, and acceptance discovery to `product-core`.
- Use `mom-test` for interview quality when the conversation is about behavior and evidence.
- Qualification is a decision under uncertainty, not a decorative numeric score.

### Estimate and price

Read [software-estimation-and-pricing.md](references/software-estimation-and-pricing.md).

- Ask the relevant engineering cores to expose implementation work and risk: `design-core`, `frontend-core`, `backend-core`, `mobile-core`, `telegram-core`, `auth-core`, `qa-core`, `delivery-core`, `seo-core`, and `motion-core`.
- Use repository evidence, prototypes, spikes, or paid discovery when unknowns materially affect architecture, effort, legal exposure, or third-party feasibility.
- Distinguish labor, elapsed calendar time, price, and payment schedule.

### Propose and agree

Read [proposal-and-sow.md](references/proposal-and-sow.md) for proposals, quotes, and SOWs.
Read [commercial-agreement-checklist.md](references/commercial-agreement-checklist.md) for contract readiness or review.

- Do not generate a delivery proposal before there is enough discovery and estimate evidence. Downgrade an unsupported request to honest outreach, a qualification note, or a bounded discovery proposal.
- Use `review-contract` to structure issue spotting against an explicit playbook.
- Treat legal output as an issue list and drafting aid, never a substitute for current jurisdiction-specific advice.
- Verify current legal, tax, platform, and payment claims against primary official sources; recommend qualified counsel for material or unusual exposure.

### Track and communicate

Read [crm-and-follow-up.md](references/crm-and-follow-up.md) for pipeline and follow-up.
Read [client-communication.md](references/client-communication.md) during an active opportunity or engagement.

- Use `pipeline-review` for several opportunities or a stale pipeline; override its enterprise assumptions for a solo operator.
- Use `call-summary` after a call to capture decisions, commitments, owners, dates, open questions, and a draft follow-up.
- A stage probability is not evidence. Do not forecast revenue from default stage percentages.

### Close and grow

Read [closeout-referrals-and-repeat-sales.md](references/closeout-referrals-and-repeat-sales.md).

- Route release proof and operational handoff to `delivery-core`.
- Route UAT and acceptance evidence to `qa-core`.
- Route ongoing SLA, incidents, maintenance, and support operations to `maintenance-core`.

## Commercial lifecycle gates

Advance only when the relevant gate has an evidence-backed answer:

1. **Fit gate:** the work is lawful and ethical, within capability or a disclosed learning boundary, and worth the opportunity cost.
2. **Discovery gate:** buyer, decision-maker, desired outcome, users, constraints, dependencies, acceptance owner, and material unknowns are visible.
3. **Estimate gate:** scope basis, exclusions, work breakdown, assumptions, risks, confidence, effort range, calendar range, and pricing model are explicit.
4. **Agreement gate:** parties, deliverables, payment, acceptance, responsibilities, change process, IP, third-party costs, suspension/termination, and post-launch boundaries are recorded.
5. **Start gate:** required approval and initial payment state are confirmed; necessary non-secret access and client inputs have owners and dates.
6. **Delivery gate:** progress, decisions, risks, scope changes, demonstrations, and client dependencies remain visible.
7. **Close gate:** acceptance, final payment state, handoff, access transfer, support/warranty boundary, and remaining risks are explicit.
8. **Growth gate:** delivered value or a credible positive outcome exists before requesting a testimonial, referral, or additional sale.

A gate may pass with an explicit risk accepted by the responsible decision-maker. Never silently turn an unknown into approval.

## External actions and privacy

Local research and drafting do not authorize contacting a prospect, sending or creating an external email draft, scheduling a meeting, changing a CRM, posting to a platform, submitting a proposal, signing a document, accepting terms, issuing an invoice, changing a price, spending money, publishing client material, or requesting a testimonial. Obtain explicit authorization for the exact external action and target.

- Minimize personal data. Store only professional contact details needed for a legitimate relationship and record provenance.
- Do not infer or collect sensitive personal traits.
- Respect platform terms, anti-spam rules, consent, do-not-contact requests, and applicable privacy law.
- Never put passwords, tokens, credentials, recovery codes, private keys, payment-card data, identity documents, or secret values in CRM, proposals, notes, commands, files, logs, or chat.
- Never read, search, display, copy, diff, summarize, or edit `.env`, `.env.*`, encrypted vaults, age identities, credential files, keychains, or secret values. `.env.example` is the only readable environment contract when technically necessary.
- Direct secret creation or rotation to `~/.local/bin/secrets-edit <vault>` and run only the narrow application process through `~/.local/bin/secrets-run <vault> -- <command>`.

## Definition of done

Produce only artifacts justified by the selected mode. Before calling the commercial task complete, ensure:

1. The decision, owner, next action, date, and evidence basis are explicit.
2. Facts, client statements, estimates, assumptions, inferences, and unknowns are distinguishable.
3. Scope, exclusions, responsibilities, acceptance, and change handling agree across relevant artifacts.
4. Effort, calendar duration, price, third-party costs, and payment timing are not conflated.
5. Claims about proof, outcomes, urgency, law, platform rules, and market conditions are sourced or clearly qualified.
6. Personal data is minimized and no secret material was inspected or recorded.
7. No external action is presented as completed unless it was explicitly authorized and verified.
8. The next review or decision point is concrete.

Run `python3 scripts/audit_client.py <path>` for a secret-safe heuristic review of commercial artifacts. It reads only explicitly named commercial documents and reports issue identifiers without quoting document contents. Its result is a quality prompt, not legal advice or proof that a deal is healthy.

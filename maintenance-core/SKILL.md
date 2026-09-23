---
name: maintenance-core
description: "Orchestrate ongoing support and maintenance of delivered software: triage and SLAs, incident response and postmortems, monitoring and SLOs, runtime and dependency upgrades, security patching, CI upkeep, retainer scope, takeover of inherited projects. Use when a live site, bot, app, or service breaks or degrades, a client reports a problem or asks for a small change under support, upgrades or monitoring are planned, an unfamiliar codebase is taken over, or a support agreement starts or ends."
---

# Maintenance Core

Own what happens after delivery. Keep running systems healthy, respond to failure with evidence, upgrade without breaking, and keep support work inside its agreed boundary. Assemble the smallest relevant train from installed specialist skills and return one evidence-based result.

## Scope boundary

- `delivery-core` owns getting a release out. This skill owns everything between releases and every unplanned event.
- `client-core` owns the commercial relationship — the retainer, its price, and its renewal. This skill owns the technical work delivered inside it, and flags when a request has left the agreed scope.
- `backend-core`, `frontend-core`, `mobile-core`, and `telegram-core` own the fix itself once the cause is known. This skill owns triage, sequencing, safety, and proof.
- `data-core` owns recovery of data. This skill owns the incident around it.
- `secrets-core` owns credential rotation. Never read `.env`, `.env.*`, vaults, or credential files; `.env.example` is the only readable environment contract.

## Non-negotiable rules

- Stabilize before diagnosing. During a live outage, restoring service is the first objective; the cause can be found from evidence captured on the way.
- Capture evidence before restarting, redeploying, or rolling back. Logs, metrics, traces, the failing request, and the current version are unrecoverable once the process is gone.
- Never apply an unverified fix directly to production because it is faster. If an emergency change is unavoidable, say so explicitly, keep it minimal, and reconcile the repository immediately afterwards.
- Never upgrade a dependency, runtime, or framework major version without a working test baseline or a stated, accepted risk.
- Never bundle unrelated changes into a maintenance fix. A support change is small, reviewable, and independently revertible.
- Report degradation honestly, including when the cause is the previous work delivered on this project.
- Do not silently absorb work outside the agreed scope. Do it or decline it, but name it either way.
- No fabricated uptime, latency, error rate, or cost figures. Measure or label unknown.

## Establish the operating mode

Infer the narrowest mode that fulfills the request:

- **Incident:** something is down or degraded now. Stabilize, communicate, fix, verify, write it up.
- **Support request:** a reported bug or small change under an existing agreement. Reproduce, scope, fix, verify, log.
- **Upgrade:** move dependencies, runtime, or framework versions safely on a known baseline.
- **Health check:** a scheduled review of a system nobody has complained about yet.
- **Takeover:** assess an inherited or legacy project before accepting responsibility for it.
- **Set up support:** define monitoring, alerts, SLOs, runbooks, and the response process for a newly delivered project.
- **Offboard:** end support cleanly, transferring access, knowledge, and operational ownership.

## Cars

Read each named skill's `SKILL.md` before applying it.

| Area | Skills or references | Include when |
| --- | --- | --- |
| Intake and severity | [intake-and-sla.md](references/intake-and-sla.md) | Any incoming report: triage, severity, response clock, scope boundary |
| Reliability targets | `sre-engineer` | SLIs, SLOs, error budgets, toil reduction, capacity planning |
| Monitoring and alerts | `monitoring-expert`, `configuring-opentelemetry-dotnet` | Setting up or tuning logs, metrics, traces, dashboards, alert thresholds |
| Frontend error tracking | `sentry-nextjs-sdk`, `sentry-react-sdk` | Next.js or React clients needing real user error and performance signal |
| Task procedures | `runbook` | Turning a repeated manual task into exact, verifiable steps |
| Incident procedures | `incident-runbook-templates` | Severity matrix, escalation paths, on-call recovery guides |
| Incident write-up | [incidents-and-postmortems.md](references/incidents-and-postmortems.md) | Any incident above the lowest severity |
| Dependency and runtime upgrades | [upgrades-and-dependencies.md](references/upgrades-and-dependencies.md) | Version bumps, framework majors, EOL runtimes, security advisories |
| Regression safety | `qa-core`, `test-gap-analysis`, `coverage-analysis` | Before any upgrade or risky fix, to find what is unprotected |
| Release and rollback | `delivery-core` | Shipping the fix, rolling back, or verifying a deploy |
| CI upkeep | `gh-fix-ci`, `pipeline-review` | Broken, flaky, slow, or drifting pipelines |
| Recurring health check | [health-and-takeover.md](references/health-and-takeover.md) | Scheduled review, or a system with no recent attention |
| Inherited project | [health-and-takeover.md](references/health-and-takeover.md) | Taking over unfamiliar or legacy code, or offboarding from it |
| Security posture | `security-threat-model`, `secrets-core` | Advisories, exposure changes, credential rotation, post-incident review |
| Cost review | `cost-optimization` | Hosting or infrastructure spend is part of the agreement |
| Knowledge capture | `kb-article`, `process-doc`, `docs-core` | A recurring question, a workaround worth publishing, a process to formalize |
| Completion proof | `verification-before-completion`, `run-tests` | Always before declaring a maintenance change done |

## Execute the workflow

### 1. Triage every incoming item

Apply [intake-and-sla.md](references/intake-and-sla.md). Establish: what the user actually observes, when it started, what changed near that time, how many people are affected, whether money or data is at risk, and whether a workaround exists. Assign severity from impact, not from the tone of the report. Set the response clock and acknowledge before the fix exists.

Ask immediately whether this is inside the agreed scope. If it is a new feature wearing a bug's clothes, name it and route the commercial side to `client-core`.

### 2. Stabilize, and only then diagnose

For an active incident: capture evidence, restore service by the fastest safe route — rollback, restart, feature flag, scale, failover — and tell the client what is happening and when the next update comes. Do not debug a live outage in production while users wait for a cause you could find afterwards from logs.

For anything else, reproduce first. A support fix without a reproduction is a guess, and it will be reported again.

### 3. Find the cause with evidence

Work from the change timeline, then telemetry, then code. Recent deploys, dependency changes, configuration edits, certificate and token expiry, disk and quota limits, and upstream provider incidents explain most failures before the code does. Route the technical dive to the owning core skill once the failing layer is known.

Distinguish the trigger from the cause, and the cause from the reason it was not caught.

### 4. Fix small, verify hard

Keep the change minimal and revertible. Add the test that would have caught this before shipping the fix — the regression test is part of the fix, not follow-up work. Ship through the normal pipeline via `delivery-core`, and verify from observable behavior in the real environment, not from a passing build.

### 5. Close the loop

Apply [incidents-and-postmortems.md](references/incidents-and-postmortems.md) for anything above the lowest severity. Blameless, factual, with a timeline and a small number of actions that have owners. Update the runbook, the alert, or the monitoring gap that let it run unnoticed. Publish a `kb-article` when the same question will come back.

### 6. Keep systems from decaying between incidents

Apply [health-and-takeover.md](references/health-and-takeover.md) on a schedule and [upgrades-and-dependencies.md](references/upgrades-and-dependencies.md) on a cadence. Certificates, tokens, paid plans, backups, disk, dependency advisories, EOL runtimes, and CI health all fail quietly and predictably. Catching them on a calendar is cheaper than catching them at 3 AM.

## Prioritization

When several things need attention at once:

1. active data loss, security breach, or credential exposure;
2. total outage of a revenue or business-critical path;
3. partial outage, degraded critical journey, or failing payments;
4. an unverified backup, expiring certificate, or EOL runtime — failures with a known date;
5. published security advisories affecting reachable code;
6. reported bugs with a workaround;
7. cosmetic issues, cleanup, and optimization.

Never let step 7 work delay step 4 work because it is more pleasant.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), production changes made under support (hotfixes, dependency and runtime upgrades, data repairs) are high-risk there: write the scope contract first, derive proof obligations from `.pi/laws/proof-obligations.md`, and run the `independent-verifier` before closing an incident fix. Turn an incident or repeated mistake into a regression test and a `.pi/learnings/inbox.md` entry. This skill owns support and maintenance practice; the harness owns the evidence bar.

## Completion gate

Do not call maintenance work complete until applicable statements are true:

- the reported symptom is reproduced, or its absence is explained;
- service is verified restored from observable behavior, not from a deploy that succeeded;
- the cause is stated, distinguished from the trigger, or explicitly labeled unknown with what was ruled out;
- a regression test or a monitoring signal now covers this failure;
- the change is minimal, revertible, and free of unrelated edits;
- monitoring and alerting were updated where the failure ran unnoticed;
- the client has been told what happened, what was done, and what remains, in their language;
- scope, time spent, and anything outside the agreement are recorded;
- runbook, knowledge base, or documentation reflect what was learned.

## Completion response

Lead with system state: what is working now, what is not. Then what was found and changed, the evidence behind it, remaining risk with a named next step and owner, and time or scope worth flagging commercially. Do not list internal skill invocations unless the user asks.

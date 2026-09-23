# Intake, severity, and the scope boundary

Use for every incoming report or request against a system under support. Contract terms and pricing belong to `client-core`; this reference covers how a request is classified and handled technically.

## Turn a report into a ticket

A client message is not a problem statement. Extract, asking only what cannot be inferred:

- what they observe, in their words, and what they expected instead;
- the exact URL, screen, bot command, or endpoint, and a screenshot or error text;
- when it started and whether it ever worked;
- who is affected — one user, one device, one region, or everyone;
- environment: browser, OS, app version, and whether it reproduces elsewhere;
- whether money, data, or a deadline is at risk;
- what changed near that time: a deploy, a config edit, a content update, a provider incident.

Reproduce before promising anything. If it does not reproduce, say so and ask for the narrowest missing detail rather than guessing.

## Severity from impact, not volume

| Severity | Meaning | Response | Fix path |
| --- | --- | --- | --- |
| S1 | Data loss, security breach, or a business-critical path fully down | Immediately, drop other work | Restore first, root cause after |
| S2 | Major function broken or payments failing, no workaround | Same working day | Fix, ship through normal pipeline |
| S3 | Function degraded, workaround exists | Next working day | Scheduled into the current cycle |
| S4 | Minor defect, cosmetic, low-traffic edge case | Acknowledge, batch it | Next scheduled release |

Two rules keep this honest: an urgent tone does not raise severity, and a quiet failure that is silently losing data is S1 even if nobody has complained. Escalate severity when new evidence justifies it, and say why.

## Acknowledge before you can fix

Acknowledgement and resolution are separate clocks. Acknowledge fast, in the client's language, with what is known and when the next update comes — then keep that update promise even when there is nothing new. Silence during an incident does more relationship damage than the outage.

State what you actually know. Do not estimate a fix time before the cause is understood; give the time of the next update instead.

## Is this inside the agreement?

Classify every request before working on it:

- **Defect** — delivered behavior does not match what was agreed. Inside support.
- **Environmental** — a provider outage, expired certificate, exhausted quota, or third-party change. Usually inside support to diagnose; the resolution may need the client's action or budget.
- **Change** — behavior working as built, but the client now wants it different. Outside support. Estimate it via `client-core`.
- **New capability** — something that does not exist. Outside support, always.
- **Consequence of client action** — content edits, direct database changes, revoked access, unpaid services. Diagnose, then decide commercially.

The failure mode of solo maintenance is absorbing changes as bug fixes until the retainer covers a second project for free. Do the work if it is small and worth the goodwill, but name it: what it was, how long it took, and that it sat outside scope. Both sides need the record.

## Log every item

Keep one lightweight record per item — date, reporter, severity, symptom, cause, change made, time spent, in or out of scope, and where verification lives. It answers three questions later that nothing else can: whether the retainer is priced correctly, which parts of the system consume support time and deserve a real fix, and what was actually done when the client asks in six months.

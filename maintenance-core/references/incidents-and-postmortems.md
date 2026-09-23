# Incident response and postmortems

Use during and after any incident above the lowest severity. Severity assignment lives in [intake-and-sla.md](intake-and-sla.md); escalation matrices and on-call guides come from `incident-runbook-templates`.

## During the incident

Order of operations, without exception:

1. **Confirm the blast radius.** What is broken, for whom, since when. Check whether it is the application at all — provider status pages, DNS, certificates, quotas, and payment or SMS gateways account for a large share of "the site is down".
2. **Capture evidence.** Current deployed version, recent deploys and config changes, error logs and stack traces, metrics around the start time, a failing request or trace, and the state of any queue or job runner. Do this before restarting anything; a restart destroys the evidence and the incident will recur.
3. **Restore service.** Fastest safe route: roll back the last deploy, revert the configuration change, disable the feature flag, restart the stuck process, scale the exhausted resource, fail over. A rollback that restores users beats a fix that is still being written.
4. **Communicate.** Tell the client what is affected, that it is being worked, and when the next update comes. Update on that schedule even with nothing new. Say when it is resolved, plainly.
5. **Verify from the user's position.** Load the real page, run the real bot command, complete the real purchase. A green deploy is not a restored service.

Keep a running timestamped note while working. Reconstructing a timeline afterwards from memory produces a wrong one.

## Emergency changes

If production must be changed directly to stop damage: keep it minimal, note exactly what was changed, and reconcile the repository the same day. An undocumented production edit becomes an unexplainable failure at the next deploy, when it is silently overwritten.

## After the incident

Write it up for anything above the lowest severity, within a day or two while detail is recoverable. Blameless and factual — the subject is the system that allowed the failure, not the person who typed.

Cover:

- **Impact:** who was affected, how, and for how long, in user and business terms rather than error counts.
- **Timeline:** first occurrence, first detection, acknowledgement, mitigation, resolution — with timestamps. The gap between occurrence and detection is usually the most valuable number in the document.
- **Trigger:** the immediate change or event.
- **Cause:** the condition that made the trigger harmful. These are different, and stopping at the trigger produces useless actions.
- **Detection:** how it was found. If a client found it before monitoring did, that is a finding on its own.
- **Recovery:** what actually restored service, including anything tried that did not work.
- **Actions:** a small number, each with an owner and a date. Three real ones beat twelve aspirational ones.

## Actions that are worth writing down

Prefer, in order: make the failure impossible, make it detected automatically, make recovery a documented procedure, make it visible in a dashboard. "Be more careful" is not an action. Neither is a training note nobody will read.

Every incident should produce at least one of: a regression test, an alert that would have fired sooner, a runbook step, or a removed sharp edge. If it produced none, the analysis stopped too early.

## Feed it back

- Add the alert or tune the threshold that missed it — via `monitoring-expert`.
- Turn the recovery steps into a `runbook` if it could recur.
- Publish a `kb-article` if clients or users will ask about it again.
- Reassess SLOs and error budget with `sre-engineer` when incidents cluster in one area.
- Review the incident log periodically: repeated incidents in the same component are a design problem being paid for in support hours, and should be raised commercially through `client-core`.

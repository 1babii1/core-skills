# Runbooks and SOPs

## Choose the artifact

- **Operational runbook:** exact procedure for a recurring technical task.
- **Incident runbook:** detection, triage, mitigation, recovery, communication, escalation.
- **SOP/process document:** roles, triggers, decisions, exceptions, evidence, and business process.
- **Checklist:** short guard against omission when the operator already knows the procedure.

Do not mix policy (“what must be true”) with procedure (“how to act”) without labeling both.

## Runbook contract

Every operational runbook should include:

- purpose, trigger, scope, and explicit non-use cases;
- owner, approver, status, last verified environment/version, and review trigger;
- exact target resolution: system, environment, region/project, version, and data scope;
- prerequisites, permissions by name, tools, inputs, and safe access path;
- numbered steps with command/action, expected result, and failure branch;
- read-only inspection or dry run before mutation where possible;
- checkpoints and stop conditions;
- verification of the intended outcome and critical invariants;
- rollback or roll-forward decision, trigger, authority, and verification;
- escalation conditions and current role/channel, without personal secrets;
- related dashboards, alerts, incident, recovery, and architecture docs.

Production instructions never authorize production execution.

If the target, current recovery evidence, rollback/roll-forward path, or
authorized approver is unknown, mark the document prominently
`DRAFT — NOT EXECUTABLE`. Do not provide a copyable destructive command and do
not perform a mutation. Replace the step with the evidence and approval needed
to make it executable.

For high-impact or irreversible steps, require an explicit operator checkpoint
and an independent authorized approver when the organization's process provides
one. Record approval metadata without credentials or secret values. Examples,
targets, thresholds, and response times from templates are illustrative until
verified for this system; this rule overrides defaults in routed template skills.

## Command safety

- Use explicit resolved targets, not broad globs or ambiguous environment variables.
- State the working directory, required tool version, and context.
- Separate inspect, plan/dry-run, execute, and verify.
- Put warnings immediately before destructive or irreversible steps.
- Require backups or recovery points when data may be lost.
- Do not embed credentials, tokens, private keys, or secret-bearing connection strings.
- Do not include a command that prints environment variables or secrets.
- Prefer application commands through the approved secrets wrapper when runtime secrets are required.
- Never auto-execute a mutating step merely because the runbook has just been
  drafted, reviewed, or displayed.

If a safe rollback does not exist, say so and define a roll-forward/recovery path.

## SOP structure

Capture:

- trigger and desired output;
- in-scope and out-of-scope cases;
- responsible, accountable, consulted, and informed roles when ambiguity exists;
- normal flow and decision points;
- required evidence and record retention;
- exceptions and escalation;
- metrics only when formula, source, owner, and decision use are known.

Do not invent RACI participants or numeric targets.

## Validation

For high-risk procedures:

1. desk-check every path and command;
2. run in a safe representative environment;
3. have an unfamiliar qualified operator follow it;
4. verify rollback/recovery where feasible;
5. update after incidents, platform changes, or failed rehearsals.

Record exactly what was tested. A syntax check is not operational validation.

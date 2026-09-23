# Client Handoff

## Handoff is an ownership transfer

The goal is not a ZIP archive. The client or named maintainer must be able to understand, operate, verify, pay for, recover, and safely change the delivered system within the agreed boundary.

## Handoff index

Create one canonical entry point covering:

| Area | Required evidence |
| --- | --- |
| Delivered scope | Accepted deliverables, exclusions, deferred work, version |
| Repositories/artifacts | Canonical locations, branches/releases, build identity |
| Architecture | Deployable units, data stores, integrations, trust boundaries |
| Environments | Purpose, owner, deployment path, non-secret configuration contract |
| Domains/platforms | Registrar, DNS, hosting, stores, Telegram/platform ownership |
| Data | Ownership, location, migration state, retention, export, deletion |
| Operations | Health, monitoring, alerts, logs, backups, restore, costs |
| Runbooks | Deploy, rollback/recovery, routine maintenance, incidents |
| API/integrations | Contracts, credentials process, limits, vendor ownership |
| Quality | Acceptance/UAT evidence, known issues, test and verification commands |
| Support | Warranty, maintenance, SLA/response boundary, escalation |
| Commercial | Third-party subscriptions, renewal dates, payer and cancellation owner |
| Open risk | Limitations, accepted risks, debt, next review and owner |

Link to canonical documents; do not duplicate their full contents.

## Accounts and access

Record account and ownership metadata without secret values:

- service/platform name;
- purpose;
- legal owner and operational administrator;
- billing owner;
- recovery owner;
- MFA and recovery process status;
- transfer state and verification;
- secure mechanism used for credentials outside the document.

Never put passwords, tokens, private keys, recovery codes, payment-card data, identity documents, or secret URLs in the handoff. Use `secrets-edit`/approved password or vault workflows outside agent context.

Use least privilege and time-limited access where the platform supports it.
Approve the exact recipient and channel, verify identity separately, enable MFA,
and retain a non-secret audit record of who transferred what category of access,
when, and whether the receiver independently confirmed it. The document may name
the approved vault or password manager, but must not contain an exported secret.

If a secret has already entered documentation, chat, logs, or version history,
stop redistributing it, treat it as compromised, revoke or rotate it through the
approved secret workflow, restrict exposed copies where authorized, and review
relevant access/audit records. Do not copy the value while investigating.

## Operational readiness

Verify with `delivery-core`:

- deployed version/artifact and target;
- health and critical journey;
- logs, metrics, traces, and alerts;
- backup success and restore evidence appropriate to risk;
- migration state and data invariants;
- rollback or roll-forward path;
- certificate/domain/subscription renewal ownership;
- current cost and budget alerts from authoritative sources.

Do not state that backup or recovery works merely because it is configured.

## Knowledge transfer

Tailor the session to the receiver:

- system overview and boundaries;
- routine operation;
- one representative change;
- one failure/recovery scenario;
- support and escalation;
- open risks and next decisions.

Record questions and update documentation after the session. A meeting occurred is not proof of successful transfer; ask the receiver to perform representative tasks where proportionate.

For access transfer, suitable evidence is the receiver authenticating with MFA
and completing an agreed safe, least-privilege check without revealing the
credential. A sender-side screenshot or “sent” status alone is insufficient.

## Sign-off

Coordinate with `client-core` and capture:

- handoff package/version;
- acceptance owner and evidence;
- accounts/assets transferred and verified;
- items explicitly retained by the developer;
- outstanding defects versus future enhancements;
- support/warranty start and end condition;
- final payment state by status only;
- unresolved risk accepted by the authorized person;
- next review or support contact.

External account transfers, production changes, publication, and messages require explicit authorization for the exact target.

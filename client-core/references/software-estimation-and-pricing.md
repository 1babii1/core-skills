# Software Estimation and Pricing

## Estimation is conditional

An estimate is valid only for a stated scope basis, assumptions, dependencies, evidence date, and confidence. It is not a promise that uncertainty has disappeared.

Start by choosing the estimate class:

- **Rough range:** early fit or budget conversation; broad scope and low commitment.
- **Discovery estimate:** price and time for reducing named unknowns.
- **Delivery estimate:** requirements and acceptance are sufficiently stable.
- **Change estimate:** delta from an agreed baseline.
- **Remaining-work forecast:** based on measured progress and newly observed complexity.

## Build the estimate

### 1. Establish the basis

Record:

- artifact/version used as scope;
- in-scope outcomes and deliverables;
- exclusions and deferred work;
- acceptance method;
- client inputs and dates;
- external systems and third-party assumptions;
- non-functional and release obligations;
- known unknowns and estimate expiry/review trigger.

### 2. Decompose by deliverable and risk

Ask relevant cores to expose work for:

- product clarification and UX;
- frontend, backend, mobile, Telegram, integrations, data and migration;
- auth, privacy, security, permissions, and abuse cases;
- testing, accessibility, compatibility, performance, and UAT;
- deployment, observability, backups, migration, handoff, and documentation;
- project communication, demonstrations, decisions, and coordination.

Do not estimate only visible screens or happy-path coding.

### 3. Use ranges

For uncertain items, record optimistic, most likely, and adverse-but-plausible cases. PERT may summarize a distribution, but the result remains conditional and should not be presented as precision.

For each work item capture:

| Field | Meaning |
| --- | --- |
| Deliverable | Observable result |
| Evidence | Repository, spec, prototype, analogous measured work, or expert decomposition |
| Effort range | Focused labor, not elapsed days |
| Dependencies | Inputs and decisions required |
| Uncertainty | What could change the range |
| Validation | Spike, question, prototype, or test that reduces uncertainty |
| Confidence | High, medium, low, with reason |

### 4. Build calendar time separately

Elapsed time includes:

- actual availability and context switching;
- parallelizable versus sequential work;
- client review and approval windows;
- third-party response times;
- environment and release windows;
- holidays and known absences;
- uncertainty and recovery capacity.

Do not convert 40 estimated hours automatically into one calendar week.

### 5. Treat risk explicitly

Do not apply a universal contingency percentage. Model named scenarios:

- integration documentation or sandbox is missing;
- migration data is inconsistent;
- app-store or platform review requires changes;
- client content or decisions arrive late;
- acceptance reveals a requirement gap;
- a security or performance constraint changes architecture.

Either include the expected scenario in the range, price it as an option, convert it to discovery, or make it a change trigger.

## Choose a commercial model

### Fixed price

Use when deliverables, acceptance, dependencies, and change handling are stable. Price covers the agreed risk allocation, not just estimated hours.

### Time and materials

Use when priorities or solution details will evolve. Define cadence, rate unit, approval/notification thresholds, reporting, and a stop or budget-review point.

### Paid discovery

Use when knowledge is the first deliverable. Define the questions, artifacts, timebox, access, decision gate, and whether the implementation estimate follows.

### Milestone delivery

Use when vertical outcomes can be demonstrated and accepted separately. Milestones should be meaningful deliverables, not arbitrary completion percentages.

### Retainer

Use for reserved capacity or recurring work. Define included capacity, response expectations, rollover, overage, priority, exclusions, minimum term, and termination.

### Value-informed pricing

Use value to understand affordability and priority only when client-provided economics are credible. Do not invent ROI or charge from a hypothetical upside. Separate value, cost, price, and risk.

## Pricing record

Show:

- currency and tax/fee treatment to verify;
- price or rate and pricing model;
- included deliverables and capacity;
- optional items;
- third-party costs and owner;
- payment milestones or billing cadence;
- validity/re-estimation trigger;
- late, pause, restart, cancellation, and change handling to place in the agreement.

Never publish or change a price externally without user approval.

## Estimate quality gate

Before commitment verify:

1. Scope basis, exclusions, acceptance, dependencies, and client inputs are explicit.
2. Unknowns that can change architecture or cost are not hidden.
3. Design, testing, security, delivery, communication, and handoff are included where relevant.
4. Effort, elapsed time, price, expenses, and payment timing are separate.
5. Ranges and confidence have an evidence basis.
6. Change and re-estimation triggers are visible.
7. The promised date includes real availability and client/third-party time.

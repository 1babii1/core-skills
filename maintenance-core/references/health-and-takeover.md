# Health checks, project takeover, and offboarding

Use for scheduled reviews of a quiet system, for assessing an inherited codebase before accepting responsibility, and for ending support cleanly.

## Recurring health check

Most production failures announce themselves in advance to anyone who looks. Run this on a schedule per supported project and record the date and result — the trend matters more than any single run.

**Fails on a known date:**
- TLS certificates and their auto-renewal, actually verified rather than assumed;
- domain registration and DNS records;
- API tokens, webhook secrets, signing keys, and OAuth credentials with expiry;
- paid plans, quotas, and free-tier limits on hosting, database, email, storage, and third-party APIs;
- runtime, framework, and database versions against their published EOL dates;
- app store signing certificates and provisioning profiles.

**Degrades gradually:**
- disk, memory, and connection pool headroom;
- database size growth, table bloat, and index health — route to `data-core`;
- log and backup storage growth;
- error rate and latency trend against the last check, not against zero;
- queue depth and job failure counts;
- bundle size and Core Web Vitals for frontends.

**Silently stops working:**
- backups: running, and restored successfully within a stated window — route to `data-core`;
- monitoring and alerting: an alert that has never fired may be broken rather than reassuring — test one;
- scheduled jobs and cron tasks: confirm last successful run, not just that they are configured;
- webhooks from payment, messaging, and auth providers;
- CI pipelines: still green, still running, still on supported runners — route to `pipeline-review` and `gh-fix-ci`.

**Also review:**
- open security advisories on reachable dependencies;
- publicly exposed surfaces that should not be — debug endpoints, staging environments, open admin routes, storage buckets;
- infrastructure cost against expectation, via `cost-optimization`.

Report as a short delta: what changed since last time, what has a deadline, what needs a decision. A health check that produces no findings should still produce dates.

## Taking over an inherited project

Never accept operational responsibility before knowing what you are accepting. Time-box an assessment and report findings before committing to a support agreement.

**Can you operate it at all?**
- Full access inventory: repository, hosting, domain, DNS, database, monitoring, error tracker, third-party accounts, app store accounts, payment provider. Missing access is the single most common blocker, and it can take weeks to resolve through a departed developer.
- Can the project be built and run locally from a clean checkout, using only documented steps and `.env.example`? Time how long it takes.
- Is the deployed version the same as the repository's main branch? Uncommitted production changes are common in inherited work and must be found before the first deploy.
- Is there a deploy path you can execute, and a rollback path you have verified?
- Do backups exist, and has a restore been performed?

**What is the risk you are inheriting?**
- Runtime and framework support status, and how far from current;
- test coverage on critical paths — `coverage-analysis` and `test-gap-analysis`;
- secrets committed to history, hardcoded credentials, exposed admin surfaces;
- personal data handling and retention — route to `data-core`;
- dependency advisories and abandoned packages;
- undocumented integrations, manual steps, and knowledge that exists only in the previous developer's head.

**Report before agreeing.** Separate what must be fixed before support can be responsibly offered, what should be fixed soon, and what can be lived with. Price the first group as project work, not as retainer work — inheriting someone else's technical debt inside a fixed monthly fee is how a support agreement becomes a loss. Route the commercial framing to `client-core`.

## Offboarding

Ending support is a deliverable, not a silence. Before the last day:

- transfer ownership of every account, domain, and service — ownership, not shared access;
- rotate every credential you held, via `secrets-core`, and confirm the client controls the new ones;
- confirm the repository, deploy configuration, and infrastructure definition are complete and current;
- hand over documentation via `docs-core`: architecture, runbooks, known issues, scheduled jobs, and the open items list with dates;
- state clearly what is now unmonitored, what has an upcoming expiry, and what the next maintenance action should be;
- remove your own access after the client confirms theirs works, and confirm the date support ends in writing.

Leave the system in a state where a competent stranger can operate it. That is what makes the referral, and it is the last piece of the delivery.

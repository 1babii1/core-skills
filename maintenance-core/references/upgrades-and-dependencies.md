# Upgrades, dependencies, and patching

Use for version bumps, framework majors, end-of-life runtimes, and security advisories on a system already in production.

## Upgrade on a cadence, not on an emergency

Systems that are never upgraded are not stable, they are accumulating a forced migration. Set a rhythm per project:

- **Weekly or per-support-cycle:** review security advisories for reachable dependencies.
- **Monthly:** patch and minor version updates, applied in a batch and shipped together.
- **Quarterly:** review runtime, framework, and platform support windows against their published EOL dates.
- **Planned:** framework and runtime majors, scoped and estimated as real work, never as a side effect of a bug fix.

Track EOL dates explicitly — .NET release cadence and support windows, Node LTS, Expo and React Native SDK support, Astro and Next.js majors, PostgreSQL and Redis versions, base container images, and the hosting platform's own runtime deprecations. Every one of these has a known date; being surprised by it is a planning failure.

## Establish the baseline before touching versions

Never start an upgrade without knowing what proves it worked:

1. Confirm the build, tests, linters, and type checks pass on the current versions. An upgrade onto a red baseline cannot be evaluated.
2. Run `test-gap-analysis` or `coverage-analysis` over the areas the upgrade touches. Where coverage is missing on a critical path, add the test before upgrading — that test is the upgrade's safety net, not follow-up work.
3. Record current behavior worth preserving: key page renders, critical journeys, bundle size, cold start, response latency.
4. Confirm the rollback path with `delivery-core`: the previous artifact still deployable, and the lockfile change revertible in one commit.

## Sequence changes so a failure is attributable

- One kind of change per step. Never combine a framework major, a dependency batch, and a refactor.
- Patch and minor updates first, shipped and verified, before any major.
- Majors one at a time, each with its own migration guide read in full before starting — official upgrade docs and release notes, not a summary.
- Never mix an upgrade with a feature or a bug fix in the same commit or the same deploy. When something breaks in production, the diff must answer why.
- Keep the lockfile change in the commit. An upgrade without a committed lockfile is not reproducible.

## Read the change, not just the version number

- Check the release notes for breaking changes, removed APIs, and changed defaults. A changed default is the one that bites, because nothing in the code mentions it.
- Look for behavior that moved rather than disappeared: stricter validation, different date or number handling, changed error shapes, altered SSR or hydration behavior, new peer requirements.
- Verify transitive dependencies did not shift under the direct one. The advisory you were fixing may live three levels down.
- For runtime majors, check platform support first: does the host, base image, and CI runner support the target version at all?

## Security advisories

- Assess reachability before urgency. A critical CVE in a package path the application never executes is not the same as a moderate one in the request pipeline — but say which one it is with evidence, not assumption.
- Prefer the minimum version bump that resolves it. A security patch is not an invitation to a major upgrade.
- When no fix exists, document the exposure, the mitigation applied, and the condition for revisiting. An unresolved advisory needs an owner and a date.
- Rotate any credential that a vulnerability could plausibly have exposed, through `secrets-core`. Rotation is cheap; assuming it was not exploited is not.
- Never fix an advisory by suppressing the warning.

## Verify like a release, because it is one

- Full build, tests, linters, and type checks green on the new versions.
- Critical journeys exercised in a real environment, not only in tests.
- Compare against the baseline recorded earlier — bundle size, startup, latency, and rendered output.
- Watch error rates and logs after deploy for a defined window before calling it done. Upgrade regressions often appear on a code path that runs hourly, not on the smoke test.
- If anything is unverifiable — a payment provider, a push service, a device-specific path — name it explicitly rather than implying it was checked.

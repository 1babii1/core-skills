# Risk and test strategy

Use this reference to turn a feature list into a proportionate quality plan.

## Risk inventory

For each feature or journey, record:

| Field | Question |
|---|---|
| Outcome | What must the user or business be able to complete? |
| Impact | What happens if it fails: money, data, access, trust, availability? |
| Likelihood | How likely is failure given complexity and change size? |
| Detectability | Would monitoring or users notice quickly? |
| Exposure | How many users, tenants, roles, browsers, or integrations are affected? |
| Recovery | Can the change be rolled back or repaired safely? |
| Evidence | Which test or review directly proves the requirement? |

Prioritize high-impact, high-likelihood, low-detectability, hard-to-recover risks.

## Coverage rules

- Map every release-scoped critical requirement to direct evidence.
- Accept indirect coverage only with written rationale.
- Test business permutations at unit/component level; keep E2E to representative critical paths.
- Test integration boundaries with real dependencies when mocks could conceal protocol, transaction, query, serialization, or configuration errors.
- Test failures as first-class behavior: timeout, retry, cancellation, duplicate delivery, partial failure, unavailable dependency, invalid input, unauthorized access.
- Derive the browser/device matrix from the product support policy or analytics. When neither exists, start with Chromium, Firefox, WebKit, and representative desktop/mobile viewports.

## Useful quality signals

Prefer:

- escaped defects by severity;
- critical requirement coverage;
- test failure classification and time to diagnosis;
- suite duration and flake rate;
- contract breaking changes;
- latency/error/throughput thresholds;
- accessibility violations and manual findings;
- UAT status and unresolved waivers.

Do not use coverage percentage alone as a quality verdict.

## Waivers

A waiver must include:

- affected requirement and risk;
- why direct evidence is unavailable;
- compensating control;
- accountable owner;
- expiry date;
- decision maker.

Expired waivers block the relevant gate.

## Exit criteria

Return:

- `PASS`: all required gates and critical evidence pass.
- `CONDITIONAL`: non-critical gaps have explicit, unexpired waivers.
- `BLOCKED`: a required gate or critical requirement fails.
- `INCONCLUSIVE`: environment, target, or evidence cannot support a verdict.

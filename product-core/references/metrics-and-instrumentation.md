# Metrics and Instrumentation

## Metric chain

Start with:

1. decision the metric informs;
2. user value moment;
3. outcome metric;
4. leading/input metrics;
5. guardrails/counter-metrics;
6. operational diagnostics.

For every metric define name, meaning, formula, numerator/denominator, population, segment, window, source, refresh cadence, owner, baseline, target or decision threshold, and known quality limits.

Do not invent a baseline or target. If absent, define a collection period or benchmark research task. A target needs a rationale: economics, prior behavior, external benchmark with context, capacity, or desired decision sensitivity.

## Event contract

For every event define:

- stable name and version;
- semantic trigger (attempt, success, or failure);
- actor/account/entity identifiers;
- properties with types and allowed values;
- source and timestamp semantics;
- consent, retention, and PII classification;
- deduplication/idempotency behavior;
- validation and QA method;
- owner and change policy.

Never send secrets, credentials, message bodies, full URLs with sensitive query parameters, or unnecessary personal data into analytics.

## Interpretation

Segment before concluding. Check denominator changes, missingness, instrumentation releases, seasonality, acquisition mix, survivorship, novelty, and multiple comparisons. Correlation proposes a hypothesis; it does not establish causation.

# Performance and observability

Read this reference for performance work, production readiness, or client telemetry.

## Measure before changing

Use a production build and representative route/journey. Inspect:

- initial and route-level JavaScript;
- server/client waterfalls;
- hydration and Client Component/island scope;
- serialized payloads;
- images, fonts, CSS, and third-party scripts;
- long tasks, rendering, large lists, and layout shifts;
- Zustand/TanStack subscriptions and avoidable rerenders;
- Core Web Vitals under realistic network/device conditions.

Do not claim improvement from code shape alone. Compare the same scenario before and after.

Define project budgets where they protect a real user or business goal. Avoid universal bundle thresholds detached from the product.

## Practical priorities

1. Remove unnecessary client JavaScript and sequential waits.
2. Fix oversized media/fonts and blocking third parties.
3. Split genuinely heavy, non-critical functionality.
4. Reduce broad subscriptions and expensive rendering.
5. Optimize micro-level JavaScript only after profiling.

## Observability

Capture unexpected errors, failed dependencies, meaningful route/navigation timing, and Web Vitals with:

- release/build identity;
- environment;
- route/template rather than sensitive full URLs;
- correlation/request ID shared with the .NET backend;
- sanitized breadcrumbs;
- useful tags for feature/domain ownership.

Never record tokens, credentials, form secrets, unnecessary personal data, complete request bodies, or sensitive query parameters.

Upload source maps through `delivery-core` without making them publicly discoverable when the provider supports private upload. Verify that reported stack traces resolve to the deployed release.

Use Sentry skills only when Sentry is already selected or explicitly requested. A provider-independent telemetry design comes first.

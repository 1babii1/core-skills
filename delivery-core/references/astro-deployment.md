# Astro deployment adapter

Use for Astro sites and applications. Prefer the simplest output that preserves required behavior.

## Select output

- Prefer the default static build for content and marketing sites that do not need request-time server behavior.
- For static output, build with the repository's locked package manager and publish the configured output directory, normally `dist`.
- Use on-demand rendering only for routes that actually require request-time logic.
- Select an official Astro adapter for the current target when available and verify its current feature support.
- For a generic VPS/container SSR path, use the official Node adapter in standalone mode unless repository constraints require middleware mode.

Do not add an SSR runtime merely for forms or data that can be handled safely by an existing backend/API or build-time generation.

## Static delivery

- Serve fingerprinted assets with long immutable caching.
- Give HTML an update-safe cache policy.
- Configure SPA fallback only when the application is actually an SPA and route behavior requires it.
- Verify the configured base path, trailing-slash policy, sitemap/canonical URLs, redirects, custom 404, and asset URLs behind the final domain/CDN.

## SSR delivery

- Build and run the adapter output using its documented entry point.
- Bind to the platform host/port and run as non-root in a minimal container.
- Handle termination and verify request draining.
- Keep server-only configuration out of client bundles; treat public-prefixed client variables as public.
- Verify cookies, sessions, proxy headers, actions/endpoints, server islands, streaming, and image behavior used by the project.

## Verification

- Run locked install, Astro checks/type checks, tests, and production build.
- Inspect build warnings and confirm the expected static/server route classification.
- Start or serve the production output locally or in preview.
- Crawl representative routes and run the critical Playwright journey.
- Verify status codes, redirects, canonical URLs, generated assets, hydration, console errors, and runtime logs.

Primary references:

- https://docs.astro.build/en/guides/deploy/
- https://docs.astro.build/en/guides/on-demand-rendering/
- https://docs.astro.build/en/guides/integrations-guide/node/

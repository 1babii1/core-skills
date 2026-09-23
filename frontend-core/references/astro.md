# Astro

Read this reference for Astro projects.

## Current rendering model

- Use static prerendering by default.
- Since Astro 5, `output: "hybrid"` no longer exists. Default static output can opt individual routes out with `export const prerender = false` when an adapter is installed.
- Use `output: "server"` only when most routes genuinely need on-demand rendering.
- Use `server:defer` for isolated personalized or dynamic server islands when it fits the UX.
- Verify behavior against the installed Astro version and current official documentation.

## Islands

Render Astro/HTML with zero client JavaScript by default. Add a React island only for actual browser interaction, state, effects, or a React-only library.

Choose hydration deliberately:

- no directive: static HTML;
- `client:load`: immediate interaction;
- `client:idle`: non-critical interaction after initial work;
- `client:visible`: below-the-fold interaction;
- `client:media`: interaction for a matching viewport/capability;
- `client:only`: last resort when SSR is impossible.

Do not hydrate an entire header, footer, or content section for one toggle. Prefer a small island or simple scoped script.

## Data and forms

- Fetch build-time/static data in Astro frontmatter or content loaders.
- Use on-demand routes, Actions, or endpoints for request-time mutations and privileged work.
- Use native HTML forms for simple submissions.
- Add RHF/TanStack Query only inside justified React islands.
- Validate untrusted input server-side. Use Zod/client validation as an additional UX layer.
- Use Nano Stores when state must cross framework-independent islands; Zustand is suitable only where React ownership is clear.

## Content and assets

- Use the current Content Layer API and define schemas.
- Use Astro image components and imported assets for optimization.
- Prefer scoped CSS for small unique sites. Use Tailwind only when its design-system and reuse benefits are real.
- Keep metadata and canonical behavior aligned with `seo-core`.

## Verification

Run the repository's check, test, and build commands. Verify that static pages remain static, only intended islands hydrate, adapter-dependent routes work in the target runtime, and no browser bundle receives server-only code.

## Primary sources

- Astro documentation: https://docs.astro.build/
- Islands: https://docs.astro.build/en/concepts/islands/
- On-demand rendering: https://docs.astro.build/en/guides/on-demand-rendering/
- Server islands: https://docs.astro.build/en/guides/server-islands/

# Internationalization and dependency policy

Read this reference for locale-sensitive work, dependency selection, or new project setup.

## Internationalization

- Use `Intl` or a chosen i18n library for dates, times, numbers, currency, relative time, and plural rules.
- Make time zone and locale explicit at system boundaries.
- Do not assemble translatable sentences by concatenating fragments.
- Design layouts for text expansion and user font scaling.
- Keep locale routing, canonical URLs, and alternates aligned with `seo-core`.
- Add RTL support when required and use logical CSS properties where practical.
- Keep stable translation keys and detect missing messages.
- Do not install a full translation framework for a single-language prototype unless near-term requirements justify it.

## Dependency policy

Before adding a package:

1. verify the framework/platform does not already solve the problem;
2. inspect installed dependencies and repository conventions;
3. identify the concrete problem and expected maintenance benefit;
4. verify current support, compatibility, bundle/runtime impact, license, and security posture;
5. avoid two libraries with overlapping ownership;
6. pin through the repository's package manager and lockfile;
7. add tests around the integration boundary.

Do not combine unrelated major upgrades with feature work. Detect versions before applying a specialist skill. Never copy exact package versions from a skill without verifying current repository and primary documentation.

## Default choices

- Astro for simple content-first sites; Next.js for application-heavy products.
- TypeScript strict for new projects.
- Native/local state first, URL for shareable state, TanStack Query for server state, Zustand for justified shared client state.
- Native forms first, RHF for complex forms, Zod at useful runtime boundaries.
- Scoped CSS/CSS Modules for small unique projects; Tailwind when systematic component styling and tokens justify it.

Defaults guide decisions; they do not override a sound existing project.

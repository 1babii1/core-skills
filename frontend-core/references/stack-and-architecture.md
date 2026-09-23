# Stack and architecture

Read this reference for stack selection, new project structure, module-boundary changes, or architecture audits.

## Framework decision

Choose Astro when the product is primarily content, marketing, documentation, editorial, portfolio, or SEO pages with isolated interaction. Choose Next.js App Router when most value comes from authenticated workflows, application state, mutations, dashboards, personalized rendering, or complex full-stack behavior.

Do not migrate a suitable existing framework without an explicit request and measured benefit.

## Growth path

### Small: route colocation

Keep code used by one route next to that route.

```text
src/
├── app-or-pages/
│   └── route/
│       ├── _ui/
│       ├── _lib/
│       └── page
└── shared/
    ├── api/
    ├── ui/
    ├── lib/
    └── config/
```

Do not create empty architectural layers.

### Medium: feature-first / FSD-inspired

```text
src/
├── app/
├── features/
│   ├── checkout/
│   └── product-search/
├── entities/
│   ├── order/
│   └── product/
└── shared/
```

Use only useful segments such as `ui`, `model`, `api`, `lib`, and `config`. A feature represents a meaningful user capability, not every button or component.

For Next.js App Router, avoid a top-level `src/pages` FSD layer because Next.js may treat it as Pages Router. Let `src/app` own routes and use feature/domain modules outside it.

### Large: domain modules / bounded contexts

```text
src/
├── app/
├── domains/
│   ├── identity/
│   ├── catalog/
│   ├── orders/
│   └── billing/
└── shared/
```

Each domain owns its UI, model, API adapters, features, and public entry point. Introduce this only when the product has real independent business language/rules, team ownership, or change boundaries.

Use a monorepo only for multiple deployables, independently versioned packages, or team ownership that benefits from package boundaries.

## Boundary rules

- Depend inward/downward through documented public APIs.
- Keep route entry files thin: composition, framework integration, metadata, and boundaries.
- Keep generated API code isolated and replaceable.
- Do not import another feature's internals. Compose at the app/route/domain layer or promote a truly shared concept.
- Avoid cyclic dependencies and cross-domain stores.
- Keep `shared` free of business orchestration.
- Prefer colocated tests and styles.
- Extract only after a stable responsibility is visible; do not guess future reuse.

Use `feature-arch` for a formal blueprint or migration audit. Its document-generation workflow is not required for routine implementation.

## Architecture decision record

For a new or materially restructured project, record compactly:

- framework and why;
- rendering model;
- directory model and import direction;
- state owners;
- API generation approach;
- styling and form defaults;
- testing layers;
- browser/deployment constraints;
- known upgrade triggers.

Do not generate ceremony when a short repository instruction is enough.

## Primary sources

- Next.js project organization: https://nextjs.org/docs/app/getting-started/project-structure
- Astro project structure: https://docs.astro.build/en/basics/project-structure/
- Feature-Sliced Design overview: https://feature-sliced.design/docs/get-started/overview

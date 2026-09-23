---
name: seo-core
description: Orchestrate end-to-end, free-first website SEO auditing, indexation preparation, implementation, trend research, performance improvement, and regression monitoring. Use when asked to audit or improve an entire site, prepare it for search indexing, raise organic visibility, investigate ranking or traffic loss, research search trends and content opportunities, coordinate multiple installed SEO skills, or run a complete SEO workflow from baseline through verified fixes.
---

# SEO Core

Own the complete SEO outcome. Assemble a sequential "train" from the installed specialist skills, skip cars that do not apply, consolidate their evidence, implement authorized fixes, and verify the result.

Do not invoke the general `seo` orchestrator from this skill; route directly to the specialist skills below to avoid duplicate orchestration. Do not require paid APIs or subscriptions.

## Establish the operating mode

Infer the narrowest mode that satisfies the request:

- **Audit:** inspect, measure, diagnose, and report. Do not modify files or external systems.
- **Improve / prepare for indexing:** audit, implement scoped repository changes, and verify them.
- **Trend and growth research:** research current search behavior, intent, competitors, and content opportunities; connect findings to concrete pages and measurements.
- **Monitor:** capture a baseline, detect SEO-critical drift, and recommend or apply authorized corrections.
- **Focused:** run only the relevant cars for a single page or issue.

Treat requests such as “fix,” “optimize,” “prepare,” or “make the site index-ready” as authorization for scoped repository changes. Do not interpret them as permission to submit URLs, change DNS, edit advertising accounts, publish content, or alter Search Console and other external dashboards.

Before starting, identify the site root, framework, route sources, build commands, deployment shape, public base URL if available, locales, business model, and conversion goals. Prefer repository evidence over guesses. If the live URL is unavailable, continue with code and local rendering and state the limitation.

## Apply non-negotiable rules

- Use free and local methods first: repository inspection, local build and tests, browser automation, Chrome DevTools, Lighthouse, public search results, official documentation, and user-provided exports.
- Browse current primary sources when search-engine guidance, Schema.org vocabulary, tooling behavior, or trends may have changed. Prefer Google Search Central, web.dev/Chrome, Bing Webmaster, and Schema.org.
- Never invent keyword volume, ranking difficulty, backlinks, traffic, Core Web Vitals field data, or Search Console data. Label evidence as **confirmed**, **likely**, or **unknown**.
- Keep lab data such as Lighthouse separate from field data such as CrUX or Search Console. Never present one as the other.
- Never promise indexing, rankings, traffic, rich results, or AI citations. Explain what is controllable and what remains search-engine dependent.
- Never read or search `.env`, `.env.*`, encrypted vaults, credential files, keychains, tokens, or secret values. Treat `.env.example` as the only readable environment-variable contract. Never ask the user to paste a secret. Use `~/.local/bin/secrets-run <vault> -- <command>` only for the narrow application process that requires it.
- Preserve unrelated user changes. Make small, reviewable edits and avoid unrelated refactors.
- Treat `llms.txt`, Markdown mirrors, and mdream output as optional machine-readable distribution aids, not Google ranking factors or substitutes for canonical HTML.

## Build the train

Read and apply each selected skill's `SKILL.md`. Run cars sequentially when a later result depends on an earlier one. Combine independent findings into one report instead of returning separate reports.

| Car | Apply these skills | When to include |
| --- | --- | --- |
| Baseline | `seo-audit`, `seo-drift` | Full audit, improvement, migration, or monitoring |
| Crawl and indexation | `seo-technical`, `seo-sitemap` | Always for a full site or index-readiness request |
| Page signals | `seo-page`, `seo-schema` | Always for representative templates and priority pages |
| Experience and engineering | `web-quality-audit`, `performance`, `core-web-vitals`, `accessibility`, `best-practices` | Full audit or implementation work |
| Information and content | `site-architecture`, `seo-content`, `content-strategy`, `copy-editing`, `seo-sxo` | Growth, content, intent, navigation, or conversion work |
| Media | `seo-images` | Image-bearing pages or performance issues |
| International | `seo-hreflang` | Multiple languages or regional URLs only |
| Local | `seo-local` | Location-based businesses only |
| Commerce | `seo-ecommerce` | Product, category, marketplace, or shopping sites only |
| AI search visibility | `seo-geo` | AI Overviews, answer engines, entity clarity, or citation readiness |
| Growth and measurement | `competitors`, `free-tools`, `cro`, `analytics` | Trend research, opportunity planning, conversions, or monitoring |
| Implementation support | `frontend-ui-engineering`, `design-core` | Use only when fixes require frontend work or material UI changes |

For a single-page request, start with `seo-page` and add only the affected specialists. For an index-readiness request, always include technical, sitemap, page, schema, rendering, and verification work. For a trends-only request, emphasize current web research, `content-strategy`, `seo-sxo`, `competitors`, and measurement; do not manufacture demand data.

## Run the workflow

### 1. Capture the baseline

Inspect source-controlled routes, templates, content sources, build configuration, and documented commands. Build or run the site using its documented workflow. Render representative pages on mobile and desktop with a real browser when possible.

Select a representative route set that includes:

- the home page;
- each distinct page template;
- the most important conversion and organic landing pages;
- pagination, filters, search, parameterized routes, and error pages when present;
- each locale, product/category type, or location template when applicable.

Record current failures and measurable values before editing. Use `seo-drift` to capture a reusable baseline when the task includes implementation, migration, or ongoing monitoring.

### 2. Prove crawlability and indexability

Reconcile application routes, internal links, XML sitemaps, canonical URLs, robots directives, and HTTP responses. Check redirects, redirect chains, duplicate URL variants, soft 404s, orphaned pages, pagination, query parameters, JavaScript rendering, and mobile parity.

Verify that intended indexable pages:

- return the correct status;
- are not blocked by robots or `noindex`;
- use a consistent, absolute canonical URL;
- appear in the appropriate sitemap;
- are reachable through crawlable internal links;
- expose meaningful rendered HTML without relying on an unsupported client state.

Verify that private, duplicate, utility, search-result, staging, and error URLs are excluded appropriately. Do not equate presence in a sitemap with guaranteed indexing.

### 3. Validate page meaning

Check titles, descriptions, headings, visible main content, internal anchor text, canonical consistency, metadata uniqueness, social metadata, and structured data on representative templates. Validate JSON-LD syntax and eligibility against current official documentation. Ensure structured data describes visible content and does not make unsupported claims.

Map each important page to one primary intent. Detect cannibalization, thin pages, duplicate content, weak entity signals, missing trust evidence, and content that fails to answer the query directly.

### 4. Measure technical quality

Run the available browser and quality checks on mobile and desktop. Examine LCP, INP proxies or interaction traces, CLS, render-blocking resources, image delivery, fonts, caching, compression, JavaScript cost, console errors, accessibility, security, and compatibility.

Report exact observed conditions and test context. Treat Lighthouse as a diagnostic snapshot. If CrUX, Search Console, analytics, or Bing data is not available, say so plainly and provide the free measurement setup needed to close the gap.

### 5. Research demand and trends

Browse current search results and primary sources for target markets and locales. Compare query intent, result types, competitors, freshness, entities, People Also Ask themes, forums, and emerging terminology. Use Google Trends or user-provided Search Console/Bing exports when available.

Separate:

- observed facts with source and date;
- reasonable inferences from result patterns;
- hypotheses requiring first-party data.

Turn the research into a page-to-intent map, content gaps, refresh opportunities, internal-link recommendations, and a prioritized editorial plan. Use ranges or qualitative labels when exact demand data is unavailable.

### 6. Prioritize and implement

Order work by dependency and expected impact:

1. crawl, render, canonical, status, and accidental blocking failures;
2. sitemap, route, duplicate, and structured-data correctness;
3. severe performance, accessibility, and mobile problems;
4. priority-page relevance, internal links, and content quality;
5. scalable template improvements and strategic growth opportunities.

For every proposed change, state the evidence, affected routes, expected outcome, effort, risk, and verification method. In an authorized improvement mode, implement safe repository changes rather than stopping at recommendations. Keep uncertain or externally controlled actions in the action plan.

Add mdream-generated Markdown, `llms.txt`, or similar artifacts only when the tool is available and the user wants machine-readable content. Preserve canonical HTML, canonical URLs, and normal search-engine discoverability as the source of truth.

### 7. Verify the complete site

Run the relevant build, lint, type, and test commands. Re-render changed templates and repeat failed audit checks. Compare the result with the baseline using the same URLs, device assumptions, and measurement method. Use `seo-drift` comparison when a baseline was captured.

Do not mark a finding fixed solely because code changed. Require observable verification or label it pending deployment/field data.

## Deliver one decision-ready result

For a full audit, produce one consolidated report in the response. Create repository artifacts such as `SEO-REPORT.md` or `SEO-ACTION-PLAN.md` only when the user asks for files or the repository already uses such artifacts.

Include:

1. an executive summary and the highest-impact next action;
2. scope, URLs/templates sampled, tools, date, device assumptions, and limitations;
3. separate pillar results for indexability, on-page, content, structured data, performance/CWV, accessibility, architecture, and measurement;
4. findings with severity, evidence, affected scope, remedy, status, and verification;
5. before/after measurements for implemented changes;
6. a prioritized backlog split into now, next, and later;
7. unresolved dependencies and a monitoring cadence.

Avoid a single opaque “SEO score.” If scores are useful, show them by pillar and explain the evidence behind each score.

## Enforce the completion gate

Do not call the work complete until all applicable statements are true:

- indexation blockers are resolved or explicitly documented with owners;
- intended routes, canonicals, robots rules, statuses, internal links, and sitemaps agree;
- structured data is valid, eligible, and consistent with visible content;
- representative mobile and desktop pages have been rendered and checked;
- applicable build, lint, tests, and browser checks pass, or failures are reported;
- implemented fixes have before/after evidence or a clearly labeled pending verification;
- trend and competitor claims include current sources and dates;
- measurement gaps and monitoring steps are explicit;
- no paid dependency, fabricated metric, secret exposure, or ranking guarantee has been introduced.

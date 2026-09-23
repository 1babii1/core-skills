---
name: article-core
description: Orchestrate end-to-end writing of publish-ready, SEO-strong articles with original content, diagrams, and generated images. Use when asked to write a blog post, article, guide, or long-form content piece; to refresh or restructure an existing article; or to plan and produce a piece of content from a topic/keyword brief through a publish-ready Markdown file with images and metadata.
---

# Article Core

Own the complete outcome of a publish-ready article: an idea or keyword goes in, a Markdown file with original prose, diagrams, generated images, and correct SEO metadata comes out. Assemble a sequential "train" from the installed specialist skills below rather than reimplementing their logic — this skill's own job is drafting the prose, sequencing the train, and placing the final artifacts.

Do not use this skill to rewrite, spin, or lightly paraphrase another site's article. Competitive reading is for identifying gaps and intent, never for producing derivative text — see the non-negotiable rules.

## Establish the operating mode

Infer the narrowest mode that satisfies the request:

- **New article:** full pipeline from brief to publish-ready file.
- **Refresh / restructure:** existing article gets updated facts, structure, metadata, or media; preserve what still holds.
- **Draft only:** prose and structure, no images or metadata (user explicitly wants a fast draft).
- **Metadata / media only:** article text already exists; only SEO metadata, diagrams, or images are needed.

Before starting, identify: target keyword/topic, audience, intent (informational/transactional/comparison), desired length, the project's content pipeline (Markdown/MDX location, frontmatter schema, image directory, framework — check `CLAUDE.md` and existing articles for conventions), and any mandatory legal/disclaimer language the project requires. Prefer repository evidence over guesses; ask only what genuinely can't be inferred.

## Apply non-negotiable rules

- **Original prose only.** Competitor and reference articles are read to extract facts, structure gaps, and unanswered questions — never phrasing. Do not paraphrase, spin, or closely mirror sentence structure from any single source. If a claim comes from a specific source, say so; don't launder it as original research.
- Never fabricate statistics, quotes, studies, or citations. Label uncertain claims as such or omit them.
- Never invent SEO demand data (keyword volume, ranking difficulty, traffic) — see `seo-core`'s evidence-labeling rule (confirmed/likely/unknown).
- Follow the global secrets policy: never read `.env`, `.env.*`, vaults, or credentials; `.env.example` is the only readable env contract.
- Image generation happens through `codex exec` (see the Images car below) — the user's normal Bash tool-permission prompt on that command *is* the approval gate. Never bypass it (`--dangerously-bypass-approvals-and-sandbox` or equivalent) and never fabricate an image result.
- Preserve unrelated content and files; make small, reviewable additions.
- Carry forward the project's own legal/disclaimer requirements verbatim if `CLAUDE.md` or existing content specifies them (e.g. a compliance disclaimer) — do not paraphrase them either.

## Build the train

Read and apply each selected skill's `SKILL.md`. Skip cars that don't apply to the request.

| Car | Apply these skills | When to include |
| --- | --- | --- |
| Topic validation & gaps | `content-strategy`, `seo-sxo` | Always for a new article; skip for metadata-only mode |
| Draft | *(self — see Workflow §3)* | Always except metadata/media-only mode |
| Structure for long-form | `docs-core` | Articles with multiple sections, comparisons, or step-by-step guides |
| Diagrams | `dataviz` | Whenever a process, comparison, or numeric relationship is better shown than described |
| Images | `codex exec` (prompt prepared by this skill) | Whenever the brief or draft calls for illustrative/hero images |
| Content quality / E-E-A-T | `seo-content` | Always — readability, thin-content, Who/How/Why check |
| On-page & schema | `seo-page`, `seo-schema` | Always — meta tags, JSON-LD |
| Image SEO | `seo-images` | Whenever images are included |
| Editing pass | `copy-editing` | Always, after the draft is complete |
| Site placement | `site-architecture` | New article changes internal linking or nav |
| Sitemap / indexability | `seo-sitemap`, `seo-technical` | New route/page, not just a content edit |
| Accessibility & performance | `accessibility`, `core-web-vitals` | Always for images/diagrams; skip for text-only draft mode |
| Regression baseline | `seo-drift` | Publishing to a live/monitored site |
| Conversion | `cro` | Article ends in a lead-gen or product CTA |
| Analytics | `analytics` | New page needs tracking/event setup |

## Run the workflow

### 1. Intake and topic validation

Confirm keyword/topic, audience, and intent. Run `content-strategy` to check the topic against existing content (avoid cannibalization, find the content gap) and `seo-sxo` to determine what page type and structure the query actually rewards. Read 3–5 top-ranking pages for the topic **only** to extract: facts, structural gaps, unanswered questions, and the intent Google is rewarding. Do not retain their phrasing.

### 2. Outline

Produce a heading structure (H1 + H2/H3) that answers the query in the first 100–150 words and closes the gap identified in step 1. Use `docs-core` for multi-section or long-form pieces.

### 3. Draft

Write original prose to the outline. One idea per section, plain sentences, no AI-tell filler. Insert `[DIAGRAM: description]` or `[IMAGE: description]` placeholders inline where visuals will go, rather than blocking the draft on media.

### 4. Diagrams

For each `[DIAGRAM]` placeholder, apply `dataviz` to produce a theme-aware mermaid diagram (or chart) and inline it in place of the placeholder.

### 5. Images

For each `[IMAGE]` placeholder:
1. Write a complete generation prompt: subject, style (match the site's existing visual style if established), aspect ratio, and the exact output file path following the project's image directory convention.
2. Run `codex exec "<prompt>, save the result to <path>"` via Bash. The tool-permission prompt this triggers is the user's approval — do not add a separate confirmation step.
3. Once the file exists, replace the placeholder with the Markdown image reference and write descriptive alt text (apply `seo-images` for format/size/alt guidance).

### 6. SEO metadata

Apply `seo-schema` to generate/validate JSON-LD appropriate to the content type (Article, FAQPage, HowTo). Apply `seo-page` for title (≤60 chars), meta description (≤155 chars), canonical, and og-tags. Apply `seo-content` to check E-E-A-T signals and readability.

### 7. Edit

Apply `copy-editing` as a distinct pass over the finished draft — tighten, remove filler, verify voice consistency. Do not rewrite structure at this stage; that belongs in step 2.

### 8. Site integration (new pages only)

Apply `site-architecture` for internal linking placement, `seo-sitemap`/`seo-technical` if the route is new, `analytics` if event tracking is required, `cro` if the article ends in a conversion action.

### 9. Verify

Apply `accessibility` and `core-web-vitals` against the images/diagrams added. If publishing to a live/monitored site, use `seo-drift` to capture a baseline for regression tracking.

## Deliver the result

Produce the Markdown/MDX file with complete frontmatter (title, description, date, slug, tags, ogImage, and any project-required fields), inline diagrams, inline images with alt text, and JSON-LD if the pipeline doesn't generate it automatically. Report alongside it:

1. the content gap / intent this article targets and its source evidence;
2. which cars ran and which were skipped, and why;
3. any claim labeled uncertain rather than fabricated;
4. remaining manual steps (e.g. an image prompt awaiting approval, a disclaimer to confirm).

## Enforce the completion gate

Do not call the work complete until all applicable statements are true:

- no sentence is a close paraphrase of a single source; sourced claims are attributed;
- no fabricated statistic, quote, or SEO demand figure is present;
- H1 is unique, meta title/description are within length limits, JSON-LD validates;
- every image has real alt text and exists on disk at the referenced path;
- diagrams render and match both light and dark theme if the site supports it;
- accessibility and Core Web Vitals checks ran against the added media;
- project-specific legal/disclaimer text (if any) is present verbatim;
- the editing pass (step 7) ran after the draft was structurally final.

# Reference Analysis

Use this procedure when a user supplies a website, gallery, screenshot, video, or design collection.

## Capture

Inspect the live page rather than relying only on a thumbnail.

1. Record the page purpose, audience, primary action, and content density.
2. Capture the initial viewport at wide desktop and narrow mobile.
3. Inspect at least the hero, one content transition, one repeated component, navigation, and footer.
4. Exercise scroll, hover, menu, carousel, pointer reaction, and 3D controls when present.
5. Observe loading, reduced motion, resize, keyboard, and failure behavior when feasible.
6. Note visible overflow, blocked content, unreadable type, prolonged loaders, and intrusive overlays.

Do not infer the exact library from appearance. Inspect public scripts or runtime evidence, then label the result as confirmed or likely.

## Decompose

Fill this compact card:

```text
Source:
Page job:
Feeling:
Protagonist:
Composition:
Typography:
Color/light/material:
Image/3D:
Motion and interaction:
Mobile transformation:
Accessibility/performance behavior:
Reusable principle:
Do not copy:
Failure/tradeoff:
Confidence:
```

## Convert observation into a rule

Keep a finding only when it answers all three questions:

1. What user or brand outcome does it serve?
2. Under what conditions does it work?
3. What failure does its guardrail prevent?

Write the result as:

```text
Use [principle] when [conditions] because [outcome].
Preserve [guardrail]; avoid [failure].
```

Bad: “Use huge serif text like Lovably.”

Good: “For a low-density identity page, let one short brand statement occupy most of the viewport so the name becomes the image; keep navigation and supporting facts quiet, and replace the gesture on small screens rather than shrinking it into illegibility.”

## Synthesize multiple sources

- Group references by transferable principle, not by visual similarity alone.
- Count repeated patterns as evidence of a direction, not proof that every project needs it.
- Prefer complementary sources: one for composition, one for motion, one for material treatment, and one for mobile behavior.
- Select at most three principles for a single page direction.
- Explicitly reject incompatible references.
- Preserve source attribution in research notes, but do not ship source names as design rationale to end users.

## Originality boundary

Do not copy:

- logos, brand marks, mascots, proprietary illustrations, photos, 3D models, sound, video, or copy;
- a source's complete hero composition;
- a distinctive animation sequence frame for frame;
- a unique combination of typeface, palette, object, and layout that functions as brand identity.

Do reuse abstract knowledge:

- hierarchy;
- pacing;
- contrast relationships;
- interaction purpose;
- material and lighting principles;
- progressive enhancement and fallback strategies.

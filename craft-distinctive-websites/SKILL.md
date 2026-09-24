---
name: craft-distinctive-websites
description: "Art-direct and build distinctive public-facing websites: translate visual references into an original composition, typography, motion and 3D system - never a copy. Use for premium landing pages, brand/studio sites, portfolios, cultural or editorial experiences, real-estate/product presentations, and any request to make a site beautiful, memorable, cinematic, or inspired by supplied references without cloning them."
---

# Craft Distinctive Websites

Turn references into an original, coherent web experience. Coordinate `design-core`, `motion-core`, and `frontend-core`; do not replace their specialist ownership or merge their instructions into this skill.

## Non-negotiable direction

- Start from the product truth, audience, desired feeling, and primary action. Choose aesthetics only after these are explicit.
- Extract principles from references; never reproduce another site's identity, copy, proprietary assets, distinctive composition, or complete interaction sequence.
- Choose one dominant art-direction thesis and at most two supporting motifs. Do not assemble a trend collage.
- Make one element the visual protagonist: a product, material object, typographic statement, photograph, spatial scene, or data idea.
- Treat typography, negative space, image crop, material, light, and motion as one composition.
- Keep navigation, copy, forms, prices, states, and calls to action as semantic DOM.
- Break a grid only when the normal reading order remains understandable.
- Preserve the task without animation, WebGL, hover, precise pointer input, or a large viewport.
- Recompose for mobile. Never ship a desktop canvas merely scaled, clipped, or hidden behind overflow.
- Verify the running result; screenshots and source inspection alone cannot prove interaction quality.

## Build the train

Read every selected skill's `SKILL.md` before applying it.

| Responsibility | Owner | Route |
| --- | --- | --- |
| Product framing, hierarchy, visual system, assets, final visual critique | `design-core` | Always |
| Motion language, scroll choreography, Canvas, WebGL, 3D, performance and fallbacks | `motion-core` | Include for material motion or immersive work |
| Architecture, responsive implementation, states, security, tests and production readiness | `frontend-core` | Always when code is created or changed |
| Fine interaction feel and taste | `impeccable`, `emil-design-eng` | Include for major visual work |
| Accessibility and browser verification | `accessibility`, `playwright` | Always when the product is runnable |

Let one skill own each decision. This skill owns art-direction synthesis; the cores own implementation standards in their domains.

## Workflow

### 1. Frame the experience

Write a compact brief:

```text
audience -> job -> primary action -> desired feeling
brand truth -> central metaphor -> visual protagonist
content density -> interaction depth -> device constraints
```

Classify the page as conversion, catalogue, editorial, portfolio, cultural, product demonstration, or experiential promo. A conversion page must not inherit the friction of an art experiment.

### 2. Analyze references

For supplied URLs, apply [reference-analysis.md](references/reference-analysis.md). Inspect real desktop and mobile rendering when possible. Separate:

- observed behavior;
- likely implementation;
- reusable principle;
- brand-specific expression that must not be copied;
- failure or tradeoff worth avoiding.

Use [source-atlas.md](references/source-atlas.md) as precedent, not as a template library.

### 3. Choose an art-direction mode

Read [art-direction.md](references/art-direction.md). Select one dominant mode:

- quiet editorial or architectural;
- product/material luxury;
- bold typographic identity;
- tactile organic surrealism;
- technical/cyber system;
- immersive spatial or 3D;
- cinematic image-led presentation.

State why the mode fits the product. Combine modes only through a shared idea, such as “precision made tactile,” not because both look fashionable.

### 4. Define the signature

Create a one-page direction containing:

- one-sentence concept;
- protagonist and supporting motif;
- grid and deliberate exception;
- type roles and scale contrast;
- palette and material/light behavior;
- image or 3D treatment;
- motion hierarchy;
- one memorable interaction;
- mobile transformation;
- reduced-motion and lower-capability form;
- explicit exclusions.

Prefer a recognizable relationship over decoration: oversized type against micro-labels, hard grid against one organic object, dark void against one luminous material, or calm editorial space against a single reactive detail.

### 5. Choreograph motion before implementation

Read [motion-language.md](references/motion-language.md). Describe material effects as:

```text
purpose -> trigger -> initial -> transition -> settled
-> interruption/reversal -> reduced-motion -> failure state
```

Choose one owner per property and effect. Use CSS/WAAPI for simple deterministic DOM motion, Motion for state/layout/gesture behavior, GSAP for authored timelines and scroll choreography, PixiJS for GPU 2D, and Three.js for real 3D.

Do not introduce a heavy engine for grain, gradients, a cursor follower, or a basic reveal.

### 6. Implement as a resilient frontend

Read [frontend-quality.md](references/frontend-quality.md) and invoke `frontend-core`. Build content and task flow first, then the enhancement layer. Preserve meaningful first paint while optional scenes load.

Create explicit quality tiers when the design is expensive:

- full: intended scene and motion;
- reduced: simpler shader, texture, particle count, DPR, or timeline;
- static: composed image/DOM fallback with the same message and action.

### 7. Critique the integrated result

Ask:

- Would the page still be recognizable with the logo removed?
- Is the protagonist obvious within one glance?
- Does every effect support meaning, orientation, feedback, or atmosphere?
- Is the page paced, or is every section shouting?
- Does the design feel authored at mobile width rather than compressed?
- Are small labels readable and large type intentionally cropped?
- Does the call to action survive the art direction?
- Is any trend present without a product reason?

Remove effects before polishing weak effects.

### 8. Verify in the browser

Check representative wide desktop, laptop, narrow mobile, and at least one intermediate width. Exercise navigation, pointer, touch-equivalent controls, keyboard, reduced motion, repeated input, resize, slow loading, scene failure, and route changes as applicable.

Inspect:

- clipping and horizontal overflow;
- fixed headers, cookie panels, chat widgets, and safe areas;
- font loading and layout shift;
- pointer-only affordances;
- loading screens that can stall;
- long animation frames and heavy initial downloads;
- cleanup of timelines, observers, loops, and GPU resources;
- semantic content availability before enhancement.

Use `playwright` for the actual checks rather than reasoning from source: capture the page at
representative widths (e.g. 1440/1024/390px) via screenshot, drive keyboard/reduced-motion/resize,
and read console/network output - a static read of the code cannot prove interaction or layout
quality.

Concrete thresholds worth checking (Lighthouse or equivalent, mobile throttled):
- LCP under ~2.5s, CLS under ~0.1 - a heavier art-directed hero still needs a fast first paint of
  real content;
- total initial JS for the enhancement layer proportionate to what it buys (no fixed number - name
  what would be too much for this page's job and say why);
- 60fps target during the signature interaction; a dropped-frame report or `performance.now()`
  timing around the interaction, not a visual impression, decides whether motion is too heavy.

## Completion gate

Do not call the work complete until:

- the result has one clear concept rather than a list of trends;
- reference influence is traceable as principles but the expression is original;
- desktop and mobile have intentional compositions;
- typography remains readable at content sizes;
- material motion has purpose, interruption, reduced-motion behavior, and one owner;
- optional graphics cannot block content or the primary action;
- relevant frontend, accessibility, performance, and browser checks pass or exact limits are reported.

Report the art-direction thesis, signature decisions, motion/3D owner, mobile and fallback behavior, checks performed, and remaining assumptions.

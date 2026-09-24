# Frontend Quality for Expressive Sites

## Layer the implementation

Build in this order:

1. semantic content, links, forms, and route structure;
2. responsive layout and all meaningful states;
3. images, fonts, and art-directed crops;
4. interaction feedback;
5. narrative motion;
6. optional Canvas, WebGL, or 3D.

Each layer must preserve the task when the next layer is unavailable.

## Recompose responsively

- Define the hierarchy separately for wide, medium, and narrow widths.
- Reorder or restage the protagonist when crop or overlap loses meaning.
- Turn side-by-side editorial layouts into intentional sequences.
- Recalculate display-type line breaks; do not rely on accidental clipping.
- Replace hover-only reveals with visible or tap-controlled states.
- Protect safe areas, browser UI, virtual keyboards, and fixed controls.
- Test actual content and translations rather than placeholder lengths.

Never use global `overflow-x: hidden` as the first fix. Identify the element that escapes and decide whether it should wrap, crop locally, scroll intentionally, or change composition.

## Load expensive experiences

- Render a meaningful poster and core copy in the first response.
- Lazy-load below-fold or optional engines and scene assets.
- Reserve aspect ratio and object bounds to prevent layout shift.
- Expose progress only when waiting is material and calculate it from real work.
- Give loaders a timeout and failure path.
- Respect reduced motion, reduced data, and explicit low-power preferences.
- Avoid preloading media that the user may never reach.

## Media and typography

- Size responsive images to rendered dimensions and modern formats.
- Preserve focal points with art direction, not indiscriminate center crop.
- Subset fonts and load only used weights/styles.
- Keep fallback metrics compatible to reduce text movement.
- Use decorative faces for display roles and robust faces for reading/interface roles.
- Verify Cyrillic, Latin, numerals, punctuation, and case combinations required by the product.

## DOM and render boundaries

- Keep content and controls in DOM; isolate GPU rendering in a leaf component.
- Avoid application rerenders on every pointer or animation frame.
- Share authoritative state between DOM and scene without duplicating business logic.
- Clean up RAF loops, observers, timelines, contexts, textures, geometry, workers, and event listeners.
- Prevent duplicate initialization under strict development modes and route transitions.

## Quality evidence

Check:

- no horizontal overflow at representative and in-between widths;
- no long-lived blank screen or loader;
- primary content appears without enhancement;
- keyboard focus is visible and follows reading order;
- touch targets and fixed overlays do not collide;
- reduced-motion flow completes the same task;
- fonts and hero media do not cause material layout shift;
- expensive code is separated from the initial route where practical;
- console and network failures have useful fallback behavior;
- animation performance is observed during interaction.

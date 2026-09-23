# DOM motion engineering

Use for CSS, WAAPI, Motion, and GSAP DOM animation.

## State and ownership

- Define named visual states and transitions between them.
- Derive animation from application state; do not create a second hidden state machine in timers.
- Let one engine own each animated property. Avoid CSS transitions fighting JS writes.
- Preserve current velocity for reversible/interruptible gestures when the engine supports it.
- Cancel or retarget stale animation when input changes rapidly.

## Rendering cost

- Prefer transforms and opacity for frequent motion, but verify compositing rather than assuming it.
- Use filter, backdrop-filter, clip-path, masks, shadows, blur, and blend modes deliberately; they may incur expensive paint/offscreen surfaces.
- Avoid animating layout properties across large trees. When layout animation is required, contain scope and measure.
- Add `will-change` shortly before motion and remove it afterward; do not promote every element permanently.
- Keep stagger short and never delay availability or interaction until a sequence finishes.

## Scroll work

- Map explicit trigger, start/end, pinning, scrub, snapping, and mobile behavior.
- Use component-scoped GSAP contexts/hooks and destroy every ScrollTrigger/timeline.
- Refresh measurements after fonts/assets/layout stabilize when necessary.
- Use responsive match/media logic; do not reuse desktop pinning blindly on touch/mobile.
- Preserve native focus navigation, anchors, back/forward restoration, and readable content.

## Page transitions

- Coordinate exit/entry with routing and data loading without leaving the application inert.
- Keep navigation cancellable and handle rapid route changes.
- Avoid masking real latency with long transitions.
- Ensure errors and reduced motion cannot leave an overlay blocking the page.

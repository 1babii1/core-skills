# Motion Language

## Establish hierarchy

Assign each effect one tier:

1. **Structural:** page transition, section change, navigation state.
2. **Narrative:** product transformation, camera movement, scroll chapter.
3. **Feedback:** hover, press, focus, drag, selection, validation.
4. **Atmosphere:** light drift, grain, subtle particles, idle material movement.

Structural and feedback motion must remain clear. Use narrative motion sparingly. Atmosphere stops first on constrained devices.

## Timing character

- Make frequent controls immediate or short.
- Let entrances finish quickly enough that content can be read without waiting.
- Use longer motion only for infrequent narrative scenes with visible progress or direct manipulation.
- Prefer easing that matches material: crisp for system UI, damped for objects, continuous for camera travel, and subtle for ambient light.
- Make every animation interruptible. New input must take control instead of queuing a long sequence.

## Scroll

- Preserve native scrolling unless a story requires pinning or scrubbing.
- Use scroll to reveal relationship or transformation, not to animate every block.
- Keep text readable while its associated scene changes.
- Limit pinned sections and provide a natural exit.
- Restore scroll correctly across routes and history.

## Pointer and hover

- Treat pointer response as enrichment, never the only affordance.
- Limit magnetic buttons, cursor followers, parallax, and tilt to large-pointer devices.
- Do not replace the system cursor when precision or accessibility suffers.
- Provide touch behavior with equivalent meaning, not simulated hover.

## 3D and material

- Begin with a product or narrative reason: inspect, configure, compare, explain, or inhabit.
- Constrain orbit, zoom, and camera bounds so interaction feels authored.
- Match geometry, texture, environment, and light to the brand metaphor.
- Keep state in application data; render the same selection and result in DOM.
- Show a poster before initialization and keep it if WebGL fails.
- Load models, HDR environments, and large textures only when the scene is likely to be used.
- Reduce DPR, texture resolution, postprocessing, shadows, particles, and animation complexity adaptively.

## Reduced motion

Design a parallel composition:

- replace scrubbed travel with discrete sections;
- replace camera flight with cuts or a static angle;
- replace parallax with stable layering;
- replace continuous object motion with direct state changes;
- keep progress, meaning, and action identical.

Do not solve reduced motion with a global zero-duration override that causes invisible initial states or broken timelines.

## Motion critique

Remove or redesign an effect when:

- it competes with the protagonist;
- it delays comprehension or action;
- several elements move with equal emphasis;
- it creates layout shift or text blur;
- it repeats on every section without new meaning;
- it is unusable by keyboard or touch;
- it cannot degrade gracefully;
- its cost is greater than its product value.

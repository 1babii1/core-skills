---
name: motion-core
description: Orchestrate advanced web motion, interaction choreography, scroll storytelling, Canvas 2D, PixiJS, WebGL, WebGPU, Three.js, shaders, particles, page transitions, gestures, and animation performance from concept through browser verification. Use when creating, improving, debugging, or auditing complex interface animation, interactive graphics, cinematic landing pages, data-driven motion, 2D/3D scenes, animated backgrounds, or GPU-rendered web experiences.
---

# Motion Core

Own advanced motion from purpose to verified runtime behavior. Select the smallest suitable engine, coordinate installed specialists, preserve semantic UI, and validate the result in a real browser. Do not require the user to invoke cars manually.

## Principles

- Give every animation a communication, feedback, continuity, orientation, demonstration, or atmosphere purpose. Remove motion whose only justification is “looks impressive.”
- Keep text, navigation, forms, controls, primary content, and accessibility semantics in the DOM. Use Canvas/WebGL for graphics and effects, not as a replacement for the product interface.
- Preserve the project's established motion language and dependencies unless a different engine solves a demonstrated limitation.
- Prefer CSS/WAAPI for predetermined DOM motion, Motion for state/layout/gesture motion, GSAP for complex timelines and scroll choreography, PixiJS for GPU-accelerated 2D, and Three.js for genuine 3D.
- Do not mix multiple animation engines inside one component or let two engines own the same transform/style property.
- Do not hand-generate SVG markup or large Lottie/Bodymovin JSON. Reuse supplied licensed assets unchanged, use a consistent icon library, or create appropriate raster/Canvas/3D assets.
- Treat `prefers-reduced-motion`, keyboard/touch behavior, seizure risk, performance, cleanup, and content availability as required behavior.
- Do not claim smoothness from source inspection or screenshots; verify the running animation.

## Establish mode and constraints

Infer the narrowest mode:

- **Design:** define motion purpose, states, choreography, engine, fallbacks, and budgets.
- **Implement:** make scoped production code changes and add verification.
- **Audit:** inspect and measure without modifying files.
- **Improve/fix:** reproduce jank or behavioral defects, change code, and compare.
- **Immersive:** create Canvas/WebGL/WebGPU/3D experiences with explicit loading and fallback behavior.

Before work, identify framework/runtime, installed animation/rendering packages and versions, target devices, input methods, browser support, accessibility requirements, scene/asset sources, content semantics, and performance budget. Read [engine-selection.md](references/engine-selection.md) before introducing a new engine.

## Build the train

Read each selected skill's `SKILL.md` before applying it.

| Need | Skill(s) | Route |
| --- | --- | --- |
| Reference-driven expressive website | `craft-distinctive-websites` | Establish the art-direction thesis and motion hierarchy before selecting effects |
| Motion taste and interaction feel | `emil-design-eng`, `impeccable` | Always for material motion work |
| DOM/state/gesture motion | Existing Motion APIs plus [dom-motion.md](references/dom-motion.md) | State transitions, shared layout, drag, gestures, interruptible springs |
| Scroll choreography | `gsap-framer-scroll-animation` | Pinning, scrubbing, timelines, parallax, horizontal narrative, text choreography |
| GPU 2D/Canvas | `pixijs` and the matching `pixijs-*` specialists | Particles, sprites, filters, meshes, editors, large 2D scenes, procedural graphics |
| 3D/WebGL/WebGPU | Matching `threejs-*` specialists plus current official docs | Real 3D geometry, cameras, models, lighting, shaders, postprocessing, raycasting |
| Video walkthroughs | `remotion` | Rendered video output, not interactive runtime UI |
| Accessibility | `accessibility`, [accessibility.md](references/accessibility.md) | Always |
| Runtime performance | `performance`, `core-web-vitals`, relevant PixiJS/Three.js performance guidance | Always for Canvas/scroll/3D or broad audit |
| Browser verification | `playwright`, [verification.md](references/verification.md) | Always when runnable |

Three.js skills are conditional and may lag the installed Three.js version. Inspect `package.json`/lockfile and verify APIs against current official Three.js documentation before implementation. PixiJS skills target official v8 patterns; still match them to the installed project version.

## Workflow

### 1. Inspect and baseline

Inventory existing CSS keyframes/transitions, Motion/GSAP/PixiJS/Three.js usage, animation ownership, lifecycle cleanup, media queries, assets, rendering boundaries, and browser tests. Run the product and capture the current interaction, console state, layout behavior, responsiveness, and representative performance evidence before editing.

Describe the motion as states and transitions, not isolated effects:

```text
trigger -> initial state -> transition -> settled state -> interruption/reversal -> reduced-motion state
```

### 2. Define purpose and hierarchy

Specify what the motion communicates and which element leads. Establish duration/physics, sequencing, spatial direction, interruption behavior, and motion intensity. Keep frequent actions fast or instant; reserve cinematic sequences for infrequent storytelling surfaces.

Do not hide critical content until JavaScript/IntersectionObserver fires. The default rendered state must remain meaningful when animation code fails, the tab is backgrounded, reduced motion is enabled, or a crawler/screenshot loads the page.

For reference-driven brand or promotional work, apply the structural, narrative, feedback, and atmosphere tiers from `craft-distinctive-websites`. Keep one protagonist in motion and stop atmospheric work before degrading content or input response.

### 3. Select one owner per effect

Use [engine-selection.md](references/engine-selection.md). Choose native browser capabilities before adding a dependency. Lazy-load heavy engines/assets when the effect is below the fold or optional. Isolate Canvas/3D in a leaf boundary so rendering updates do not force the application tree to rerender.

For scroll motion, preserve native scrolling unless a concrete narrative requires pin/scrub behavior. Never hijack wheel/touch navigation globally, trap the user in a scene, or break history/restoration.

### 4. Implement lifecycle and fallbacks

Apply [dom-motion.md](references/dom-motion.md) for DOM work or [canvas-webgl.md](references/canvas-webgl.md) for PixiJS/Three.js. Keep interaction states reachable by keyboard and touch. Pause or reduce nonessential work when offscreen, hidden, backgrounded, or under reduced motion/data constraints.

Clean up timelines, ScrollTriggers, tickers, RAF loops, observers, listeners, textures, geometries, materials, render targets, workers, and contexts on unmount/reinitialization. Avoid duplicate initialization under React Strict Mode and route transitions.

### 5. Protect accessibility and content

Apply [accessibility.md](references/accessibility.md). Provide a reduced-motion experience designed for the same task, not merely a global `animation-duration: 0`. Keep focus, reading order, hit targets, announcements, and controls in semantic DOM. Provide pause/stop controls for persistent or auto-playing motion where required.

### 6. Meet explicit performance budgets

Measure rather than assume GPU acceleration. Inspect main-thread work, long animation frames, layout/paint, layer count, texture memory, draw calls, shader cost, resolution/DPR, asset decoding, bundle size, scene initialization, and interaction latency.

Optimize in this order:

1. remove unnecessary work/effects;
2. reduce scene/object/particle/texture complexity;
3. avoid layout-triggering DOM animation and excessive filters;
4. batch/instance/cull and pause offscreen work;
5. reduce DPR/postprocessing/shader quality adaptively;
6. micro-optimize only after profiling.

### 7. Verify in the running product

Apply [verification.md](references/verification.md). Exercise desktop, narrow mobile, pointer/touch, keyboard, reduced motion, fast repeated input, route navigation, background/foreground, resize/orientation, slow loading, and asset failure as applicable. Inspect console errors and resource cleanup.

Repeat after fixes. A visually attractive first frame is not completion.

## Completion gate

Do not call motion work complete until applicable statements are true:

- every material animation has a stated purpose and one engine owner;
- semantic content and controls remain in accessible DOM;
- reduced-motion and touch/keyboard behavior preserve the task;
- critical content is visible without animation initialization;
- timelines, loops, listeners, GPU resources, and observers clean up correctly;
- no unintended scroll trapping, layout shift, input delay, console error, or route duplication remains;
- Canvas/3D has loading, resize, failure, and lower-capability behavior;
- performance was observed under representative interaction, not inferred;
- the actual flow was replayed in a browser at representative desktop/mobile sizes.

## Completion response

Report the motion outcome, chosen engine and why, accessibility/performance behavior, runtime checks actually performed, and remaining device/browser assumptions. Do not list every internal skill invocation unless asked.

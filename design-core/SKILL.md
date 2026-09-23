---
name: design-core
description: Orchestrate end-to-end product interface design, implementation, visual asset creation, polish, and browser-based quality review. Use for new or existing websites, web apps, mobile apps, Telegram Mini Apps, dashboards, landing pages, UI components, redesigns, and any request to create or materially improve a user-facing interface across projects.
---

# Design Core

Own the interface from intent to verified result. Invoke the most relevant installed design skills and tools yourself; do not require the user to run them one by one.

## Operating principles

- Lead with the user's goal, audience, primary action, and constraints.
- Inspect the existing product, code, design system, and brand assets before proposing changes.
- Preserve established patterns unless the task explicitly calls for a redesign.
- Make reasonable, reversible assumptions. Ask only when a missing decision would materially change the product.
- Prefer a coherent direction over a collage of trends.
- Keep text, controls, navigation, and data as real accessible UI, never baked into generated images.
- Do not hand-generate SVG markup for icons, illustrations, logos, or decorative graphics.
- Do not claim completion without proportional verification.

## Route the work

Select only the stages needed for the request.

### 1. Frame

Define briefly:

- product and target user;
- job to be done and primary action;
- platform, viewport range, and technical constraints;
- required states: loading, empty, error, success, disabled, and edge cases;
- visual references or existing brand direction;
- whether any object must be seen in the round, rotated, or physically simulated. If yes, the interface needs a real rendering engine, and `motion-core` selects it now, during framing — not after the layout is already built in flat DOM. Retrofitting 3D into finished markup wastes the layout work.

For vague requests, create a concrete working brief and state the assumptions.

### 2. Establish visual direction

For a new interface or major redesign:

- Use `enhance-prompt` when preparing a generative design brief.
- Use `stitch::generate-design` or an available Stitch design workflow when editable screen concepts or variants would reduce uncertainty.
- Use `impeccable` to shape hierarchy, composition, typography, color, interaction, and overall taste.
- Use `craft-distinctive-websites` for reference-driven public websites, premium landing pages, portfolios, cultural/editorial experiences, product presentations, and requests for a memorable, cinematic, tactile, experimental, or non-template result. Let it synthesize art direction and route motion/frontend ownership; do not copy a reference's identity or assemble unrelated trends.
- Generate at most three meaningfully different directions; recommend one with reasons tied to the product goal.

Skip concept generation when an existing design system already answers the question.

### 3. Create visual assets only when useful

Use image generation for illustrations, textures, hero art, editorial imagery, mockups, social cards, logos, or icon exploration. Use `image-logo-icons` when available for structured brand-asset prompts.

Do not use generated raster images for functional screens, body copy, buttons, forms, navigation, charts, or information the user must read or interact with. Check licensing and brand constraints for client work.

For interface icons, use the project's existing icon set or one consistent, reputable icon library. Reuse official supplied brand SVG assets unchanged when appropriate, but never invent or draw replacement SVG markup. For custom decorative art, generate or commission a proper image asset instead.

Prefer procedural Canvas/WebGL textures over generated images for surfaces owned by a rendering engine — die faces, wheel sectors, gauge dials, labels drawn onto 3D geometry. They stay crisp at any size, follow the design tokens, and change with the data; a raster asset for the same surface has to be regenerated whenever a value or color changes.

### 4. Implement

- Use `frontend-ui-engineering` for production-quality responsive and accessible implementation.
- Use the relevant Stitch conversion skill when implementing an accepted Stitch screen.
- Follow the repository's framework, component library, tokens, and conventions.
- Build all meaningful interaction states, keyboard behavior, focus treatment, validation, reduced-motion behavior, and responsive layouts.
- Avoid unnecessary dependencies and unrelated refactors.
- Never let a value exist only inside a canvas. Anything the user reads, copies, or acts on — results, labels, prices, statuses — is rendered as real DOM text alongside the visual, with a timeout fallback so a stalled or failed scene cannot withhold it.
- Budget the weight of a rendering engine. Load it as a lazy chunk after first paint, skip it under `saveData`, reduced motion, or an explicit low-power preference, and keep the page fully usable when it never loads.

### 5. Polish

- Use `emil-design-eng` for component feel, interaction feedback, motion, transitions, and small details.
- Use `impeccable` again to critique and refine the integrated result, not isolated components only.
- Make motion purposeful, interruptible, and respectful of reduced-motion preferences.
- Use `motion-core` when the design includes material animation, scroll choreography, page transitions, gestures, Canvas/PixiJS, particles, WebGL/WebGPU, or 3D. Let it select and verify the rendering engine rather than improvising effects inside ordinary UI components.

### 6. Verify in the real interface

When the product is runnable:

1. Start it using the repository's documented command.
2. Inspect the rendered interface with available browser or screenshot tools at representative desktop and mobile sizes.
3. Exercise the primary flow and important states.
4. Fix visible layout, hierarchy, contrast, overflow, interaction, and responsiveness problems.
5. Repeat until no material issue remains.

If browser tooling or a runnable environment is unavailable, say exactly what could not be verified and provide a short manual check instead.

### 7. Final quality gate

Use `web-design-guidelines` for the final standards review when available. Confirm:

- primary action is obvious;
- hierarchy and spacing are coherent;
- contrast, semantics, keyboard access, and focus states are sound;
- layouts work at narrow and wide widths;
- loading, empty, error, and success states are handled;
- copy is concise and useful;
- generated assets do not contain functional UI or unreadable text;
- icons come from one consistent library and no improvised SVG markup was introduced;
- advanced motion has reduced-motion behavior, lifecycle cleanup, and real-browser performance evidence;
- rendered graphics agree with the data behind them — the die face, wheel sector, chart bar, or gauge needle shown in the scene is the value the model holds, confirmed by a screenshot of the settled state, not by reading the code;
- no obvious console, build, lint, or test failure was introduced.

## Completion response

Report concisely:

- what was designed or changed;
- which checks were actually performed;
- remaining assumptions or limitations;
- the most valuable next step, only if one remains.

Do not list every internal skill invocation unless the user asks. Describe outcomes and evidence.

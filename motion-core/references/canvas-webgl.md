# Canvas, PixiJS, WebGL, and Three.js

Use for GPU-rendered 2D/3D work.

## Architecture

- Keep the renderer in an isolated leaf component with explicit create, resize, pause, resume, and destroy lifecycle.
- Keep accessible text, controls, links, forms, and primary data in DOM. Mirror necessary scene state through semantic controls/status, not invisible Canvas hit areas alone.
- Separate simulation/update from rendering so timing and tests remain controllable.
- Use elapsed time/delta carefully; clamp long background-tab deltas and avoid frame-rate-dependent behavior.
- Handle device/context loss and asset-load failure with a meaningful fallback.

## Resolution and sizing

- Size from a stable container with `ResizeObserver` or framework equivalent.
- Cap device pixel ratio based on workload/device; full high-DPR postprocessing is often wasteful.
- Recompute camera/projection/render targets on resize and orientation changes.
- Avoid reading layout every frame.

## Assets and memory

- Compress and right-size textures/models; lazy-load optional scenes.
- Define asset ownership and cache lifetime.
- Dispose textures, geometries, materials, render targets, filters, loaders/workers, and event handlers when no longer owned.
- Avoid recreating GPU resources or allocating objects inside the frame loop.
- Test route re-entry for duplicated canvases, tickers, and retained GPU memory.

## Throughput

- Batch sprites, use particle containers/instancing where appropriate, and reduce state/material changes.
- Cull offscreen/hidden objects and pause rendering when nothing changes.
- Reduce transparent overdraw, oversized filters, shadow maps, postprocessing passes, particle count, and shader complexity before lower-level tuning.
- Avoid per-frame React/application state updates; write simulation/render state inside the isolated rendering boundary.
- Profile CPU and GPU separately when tooling permits.

## Three.js/WebGPU caution

- Match code to the installed Three.js revision and current official docs.
- Treat WebGPU as progressive enhancement unless target support is explicitly constrained.
- Provide WebGL or non-3D fallback where product reach requires it.
- Compile/test shaders and validate precision, uniforms, color space, tone mapping, and device limits on representative hardware.

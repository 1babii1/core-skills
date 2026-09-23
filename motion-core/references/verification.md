# Runtime motion verification

Use after implementation or during an animation audit.

## Functional matrix

- first load before fonts/assets settle;
- repeat trigger rapidly, reverse mid-flight, and navigate away mid-animation;
- desktop pointer, keyboard, touch/coarse pointer, and narrow mobile;
- reduced-motion enabled;
- resize, orientation change, zoom, and route back/forward;
- hidden/background tab then foreground;
- slow asset/network load and asset failure;
- optional engine unsupported or context lost where practical.

## Browser evidence

- Inspect console errors/warnings and duplicate initialization.
- Record/observe the full motion, not only screenshots.
- Use browser animation tooling or temporary slow-motion playback to inspect sequencing.
- Check computed styles and DOM availability before triggers fire.
- Inspect layout shifts, long animation frames, input latency, paint/compositing, memory growth, and retained listeners/resources.
- For Canvas/3D, compare object/draw-call/texture/resource behavior before and after repeated mount/unmount where tooling permits.

## Acceptance

- The interface remains usable throughout the animation.
- Fast repeated input does not jump, queue stale transitions, or leave intermediate state.
- Reduced motion preserves meaning and task completion.
- Mobile avoids desktop-only pin/parallax/particle cost when necessary.
- Critical content is present if animation initialization fails.
- No persistent RAF/ticker/observer/listener/GPU resource survives after its owning view is gone.
- Performance claims include device/browser/test context and observed evidence.

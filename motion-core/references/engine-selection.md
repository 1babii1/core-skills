# Motion engine selection

Choose the lowest-complexity engine that owns the required behavior.

| Requirement | Preferred approach | Avoid |
| --- | --- | --- |
| Hover/focus/short deterministic transition | CSS transition/keyframes | Shipping a JS engine |
| Programmatic deterministic DOM animation | WAAPI | Manual RAF tweening |
| React enter/exit, layout, shared element, gestures | Motion | GSAP and Motion controlling the same node |
| Complex sequence/timeline | GSAP | Nested timeout choreography |
| Scroll pin/scrub/storytelling | GSAP ScrollTrigger | Global smooth-scroll hijacking by default |
| Native simple scroll progress | CSS scroll-driven animations when supported with fallback | JS polling scroll position |
| Large interactive 2D scene, particles, sprites | PixiJS | Thousands of DOM nodes |
| Simple custom 2D drawing/editor | Canvas 2D or PixiJS depending scale | Three.js solely because it is impressive |
| True 3D/models/lighting/camera/shaders | Three.js or React Three Fiber in React | Simulating a full 3D scene with DOM transforms |
| Rendered promotional video | Remotion | Running an interactive engine only to export frames manually |
| Designer-authored stateful vector asset | Supplied Rive asset/runtime | Hand-generated SVG or Rive binary |
| Designer-authored timeline vector asset | Supplied Lottie asset/runtime | Agent-generated large Bodymovin JSON |

## Decision questions

1. Is the target semantic UI or decorative/visual content?
2. Is movement state-driven, timeline-driven, scroll-driven, or continuously simulated?
3. Must users directly manipulate it?
4. How many objects/pixels/draw calls and what target devices?
5. Can CSS/WAAPI meet interruption and sequencing needs?
6. What happens without JavaScript, WebGL/WebGPU, the asset, or full motion?
7. Does the repository already ship an engine capable of the effect?

Do not introduce two engines where one can own the full effect. Keep optional rendering engines dynamically imported behind stable DOM layout.

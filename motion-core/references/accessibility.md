# Motion accessibility

Use for all material motion and Canvas/3D experiences.

- Respect `prefers-reduced-motion` in CSS and JavaScript/engine configuration.
- Design a reduced variant: replace large travel, parallax, zoom, spin, shake, and auto-scroll with instant state or short opacity/color feedback.
- Never require watching animation to understand content, status, order, or completion.
- Avoid flashes exceeding safe frequency and large high-contrast strobing regions.
- Provide pause/stop/hide control for persistent, auto-starting, or distracting motion where applicable.
- Keep keyboard focus stable and visible during transforms, portals, route transitions, and reordered layouts.
- Do not animate focus away from the user's action or move hit targets while they are being acquired.
- Gate hover-specific effects behind hover-capable/fine-pointer media conditions and provide touch/keyboard equivalence.
- Keep Canvas scene controls and status available through semantic DOM; provide alternative text/data representation when the scene conveys information.
- Do not announce every animation frame. Announce meaningful application state changes only.

Test with reduced motion enabled, keyboard only, touch/coarse pointer, zoom, and screen-reader-relevant DOM inspection.

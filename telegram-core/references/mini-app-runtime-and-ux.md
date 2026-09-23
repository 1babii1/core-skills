# Mini App Runtime and UX

- Initialize the official/current Telegram Mini Apps SDK once at the application boundary.
- Let the SDK own theme, viewport, safe-area insets, BackButton, MainButton/BottomButton, closing behavior, haptics, fullscreen, and capability state.
- Subscribe to SDK events; do not poll layout values on an arbitrary timer.
- Use CSS environment/runtime values and measured content. Avoid magic viewport fallbacks.
- Design for light/dark themes, dynamic viewport changes, keyboard overlap, safe areas, slow networks, and interrupted sessions.
- Use feature/version checks and graceful fallbacks.
- A Mini App can be reloaded or closed at any time; preserve only meaningful drafts and make submissions idempotent.

Test in:

- Telegram on current iOS and Android;
- Telegram Desktop where supported;
- browser development with a deliberate SDK mock;
- compact/tall viewports, rotation/keyboard, light/dark and accessibility settings.

Use `frontend-core`, `design-core`, and `qa-core`. Prefer library icons and real/generated raster imagery; do not create decorative SVG filler.

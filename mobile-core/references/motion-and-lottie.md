# Motion, gestures, and Lottie

Use motion to clarify state, hierarchy, causality, navigation, and direct manipulation. Do not animate merely to make a screen feel generated or “premium.”

Official Reanimated baseline: https://docs.swmansion.com/react-native-reanimated/docs/

## Selection

- Use platform/native navigation transitions when they communicate the interaction.
- Use Reanimated 4 for gesture-driven, interruptible, scroll-linked, layout, or high-frequency motion.
- Use simple framework animation only when it is sufficient and compatible with the project.
- Use Lottie for bounded, authored illustration sequences such as onboarding, celebration, or a branded loading moment.
- Use static raster/WebP/AVIF images or established icon libraries when motion adds no value.

Do not generate SVG icons or decorative SVG artwork. Prefer supplied, licensed, or image-generated assets that satisfy `design-core`.

## Reanimated rules

- Verify compatibility with installed Expo/RN, New Architecture, and React Compiler versions.
- Prefer transform and opacity for smooth animation; measure exceptions.
- Keep high-frequency calculations off React render paths.
- Avoid broad subscriptions and JS/UI thread crossings.
- Make gestures interruptible and define cancellation/end states.
- Respect the system reduced-motion setting and provide a calm equivalent.

## Lottie rules

- Use a maintained Lottie package compatible with the installed Expo SDK.
- Validate ownership/license and keep editable source outside the runtime bundle when appropriate.
- Bound dimensions, duration, looping, layer count, masks, blur, gradients, and embedded image sizes.
- Avoid indefinite loops that consume battery or distract from content.
- Provide a static or reduced-motion fallback.
- Do not use Lottie as the only loading, success, or error signal; preserve accessible text and semantics.
- Test rendering, memory, startup impact, dark mode, transparency, and reduced motion on iOS and representative lower-end Android hardware.

## Completion

Motion must preserve input responsiveness, accessibility focus, touch targets, readable content, and predictable navigation. Remove animation that cannot meet its frame budget or communicate a useful state change.

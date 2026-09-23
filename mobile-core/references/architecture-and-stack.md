# Architecture and stack

Read for new applications, structural changes, or uncertain native boundaries.

## Stack selection

- Prefer Expo and Expo Router for new cross-platform applications.
- Use a development build for real applications requiring native configuration, remote push, app links, custom modules, or production-like testing.
- Preserve bare React Native when the project already owns native folders or requires native integration that managed Expo cannot reasonably express.
- Verify the installed Expo SDK and React Native compatibility before selecting package versions.
- Keep web-only assumptions out of native code. Use platform files when behavior or dependencies differ materially.

## Structure by scale

For a small application:

```text
src/
  app/          routes only
  screens/      substantial screen bodies
  components/   genuinely reusable UI
  lib/          narrow technical adapters
  theme/
```

As product behavior grows:

```text
src/
  app/
  features/
    checkout/
      api/
      model/
      ui/
      index.ts
  entities/
  shared/
    api/
    config/
    native/
    storage/
    ui/
```

For large products, group features and entities within bounded domains. Domains express business ownership, not technical layers. Keep each domain's public entry point narrow and dependencies one-way.

## Extraction rules

- Keep one-off code close to its route or feature.
- Extract because cohesion, reuse, independent testing, ownership, or platform separation improves.
- Avoid global dumping grounds named `utils`, `hooks`, `services`, `types`, or `components` once business behavior becomes fragmented.
- Keep route files thin: parse route inputs, compose providers/layout, and render a screen or feature.
- Keep native adapters behind typed TypeScript interfaces so business logic is testable without a device.
- Keep native dependencies in the application package in monorepos and maintain one compatible version.

## Native boundary

Choose in order:

1. React Native or Expo built-in capability;
2. maintained Expo SDK module;
3. maintained third-party module with compatible New Architecture support;
4. config plugin;
5. local Expo module;
6. direct native project ownership.

Before adding native code, verify maintenance, platform coverage, licensing, compatibility, privacy impact, binary size, and release implications.

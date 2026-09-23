---
name: mobile-core
description: Orchestrate architecture, implementation, review, repair, testing, security, performance, offline behavior, native permissions, push notifications, animations, and store readiness for React Native and Expo mobile applications. Use for new or existing iOS and Android apps when asked to build, structure, improve, audit, refactor, debug, optimize, add native capabilities, or prepare releases.
---

# Mobile Core

Own the mobile outcome from stack selection through verified device behavior and release readiness. Assemble the smallest relevant train from installed specialist skills; do not require the user to invoke cars manually.

## Non-negotiable defaults

- Inspect repository instructions, Expo and React Native versions, package manager, lockfile, New Architecture state, app config, native folders, navigation, build profiles, supported OS versions, test stack, and existing conventions before advising or editing.
- Prefer managed Expo with development builds for new production applications. Use bare React Native or custom native code only when capabilities, integration constraints, or an existing project justify it.
- Preserve an existing suitable stack. Never migrate, prebuild, eject, add native folders, or change bundle identifiers merely for fashion.
- Use TypeScript strict mode for new work. Tighten existing applications incrementally when a full switch would be disruptive.
- Keep `src/app` routes-only with Expo Router. Use route colocation for small apps, feature-first boundaries as complexity grows, and bounded domain modules only when product and team complexity justify them.
- Classify state before choosing a library. Never mirror server or SQLite-owned records into Zustand without an explicit synchronization design.
- Use native and Expo SDK capabilities before introducing a third-party dependency. Install packages with the repository package manager and `npx expo install` when Expo version alignment matters.
- Treat iOS and Android as distinct platforms with a shared product, not as identical rendering targets.
- Never read `.env`, `.env.*`, secret stores, signing keys, provisioning profiles, service-account files, credentials, tokens, or encrypted vaults. Read `.env.example` only and route secret workflows through `secrets-core`.
- Preserve unrelated changes and verify behavior on representative devices or emulators.

## Resolve guidance conflicts

Apply guidance in this order:

1. explicit user requirements and repository-scoped instructions;
2. behavior of installed versions, verified against current official documentation when unstable;
3. this skill's architecture, ownership, state, security, and release rules;
4. specialist-skill recommendations.

Treat specialist claims such as “always use Expo Go”, fixed retry counts, fixed cache durations, universal folder layouts, and platform-wide styling rules as suggestions unless they are correctness or security invariants. For real applications, prefer a development build when push, native configuration, custom modules, or production-like testing is involved.

## Select the operating mode

- **Create:** choose the smallest sustainable stack, implement the product, add proportional tests, and verify development and production builds.
- **Improve/fix:** establish a baseline, reproduce the problem, make the smallest effective change, and prove the regression is resolved.
- **Audit:** inspect and report evidence without modifying code, stores, credentials, builds, or releases.
- **Audit and repair:** prioritize findings, repair authorized issues, and rerun the quality gate.
- **Debug:** reproduce and explain the cause; implement only when the user asks for a fix.
- **Release readiness:** verify device behavior, privacy, security, performance, accessibility, signing configuration shape, store assets, rollback, and staged rollout without publishing unless explicitly authorized.

## Mandatory baseline

Read every selected skill's `SKILL.md` before applying it.

| Area | Skill or reference | Requirement |
| --- | --- | --- |
| Expo UI | `expo-native-ui` | Apply to native-feeling screens and Expo SDK UI |
| Navigation | `expo-router` | Apply to routes, stacks, tabs, sheets, links, and deep links |
| Performance | `vercel-react-native-skills` | Apply relevant list, image, animation, rendering, and native rules |
| Type safety | `typescript` | Apply to TypeScript implementation and configuration |
| Secrets | `secrets-core` | Enforce the `.env.example`-only boundary |
| Security | `security-best-practices`, [security-resilience.md](references/security-resilience.md) | Review mobile trust boundaries and changed attack surface |
| Verification | `run-tests`, `qa-core`, [testing-and-release.md](references/testing-and-release.md) | Run proportional static, automated, device, and build checks |
| UX | `design-core` | Apply to user-facing work, including its no-generated-SVG policy |

For authentication and protected navigation, include `auth-core`. For API contracts and push backend changes, include `backend-core`. For CI/CD, signing workflows, rollout, and operational readiness, include `delivery-core`. For public Expo web surfaces, include `frontend-core` and `seo-core`.

## Route by concern

| Concern | Skills or references | Include when |
| --- | --- | --- |
| New project structure | `expo-project-structure`, [architecture-and-stack.md](references/architecture-and-stack.md) | A new Expo application has no established structure |
| Existing architecture | [architecture-and-stack.md](references/architecture-and-stack.md) | Feature boundaries, domains, imports, or platform variants need decisions |
| State and forms | `tanstack-query`, `react-hook-form`, `zod`, [state-forms-and-data.md](references/state-forms-and-data.md) | Shared state, forms, validation, server data, cache, or persistence |
| Networking | `expo-data-fetching`, [state-forms-and-data.md](references/state-forms-and-data.md) | API requests, cancellation, retry, mutations, pagination, or caching |
| Permissions | [permissions-and-capabilities.md](references/permissions-and-capabilities.md) | Camera, photos, location, microphone, contacts, Bluetooth, biometrics, tracking |
| Offline/local-first | [offline-storage-and-sync.md](references/offline-storage-and-sync.md) | Durable local data, query persistence, outbox, synchronization, conflicts |
| Push/background | [push-and-background.md](references/push-and-background.md) | Notifications, deep links, background tasks, tokens, receipts |
| Motion | `expo-native-ui`, `vercel-react-native-skills`, `motion-core`, [motion-and-lottie.md](references/motion-and-lottie.md) | Reanimated, gestures, Lottie, transitions, reduced motion |
| Native extension | `expo-dev-client`, `expo-module` | Config plugins, native SDKs, custom Swift/Kotlin modules or views |
| Store release | `eas-app-stores`, `delivery-core`, [testing-and-release.md](references/testing-and-release.md) | TestFlight, Play tracks, metadata, signing, staged rollout |
| Design conversion | `stitch::react-native`, `design-core` | Implementing a supplied or Stitch-generated design in React Native |

Do not introduce Zustand merely because it is preferred for web projects; use it only when shared client state is demonstrated. Do not introduce Reanimated or Lottie for static screens. Do not introduce EAS cloud services when local builds or another delivery system satisfy the requirement.

## Execute the workflow

### 1. Inventory the real application

Map:

- routes, stacks, tabs, modals, deep links, protected flows, startup path, and critical journeys;
- feature/domain ownership, import direction, platform variants, shared UI, native modules, and generated code;
- each state value's owner, lifetime, persistence, sensitivity, and synchronization semantics;
- API clients, query keys, local databases, migrations, outbox, push handling, background work, and error contracts;
- permissions declared at build time and requested at runtime;
- tests, supported devices and OS versions, accessibility, performance telemetry, build profiles, update channels, and release tracks.

Separate confirmed evidence from assumptions. Establish existing failures before editing.

### 2. Select structure and native boundary

Apply [architecture-and-stack.md](references/architecture-and-stack.md). Keep route files thin. Colocate one-off behavior, extract a feature when cohesion or ownership improves, and introduce domains only for genuine business boundaries.

Prefer Expo SDK modules and config plugins. Add `ios/` or `android/` ownership only when required. Use `expo-module` for intentional reusable Swift/Kotlin boundaries, not to reimplement an available maintained package.

### 3. Assign state, data, and storage ownership

Apply [state-forms-and-data.md](references/state-forms-and-data.md) and [offline-storage-and-sync.md](references/offline-storage-and-sync.md).

Keep ephemeral UI state local, navigation state in route parameters, form state in RHF when complexity warrants it, remote server state in TanStack Query, small shared client state in scoped Zustand stores, sensitive credentials in SecureStore, preferences in a key-value store, and durable relational/offline data in SQLite.

### 4. Implement complete native UX

Use `expo-native-ui`, `expo-router`, and `design-core`. Cover loading, success, empty, stale, offline, denied permission, blocked permission, validation, unauthorized, forbidden, not-found, rate-limited, partial-success, background-resume, and unexpected-error states when applicable.

Use real image/icon assets or established icon libraries. Do not generate SVG icons or decorative SVG illustrations. Test safe areas, keyboard avoidance, font scaling, dark mode, reduced motion, screen readers, touch targets, orientation, and small/large screens.

### 5. Engineer permissions, push, and lifecycle behavior

Apply [permissions-and-capabilities.md](references/permissions-and-capabilities.md) and [push-and-background.md](references/push-and-background.md). Request the minimum capability in response to a clear user action. Design foreground, background, terminated, offline, token-rotation, logout, and account-switch behavior.

Never treat background execution or push delivery as guaranteed. The server remains authoritative for important state.

### 6. Engineer security and resilience

Apply [security-resilience.md](references/security-resilience.md). Treat the installed app and device as untrusted clients. Keep authorization and privileged decisions on the server. Bound retries, use idempotency for replayable mutations, sanitize deep links and remote content, minimize stored personal data, and avoid logging tokens, payloads, or sensitive identifiers.

### 7. Add motion deliberately

Apply [motion-and-lottie.md](references/motion-and-lottie.md). Prefer Reanimated 4 for interactive, gesture-driven, or layout motion. Use Lottie for bounded authored sequences, not general UI state. Respect reduced motion and verify performance on a representative lower-end Android device.

### 8. Test by risk and prepare release

Apply [testing-and-release.md](references/testing-and-release.md) and `qa-core`. Test business logic, component behavior, API scenarios, offline recovery, permission branches, deep links, notification responses, upgrades/migrations, and the few critical journeys end to end.

Use a development build for production-like native validation. Verify both platforms and a representative device matrix. Prepare store metadata, privacy disclosures, signing inputs, release notes, rollback/update compatibility, and staged rollout. Do not build in paid cloud services, submit, publish, or change production tracks without explicit user authorization.

## Completion gate

Do not call mobile work complete until applicable statements are true:

- Expo/RN versions, architecture, native boundary, supported platforms, and ownership are explicit;
- state, cache, local database, form, route, and credential ownership have no avoidable duplication;
- permissions have build-time declarations, contextual runtime requests, denial handling, and store-ready explanations;
- offline behavior, migrations, outbox, idempotency, conflicts, and recovery are defined where data persists;
- foreground, background, terminated, deep-link, notification, logout, and account-switch behavior are coherent;
- no secret file or value was inspected or exposed, and sensitive data uses appropriate storage;
- accessibility, reduced motion, safe areas, keyboard, font scaling, list/image performance, and platform differences were verified proportionally;
- typecheck, lint, relevant tests, representative device journeys, and production build checks pass or exact failures are reported;
- store release, staged rollout, monitoring, compatibility, and rollback risks are explicit;
- integration with design, auth, backend, QA, delivery, and secrets cores has no silent gap.

## Completion response

Lead with the mobile outcome. Report material architecture or implementation changes, platforms and device states verified, checks actually run, and remaining release or operational risks. Do not dump internal skill invocations unless asked.

# Testing and release

Use `qa-core` for the full strategy and this reference for mobile-specific gates.

## Risk-based layers

- Unit-test domain decisions, validation, reducers, migrations, conflict resolution, and serialization.
- Component-test forms, loading/error/empty states, accessibility labels, and permission-dependent rendering.
- Contract-test API clients and push payloads against backend schemas.
- Integration-test storage repositories, migrations, outbox replay, auth reset, and native adapters where tooling permits.
- E2E-test only the critical journeys whose failure materially harms users or release confidence.

Prefer test IDs only where semantic selectors are insufficient. Mock OS boundaries at lower layers, but verify critical native behavior on real development/release builds.

## Device-state matrix

Cover applicable combinations:

- iOS and Android, minimum supported and current OS;
- small and large screen, lower-end Android, dark mode, large text, reduced motion, screen reader;
- fresh install, upgrade, logout/account switch, cold start, background/resume, process death;
- online, offline, flaky network, token expiry, duplicate response;
- permission undetermined, granted, limited, denied, blocked;
- notification foreground, background, terminated, tapped, duplicate, stale;
- low disk, migration failure, unavailable service, and corrupted recoverable cache.

## Build gate

Run repository-native format, lint, typecheck, unit/integration tests, affected mobile E2E journeys, and production build/config checks. Inspect final native permissions, entitlements, deep links, bundle identifiers, version/build numbers, update runtime compatibility, package size, source maps, and privacy-sensitive SDKs.

Use development clients for native iteration and release-like builds for final validation. Do not equate Metro success with a valid store binary.

## Store readiness

Prepare:

- app name, category, descriptions, localized metadata, screenshots, icons, privacy/support URLs;
- privacy labels/data safety declarations derived from actual SDK behavior;
- permission explanations and review notes;
- signing/configuration contract without reading secret files;
- staged rollout plan, monitoring, crash-free baseline, support path, and rollback/stop criteria;
- database/API/update compatibility with the previous supported release.

Use internal/TestFlight tracks before staged production. Store submission, paid EAS builds, production rollout, and OTA publication are external changes and require explicit user authorization.

## Release evidence

Record the source revision, dependency lock, native runtime/version, build profile, tests run, device matrix, known issues, migration plan, update channel, monitoring signals, and rollback decision. A successful upload is not a successful release.

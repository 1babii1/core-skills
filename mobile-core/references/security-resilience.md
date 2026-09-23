# Mobile security and resilience

Treat the shipped application, JavaScript bundle, device, network, deep links, local database, and notification payloads as attacker-observable and potentially modifiable.

## Trust boundaries

- Enforce authentication, authorization, business rules, entitlements, prices, quotas, and ownership on the backend.
- Consider every client-bundled variable public, including all `EXPO_PUBLIC_*` values.
- Keep server credentials, signing keys, service-account files, private API keys, and provider secrets outside the app.
- Route login, token refresh, logout, account switching, biometrics, and protected navigation through `auth-core`.
- Store only small necessary credentials in SecureStore; never place tokens in ordinary key-value storage.
- Do not use device biometrics as a replacement for server authentication.

## Inputs and navigation

- Allowlist schemes, hosts, routes, actions, and parameter shapes for deep links and notification navigation.
- Validate API, SQLite, file, WebView, clipboard, QR, and native-module inputs.
- Avoid arbitrary code, URL, HTML, or intent execution.
- Minimize WebView use; restrict origins, navigation, bridges, file access, and injected content.
- Use safe SQL parameters and safe filesystem paths.

## Data and privacy

- Minimize collection and retention of personal data.
- Define deletion, logout, account-switch, backup, screenshot, clipboard, and analytics behavior.
- Redact tokens, credentials, personal payloads, request bodies, and sensitive identifiers from logs and crash reports.
- Align permissions, SDK data collection, tracking, privacy manifests, store disclosures, and actual behavior.
- Threat-model rooted/jailbroken devices only when product risk justifies controls; do not rely on root detection alone.

## Resilience

- Bound timeouts, retries, queue sizes, caches, database growth, media size, and background work.
- Use cancellation and cleanup for subscriptions, sensors, listeners, and tasks.
- Use idempotency for replayable mutations and push actions.
- Handle process death, low memory, low disk, offline startup, corrupt persistence, incompatible API versions, and partial migrations.
- Keep a last-known-good binary/update strategy and ensure OTA changes remain compatible with the native runtime.

Security testing must target changed attack surfaces. Do not claim certificate pinning, encryption, obfuscation, or device integrity controls unless the threat model, maintenance burden, and recovery behavior justify them.

# Push notifications and background work

Official baselines:

- https://docs.expo.dev/push-notifications/overview/
- https://docs.expo.dev/push-notifications/what-you-need-to-know/
- https://docs.expo.dev/push-notifications/sending-notifications/

## Provider choice

Use `expo-notifications` on the client unless an existing provider SDK or missing capability justifies another integration. Choose one client-side notification implementation. The backend may use Expo Push Service or direct APNs/FCM; document the tradeoff and token types.

Remote push requires a development build for production-like testing. Never assume Expo Go behavior represents release behavior.

## Token lifecycle

- Request notification permission contextually.
- Obtain tokens only after required native configuration is present.
- Associate tokens with installation, user, platform, environment, and provider without treating them as permanent identity.
- Upsert token changes and remove or disable tokens after logout, account changes, permission revocation, or invalid receipts.
- Store provider credentials only on the backend through `secrets-core`.
- Make registration and deregistration idempotent.

## Delivery and response

Design and test foreground, background, terminated, cold-start, duplicate, stale, and tapped-notification paths.

- Validate payload schema and allowed route/action identifiers.
- Treat notification text and data as untrusted input.
- Do not place secrets or sensitive personal data in notification payloads.
- Authorize the destination after opening; a deep link is not authorization.
- Deduplicate actions and make backend effects idempotent.
- Configure Android channels before sending to them and avoid changing established channel semantics unexpectedly.
- Track send tickets and receipts; stop sending to tokens reported as unregistered.

Push delivery and background execution are best effort. Do not use either as the only mechanism for critical data consistency, security, alarms, or financial operations. Reconcile authoritative state when the app opens.

## Background tasks

- Keep work small, resumable, idempotent, and tolerant of termination.
- Persist checkpoints before yielding.
- Respect OS scheduling, battery, network, and frequency constraints.
- Prefer normal notification messages unless background processing is genuinely required.
- Provide an in-app recovery path when the background task never runs.

Measure opt-in, token registration, send acceptance, provider receipts, open/action outcomes, and failures without logging payload contents or personal data.

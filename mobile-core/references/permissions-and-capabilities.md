# Permissions and native capabilities

Use for camera, media library, microphone, location, contacts, Bluetooth, notifications, biometrics, tracking, calendars, and similar protected capabilities.

Official baseline: https://docs.expo.dev/guides/permissions/

## Model both layers

1. **Build-time declaration:** config plugin, Android manifest permissions, blocked permissions, iOS usage descriptions, entitlements, and capabilities.
2. **Runtime state:** unavailable, undetermined, granted, limited, denied-but-requestable, and blocked/settings-required where the API exposes them.

A JavaScript request cannot repair a missing build-time declaration. Native configuration changes require a new binary and cannot be delivered only through OTA update.

## Request flow

- Ask only for the minimum capability and precision needed.
- Explain the concrete user benefit before the OS dialog when context is not already obvious.
- Trigger the request from a relevant user action, not on first launch.
- Continue with a useful degraded path when possible.
- On denial, do not loop prompts. Explain alternatives.
- Offer a settings link only when the user can no longer be prompted and the capability is necessary.
- Recheck status after returning from settings or foregrounding the app.
- Treat limited photo/library access as its own supported state.

## Platform requirements

- Tailor iOS usage descriptions to the actual feature; boilerplate text risks store rejection.
- Audit permissions brought transitively by dependencies and block unused Android permissions.
- Account for Android API-level differences, one-time permissions, approximate location, notification permission, background restrictions, and foreground services.
- Request background location or continuous capabilities only after foreground value is established and the store justification is documented.
- Test on real devices when simulator behavior is incomplete.

## Verification matrix

Test first request, grant, deny, limited access, permanent denial, settings recovery, app restart, OS upgrade when relevant, and capability removal. Verify that protected screens do not crash or become dead ends.

Never infer authorization from the presence of a permission. Server-side authorization and product consent remain separate concerns.

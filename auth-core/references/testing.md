# Authentication verification

Use for every auth implementation or hardening change. Prefer real in-process protocol components over mocking the token pipeline itself.

## Test layers

### Unit

Test custom policy handlers, redirect validation, claim mapping, account-linking decisions, OTP/magic-link consumption rules, and pure authorization logic. Do not unit-test framework cryptography.

### Integration

Host the real application with `WebApplicationFactory` or the repository equivalent. Exercise the actual Identity/OpenIddict registration, persistence, endpoint handlers, signing, validation, authorization middleware, and database constraints. Substitute only true external I/O where necessary.

### Protocol

Validate discovery and JWKS, authorization requests, callbacks, code exchange, refresh, client credentials, userinfo, revocation/logout behavior, and API token validation. Inspect protocol status and error fields without logging credentials.

### Browser/E2E

Use Playwright for login, logout, callback, cookies, protected navigation, recovery, external-provider stubs/test tenants, multiple tabs, expired sessions, and redirect behavior. Use dedicated test accounts and secrets supplied through the approved secret runner.

## Required negative cases

Select all applicable cases:

- anonymous request to protected resource;
- authenticated user lacking permission, scope, resource ownership, or tenant membership;
- wrong issuer, audience, client, redirect URI, grant, scope, response type, or authentication method;
- expired, not-yet-valid, malformed, tampered, unsigned, or wrong-algorithm token;
- authorization code reused or presented by the wrong client/redirect/PKCE verifier;
- refresh token replay, expiry, revocation, or use after account disable/security change;
- missing/invalid state, nonce, antiforgery token, correlation cookie, or callback parameters;
- open/local redirect bypass attempts;
- duplicate external-account linking and email collision;
- OTP/magic-link expiry, incorrect value, replay, concurrent redemption, and rate limit;
- cookie theft mitigations, logout behavior, and session invalidation;
- proxy-generated wrong scheme/host/issuer;
- unavailable authority/key store/database/provider and safe failure behavior.

## Assertions

- Assert both HTTP/protocol outcome and absence of unintended side effects.
- Assert tokens contain only intended claims, scopes, audience, issuer, and lifetimes.
- Assert 401 for unauthenticated and 403 for authenticated-but-forbidden where the framework contract applies.
- Assert logs and error responses do not contain credentials or tokens.
- Keep test clients/scopes minimal so broad fixtures do not hide permission bugs.
- Never disable authorization globally to make application integration tests convenient. A test handler is acceptable only for isolated resource-server tests, with separate real-flow coverage.

## Completion evidence

Record commands, tested flows, relevant environment/topology, and failures. Distinguish local/in-process proof from deployed proof. If external-provider or production-key behavior cannot be exercised, state the exact unverified assumption.

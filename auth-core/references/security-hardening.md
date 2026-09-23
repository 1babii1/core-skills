# Authentication security hardening

Use for implementation reviews and before production deployment. Verify current recommendations in primary framework and protocol documentation.

## Accounts and recovery

- Require unique normalized identifiers only when the product model permits them.
- Use framework password hashing and configurable modern password policy; never store reversible passwords.
- Rate-limit and monitor login, registration, OTP, recovery, verification, and token endpoints.
- Avoid account enumeration in response body, status, and meaningful timing differences.
- Require confirmed ownership where needed and protect email/phone changes as sensitive operations.
- Invalidate relevant sessions/tokens after password reset, credential removal, account disable, or security-sensitive profile changes according to policy.
- Offer MFA/passkeys when risk and audience justify them; protect enrollment and recovery as strongly as login.

## Cookies and browser flows

- Set HttpOnly, Secure in production, an intentional SameSite policy, narrow domain/path, and appropriate lifetime.
- Regenerate the authenticated session after login and privilege elevation.
- Apply antiforgery protection to cookie-authenticated state changes.
- Permit redirects only to validated local or exactly registered destinations.
- Protect login, logout, callback, and account-linking flows against CSRF and session swapping.
- Keep access and refresh tokens out of browser-readable storage when a server-side session/BFF is feasible.

## OAuth/OIDC

- Use Authorization Code with PKCE; prohibit implicit and password grants.
- Match redirect URIs exactly; never use production wildcards.
- Constrain grants, endpoints, scopes, resources, response types, and authentication methods per client.
- Validate issuer, audience/resource, signature, lifetime, nonce/state where applicable, and allowed algorithms.
- Rotate refresh tokens or otherwise provide replay detection when supported; define revocation semantics.
- Never use an ID token as an API access token.
- Never let a client decide authorization solely through untrusted token fields or UI state.
- Prevent token substitution and confused-deputy behavior across APIs, clients, tenants, and issuers.

## Keys and secrets

- Keep client secrets, provider secrets, signing keys, encryption keys, cookies, and tokens outside source control.
- Use asymmetric signing for multi-service validation and publish only public key material through JWKS.
- Pin allowed algorithms; reject unsigned or unexpected algorithms.
- Define key generation, access, backup, rotation, overlap, revocation, and emergency replacement.
- Persist data-protection keys safely for multi-instance/restart continuity.
- Never place secrets in URLs, logs, traces, analytics, exception bodies, or support screenshots.

## Network and deployment

- Enforce HTTPS externally; configure HSTS where appropriate.
- Trust forwarded headers only from known proxies/networks and verify external scheme/host reconstruction.
- Restrict CORS to exact necessary origins, methods, and headers; CORS is not authorization.
- Keep clocks synchronized and choose only the minimum necessary skew.
- Separate development shortcuts from production configuration and fail startup when mandatory production keys/configuration are absent.
- Avoid health endpoints that reveal clients, keys, claims, or provider configuration.

## Authorization

- Require authorization by default and mark public endpoints deliberately.
- Prefer policies and resource checks over ad hoc string comparisons.
- Validate tenant/resource ownership in the data access path, not only in the UI.
- Separate client scopes from user permissions and require both when both matter.
- Treat role/permission changes as session/token lifecycle events when prompt revocation is required.

## Observability

Record safe audit events for login success/failure, lockout, MFA/recovery changes, token/client failures, account linking, privilege changes, revocation, and key events. Use stable internal identifiers and correlation IDs; exclude credentials and token contents. Alert on abnormal rate, replay, impossible client behavior, repeated invalid redirects, and key/configuration failures.

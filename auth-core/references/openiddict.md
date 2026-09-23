# OpenIddict engineering

Use this reference for any project containing OpenIddict packages or requesting an OpenIddict client, server, or validator. Confirm APIs against the installed version and current official documentation at https://documentation.openiddict.com/ before editing.

## Identify the role

- `AddCore`: persistence/managers for applications, authorizations, scopes, and tokens.
- `AddClient`: consume external OAuth/OIDC providers.
- `AddServer`: expose OAuth/OIDC endpoints and issue tokens.
- `AddValidation`: validate access tokens for a resource server.

A host may use several roles, but each must have a stated reason. Avoid accidental circular trust or ambiguous default authentication schemes.

## Server checklist

- Set one stable externally correct issuer.
- Enable only required flows and endpoints.
- Require PKCE for authorization-code clients.
- Register exact scopes and map them to resources/audiences.
- Register each client with its correct type, secret/authentication method, redirect URIs, post-logout URIs, endpoint permissions, grant permissions, response types, and scopes.
- Use passthrough only where custom endpoint logic is required and test that logic end to end.
- Assign claim destinations deliberately; do not copy every Identity claim into every token.
- Keep sensitive/internal claims out of identity and access tokens.
- Use durable protected production signing/encryption keys; development certificates are development-only.
- Choose JWT/reference/encrypted-token behavior intentionally based on consumer and revocation requirements.
- Revalidate active user/account state during code and refresh exchanges when requirements demand immediate disable/revocation behavior.

## Client checklist

- Use exact callback URIs and state/correlation protections provided by the framework.
- Use discovery rather than hardcoded provider endpoints when supported.
- Validate issuer and provider identity.
- Keep confidential client credentials server-side.
- Map external identities using stable provider subject plus issuer/provider, not email alone.
- Handle account linking explicitly to prevent takeover.
- Treat provider email verification semantics as provider-specific.

## Validation checklist

- Prefer local-server validation only when the validator and issuer genuinely share the same trusted host/configuration boundary.
- For remote APIs, validate against the intended issuer and constrain audience/resource.
- Do not disable lifetime, issuer, audience, or signature checks to resolve integration failures.
- Keep scheme selection explicit when cookies and bearer tokens coexist.

## Identity integration

Use Identity for accounts, local credentials, lockout, confirmation, recovery, roles, security stamps, and local cookies. Use OpenIddict for protocol processing and token lifecycle. Map claims deliberately between the two.

For passwordless/OTP/magic-link login:

- use one-time, short-lived, purpose-bound tokens;
- store only safe representations when persistence is necessary;
- rate-limit request and verification endpoints;
- prevent account enumeration;
- invalidate or consume tokens atomically;
- require a separate authenticated protocol exchange before issuing OAuth/OIDC tokens;
- test replay and concurrent redemption.

## Changes requiring extra review

- custom grant types;
- custom token endpoint handlers;
- disabling token encryption;
- long-lived refresh tokens;
- multi-tenant issuer/audience logic;
- external account linking;
- key rotation or migration;
- accepting tokens from multiple issuers;
- proxy-rewritten issuer or callback URLs.

For each, document the threat, compatibility requirement, control, and negative test.

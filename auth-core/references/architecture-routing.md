# Authentication architecture routing

Use this reference when selecting or changing the authentication architecture.

## Separate the layers

| Layer | Responsibility | Typical .NET component |
| --- | --- | --- |
| User store | Accounts, credentials, profile, roles, recovery | ASP.NET Core Identity or external directory |
| Local session | Browser login state and CSRF boundary | Protected HttpOnly cookie |
| Authorization server | OAuth/OIDC clients, grants, tokens, discovery, JWKS | OpenIddict, Duende, Keycloak, managed IdP |
| OIDC client | Redirect login and callback against an authority | ASP.NET Core OIDC handler or OpenIddict Client |
| Resource server | Validate access token and authorize API request | OpenIddict Validation or JWT Bearer handler |

Never describe ASP.NET Core Identity alone as an OIDC server.

## Decision guide

1. If only one server-rendered application needs local accounts, use Identity and cookies.
2. If an application only needs login through an existing provider, make it an OIDC client; do not host a new authorization server.
3. If multiple applications need one first-party issuer, SSO, standardized tokens, or machine clients, evaluate an established authorization server.
4. If the organization already owns an identity platform, integrate with it unless requirements justify another authority.
5. If the client is a browser SPA, evaluate BFF first. If tokens must reach the browser, minimize lifetime and storage exposure and document the threat trade-off.
6. If the client is native/mobile, use Authorization Code with PKCE and system-browser patterns; never embed a confidential client secret.
7. For machine access, prefer managed workload identity when available; otherwise constrain client credentials by audience, scope, lifetime, storage, and rotation.

## Provider choice

Compare providers using current requirements:

- protocol/profile support and conformance;
- license and production cost;
- operational ownership and availability needs;
- framework/runtime compatibility;
- key management, revocation, sessions, federation, and audit support;
- customization requirements;
- migration and vendor-lock-in cost;
- local legal, hosting, and supply-chain constraints.

Do not replace OpenIddict with Duende, or vice versa, merely because one has more agent skills.

## Required architecture output

Record:

- actors and client types;
- public versus confidential clients;
- issuer and token consumers;
- browser/session boundary;
- selected flows and scopes;
- user/tenant/resource authorization model;
- key and secret ownership;
- logout, revocation, and account-disable behavior;
- availability dependency if the authority is unavailable.

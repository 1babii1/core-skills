---
name: auth-core
description: "Orchestrate secure authentication and authorization in .NET: ASP.NET Core Identity, OAuth 2.0/OIDC, JWT, cookies, and OpenIddict, from architecture through hardening, testing, and production verification. Use when creating, changing, debugging, reviewing, or auditing login, registration, external providers, roles, permissions, claims, sessions, token issuance or validation, refresh tokens, service-to-service access, SSO, an authorization server, or protected APIs."
---

# Auth Core

Own the authentication and authorization outcome. Route to installed specialist skills, inspect the live code and dependency versions, consult current primary documentation, make authorized changes, and prove the resulting flows. Never require the user to invoke the cars one by one.

## Non-negotiable rules

- Treat authentication as a security boundary, not ordinary plumbing.
- Never invent an OAuth/OIDC protocol, JWT format, password scheme, token validator, signing algorithm, or cryptographic primitive.
- Separate four concerns explicitly: user store, login/session, authorization server, and resource-server validation.
- Preserve the project's established provider unless replacement is explicitly requested and justified.
- Prefer secure cookies for browser sessions and standards-based OAuth/OIDC for cross-application/API access.
- Use Authorization Code with PKCE for interactive public clients. Do not introduce implicit flow or resource-owner password credentials.
- Validate issuer, audience, signature, lifetime, allowed algorithms, client identity, redirect URIs, scopes, and authorization policies as applicable. Fail closed.
- Keep access tokens short-lived. Treat refresh tokens, authorization codes, cookies, client credentials, signing keys, and recovery tokens as secrets.
- Never read `.env`, `.env.*`, encrypted vaults, credential files, keychains, tokens, or secret values. Read `.env.example` only. Use `secrets-core` for secret handling.
- Do not log tokens, authorization codes, passwords, OTP values, cookies, client secrets, or sensitive claims.
- Do not weaken production security to make development or tests pass.
- Never claim that a flow is secure or complete without proportional negative and end-to-end verification.

## Establish the operating mode

Infer the narrowest mode that satisfies the request:

- **Design:** choose boundaries, flows, clients, stores, session model, and threat controls.
- **Implement:** make scoped code/configuration changes and add tests.
- **Debug:** reproduce and diagnose 401/403, redirect loops, invalid grants, claim mapping, cookie, token, discovery, or key failures. Do not implement a fix unless requested.
- **Audit:** inspect and report evidence without modifying code or external systems.
- **Harden:** review a working implementation against current security guidance, repair authorized issues, and verify regressions.

Before work, identify framework/runtime versions, application types, trust boundaries, clients, authority/issuer, token consumers, reverse proxies, deployment topology, user store, and existing authentication schemes. Read [architecture-routing.md](references/architecture-routing.md) when choosing or changing the architecture.

## Build the train

Read and apply only relevant installed skills. Keep one coordinated result.

| Car | Skill or reference | Include when |
| --- | --- | --- |
| ASP.NET authentication | `aspnetcore-authentication` | Cookies, schemes, OIDC clients, JWT validation, external providers, 401/redirect debugging |
| ASP.NET authorization | `aspnetcore-authorization` | Policies, scopes, claims, roles, permissions, resource-based access, 403 debugging |
| Protocol correctness | `oauth-oidc-protocols` | OAuth/OIDC flow selection, discovery, JWKS, PKCE, refresh, revocation, introspection |
| User management | Current Microsoft ASP.NET Core Identity documentation | Accounts, passwords, email confirmation, lockout, MFA, recovery, security stamps |
| OpenIddict | [openiddict.md](references/openiddict.md) plus current official OpenIddict docs | OpenIddict client, server, validation, token issuance, custom flows, external providers |
| Threat analysis | [threat-model.md](references/threat-model.md) | New auth boundary, new client/provider, material flow change, or security audit |
| Hardening | [security-hardening.md](references/security-hardening.md), `secrets-core`, `best-practices` | Implementation, audit, production readiness, or incident follow-up |
| Known defect classes | [defect-checks.md](references/defect-checks.md); `auth-service` when installed (authoritative) | Register/login/recovery, external providers, credential or email changes, step-up, key rotation, passwords, passkeys |
| Verification | [testing.md](references/testing.md), relevant .NET test skills, `playwright` | Every implementation/hardening task and auth-related regression |

Do not use Duende-specific skills or APIs for an OpenIddict project. `aspnetcore-authentication`, `aspnetcore-authorization`, and `oauth-oidc-protocols` are provider-neutral; skills named `identityserver-*`, `duende-*`, or `token-management` are conditional on actual Duende dependencies.

## Execute the workflow

### 1. Inventory the existing system

Inspect package manifests, startup/DI registration, authentication schemes, endpoint mapping, persistence models/migrations, client and scope seeding, reverse-proxy configuration, `.env.example`, tests, and deployment configuration. Search for Identity, OpenIddict, Duende, OpenID Connect, JWT bearer, cookies, authorization policies, claims, scopes, signing keys, external providers, and auth endpoints.

Produce a compact model:

```text
Actors/clients -> login/session -> authorization server -> tokens -> APIs/resources
```

Mark which component owns users, issues credentials, validates credentials, and makes authorization decisions. Detect ambiguous default schemes and duplicated auth stacks before changing anything.

### 2. Select the simplest correct architecture

Choose by need, not fashion:

- one server-rendered web application: Identity plus secure cookie is usually enough;
- application consuming an external identity provider: configure an OIDC client;
- protected API: validate tokens from a trusted authority and enforce policies;
- multiple first-party applications or SSO: use an established authorization server such as OpenIddict, Duende, Keycloak, or a managed provider;
- service-to-service access: use a constrained workload identity or client credentials where appropriate;
- browser SPA: prefer a BFF or another architecture that avoids long-lived browser-held tokens when feasible.

State trust boundaries and why the selected flow fits each client. Do not add an authorization server to a project that only needs local login.

### 3. Model authorization independently

Define resources and actions before claims. Prefer policy- and resource-based authorization over scattered role string checks. Distinguish:

- OAuth scopes: what a client may request;
- user permissions/roles: what the subject may do;
- resource ownership/tenant membership: what is allowed for this specific object;
- audience/resource: which API may accept the token.

Require explicit authorization by default. Test both authenticated-but-forbidden and unauthenticated cases.

### 4. Implement narrowly

Follow repository conventions and current official documentation for the detected package versions. Make small, reviewable changes. Configure exact redirect and post-logout URIs, client types, permitted grants, endpoints, scopes, resources, and claim destinations. Store production keys and credentials outside source control through the established secret system.

For OpenIddict, read [openiddict.md](references/openiddict.md) before editing. Do not translate Duende classes mechanically; map protocol concepts to OpenIddict APIs supported by the installed version.

### 5. Threat-model and harden

For new or materially changed flows, read [threat-model.md](references/threat-model.md), identify assets and trust boundaries, enumerate abuse cases, and connect each material threat to a control and test.

Apply [security-hardening.md](references/security-hardening.md), then walk [defect-checks.md](references/defect-checks.md) for every flow the change touches: those are failures that shipped in a real service, not generic advice. Pay particular attention to account enumeration, brute force, credential stuffing, CSRF, open redirects, login CSRF, token/code replay, refresh-token theft, claim confusion, issuer/audience confusion, cross-tenant access, session fixation, key exposure, unsafe logging, and proxy/header mistakes.

### 6. Verify from inside and outside

Read [testing.md](references/testing.md). Run build, static analysis, relevant unit/integration tests, and real HTTP/browser flows. Test success, rejection, expiry, reuse, tampering, wrong client, wrong audience, missing scope/permission, logout, and recovery behavior as applicable.

When a runnable UI exists, use `playwright` for the complete redirect/cookie/login/logout flow. Do not expose real secrets or bypass authorization in end-to-end tests.

### 7. Review production topology

Confirm external issuer and endpoint URLs, HTTPS enforcement, forwarded headers and trusted proxies, cookie domain/path/SameSite/Secure settings, CORS origins, data-protection/key persistence, signing-key availability and rotation plan, clock synchronization, rate limits, audit events, revocation/session behavior, and health/observability without secret leakage.

## Harness integration

When the repository has `.pi/laws/signals.md` (pi-engineering-harness), authentication and credential work is **high-risk** there: derive proof obligations from `.pi/laws/proof-obligations.md` (credential change, external identity linking, token/key lifecycle, step-up) and run the `independent-verifier` before calling the work complete. This skill owns the auth domain knowledge; the harness owns the evidence bar. Without the harness, the completion gate below still applies.

## Completion gate

Do not call the work complete until applicable statements are true:

- architecture and trust boundaries are explicit;
- authentication schemes and challenge/sign-in/sign-out behavior are unambiguous;
- redirect URIs, clients, grants, scopes, audiences, and claim destinations are least-privilege;
- resource authorization is enforced server-side and defaults closed;
- secrets and production keys are absent from source and logs;
- positive, negative, expiry, replay, and authorization tests cover the changed flow;
- every applicable row of [defect-checks.md](references/defect-checks.md) has a test that fails when the guard is removed;
- build and relevant automated checks pass;
- a real browser or HTTP flow has been exercised when runnable;
- production-only assumptions and unverified external dependencies are clearly reported.

## Completion response

Report the resulting auth architecture, material changes or findings, security controls, tests actually run, and remaining production assumptions. Prefer evidence over a generic security score. Mention specialist skills only when the user asks; otherwise describe the outcome.

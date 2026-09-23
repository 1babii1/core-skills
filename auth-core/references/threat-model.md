# Authentication threat model

Use for a new authentication boundary, new client/provider, material flow change, or security audit.

## Build the model

1. Draw actors, browser/native clients, backend, authority, external providers, APIs, stores, queues, caches, proxies, and administrators.
2. Mark trust boundaries and every location where credentials, codes, cookies, or tokens cross or persist.
3. List assets: accounts, sessions, refresh tokens, signing keys, client credentials, recovery channels, tenant data, roles, and audit evidence.
4. Enumerate abuse cases by attacker capability.
5. Map each material threat to prevention, detection, recovery, and a verification method.

## Minimum abuse cases

- account discovery, brute force, credential stuffing, and OTP flooding;
- stolen password, cookie, authorization code, access token, refresh token, client secret, or signing key;
- open redirect, callback manipulation, login CSRF, session fixation, and account-linking takeover;
- authorization-code or refresh-token replay and concurrent redemption;
- malicious or confused OAuth client requesting excessive access;
- wrong issuer, audience, algorithm, key, scope, tenant, or token type accepted;
- ID token accepted as access token;
- user disabled or permission removed while an old session/token remains valid;
- horizontal/vertical privilege escalation and cross-tenant access;
- external provider compromise or ambiguous identity mapping;
- proxy/host-header manipulation producing incorrect issuer or redirect URLs;
- secrets exposed through source, CI, logs, traces, analytics, crash dumps, or generated agent output;
- authorization server, database, cache, key store, DNS, or external provider unavailable.

## Decision record

For every high-impact threat, record:

| Field | Meaning |
| --- | --- |
| Asset/flow | What is at risk |
| Attacker | Required capability |
| Abuse path | Concrete sequence, not a generic label |
| Existing control | Evidence in code/configuration |
| Gap | Missing or uncertain protection |
| Change | Minimal mitigation |
| Test/monitor | How prevention or detection is proven |
| Residual risk | What remains and who accepts it |

Prioritize threats that cross trust boundaries or yield account takeover, signing authority, tenant escape, or persistent access.

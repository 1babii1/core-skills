# Auth defect checks

Failures found in a real ASP.NET Core Identity + OpenIddict service, each with the test that proves it
closed. Apply the ones that match the flow being changed; verify against the installed library versions,
not memory. When the repository has the `auth-service` skill (pi-engineering-harness), that skill is the
authoritative, versioned copy of this list and its proof obligations; this file is the short form for
repositories without it.

| Check | What breaks | Proof |
| --- | --- | --- |
| Enumeration on register | A framework duplicate-account error (`DuplicateUserName`/`DuplicateEmail`, code and message) passes through uncaught, so register answers differently for a taken address while login and forgot-password were written carefully. A database unique violation racing the framework's own pre-check surfaces as an unhandled 500. | Register an existing and an unknown address; status, body and rough timing match. Two concurrent registrations of one address end gracefully, not with a raw unique-violation exception. |
| Two throttles | Only a per-IP limit (attackers rotate IPs) or lockout that ignores second-factor and recovery-code failures. Lockout also becomes a way to lock a victim out. | Repeated wrong second-factor codes lock the account; recovery still works during lockout; lockout is time-boxed. |
| Credential change keeps old sessions | Password, 2FA, email, or passkey change rotates the security stamp but leaves server-side session records and refresh tokens valid, so another browser stays signed in. | Two sign-ins; change in one; the other's cookie and refresh token are rejected. |
| External identity linking | The provider's `email_verified` is not mapped (the stock Google handler does not) or missing counts as true; linking into an unconfirmed local account lets a squatter who pre-registered the victim's address with a known password keep access (account pre-hijacking); linking by email after the first link; first link skipping the local account's 2FA. | Unverified or absent flag refuses; an unconfirmed local account is taken over (password removed, address confirmed, stamp rotated) or refused; later sign-ins match on `sub`; a 2FA-enabled account gets the normal challenge on first link. |
| Step-up | A claim present only in OIDC access tokens cannot guard cookie-authenticated endpoints; a policy registered in one host and used by an attribute in another returns 500, not 403. | Denied and elevated paths both tested in every host that uses the attribute. |
| Key rotation | Retention counted from creation instead of from when the key stops being current; encryption keys (which protect refresh tokens) retired at signing-key age; cached options not invalidated so new tokens are issued but rejected; several instances each mint a key during a rolling deploy; private keys stored in plaintext. | Token issued before rotation validates after; new token carries a new `kid`; no restart; concurrent callers produce one key (remove the lock and watch the test fail); a database-only leak yields no usable signing key. |
| Data Protection key ring | Not persisted or shared, so every deploy signs users out and kills pending reset and confirmation links. | Restart or second instance accepts an existing cookie and reset link. |
| Passwords | Composition rules, forced periodic change, or a breached-password check with undefined behavior when the checker is unreachable. | NIST SP 800-63B policy; unreachable checker behavior chosen, documented, and tested (HIBP range API is k-anonymous: first 5 hex chars of the SHA-1, `Add-Padding: true`). |
| Passkeys/WebAuthn | Relying-party ID or origin taken from the request instead of configuration; reusable or long-lived challenges. | Challenge is single-use and expires; RP ID and origins come from configured public issuer. |
| Email change and deletion | No re-authentication, no confirmation at the new address, no notice to the old one, tokens not bound to the security stamp or reusable, deletion leaving sessions and downstream derived data. | Old address notified; reused token rejected; after deletion all sessions and tokens fail and a deletion event is published. |
| Recovery and admin paths | The main path is hardened but recovery or admin reset skips session revocation, audit event, or notification. | Same assertions as the main path, run through the recovery and admin entry points. |

Sources: NIST SP 800-63B, OWASP Authentication/Forgot Password/Session Management cheat sheets, RFC 9700,
OpenID Connect Core, W3C WebAuthn, Microsoft Research "Pre-hijacking Attacks on Web User Accounts"
(USENIX Security 2022).

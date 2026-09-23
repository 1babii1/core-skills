# Deep Links and Referrals

Use the correct surface: `start`, `startgroup`, `startapp`, or current documented equivalent.

- Keep payloads compact, opaque, versioned, and URL-safe.
- Store business context server-side and pass a random reference.
- Apply TTL and one-time consumption to account linking or other sensitive flows.
- Sign payloads when tampering changes meaning.
- Never embed secrets, PII, raw database IDs, authorization, or prices trusted by the server.
- Resolve attribution once using explicit rules; do not allow self-referral or repeated reward.
- Preserve the original source separately from later campaign touches.
- Make redemption/reward issuance transactional and idempotent.

Test malformed, expired, consumed, tampered, replayed, and cross-user payloads.

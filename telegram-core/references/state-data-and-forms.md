# State, Data, and Forms

Assign every datum one owner:

| Kind | Owner | Examples |
|---|---|---|
| Local UI | React state | open sheet, selected tab |
| Navigation | URL/Telegram launch parameter | route, `startapp`, referral reference |
| Form | React Hook Form + Zod | draft input, client validation |
| Remote state | TanStack Query | profile, catalog, order status |
| Small shared UI | scoped Zustand | client-only wizard/UI preference |
| Telegram runtime | Telegram SDK | theme, viewport, safe area, back/main button |
| Durable business state | PostgreSQL | user, conversation, order, entitlement, payment |
| Transient coordination | Redis when needed | rate limit, short lock, distributed cache |

Rules:

- Do not copy Query cache or Telegram SDK state into Zustand.
- Invalidating/refetching server state is safer than maintaining parallel client truth.
- Persist multi-step bot conversations if restart loss is unacceptable.
- Model conversation transitions explicitly; include version, expiry, and cancellation.
- Never use Redis as the sole record of a payment, entitlement, order, or audit event.
- Validate on both client and server. Zod improves UX; server validation protects trust boundaries.
- Scope query keys by authenticated identity and clear sensitive cache on logout/session replacement.

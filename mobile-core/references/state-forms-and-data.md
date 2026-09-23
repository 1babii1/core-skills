# State, forms, and remote data

Use the same ownership model as `frontend-core`, adjusted for navigation, device persistence, and offline behavior.

## Classification

| State kind | Default owner |
| --- | --- |
| Ephemeral interaction | `useState` or `useReducer` |
| Navigation and shareable screen input | Expo Router params |
| Form values, errors, dirty state | local state or React Hook Form |
| Server-owned remote data | TanStack Query |
| Stable subtree dependency | Context/provider |
| Small cross-tree client state | scoped Zustand store |
| Preferences and non-sensitive drafts | explicit key-value persistence |
| Sensitive credentials | SecureStore through `auth-core` |
| Durable relational/offline records | SQLite repository |
| Animation progress | Reanimated shared values |

Do not select a library until owner, lifetime, sensitivity, serialization, freshness, logout behavior, and offline semantics are known.

## TanStack Query

- Colocate query keys and options with the owning feature/domain.
- Include every fetch dependency in deterministic keys.
- Derive freshness and retries from business semantics; do not copy fixed examples.
- Connect online and focus managers to app lifecycle and network state when needed.
- Cancel obsolete requests through `AbortSignal`.
- Persist only the cache entries that improve recovery; persistence is not a local database or synchronization engine.
- Use optimistic updates only for reversible operations with reliable rollback or idempotent replay.
- Never duplicate query results into Zustand merely for access convenience.

## Zustand

Use for small shared client state such as theme preference, a temporary multi-step workflow, a client-only cart, or UI coordination across routes.

- Prefer feature-scoped stores over one universal store.
- Select the smallest state slice a component needs.
- Derive values rather than storing duplicates.
- Keep server and database-owned records out.
- For persistence, define a schema version, migration, partial serialization, hydration state, corrupt-data fallback, logout reset, and account-switch behavior.
- Never persist access tokens, refresh tokens, signing material, or unnecessary personal data.

Prefer local state until sharing is demonstrated.

## Forms and validation

- Use controlled local state for small forms and React Hook Form for complex validation, dynamic fields, multi-step flows, or performance-sensitive forms.
- Use Zod for runtime validation at untrusted boundaries and for shared form schemas when it improves clarity.
- Treat client validation as UX only; validate and authorize again on the server.
- Map server field errors without discarding user input.
- Prevent duplicate submissions and preserve drafts only when product semantics demand it.
- Test keyboard navigation, autofill, password managers, secure text fields, screen-reader labels, dynamic type, and submit behavior on both platforms.

## Networking

- Prefer the repository's established client; for new Expo apps prefer standards-based fetch APIs supported by the installed SDK.
- Model transport, timeout, cancellation, authentication, validation, domain, rate-limit, and offline errors distinctly.
- Retry only transient and safe operations. Use exponential backoff with jitter and a cap.
- Require idempotency keys or an equivalent server contract before replaying mutations.
- Never read environment files. Use names from `.env.example`; remember that every client-bundled value is public.

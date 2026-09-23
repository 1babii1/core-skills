# State and URL ownership

Read this reference before introducing or expanding state management.

## Classification

| State kind | Default owner |
| --- | --- |
| Ephemeral component interaction | `useState` or `useReducer` |
| Shareable navigation/filter state | route params or search params |
| Form fields/errors/dirty state | native form or React Hook Form |
| Server-owned remote data | framework server data/cache or TanStack Query |
| Stable dependency available to a subtree | Context/provider |
| Small cross-tree client state | Zustand |
| Persisted preferences/drafts | Explicit browser persistence, usually through a scoped store |

Do not select a library until the value's owner, lifetime, serialization, sharing, and freshness are known.

## URL state

Use the URL for search, filters, sorting, pagination, selected tabs, and other state that should support refresh, browser history, bookmarks, or link sharing.

Use native framework search params for simple cases. Use `nuqs` only when typed parsers, batched updates, server/client sharing, or complex query-state ergonomics justify it.

Do not put sensitive values or large payloads in URLs.

## TanStack Query

Use for server state that needs client refetch, polling, mutations, optimistic UI, infinite queries, or shared browser cache.

- Colocate query options and keys with the owning feature/domain.
- Include every fetch dependency in a deterministic key.
- Define freshness from business semantics.
- Cancel obsolete requests through `AbortSignal`.
- Prefer precise cache updates or invalidation.
- Use optimistic behavior only for reversible, low-risk interactions with a reliable rollback.
- Avoid duplicating the same resource in server cache, Query cache, and Zustand without an explicit synchronization design.

## Zustand

Use for small shared client state such as UI preferences, a client-only draft, a multi-step workflow, or an unauthenticated local cart.

- Scope stores by feature/domain rather than creating one universal store.
- Select the smallest value a component needs.
- Derive values instead of storing duplicates.
- Keep server state out.
- For persistence, define `partialize`, a schema version, migration, safe fallback, and hydration behavior.
- Never persist access tokens, refresh tokens, secrets, or unnecessary personal data.
- Reset user-scoped state on logout/account change.

Prefer local state until sharing is demonstrated.

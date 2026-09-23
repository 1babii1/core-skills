# Caching strategy

Use when deciding what to cache, for how long, and how it becomes correct again. Redis mechanics live in `redis-core`, `redis-connections`, `redis-security`, and `redis-observability`; this reference covers the policy those skills implement.

## Earn the cache

- Measure and optimize the underlying query first. A cache in front of a missing index hides the defect and multiplies the cost of every invalidation bug.
- State the problem being solved: latency, database load, an external rate limit, or cost. If none can be named with a number, do not add a cache.
- Prefer the cheapest layer that solves it: a better query, an HTTP cache header, an in-process memory cache with a short TTL, then a distributed cache. Each step adds a consistency problem.
- A single-instance application usually does not need Redis. Introduce it when instances must share state, or when the data outlives the process.

## Define every cached value

Nothing enters a cache without answers to all five:

1. **Key.** Full shape, including tenant, locale, user, and version segments. A key that omits a variable that affects the value is a leak.
2. **Owner.** The one place that writes it and the one place that invalidates it.
3. **Staleness tolerance.** How wrong this value may be, in seconds, before a user is harmed. Prices, permissions, and balances usually tolerate nothing.
4. **Invalidation trigger.** The write that makes it wrong. TTL alone is expiry, not invalidation.
5. **Miss and outage behavior.** What happens when the entry is absent, and what happens when the cache itself is unreachable.

## Correctness rules

- Never cache authorization decisions, permission sets, or anything a security check reads, unless the invalidation path is exact and tested. A revoked user reading a cached permission is an incident.
- Include a version or schema segment in the key so a deploy that changes the shape cannot deserialize an old value into a new type.
- Namespace by tenant and by user where relevant. Cross-tenant cache bleed is a data breach, and it looks like a caching bug in review.
- Prefer delete-on-write over update-on-write. Writing the new value into the cache from two places will eventually write the wrong one.
- Accept eventual consistency explicitly, in the response contract or the UI, rather than pretending a stale read is fresh.
- Do not cache errors, empty results, or partial failures unless negative caching is deliberate and short — and say so in the key naming.

## Failure modes to design for

- **Stampede.** Many concurrent misses on a hot key hit the database at once. Use a short lock or single-flight per key, or stagger TTLs with jitter so a batch of entries does not expire together.
- **Unavailable cache.** A cache outage must degrade to slower, not to broken. Set explicit connect and read timeouts, treat cache failure as a miss, and never let it surface as a request error.
- **Unbounded growth.** Set a maxmemory policy and know which eviction policy is configured. An unbounded cache becomes an outage on a schedule you did not choose.
- **Thundering invalidation.** A single write that clears thousands of keys can be worse than no cache. Scope invalidation to the keys actually affected.
- **Hot key.** One key serving a disproportionate share of traffic can saturate a single node. Detect it in `redis-observability` metrics before it becomes a limit.

## Verification

- Prove the hit ratio and the latency change against the baseline captured before the cache existed.
- Test invalidation with a behavioral test: write, then read, and assert the new value — not a code review of the invalidation call.
- Test the outage path by making the cache unreachable and confirming the application still serves correct, slower responses.
- Confirm no personal data, token, or secret is stored in a cache that outlives the request or lacks the same protection as the source store.

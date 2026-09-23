# Evidence-driven .NET performance

Use for performance requests and broad production audits.

## Method

1. Define the user/business operation, workload, data shape, concurrency, hardware/container limits, runtime mode, and target SLO.
2. Capture baseline latency distributions, throughput, errors, CPU, memory/GC, allocations, database/query metrics, and downstream time.
3. Locate the dominant constraint with traces, profiles, counters, logs, query plans, or controlled experiments.
4. Change one meaningful bottleneck at a time.
5. Repeat the same measurement and check correctness/resource trade-offs.

## Investigation order

- unnecessary network/database round trips and N+1 queries;
- missing indexes, unbounded data, poor pagination, or large payloads;
- blocking I/O, thread-pool starvation, lock/contention, and excessive fan-out;
- serialization and allocation pressure, large-object-heap behavior, and GC pauses;
- cache hit ratio, stampede, serialization cost, and invalidation;
- connection-pool exhaustion and timeout/retry amplification;
- hot-path LINQ, regex, string, collection, reflection, and logging overhead;
- JIT/AOT/vectorization/micro-optimizations only after higher-level costs are excluded.

## Rules

- Benchmark Release builds with representative data and warmup; separate cold start from steady state.
- Do not compare different frameworks, ORMs, SQL strategies, payloads, or safety semantics as if language alone caused the result.
- Do not add caching without freshness, invalidation, memory, failure, and observability contracts.
- Avoid pooled/manual-memory complexity unless profiles show durable benefit and tests prove ownership safety.
- Record before/after values and methodology; label microbenchmarks separately from end-to-end results.

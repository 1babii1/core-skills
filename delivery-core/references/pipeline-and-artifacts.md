# Pipeline and artifact rules

Use this reference when designing or implementing CI/CD, containers, artifact promotion, or release strategies.

## Required ordering

1. Resolve repository instructions, supported runtime, dependency locks, and target.
2. Restore dependencies deterministically.
3. Build once in release mode.
4. Run analyzers, tests, dependency checks, static analysis, and artifact scanning.
5. Produce an immutable artifact or image identified by version and commit.
6. Publish to a registry with restricted write access.
7. Deploy that exact artifact to preview or staging.
8. Run migration preparation and staging verification.
9. Promote the same artifact to production after required approval.
10. Verify runtime behavior and telemetry; stop or roll back on defined failure signals.

Do not rebuild at the production stage. Record artifact digests when the registry exposes them.

## GitHub Actions

Use `github-actions-templates` for semantic pipeline implementation and `authoring-github-workflows` for workflow syntax and `actionlint` validation.

- Pin third-party actions to an immutable commit SHA when the repository policy supports it.
- Set explicit job and workflow permissions.
- Separate untrusted pull-request validation from jobs that can access deployment credentials.
- Use protected environments for production approvals and environment-scoped credentials.
- Prevent concurrent production releases when ordering matters.
- Set timeouts and retain only useful non-sensitive artifacts.
- Never echo environment state, tokens, connection strings, signing material, or generated secret files.

## Containers

Apply `devops-engineer` and the stack-specific reference.

- Use a multi-stage build.
- Copy only required runtime output.
- Run as a non-root user.
- Handle `SIGTERM` and allow in-flight work to drain.
- Keep secrets out of build arguments and layers.
- Use a read-only filesystem when compatible; mount only required writable paths.
- Define resource expectations and avoid unbounded local logs.
- Scan the final image and generate an SBOM when supported by trusted project tooling.
- Test the image with the same entry point, port, and runtime configuration shape used in production.

## Rollout selection

- Use a simple restart for low-risk, low-traffic systems where brief documented downtime is acceptable.
- Use rolling deployment only when old and new versions can overlap safely.
- Use blue-green when a fast traffic switch and retained prior environment justify double capacity.
- Use canary only when traffic splitting and automated health metrics can make a real promotion decision.

Never label a rollout zero-downtime without testing connections, sessions, migrations, jobs, caches, streaming, and version skew.

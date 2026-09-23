# .NET deployment adapter

Use for ASP.NET Core APIs, web applications, SignalR/gRPC services, workers, and scheduled .NET processes. Apply `aspnet-core`, `devops-engineer`, `authoring-github-workflows`, and `configuring-opentelemetry-dotnet`.

## Choose the publish model

- Prefer framework-dependent deployment when the target supplies the exact supported .NET runtime and smaller artifacts matter.
- Use self-contained deployment when runtime independence justifies the larger artifact.
- Use a container for a portable Linux PaaS/VPS path, consistent runtime dependencies, and reproducible promotion.
- Consider Native AOT only after compatibility and measured startup/memory benefits are demonstrated.
- Respect the repository's target framework and SDK pin. For new work, verify the current supported/LTS choice against Microsoft documentation.

Publish in Release mode and test the publish output, not only `dotnet run`.

## Runtime and proxy requirements

- Bind Kestrel to the platform-provided interface and port without hard-coding a secret or environment-specific URL.
- Configure forwarded headers only for known proxies/networks. Verify scheme, host, client IP, redirects, secure cookies, and OIDC callback URLs through the real proxy.
- Persist ASP.NET Core Data Protection keys when cookies, antiforgery, Identity, or other protected state must survive restart or scale-out. Protect the key store appropriately.
- Separate liveness from readiness. Readiness may include only dependencies whose absence must remove the instance from traffic.
- Propagate cancellation and drain HTTP requests and background work on `SIGTERM`.
- Verify WebSocket, SignalR, gRPC, large uploads, response streaming, and request limits when used.
- Set production logging levels and prevent sensitive data, tokens, claims, connection strings, and personal data from entering logs or traces.

## Containers

- Build/publish with the pinned SDK image and run on the corresponding supported ASP.NET runtime image.
- Use the platform's non-root runtime conventions or create a dedicated non-root user.
- Copy published output only.
- Do not place NuGet credentials, package feeds, certificates, or `.env` files in image layers.
- Validate architecture compatibility (`amd64` or `arm64`) with the target.
- Expose/document the application port; do not rely on `EXPOSE` as a firewall.

## EF Core release

- Generate and review migrations in source control.
- Prefer a reviewed migration bundle or dedicated release job for production.
- Never start automatic migration from every application replica.
- Test the migration against a production-like schema and representative volume.
- Use expand/backfill/contract for changes that must coexist with old and new versions.
- Create indexes using database-appropriate online/concurrent behavior when availability requires it.
- Treat destructive column/table changes and irreversible data transformations as explicit cutovers.
- Prefer roll-forward when a down migration would discard new data.

## Release verification

- Run restore, build, analyzers, tests, publish, and package vulnerability checks supported by the repository.
- Start the published artifact/container with placeholder configuration shaped from `.env.example`.
- Verify health/readiness, representative API behavior, auth redirects, database connectivity, background workers, and graceful shutdown.
- Confirm `service.name`, `service.version`, and deployment environment telemetry attributes without exposing sensitive values.

Primary references:

- https://learn.microsoft.com/aspnet/core/host-and-deploy/
- https://learn.microsoft.com/dotnet/core/deploying/
- https://learn.microsoft.com/ef/core/managing-schemas/migrations/applying

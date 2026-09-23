# Next.js deployment adapter

Use for Next.js applications. Apply `devops-engineer`, `deployment-pipeline-design`, browser verification, and the official documentation for the repository's installed Next.js version.

## Select the runtime shape

- Use static export only when every required route and feature is compatible with static output.
- Use a Node.js server or container when Server Components, dynamic rendering, Route Handlers, Server Actions, ISR, image optimization, streaming, or other runtime features require it.
- Prefer `output: "standalone"` for a compact self-hosted Node container when compatible with the repository.
- Use a provider adapter only after verifying current feature fidelity for the installed Next.js version.

Do not silently convert a dynamic application to static export to simplify hosting.

## Configuration boundary

- Treat `NEXT_PUBLIC_*` values as public and build-time inlined. They must never contain secrets.
- Keep private runtime configuration server-side.
- Build one image that can be promoted between environments where framework semantics permit runtime configuration.
- Read names from `.env.example` only; never inspect Next.js `.env*` files.

## Self-hosting

- Put a hardened reverse proxy such as Nginx in front of the Node server on a VPS.
- Preserve streaming end to end; disable proxy buffering where required and verify with a real streamed response.
- Use the production server entry point and handle `SIGTERM` with an adequate drain period.
- Include `sharp` when the selected self-hosted image-optimization path requires it.
- Verify server action request limits, uploads, WebSocket-like connections used by dependencies, image routes, and cache headers.

## Cache and multiple instances

- A single persistent instance may use the default local cache when its durability matches requirements.
- Multiple instances or ephemeral filesystems require an intentional shared cache and tag-invalidation strategy for ISR and cached server output.
- Use a consistent deployment/build identity across instances in one release.
- Test rolling-version skew, static asset consistency, server actions, revalidation, and CDN behavior before claiming safe rolling deployment.

## Verification

- Run the repository's locked install, lint, type check, tests, and production build.
- Start the production artifact/container rather than relying on the development server.
- Exercise static and dynamic routes, authentication, server actions, image optimization, ISR/revalidation, error boundaries, streaming, and critical Playwright journeys that exist.
- Inspect browser console, server logs, status codes, cache headers, and production telemetry.

Primary references:

- https://nextjs.org/docs/app/getting-started/deploying
- https://nextjs.org/docs/app/guides/self-hosting
- https://nextjs.org/docs/app/guides/deploying-to-platforms

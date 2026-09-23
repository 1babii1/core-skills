# Backend security and supply chain

Use for secure implementation, audits, dependency changes, and production readiness. Pair with `auth-core` and repository-grounded threat modeling.

## Application boundaries

- Validate and normalize untrusted input once at the correct boundary; parameterize database access.
- Enforce authorization server-side against the real tenant/resource; never trust client-side hiding or supplied owner IDs.
- Prevent mass assignment by using explicit request contracts and allowed field mappings.
- Protect outbound fetches from SSRF with scheme/host/address policy, redirect handling, DNS/rebinding awareness, and network egress controls where warranted.
- Treat file names, MIME types, archives, parsers, templates, and deserialization input as hostile. Bound size/depth/count and isolate risky processing.
- Avoid unsafe polymorphic deserialization, dynamic code execution, shell interpolation, and untrusted format strings.
- Return minimal production errors and redact sensitive structured-log fields.
- Rate-limit abuse-prone and expensive operations by the identity/key/resource that represents actual cost.

## Multi-tenancy

- Resolve tenant identity from trusted authentication/context, not an arbitrary request field alone.
- Apply tenant filters and resource authorization at every data-access path, including jobs and admin tools.
- Test cross-tenant IDs, enumeration, indirect references, caches, search indexes, exports, queues, and object storage.
- Define privileged support/admin access with auditability and least privilege.

## Dependencies and build

- Pin and centrally manage package versions where the repository supports it.
- Run SDK/package vulnerability checks and review transitive findings, exploitability, and upgrade impact.
- Remove unused packages and avoid abandoned/untrusted libraries for trivial functionality.
- Treat package scripts, source generators, analyzers, containers, actions, and build tools as executable supply-chain dependencies.
- Pin CI actions/container images appropriately and minimize workflow permissions.
- Produce/review lock files or dependency manifests where applicable; generate an SBOM when delivery requirements justify it.

## Semgrep gate

1. Detect an existing repository Semgrep configuration and preserve trusted local rules.
2. Prefer a pinned local CLI/container and C#/.NET-relevant official or reviewed rules.
3. Scan changed code for focused work and the relevant repository for broad audits.
4. Triage findings by reachable data flow and impact; do not mass-suppress.
5. Add narrow documented suppressions only after proving false-positive status.
6. Report command, rules/config, scope, version, findings, and limitations.

If Semgrep is unavailable, do not download or execute an unreviewed binary silently. Report the missing gate and continue with analyzers, package audit, tests, and manual evidence.

## Security completion

Require threat/control/test linkage for high-impact findings. Static tools complement but do not replace auth, business-authorization, concurrency, and deployment reviews.

# Error states, resilience, and browser security

Read this reference for failure behavior, browser trust boundaries, or production readiness.

## UI state matrix

Consider applicable states:

- idle;
- loading or streaming;
- success;
- empty;
- stale;
- offline;
- validation error;
- unauthorized;
- forbidden;
- not found;
- conflict;
- rate limited;
- partial success;
- recoverable dependency failure;
- unexpected failure.

Do not show a spinner forever or collapse every failure into “Something went wrong.” Give a safe next action.

## Resilience

- Cancel obsolete work after navigation or changed parameters.
- Use bounded timeouts where a request can hang.
- Retry only safe transient operations and honor server retry guidance.
- Use exponential backoff with jitter for reconnect loops.
- Isolate widget/route failures with appropriate error boundaries.
- Make optimistic changes reversible.
- Avoid turning telemetry failure into product failure.
- Preserve stale usable data when product semantics allow it and label its state.
- Design WebSocket/SSE reconnect, duplicate-event, ordering, and resynchronization behavior explicitly.

## Browser security

Review:

- unsafe HTML, DOM injection, URL construction, and markdown rendering;
- redirects and external links;
- third-party scripts and widgets;
- CSP and Trusted Types where justified;
- storage of credentials or personal data;
- `postMessage`, iframe, clipboard, camera, location, and file APIs;
- source maps and debug output;
- client-exposed configuration;
- CSRF/session behavior with `auth-core`;
- dependency and supply-chain risk.

Treat all code and values shipped to the browser as public. Hiding a control is not authorization.

Never inspect real secret files. Use `.env.example` to verify public/private variable naming and runtime contracts.

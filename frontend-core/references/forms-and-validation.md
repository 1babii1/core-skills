# Forms and validation

Read this reference for form design, RHF, Zod, or server validation.

## Tool selection

Use a native form and `FormData` for a small, mostly independent submission. Use React Hook Form when field count, conditional sections, controlled widgets, arrays, performance, or client-side workflow complexity justifies it.

Use Zod for runtime validation where it fits the repository. Do not add it only to restate compile-time types.

## Ownership

- Keep form state inside the form.
- Keep UI-only state such as popover visibility local.
- Keep submitted server state in the server/TanStack owner after success.
- Do not mirror all fields into Zustand.
- Derive TypeScript types from the schema when the schema is authoritative.
- Distinguish `z.input` and output types when transforms/coercion exist.

## Behavior

- Provide complete initial/default values.
- Use semantic labels, descriptions, grouping, fieldset/legend, and accessible error association.
- Preserve keyboard and focus behavior.
- Surface field validation and a form-level server failure.
- Prevent accidental duplicate submission.
- Preserve intentional user input after recoverable server errors.
- Confirm destructive or irreversible actions.
- Handle upload size/type/progress/cancellation when files exist.
- Do not disable submission solely because the client has not yet computed validity; provide understandable validation feedback.

## Trust boundary

Client validation is an enhancement. Repeat authoritative validation and authorization on the server. Never trust hidden fields, disabled controls, client totals, role values, prices, resource IDs, or upload metadata.

## States to test

Test applicable pristine, dirty, invalid, submitting, server validation error, authorization error, network failure, duplicate click, success, reset, and navigation-away states. Include keyboard and mobile behavior.

Use `react-hook-form-audit` only for an explicit audit or significant RHF review.

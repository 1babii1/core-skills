# User Help and Release Documentation

## Choose by reader intent

- **Tutorial:** learning-oriented path to a first result.
- **How-to:** goal-oriented steps for a known task.
- **Reference:** precise facts, options, fields, and limits.
- **Explanation:** concepts, rationale, and mental model.
- **Troubleshooting:** symptom-led diagnosis and recovery.
- **FAQ:** concise answer to a repeated question.
- **Known issue:** current impact, status, workaround, and updates.

Do not force every article to perform all roles.

## User-help standard

- Use the reader's words and observable UI labels.
- State audience, product/version, prerequisites, permissions, and impact.
- Begin with the desired result or symptom.
- Give numbered actions with expected results.
- Separate safe workaround from permanent resolution.
- Explain data loss, billing, permission, or availability consequences before the action.
- Provide a “still blocked” path with the minimum diagnostic information needed.
- Link to canonical reference rather than duplicating it.

Screenshots support text but are not the only instruction. Keep them current, crop sensitive data, add useful alt text, and avoid exposing accounts, personal information, internal URLs, or tokens.

## Known issues

Include:

- verified status and affected versions/platforms;
- symptoms and scope;
- safe workaround and limitations;
- fix state without an invented date;
- update history and owner;
- resolved version and migration/retry steps.

Publishing or changing a public status is an external action requiring authorization.

## Release notes

Write for the affected reader, not from raw commit messages:

- version/date and availability;
- user-visible additions, changes, fixes, and removals;
- breaking changes and exact migration action;
- security information at a safe disclosure level;
- known limitations;
- links to detailed guides and API changes.

Do not list internal refactors as features. Do not claim a fix from a commit alone; verify release inclusion and behavior.

## Deprecation

Document:

- deprecated capability and affected versions;
- supported replacement;
- compatibility and migration steps;
- dates only when approved;
- telemetry or evidence used to assess migration;
- support path and final removal confirmation.

Keep old search terms and error text discoverable during the migration window.

## Accessibility and localization

- Use meaningful headings, link labels, tables, and alt text.
- Do not communicate warnings by color alone.
- Keep sentence structure translatable and avoid unexplained idioms.
- Distinguish locale-specific legal, payment, date, number, and platform behavior.
- Route a full accessibility review through `accessibility` when documentation delivery format is in scope.

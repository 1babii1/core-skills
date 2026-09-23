# API Version and Capabilities

Telegram evolves quickly. Before using a recent field or method:

1. Inspect the repository's resolved `Telegram.Bot` package version.
2. Check the current official Bot API changelog and method/object documentation.
3. Confirm the library exposes the feature and note any naming/model differences.
4. Add runtime capability/version checks for Mini App features.
5. Provide a graceful fallback when older clients or unavailable surfaces are supported.

Primary sources:

- <https://core.telegram.org/bots/api-changelog>
- <https://core.telegram.org/bots/api>
- <https://core.telegram.org/bots/webapps>
- <https://core.telegram.org/bots/payments-stars>
- <https://telegrambots.github.io/book/>
- <https://www.nuget.org/packages/Telegram.Bot>

Third-party skills are conceptual guidance, not a frozen API specification. Official current documentation and the installed SDK are authoritative.

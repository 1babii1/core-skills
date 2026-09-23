# core-skills

Personal orchestration skills for Claude Code and Codex. Each `*-core` skill owns one domain end to
end (backend, frontend, auth, data, delivery, product, SEO, ...) and routes to narrower specialist
skills ("cars") when they are installed.

## Relationship to pi-engineering-harness

- [pi-engineering-harness](https://github.com/1babii1/pi-engineering-harness) is project-scoped and
  owns **how decisions are made and proven**: engineering laws, signals, proof obligations,
  verification, hooks, audits, project context.
- `core-skills` is user-scoped and owns **domain knowledge and implementation**: how to do X well.
- One rule, one owner. Where both cover a topic, one side links to the other instead of copying it.

## Install

Skills are loaded from the agent's skills directory, so link each one in:

```bash
for s in ~/homework/core-skills/*-core; do
  ln -sfn "$s" ~/.claude/skills/"$(basename "$s")"
  ln -sfn "$s" ~/.codex/skills/"$(basename "$s")"
done
```

Specialist skills referenced as cars (`aspnet-core`, `redis-core`, `dotnet-webapi`, ...) are
third-party and are not part of this repository; install them from their own sources.

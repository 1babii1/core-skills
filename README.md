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

## Quality gate

```bash
python3 scripts/check.py
```

Fails on: a description over 500 characters (every description is loaded into every session), a
description that does not say when to use the skill, a `name` that differs from its directory, a
`SKILL.md` over 200 lines, a broken relative link, an unread `references/` file, or a credential-shaped
string. Run it before each commit.

## Conventions

- Keep `SKILL.md` an orchestrator: mode, cars (specialist skills), workflow, completion gate. Put
  detail in `references/` and link it so it loads on demand.
- Add knowledge only when it comes from a verified failure (an incident, a test that caught a defect,
  a review finding), with the test that proves it closed. Generic advice the model already follows
  does not earn a line.
- Engineering skills end with a **Harness integration** section: when the repository has
  `.pi/laws/signals.md`, this skill supplies domain knowledge and pi-engineering-harness supplies the
  proof-obligation and independent-verifier bar. Do not copy harness text; point to it.

---
name: secrets-core
description: Establish and maintain safe secret-management conventions for new and existing projects using a local SOPS plus age vault, environment-variable contracts, CI/CD secret stores, and GitHub Packages/NuGet authentication. Use when initializing a project, adding API keys or private package access, creating env templates, configuring deployment or CI secrets, checking for leaked credentials, or deciding how an agent may interact with secrets.
---

# Secrets Core

Manage secret names and delivery paths without exposing secret values to the model, repository, logs, or command history.

## Non-negotiable boundary

- Read `.env.example` as the canonical environment contract.
- Never read, display, summarize, copy, diff, search inside, or edit `.env`, `.env.*`, secret exports, credential files, keychains, or secret-manager values. The only exception is an explicitly public example such as `.env.example`.
- Never ask the user to paste a token into chat.
- Never put a secret value in a tool argument, source file, patch, shell history, log, issue, commit, or final response.
- Let `~/.local/bin/secrets-run` or the deployment platform inject values directly into the target process.
- If a value must be entered, direct the user to an interactive secret-manager or provider UI.
- Treat automated scanners as allowed to inspect bytes locally only when they report filenames/rule IDs and never matching values.

## Project initialization

1. Inspect only safe files: `.env.example`, `.gitignore`, manifests, CI definitions, deployment configuration, and documentation.
2. Run `scripts/init-project.sh <project-root>` or reproduce its minimal changes with the repository's conventions.
3. Keep `.env.example` committed and fill it with variable names, harmless defaults, and concise comments only.
4. Ignore every real env variant while explicitly allowing `.env.example`.
5. Separate shared development secrets from per-project secrets and keep production isolated.

Use this global vault layout:

```text
~/.local/share/secrets-core/
├── github-nuget.enc.json
├── shared-tools.enc.json
└── <project-slug>-dev.enc.json
```

Keep the age identity at `~/.config/sops/age/keys.txt`; never read it. Back it up offline because losing it makes the vaults unrecoverable. Prefer runtime injection:

```bash
~/.local/bin/secrets-run <vault-name> -- <command>
```

Let the user add or rotate values interactively with `~/.local/bin/secrets-edit <vault-name>`. Never invoke `secrets-edit` autonomously and never inspect its editor or decrypted temporary content.

Do not export a plaintext `.env` unless a tool has no runtime-injection option, and remove such a temporary file immediately after use.

## GitHub Packages / NuGet

Read `references/github-nuget.md` when a .NET project consumes or publishes GitHub Packages.

- Use owner `1babii1`, source name `github`, and `https://nuget.pkg.github.com/1babii1/index.json` unless the project specifies another owner.
- Keep only the package source in repository `NuGet.Config`; never store credentials there.
- Store `GITHUB_NUGET_USERNAME` and `GITHUB_NUGET_TOKEN` in encrypted vault `github-nuget`.
- Use a classic GitHub PAT with `read:packages` for restore. Add `write:packages` only for local publishing. Add `repo` only when private repository inheritance actually requires it.
- In GitHub Actions, prefer the workflow `GITHUB_TOKEN` with explicit `packages: read` or `packages: write`; use a PAT only for cross-repository packages that are not granted workflow access.
- Deliver NuGet credentials through environment variables at command runtime.

## Agent and tool access

- Launch applications with only the paths they require.
- Do not launch Claude, Codex, an IDE, or a general shell with all project or production secrets injected.
- If an MCP server needs one key, inject only that key into that MCP process or its parent agent session.
- Prefer short-lived credentials and OIDC over long-lived cloud keys when supported.

## Enforcement

Rules in text are only followed, not enforced. In a repository with pi-engineering-harness installed for Claude Code (`install.sh --agent claude`), a PreToolUse hook (`.harness/hooks/guard-secrets.py`) blocks Read/Edit/Write/Grep/Glob/Bash access to env files (except `.env.example`), `*.enc.json|yaml`, age and private keys, and shell environment dumps. It is defense in depth, not a sandbox: it works on command text, so it also blocks a command that merely mentions such a path (a commit message, an `echo`); write the script to a file with the Write tool and run that instead of inlining the path. Add project-specific patterns in `.pi/project/secret-patterns.txt`. Keep real permissions underneath it.

## Verification

Run `scripts/audit-project.sh <project-root>`. Fix failures without opening secret files. Confirm:

- `.env.example` exists;
- real env files are ignored;
- no real env file or credential-bearing NuGet config is tracked;
- required names appear in `.env.example`;
- CI refers to secret contexts instead of literals;
- commands can run with runtime-injected values without printing them.

Report only names, paths, scopes, and verification outcomes. Never report secret values.

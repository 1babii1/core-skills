#!/usr/bin/env bash
set -euo pipefail

project_root="${1:-$PWD}"
cd "$project_root"
status=0

pass() { printf 'PASS: %s\n' "$1"; }
fail() { printf 'FAIL: %s\n' "$1"; status=1; }

[[ -f .env.example ]] && pass '.env.example exists' || fail '.env.example is missing'
[[ -f .gitignore ]] || fail '.gitignore is missing'

if [[ -f .gitignore ]] && grep -Fqx '.env' .gitignore && grep -Fqx '.env.*' .gitignore && grep -Fqx '!.env.example' .gitignore; then
  pass 'real env files are ignored and .env.example is allowed'
else
  fail '.gitignore env rules are incomplete'
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  tracked_env="$(git ls-files | grep -E '(^|/)\.env($|\.)' | grep -vE '(^|/)\.env\.example$' || true)"
  if [[ -z "$tracked_env" ]]; then
    pass 'no real env file is tracked'
  else
    while IFS= read -r file; do printf 'FAIL: tracked secret-like env file: %s\n' "$file"; done <<< "$tracked_env"
    status=1
  fi

  credential_configs="$(git ls-files '*[Nn]u[Gg]et.[Cc]onfig' | while IFS= read -r file; do
    [[ -f "$file" ]] || continue
    if grep -E '<add key="ClearTextPassword"' "$file" | grep -qv '%' || grep -Eq '<add key="Password"' "$file"; then
      printf '%s\n' "$file"
    fi
  done)"
  if [[ -z "$credential_configs" ]]; then
    pass 'tracked NuGet configs contain no obvious literal credentials'
  else
    while IFS= read -r file; do printf 'FAIL: credential-bearing NuGet config: %s\n' "$file"; done <<< "$credential_configs"
    status=1
  fi
fi

exit "$status"

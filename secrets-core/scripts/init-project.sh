#!/usr/bin/env bash
set -euo pipefail

project_root="${1:-$PWD}"
if [[ ! -d "$project_root" ]]; then
  printf 'ERROR: project directory does not exist: %s\n' "$project_root" >&2
  exit 1
fi

skill_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
env_example="$project_root/.env.example"
gitignore="$project_root/.gitignore"

if [[ ! -e "$env_example" ]]; then
  cp "$skill_root/assets/env.example.template" "$env_example"
  printf 'CREATED .env.example\n'
else
  printf 'KEPT .env.example\n'
fi

touch "$gitignore"
for rule in '.env' '.env.*' '!.env.example'; do
  if ! grep -Fqx "$rule" "$gitignore"; then
    printf '%s\n' "$rule" >> "$gitignore"
  fi
done
printf 'UPDATED .gitignore\n'

if find "$project_root" -maxdepth 2 \( -name '*.sln' -o -name '*.csproj' -o -name '*.fsproj' \) -print -quit | grep -q .; then
  if [[ ! -e "$project_root/NuGet.Config" && ! -e "$project_root/nuget.config" ]]; then
    cp "$skill_root/assets/NuGet.Config.template" "$project_root/NuGet.Config"
    printf 'CREATED NuGet.Config without credentials\n'
  fi
fi

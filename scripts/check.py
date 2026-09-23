#!/usr/bin/env python3
"""Consistency checks for the *-core skills in this repository. Standard library only.

  scripts/check.py            run every check, exit 1 on any error

Checks (each is something that silently degrades a skill if it drifts):
  frontmatter     SKILL.md has name (== directory) and a description
  description     valid YAML (a plain scalar cannot contain ': ' - the skill would not load), <= 500 chars (every description is loaded into every session's context) and says
                  when to use the skill ("Use when ..." / "Use for ...")
  links           every relative markdown link in SKILL.md and references/ resolves
  orphans         every references/*.md is linked or mentioned by path in SKILL.md (else it is never read)
  size            SKILL.md <= 200 lines (long detail belongs in references/, loaded on demand)
  secrets         no obvious credential material committed (key/token shapes)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESCRIPTION_MAX = 500
SKILL_LINES_MAX = 200
SECRET_SHAPES = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|"
    r"xox[bap]-|AIza[0-9A-Za-z_-]{30,}|AGE-SECRET-KEY-)"
)
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def main() -> int:
    errors: list[str] = []
    skills = sorted(p for p in ROOT.glob("*-core") if p.is_dir())
    if not skills:
        print("no *-core skills found", file=sys.stderr)
        return 1

    for d in skills:
        name = d.name
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{name}: SKILL.md missing")
            continue
        text = skill_md.read_text()
        fm = frontmatter(text)

        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name is {fm.get('name')!r}, expected {name!r}")
        raw = re.search(r"^description:[ \t]*(.*)$", text, re.M)
        if raw:
            value = raw.group(1)
            if value and value[0] not in "\"'" and (": " in value or " #" in value or value[0] in "[]{}&*!|>%@`"):
                errors.append(f"{name}: unquoted description is not valid YAML (contains ': ' or ' #'); wrap it in double quotes")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{name}: description missing")
        else:
            if len(desc) > DESCRIPTION_MAX:
                errors.append(f"{name}: description is {len(desc)} chars (max {DESCRIPTION_MAX})")
            if not re.search(r"\buse (when|for)\b", desc, re.I):
                errors.append(f"{name}: description does not say when to use the skill ('Use when ...')")

        n_lines = text.count("\n") + 1
        if n_lines > SKILL_LINES_MAX:
            errors.append(f"{name}: SKILL.md is {n_lines} lines (max {SKILL_LINES_MAX}); move detail to references/")

        linked: set[Path] = set()
        for md in [skill_md, *sorted((d / "references").glob("*.md"))]:
            for target in LINK.findall(md.read_text()):
                if re.match(r"[a-z]+://", target) or target.startswith("mailto:"):
                    continue
                resolved = (md.parent / target).resolve()
                if not resolved.exists():
                    errors.append(f"{name}: {md.relative_to(ROOT)} links to missing {target}")
                elif md == skill_md:
                    linked.add(resolved)
        for ref in sorted((d / "references").glob("*.md")):
            # A markdown link or a plain `references/<file>` mention both make the model open it.
            if ref.resolve() not in linked and f"references/{ref.name}" not in text:
                errors.append(f"{name}: references/{ref.name} is not linked or mentioned in SKILL.md")

    for f in ROOT.rglob("*"):
        if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".yaml", ".yml", ".sh", ".py", ".json", ".template"}:
            if f == Path(__file__).resolve():
                continue
            if SECRET_SHAPES.search(f.read_text(errors="ignore")):
                errors.append(f"secrets: {f.relative_to(ROOT)} contains a credential-shaped string")

    for e in errors:
        print(f"FAIL {e}")
    print(f"{len(skills)} skills checked, {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

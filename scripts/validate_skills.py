#!/usr/bin/env python3
"""Validate Claude Enterprise Skills repository structure.

Checks:
- every skill directory contains SKILL.md;
- SKILL.md starts with YAML frontmatter;
- frontmatter contains name and description;
- required root files exist.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "ROADMAP.md",
]

FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")

    metadata: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata


def discover_skill_dirs() -> list[Path]:
    if not SKILLS_DIR.exists():
        return []
    return sorted(path.parent for path in SKILLS_DIR.glob("*/*/SKILL.md"))


def main() -> int:
    errors: list[str] = []

    for filename in REQUIRED_ROOT_FILES:
        if not (ROOT / filename).exists():
            errors.append(f"missing root file: {filename}")

    skill_dirs = discover_skill_dirs()
    if not skill_dirs:
        errors.append("no Skills found under skills/*/*/SKILL.md")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        readme_file = skill_dir / "README.md"
        checklist_file = skill_dir / "checklist.md"

        if not readme_file.exists():
            errors.append(f"missing README.md: {skill_dir.relative_to(ROOT)}")
        if not checklist_file.exists():
            errors.append(f"missing checklist.md: {skill_dir.relative_to(ROOT)}")

        try:
            metadata = parse_frontmatter(skill_file)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid SKILL.md frontmatter in {skill_file.relative_to(ROOT)}: {exc}")
            continue

        for field in ("name", "description"):
            if not metadata.get(field):
                errors.append(f"missing '{field}' in {skill_file.relative_to(ROOT)}")

        description = metadata.get("description", "")
        if len(description) < 20:
            errors.append(f"description too short in {skill_file.relative_to(ROOT)}")

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(f"OK: validated {len(skill_dirs)} Skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

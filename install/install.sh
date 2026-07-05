#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

mkdir -p "$TARGET_DIR"

find "$SOURCE_DIR/skills" -mindepth 2 -maxdepth 2 -type d | while read -r skill; do
  name="$(basename "$skill")"
  echo "Installing $name -> $TARGET_DIR/$name"
  rm -rf "$TARGET_DIR/$name"
  cp -R "$skill" "$TARGET_DIR/$name"
done

echo "Done. Restart Claude Code or open a new session."

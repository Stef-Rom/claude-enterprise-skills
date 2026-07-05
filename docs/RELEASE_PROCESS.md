# Release Process

## Versioning

This project uses semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

- `v0.1.0` — initial foundation
- `v0.2.0` — open source readiness
- `v0.3.0` — engineering core Skills
- `v1.0.0` — stable release

## Release checklist

1. Run validation:

```bash
python scripts/validate_skills.py
```

2. Update `CHANGELOG.md`.
3. Commit changes:

```bash
git add .
git commit -m "chore: prepare v0.2.0 release"
```

4. Create a tag:

```bash
git tag v0.2.0
git push origin main --tags
```

5. Create a GitHub Release from the tag.

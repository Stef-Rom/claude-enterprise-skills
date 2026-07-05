# GitHub Setup

## Create the repository

Recommended repository name:

```text
claude-enterprise-skills
```

Recommended description:

```text
Enterprise-grade Claude Code Skills for Azure, Python, React, DevOps and AI Engineering.
```

Create the repository without README, `.gitignore`, or license if you are pushing this project as the first commit.

## First commit

```bash
git init
git branch -M main
git add .
git commit -m "feat: initial release of Claude Enterprise Skills framework"
git remote add origin https://github.com/Stef-Rom/claude-enterprise-skills.git
git push -u origin main
```

## Validate locally

```bash
python scripts/validate_skills.py
```

Expected output:

```text
OK: validated 13 Skills.
```

## Recommended repository settings

Enable:

- Issues
- Discussions, optional
- Pull request reviews
- Branch protection on `main`
- GitHub Actions

Recommended branch protection:

- Require pull request before merging
- Require status checks to pass
- Require linear history, optional

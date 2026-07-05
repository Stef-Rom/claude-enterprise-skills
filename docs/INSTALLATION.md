# Installation guide

## Personal installation

Personal skills are available across projects:

```bash
bash install/install.sh
```

Default target:

```text
~/.claude/skills/
```

## Project installation

Project skills are scoped to one repository:

```bash
mkdir -p .claude/skills
cp -R /path/to/claude-enterprise-skills/skills/devops/deployment-orchestrator .claude/skills/
```

## Verify

Start Claude Code in a new terminal and ask:

```text
List the available enterprise skills you can use from my Claude skills folder.
```

# Claude Enterprise Skills

A professional Claude Skills library for Azure, Python, React, DevOps, SaaS architecture, customer delivery, documentation, and career acceleration.

Author: Stef-Rom  
Version: 0.1.0

## What is included

This repository contains production-oriented Claude Skills. Each skill is a self-contained directory with a `SKILL.md` file and optional supporting resources.

Core skills in this first release:

| Domain | Skill | Purpose |
|---|---|---|
| Career | `cv-signature` | Premium CV, ATS, LinkedIn, job matching |
| Career | `job-match-analyzer` | Analyze job offers and adapt CV/profile |
| Career | `recruiter-review` | Simulate HR, engineering manager, CTO review |
| Career | `linkedin-profile-optimizer` | Update LinkedIn profile, headline, About, experience, skills and recruiter visibility |
| Azure | `azure-architect` | Azure architecture review and design |
| Azure | `cosmosdb-expert` | Cosmos DB performance, storage, RU, partitioning |
| Azure | `azure-devops-expert` | Azure DevOps pipelines and delivery workflows |
| DevOps | `deployment-orchestrator` | QA, tests, rollout, rollback, release comms |
| Development | `python-architect` | Python backend architecture and quality |
| Development | `react-enterprise` | React enterprise frontend architecture |
| AI | `ai-assisted-development` | AI-assisted coding, review, prompting, agents |
| Architecture | `saas-architect` | SaaS multi-tenant architecture and upgrade strategy |
| Documentation | `technical-writer` | Technical docs, ADR, API docs, meeting notes |
| Business | `customer-solution-architect` | Customer requirements, workshops, solutions |

## Install

### Linux/macOS

```bash
git clone https://github.com/Stef-Rom/claude-enterprise-skills.git
cd claude-enterprise-skills
bash install/install.sh
```

### Windows PowerShell

```powershell
git clone https://github.com/Stef-Rom/claude-enterprise-skills.git
cd claude-enterprise-skills
powershell -ExecutionPolicy Bypass -File install/install.ps1
```

### Manual install

Copy the skill folders into your Claude user skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R skills/*/* ~/.claude/skills/
```

For a project-local install, copy the selected skills into:

```text
<your-project>/.claude/skills/
```

## Usage

In Claude Code, ask naturally:

```text
Use the deployment-orchestrator skill to design a safe release plan for this branch.
```

or:

```text
Use cv-signature to adapt my CV to this job offer.
```

## Security note

Skills can contain instructions and optional scripts. Review third-party skills before installation. This repository is designed to be mostly instruction-based and avoids destructive automation by default.

## Repository Quality

This repository includes open source project assets:

- GitHub issue templates
- Pull request template
- CODEOWNERS
- Code of Conduct
- Security policy
- Roadmap
- Local validation script
- GitHub Actions workflow

## Validate the repository

Run:

```bash
python scripts/validate_skills.py
```

Expected output:

```text
OK: validated 14 Skills.
```

## GitHub first commit

See [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md) for the recommended first commit procedure.

## Release process

See [`docs/RELEASE_PROCESS.md`](docs/RELEASE_PROCESS.md).

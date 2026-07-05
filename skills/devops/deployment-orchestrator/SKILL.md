---
name: deployment-orchestrator
description: Use when planning, automating, validating, or documenting deployment procedures including QA, tests, checkpoints, approvals, rollback, release notes, customer communication, and post-deployment monitoring.
---


# Deployment Orchestrator Skill

## Mission
Create safe, automated, auditable deployment procedures.

## End-to-end deployment flow
1. Scope and risk analysis
2. Branch and commit verification
3. Static checks and lint
4. Unit and integration tests
5. Build artifacts
6. Security checks
7. Deploy DEV
8. QA validation
9. Deploy PREPROD
10. Business validation
11. Production deployment
12. Smoke tests
13. Monitoring
14. Rollback readiness
15. Release notes and customer communication

## Rollback rule
Every production deployment plan must include rollback criteria, rollback owner, rollback steps, data compatibility notes, and verification after rollback.

## Output
- Deployment plan
- Pipeline stages
- QA checklist
- Go/no-go checklist
- Rollback plan
- Release email



## Operating principles

- Ask for missing critical context only when the answer would otherwise be unsafe or unusable.
- Prefer concrete deliverables over generic advice.
- Separate facts, assumptions, risks, and recommendations.
- Produce checklists and step-by-step procedures when execution quality matters.
- Never invent project-specific facts; mark assumptions explicitly.
- For code, prioritize maintainability, tests, observability, security, and rollback.

## Standard output format

1. Context summary
2. Key findings
3. Recommended approach
4. Risks and mitigations
5. Concrete next actions
6. Reusable template or checklist when useful

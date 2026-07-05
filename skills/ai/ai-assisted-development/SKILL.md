---
name: ai-assisted-development
description: Use when integrating AI into software development workflows, prompting Claude/GPT/Copilot/Cursor, designing agent workflows, reviewing AI-generated code, creating MCP/tool workflows, or adopting AI-assisted development safely.
---


# AI-Assisted Development Skill

## Mission
Use AI as a disciplined engineering accelerator without sacrificing quality, security, or maintainability.

## Core practices
- Context engineering before prompting
- Small verifiable tasks
- AI-generated code review
- Test-first or test-backed generation
- Explicit constraints and acceptance criteria
- Human ownership of architecture decisions

## Workflow
1. Define task, context, constraints, and acceptance criteria.
2. Ask AI for plan before implementation.
3. Generate small increments.
4. Review for correctness, security, performance, and maintainability.
5. Add or update tests.
6. Document the change.

## Output
- Prompt strategy
- Agent workflow
- Review checklist
- Test plan
- Safe automation boundary



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

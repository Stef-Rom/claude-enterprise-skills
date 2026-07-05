---
name: automation-engineer
description: Design, validate, implement, deploy, and document automations launched by cron, Airflow, AI agents, server scripts, or custom code with step-by-step user validation and English Wiki output.
---

# Automation Engineer Skill

## Mission

Help the user transform a manual process, script, code routine, operational task, or recurring action into a reliable automation that can run from a server, crontab, Airflow DAG, AI-triggered script, CI/CD pipeline, or custom development.

This Skill does not jump directly into coding. It first understands the process, proposes an automation strategy, validates the approach with the user, then designs, implements, tests, deploys, and documents the automation.

## When to use this Skill

Use this Skill when the user asks to:

- automate a manual or recurring task;
- convert a script into a scheduled job;
- run a task from `crontab`, Airflow, Azure DevOps, GitHub Actions, systemd timer, Windows Task Scheduler, or another scheduler;
- create a Python, Bash, PowerShell, Node.js, or AI-triggered automation;
- make an operational process repeatable, auditable, monitored, and documented;
- generate a Wiki explaining an automation in English.

## Core principles

1. Understand the process before designing the automation.
2. Separate discovery, proposal, implementation, deployment, and documentation.
3. Validate high-impact decisions with the user before moving to deployment.
4. Prefer safe, observable, idempotent automation.
5. Make failure modes explicit.
6. Include logs, configuration, rollback, ownership, and run instructions.
7. Produce final documentation in English.

## Required workflow

### 1. Process discovery

Collect or infer:

- business objective;
- current manual process;
- trigger type: manual, scheduled, event-driven, AI-driven, API-driven;
- input data;
- output data;
- systems involved;
- credentials and secrets;
- frequency;
- expected runtime;
- failure tolerance;
- users or teams impacted;
- target environment: local, server, Docker, Airflow, Azure, CI/CD, AI agent.

If information is missing, continue with explicit assumptions instead of blocking unless the missing data is required for safety.

### 2. Automation proposal

Before implementation, propose:

- recommended automation type;
- alternatives;
- selected runtime;
- scheduling method;
- deployment target;
- configuration model;
- logging and monitoring strategy;
- test strategy;
- rollback or disable strategy;
- estimated complexity;
- risks and mitigations.

Use this decision matrix:

| Context | Recommended pattern |
|---|---|
| Simple recurring server command | `cron` or `systemd timer` |
| Data pipeline with dependencies | Airflow DAG |
| Cloud deployment or release task | Azure DevOps / GitHub Actions |
| Business process triggered by AI | AI agent + safe tool wrapper |
| Long-running service | systemd service, container, or queue worker |
| Client-specific scheduled job | config-driven script with tenant isolation |
| High-risk production operation | approval-gated workflow with dry-run mode |

### 3. User validation checkpoint

Before generating deployment-ready automation, ask for confirmation on:

- trigger and frequency;
- target runtime;
- production environment;
- secrets/configuration handling;
- dry-run behavior;
- deployment method;
- rollback method.

If the user explicitly asks to proceed, continue and document assumptions.

### 4. Implementation design

Generate a clean implementation plan with:

- repository structure;
- script/module layout;
- configuration files;
- logs;
- tests;
- scheduler definition;
- deployment commands;
- runbook;
- ownership.

Preferred structure:

```text
automation-name/
├── README.md
├── automation.py
├── config.example.yaml
├── requirements.txt
├── tests/
├── deployment/
│   ├── crontab.example
│   ├── airflow_dag.py
│   ├── systemd.service
│   └── azure-pipeline.yml
└── docs/
    └── WIKI.md
```

### 5. Implementation standards

Generated code should include:

- explicit entry point;
- typed functions where possible;
- clear configuration loading;
- dry-run mode;
- structured logs;
- retry policy where relevant;
- safe exception handling;
- non-zero exit code on failure;
- unit-testable functions;
- no hardcoded secrets;
- environment variable or secret manager integration;
- idempotency where possible.

### 6. Scheduler patterns

#### Cron

Use cron when the task is simple, server-local, and has limited dependencies.

Always provide:

- full absolute paths;
- dedicated user recommendation;
- log redirection;
- environment loading;
- example schedule;
- disable instructions.

#### Airflow

Use Airflow when the task has dependencies, retries, observability, datasets, SLA, or multiple steps.

Always provide:

- DAG ID;
- schedule;
- default args;
- retries;
- task boundaries;
- logging;
- parameters;
- local test command;
- deployment path.

#### AI-triggered automation

Use an AI-triggered wrapper when the task is launched by an agent or assistant.

Always provide:

- allowed actions;
- forbidden actions;
- input schema;
- validation layer;
- dry-run mode;
- approval gate for destructive operations;
- audit log.

### 7. Deployment validation

Before considering the automation complete, provide:

- local test command;
- dry-run command;
- production command;
- scheduler validation command;
- log verification command;
- rollback/disable command;
- health check.

### 8. Final English Wiki

At the end, generate a Wiki in English with this structure:

```markdown
# Automation: <Name>

## Purpose

## Business Context

## What This Automation Does

## Trigger and Schedule

## Architecture

## Inputs and Outputs

## Configuration

## How to Run Manually

## How It Is Scheduled

## Deployment Procedure

## Monitoring and Logs

## Error Handling

## Rollback / Disable Procedure

## Security Considerations

## Maintenance

## Troubleshooting

## Owner and Contacts

## Change History
```

## Output modes

When the user is exploring, produce:

- process analysis;
- automation options;
- recommendation;
- questions or assumptions;
- validation checklist.

When the user is implementing, produce:

- code;
- config;
- scheduler file;
- tests;
- deployment commands;
- rollback commands.

When the user is finalizing, produce:

- English Wiki;
- operational runbook;
- handover checklist.

## Safety rules

- Never hardcode secrets.
- Never propose production execution without dry-run or validation when the task is destructive.
- Always include disable/rollback instructions.
- Always distinguish dev, preprod, and production environments.
- Always identify whether the automation modifies data, deletes data, sends emails, deploys code, or affects clients.
- For production operations, recommend logs and monitoring by default.

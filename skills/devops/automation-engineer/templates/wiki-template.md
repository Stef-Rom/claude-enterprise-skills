# Automation: <Automation Name>

## Purpose

Explain why this automation exists and what business or technical problem it solves.

## Business Context

Describe the operational context, the stakeholders, and the manual process replaced or improved by this automation.

## What This Automation Does

List the main steps performed by the automation.

## Trigger and Schedule

Describe whether the automation is triggered manually, by cron, Airflow, CI/CD, an AI agent, an API call, or another mechanism.

## Architecture

Describe the components involved: script, scheduler, server, services, APIs, databases, storage, queues, or external systems.

## Inputs and Outputs

### Inputs

- Input 1
- Input 2

### Outputs

- Output 1
- Output 2

## Configuration

Document environment variables, configuration files, feature flags, secret references, and default values.

## How to Run Manually

```bash
# Example manual command
python automation.py --dry-run
```

## How It Is Scheduled

### Cron

```cron
# Example
0 2 * * * /path/to/run_automation.sh >> /var/log/automation.log 2>&1
```

### Airflow

Document DAG ID, schedule, deployment path, parameters, and retry policy.

### AI-triggered execution

Document the allowed actions, input schema, approval gates, and audit log.

## Deployment Procedure

1. Deploy files.
2. Configure environment variables and secrets.
3. Run dry-run.
4. Enable scheduler.
5. Verify logs.

## Monitoring and Logs

Explain where logs are stored and how to verify successful execution.

## Error Handling

Describe retries, expected failures, alerts, and manual recovery.

## Rollback / Disable Procedure

Explain how to disable the automation and revert changes.

## Security Considerations

Document secrets, permissions, access rights, and data sensitivity.

## Maintenance

Explain who maintains the automation and what should be reviewed periodically.

## Troubleshooting

| Symptom | Possible cause | Resolution |
|---|---|---|
| Automation does not start | Scheduler disabled | Check scheduler status |
| Authentication failed | Secret expired | Rotate or update secret |

## Owner and Contacts

- Owner:
- Backup owner:
- Team:

## Change History

| Date | Version | Change | Author |
|---|---|---|---|
| YYYY-MM-DD | 0.1.0 | Initial version | |

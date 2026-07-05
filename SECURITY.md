# Security Policy

## Supported versions

This project is in early development. Security fixes are applied to the latest published version.

## Reporting a vulnerability

Do not open a public issue for sensitive vulnerabilities.

Report security concerns privately to the repository owner through GitHub.

## Scope

Relevant security issues include:

- scripts that may overwrite user data;
- unsafe shell behavior;
- prompt content that encourages insecure engineering practices;
- accidental inclusion of secrets, tokens, credentials, or private customer information.

## Security principles

Skills should never require secrets to be pasted into prompts. Installation scripts should be simple, auditable, and avoid destructive operations.

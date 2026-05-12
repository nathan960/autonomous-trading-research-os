# Trigger Scan Routine

## Purpose

Run the Trigger Scan layer in a stateless, auditable way.

## Commands

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/trigger_scan.py
git status --short
git diff
git add .
git commit -m "Trigger Scan: audited run" || true
git push
```

## Safety notes

- Do not print secrets.
- Do not create `.env` in cloud.
- Do not bypass risk gates.
- If the script fails, log the error and stop.

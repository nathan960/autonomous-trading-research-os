# Data Refresh Routine

## Purpose

Run the Data Refresh layer in a stateless, auditable way.

## Commands

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/data_refresh.py --alpaca
git status --short
git diff
git add .
git commit -m "Data Refresh: audited run" || true
git push
```

## Safety notes

- Do not print secrets.
- Do not create `.env` in cloud.
- Do not bypass risk gates.
- If the script fails, log the error and stop.

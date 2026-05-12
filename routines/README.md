# Routine Playbooks

Each routine is stateless: clone/pull, run deterministic checks, run the layer script, inspect diff, commit, and push or open a PR.

Use environment variables supplied by the routine runner. Do not create `.env` in cloud.

Execution routine is the only routine that can submit Alpaca paper orders, and only when every execution guard passes.

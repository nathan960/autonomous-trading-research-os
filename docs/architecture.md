# Architecture

The system separates trade-critical deterministic state from research context.

## Trade-critical path

`Data Refresh -> Trigger Scan -> Trade Plan Generation -> Trade Execution -> Position Monitor`

Only Alpaca-derived account, position, order, clock, bar, quote, and spread data may feed this path.

## Research path

`Research Context -> Weekly Review -> Strategy Improvement Review`

Research can propose hypotheses but cannot create orders or change production strategy.

## Fail-closed controls

- Missing snapshot: trigger scan fails.
- Missing trigger snapshot: trade-plan generation fails.
- Missing trade plan: execution fails.
- Stale or unapproved plan: execution blocks.
- Any failed risk gate: execution blocks.
- Any live trading flag: execution blocks.

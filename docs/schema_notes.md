# Schema Notes

Current JSON outputs are plain dictionaries for rapid iteration. Keep these fields stable:

- `schema_version`
- `run_id`
- `generated_at`
- `source_data_hash` or plan/snapshot hash
- `risk_gates`
- `approval.status`
- `no_trade_reasons`

Future schema migrations should be committed as explicit PRs with backward-compatibility notes.

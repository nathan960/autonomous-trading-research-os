## System Status — 2026-05-14T15:28:02Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.70  drawdown=-0.00%  positions=3  open_orders=1
**Trade Plan:** trade_plan-20260514T152756-a1cc9ba9  approved=False
**Dry-run gates:** PASS  failed=[]

**Blocking Issues:**
- Open duplicate orders for planned symbols: ['EQIX']

**Warnings:**
- 40 wide-spread symbols (['AMT', 'APD', 'AXP', 'BA', 'BLK', 'CAT', 'COST', 'CVX', 'DIS', 'DUK', 'ECL', 'EOG', 'GS', 'HD', 'HON', 'INTU', 'ISRG', 'JNJ', 'JPM', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MS', 'NEE', 'ORCL', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'SRE', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Cancel or wait for existing open orders to settle before re-running

---
## System Status — 2026-05-14T15:29:43Z

**Overall:** RED  | Research: NO  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.69  drawdown=-0.00%  positions=3  open_orders=1
**Trade Plan:** trade_plan-20260514T152756-a1cc9ba9  approved=False
**Dry-run gates:** FAIL  failed=['NO_DUPLICATE_OPEN_ORDERS']

**Blocking Issues:**
- Open duplicate orders for planned symbols: ['EQIX']
- Execution gates: unexpected failures: ['NO_DUPLICATE_OPEN_ORDERS']

**Warnings:**
- 36 wide-spread symbols (['ABBV', 'ADBE', 'AMGN', 'AMT', 'APD', 'AXP', 'BA', 'BLK', 'COST', 'CRM', 'CVX', 'DE', 'ECL', 'EOG', 'GS', 'HD', 'HON', 'ISRG', 'JNJ', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MS', 'ORCL', 'PG', 'PM', 'RTX', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution

**Required Operator Actions:**
- [ ] Cancel or wait for existing open orders to settle before re-running
- [ ] Investigate gate failures: ['NO_DUPLICATE_OPEN_ORDERS']

---

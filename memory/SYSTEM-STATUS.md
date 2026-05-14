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
## System Status — 2026-05-14T17:45:26Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.43  drawdown=-0.00%  positions=4  open_orders=1
**Trade Plan:** trade_plan-20260514T174516-ddb701fd  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 37 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AMGN', 'APD', 'AXP', 'BA', 'BKNG', 'CAT', 'COP', 'COST', 'CVX', 'DE', 'DIS', 'ECL', 'FCX', 'GS', 'HON', 'INTU', 'ISRG', 'LLY', 'LOW', 'MA', 'MCD', 'MS', 'ORCL', 'PEP', 'PG', 'PLD', 'PM', 'RTX', 'SHW', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 6 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=4,limit=1)', 'JNJ(count=1,limit=1)', 'WMT(count=1,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---

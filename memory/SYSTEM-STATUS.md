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
## System Status — 2026-05-14T18:08:57Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.14  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260514T180756-fc25ae26  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 28 wide-spread symbols (['ABBV', 'ADBE', 'AMD', 'AMGN', 'AMT', 'APD', 'CAT', 'COST', 'DE', 'ECL', 'EOG', 'GE', 'HON', 'ISRG', 'JPM', 'LIN', 'LLY', 'LOW', 'MCD', 'MS', 'ORCL', 'PEP', 'PG', 'PM', 'RTX', 'TMUS', 'UNP', 'WELL']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 11 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=7,limit=1)', 'JNJ(count=2,limit=1)', 'WMT(count=2,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---
## System Status — 2026-05-14T22:18:59Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,802.93  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260514T214947-b0ee5f7f  approved=False
**Dry-run gates:** PASS  failed=[]

**Warnings:**
- 44 wide-spread symbols (['AAPL', 'ABBV', 'AEP', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'AVGO', 'AXP', 'BA', 'CAT', 'CL', 'CMCSA', 'COST', 'CRM', 'CSCO', 'CVX', 'DIS', 'DUK', 'EOG', 'EQIX', 'GE', 'HON', 'INTU', 'LLY', 'LOW', 'META', 'MRK', 'MSFT', 'NEE', 'ORCL', 'PEP', 'PG', 'PM', 'RTX', 'SHW', 'SLB', 'SO', 'TMUS', 'UNH', 'UPS', 'WELL', 'WMT']) — SPREAD_NOT_TOO_WIDE may block execution
- Daily order limit reached: 11 orders today (max_total_paper_orders_per_day=3)
- Per-symbol daily order limits reached: ['EQIX(count=7,limit=1)', 'JNJ(count=2,limit=1)', 'WMT(count=2,limit=1)']

**Required Operator Actions:**
- [ ] Daily order limits hit — churn guard will block new orders until tomorrow

---
## System Status — 2026-05-15T22:09:58Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,799.26  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260515T214104-7822211e  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 45 wide-spread symbols (['ABBV', 'ADBE', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'BA', 'BAC', 'BKNG', 'BLK', 'CAT', 'CMCSA', 'COP', 'COST', 'CSCO', 'CVX', 'DIS', 'DUK', 'EOG', 'FCX', 'HD', 'HON', 'INTU', 'JNJ', 'KO', 'MA', 'MCD', 'MDLZ', 'META', 'MRK', 'NEE', 'NKE', 'NVDA', 'ORCL', 'PLD', 'SBUX', 'SHW', 'SRE', 'TMO', 'UNH', 'UPS', 'WELL', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-18T22:12:09Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.42  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260518T215059-e7e56c9f  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 54 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AMD', 'AMGN', 'AMZN', 'APD', 'AXP', 'BA', 'BAC', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'DE', 'DIS', 'ECL', 'EOG', 'FCX', 'GE', 'HON', 'INTU', 'ISRG', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'META', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PLD', 'SHW', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'UNH', 'UNP', 'UPS', 'V', 'WFC', 'WMT', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-19T22:23:47Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.35  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260519T220014-e0847b4b  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 55 wide-spread symbols (['AAPL', 'ABBV', 'ABT', 'ADBE', 'AEP', 'AMGN', 'APD', 'AVGO', 'AXP', 'BA', 'BKNG', 'BLK', 'CL', 'COP', 'COST', 'CSCO', 'CVX', 'DE', 'DIS', 'ECL', 'GE', 'GOOGL', 'GS', 'HD', 'HON', 'INTU', 'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'MA', 'MDLZ', 'META', 'MRK', 'MS', 'NEE', 'NFLX', 'NVDA', 'ORCL', 'PEP', 'PG', 'PLD', 'SBUX', 'SLB', 'SO', 'SPY', 'SRE', 'TMO', 'TMUS', 'TSLA', 'UNP', 'UPS', 'WFC', 'XOM']) — SPREAD_NOT_TOO_WIDE may block execution

---
## System Status — 2026-05-20T22:42:29Z

**Overall:** YELLOW  | Research: YES  | Paper Execution: NO  | Scheduled: NO (policy)

**Account:** equity=$99,800.44  drawdown=-0.00%  positions=4  open_orders=0
**Trade Plan:** trade_plan-20260520T221523-26202569  approved=False
**Dry-run gates:** FAIL  failed=['QUOTE_FRESHNESS']

**Warnings:**
- Dry-run gates failed for market/timing reasons: ['QUOTE_FRESHNESS']
- 49 wide-spread symbols (['ABBV', 'ABT', 'ADBE', 'AEP', 'AMD', 'AMGN', 'AMT', 'APD', 'AVGO', 'AXP', 'BAC', 'BLK', 'CAT', 'CL', 'CMCSA', 'COP', 'CRM', 'CSCO', 'DUK', 'EOG', 'EQIX', 'GE', 'GS', 'HD', 'INTU', 'ISRG', 'KO', 'LLY', 'LMT', 'MDLZ', 'META', 'MS', 'NEE', 'NFLX', 'NKE', 'NVDA', 'O', 'ORCL', 'PEP', 'PG', 'PLD', 'RTX', 'SBUX', 'SO', 'SRE', 'TMO', 'UNH', 'WELL', 'WFC']) — SPREAD_NOT_TOO_WIDE may block execution

---

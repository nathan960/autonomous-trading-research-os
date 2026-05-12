# Trade Log

Execution attempts, submitted paper orders, skips, errors, and position-monitor outcomes are logged here.

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:20Z",
  "run_id": "execution-20260512T153120-a20828c0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.02559465,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:31:20Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153120-83bf6e24",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:30Z",
  "run_id": "execution-20260512T153129-86d9b9f0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01597525,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:32:53Z",
  "run_id": "execution-20260512T153253-0ba5873e",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.023264183333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:32:53Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153253-f5b2f106",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:05Z",
  "run_id": "execution-20260512T153305-15251a6c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.013966983333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:33:05Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153305-53451c31",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:12Z",
  "run_id": "execution-20260512T153311-29338c98",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016075883333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:25:43Z",
  "run_id": "execution-20260512T162543-f43bd673",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "8775d5146cc11c1af1ebf14fdd8b2fa5c4ecdf4f94d15577d3e2bbb212508e12",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010717966666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:41:43Z",
  "run_id": "execution-20260512T164143-d22ae89d",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "704c77858eb7b24f9b54c7a1e9924cc05a21a5b37f8bb3f8da5f6fd0bb8e5841",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0046165166666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:56:01Z",
  "run_id": "execution-20260512T165601-c8d84990",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "43c6e75e13b2091d0ef514e42e32c4645ef595f00933206e90df501659d3fdbb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010833116666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:04Z",
  "run_id": "execution-20260512T170904-4530a860",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "45e42630febca33310762bd820c61df313580a19f15d3cad2c47422ad66e32af",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01146715,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:39Z",
  "run_id": "execution-20260512T170939-8ba4104f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "50ac2d692a66edd4310fcb296642f30c215fed8f5c373fb323d25e6285688d27",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007178916666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T17:21:53Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 11,
  "orders_validated": 11,
  "plan_id": "trade_plan-20260512T171215-200ec4ba",
  "run_id": "execution-20260512T172153-12e1a120",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "0d9edf4f1ccc2f9df3dad0de535b6faad1673807e4f71a748eaa2b3b4e8dd139"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:35:26Z",
  "run_id": "execution-20260512T173526-4e3f28d8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "054760162b875c1258d7e9eeb6d0b1da74f538139859fea34e629b163a5ffba4",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0107853,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:36Z",
  "run_id": "execution-20260512T174736-aab62b09",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "e9cf75575fe00cf90f6568e97f76fe4bea47b77312fa7bb892cd85658ba5a8ce",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010707,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:44Z",
  "run_id": "execution-20260512T174744-3632a627",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "9552350933e92f326793c4b9c4a89058da4983262fbaf2e4d7d637a4dc3acbee",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.019361383333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:49Z",
  "run_id": "execution-20260512T174749-0e432044",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4628a115d34f79cc64d7304791ba0900e8048dd093b3510c25141d2ea8d11438",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008237616666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:47:55Z",
  "run_id": "execution-20260512T174755-44c42d0c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "f2d9abf471ece7e6cd38bf21fde5354df7916bb0f6119876db4c7be4804b9c21",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.006437300000000001,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "SPREAD_NOT_TOO_WIDE"
  ],
  "generated_at": "2026-05-12T17:48:33Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 15,
  "orders_validated": 17,
  "plan_id": "trade_plan-20260512T174833-a95ddc3a",
  "run_id": "execution-20260512T174833-8a168561",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "7187194f79dbf8a3c6f64fb9cc356eaee1ab6456b3396a6ed6aaf7c95cb0a9e9"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:23:53Z",
  "run_id": "execution-20260512T182353-45daa85c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "da79f7820b51fca182ae899b675e835f364d36d715dceb7f61e8a03e743aac18",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01570595,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:13Z",
  "run_id": "execution-20260512T182413-184b60f8",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "b024ae27bcc8ba7a0baf5470ce2eb62124ac106003f72af751fe2b68ecf80774",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.020626066666666668,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:19Z",
  "run_id": "execution-20260512T182419-3035be12",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4529428e6110412e5bc4302d23693624cb2220b56fc4a5242852761876af8bbc",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.005748433333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:25Z",
  "run_id": "execution-20260512T182425-d7f0fbc3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "c582a4e5785e46172c36164d9103016ea752b9b87025b41039ea8d6c8bfda988",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016776266666666664,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T18:24:31Z",
  "run_id": "execution-20260512T182431-d1a4cff4",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "4abd85771a1f7a0f6d4e38c0b0769d266624c681fc90de71ce6841f653731c15",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.00974325,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "RISK_STATE_NOT_PAUSED"
  ],
  "generated_at": "2026-05-12T18:25:07Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 11,
  "orders_validated": 11,
  "plan_id": "trade_plan-20260512T182449-e8679da5",
  "run_id": "execution-20260512T182507-73855233",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "e93171f73d02323ba8d12bf92d714be2aa9fda4bade9192679e05b01aacadac1"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "SPREAD_NOT_TOO_WIDE"
  ],
  "generated_at": "2026-05-12T19:45:51Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 13,
  "orders_validated": 15,
  "plan_id": "trade_plan-20260512T194551-286a1ccf",
  "run_id": "execution-20260512T194551-8b775a07",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "129d27c931075227bc616d6d83e64909e1de5f989cc8c58e9ce81a5b730cc51d"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:46:26Z",
  "run_id": "execution-20260512T204626-14c11f55",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "df7e66450535adfaba51e8edec8e1113e34ff9482e5a82a45a9b65edeee3c8ca",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.004942533333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:49:02Z",
  "run_id": "execution-20260512T204902-2160169f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "d2c85fdd0f532536fc281ae4c7082d3c77bfa0650545f5544856ef00ef891146",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0062546,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:50:36Z",
  "run_id": "execution-20260512T205036-03817eb3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "fdbe7fbf89cba55fd53b0dd36d865f47cfb78d2d6b660e8dff2838c893d57aea",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007643366666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:51:34Z",
  "run_id": "execution-20260512T205134-5a169ba6",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "54ee2d8eeb40bf0119d7e3fc68c9ce58fbb4ee8e6484b039ab624111de237df7",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008520583333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:51:56Z",
  "run_id": "execution-20260512T205156-c61deb8e",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "a46a349a7f936ba49b22e8c264ca526e6888a95e73f96c5797a046907f8b9248",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007743166666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:13Z",
  "run_id": "execution-20260512T205213-d32d0cbf",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "54abef48d25e009a00dbb218e857516089bf9b6f632dce39c89fd75d43d5c1a5",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010255366666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:22Z",
  "run_id": "execution-20260512T205222-c45b38f9",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "72e596acf4000d83e564ed09b7564190e75ec4cabe28f1da66ffe1b62ffecb78",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0152097,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:28Z",
  "run_id": "execution-20260512T205228-c66044bf",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "5bf1f4d16797bf28375bd97c8d582edcd70f102afcc3ddc9b494eb3c71bc7502",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.015124416666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:36Z",
  "run_id": "execution-20260512T205236-2ee9428f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "0dba45346458e6e79898c167aee17f8898366247aeb4cc5a56cad3eefc954485",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.012359716666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:52:43Z",
  "run_id": "execution-20260512T205243-cb30ace3",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "716e3a673ba6b7b2b35758d26c7c68fd6d83c49aa156e09d025419d0f70fffff",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007410016666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": false,
  "dry_run": true,
  "failed_gates": [
    "RISK_STATE_NOT_PAUSED"
  ],
  "generated_at": "2026-05-12T20:55:41Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205538-6e92e41f",
  "run_id": "execution-20260512T205541-f6030429",
  "status": "DRY_RUN_FAIL",
  "trade_plan_hash": "a60cf1f47122f119465ec97026fbeb226c5790f69ce8b876b0de028eb3b05d2e"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:56:07Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205538-6e92e41f",
  "run_id": "execution-20260512T205607-5978f6f5",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "a60cf1f47122f119465ec97026fbeb226c5790f69ce8b876b0de028eb3b05d2e"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:56:11Z",
  "run_id": "execution-20260512T205611-08292204",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "410a9b72153b1f52a740ec95688f6f9428c303e4220b6159a0f85140e2d33ff6",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.008039766666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:57:30Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205611-b0ec7467",
  "run_id": "execution-20260512T205730-981a1726",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "c2a47ebea76369ce01a751c6ee3bff86059ad55ee73e3511646827b4f28445df"
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T20:57:37Z",
  "run_id": "execution-20260512T205736-c3491168",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "9e6196fd88e15f96a2d29b9fc724d7d5c4dbeaa8d4cfb3939d4f6c2e1cf7a1a1",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016469833333333333,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T20:59:18Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T205918-71daec15",
  "run_id": "execution-20260512T205918-0602a349",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "935f3ddc4666246177b96f599daedb2749f5400466f02d50624539ed9f1d3a2c"
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T21:16:51Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 1,
  "orders_validated": 1,
  "plan_id": "trade_plan-20260512T211650-20309759",
  "run_id": "execution-20260512T211651-ec294806",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "74a42f0a5a7c7356bc22d8c767aa170ff8530965987efaf083bc8dad198adc4c"
}
```

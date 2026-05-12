# Signal Log

Candidate ranking, trade-plan generation, and no-trade reasons are logged here.

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153120-a8d76fc7",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153120-b24052c1",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153129-62645e34",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153129-9869c4d7",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153253-d75f00af",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153253-0f139ccb",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e"
}
```

## Trade plan generated

```json
{
  "approval_status": "BLOCKED",
  "candidate_order_count": 11,
  "failed_gates": [
    "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER"
  ],
  "run_id": "trade_plan-20260512T153300-41352dc4",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "66e19502a46c261f9951c0a598c6ff33647003f663b581b39f96e00fec45a5aa"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153305-2d0c50dd",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153305-8ba0bff3",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153311-53c96d1b",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153311-897f45cf",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb"
}
```

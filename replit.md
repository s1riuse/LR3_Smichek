# Project Overview

Python-based utility with two distinct functional modules:

## Modules

### 1. VM Creation Simulation (`main_cont.py`)
Simulates user requests to create virtual machines with rate limiting and disk space checks. Logs results and generates visual reports (pie chart + bar chart) in the `logs/` directory.

- Entry point: `main.py` (imports from `main_cont.py`)
- Core logic: `calc.py` (rate limiting, disk usage check)
- Visualization: `visual.py` (matplotlib charts)
- Output: `logs/events.json`, `logs/stats_pie.png`, `logs/stats_bar.png`

### 2. Depreciation Calculations (`main_LR.py`)
Performs financial depreciation calculations using two methods:
- Linear (straight-line) depreciation
- Declining balance (reducing balance) depreciation

Generates charts (chart7–chart12) in the `visual_LR/` directory.

## Tech Stack

- **Language:** Python 3.11+
- **Data Analysis:** pandas, numpy
- **Math/Symbolic:** sympy
- **Visualization:** matplotlib
- **System Monitoring:** psutil
- **Config:** python-dotenv

## Configuration

Environment variables (via `.env`):
- `RATE_LIMIT_THRESHOLD` — max VM requests per minute per user (default: 3)
- `DISK_CRITICAL_PERCENT` — disk usage threshold to block requests (default: 90)

## Workflow

- **Start application** — runs `python main.py` (console output)

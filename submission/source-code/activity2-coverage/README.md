# Activity 2: Statement, Branch, and Condition Coverage

## Overview

This activity demonstrates three levels of code coverage using **Coverage.py** on a grade-scoring function. Each coverage type targets a different aspect of white-box testing thoroughness.

## Coverage Types

### 1. Statement Coverage
**Goal:** Every executable statement in the code runs at least once.

For `grade_score()`, this means:
- Each `return` statement executes (Invalid, A, B, C, D, F)
- Each `if` condition is evaluated
- All 14 executable statements are covered

**Tests required:** At least one test per return path (7 tests)

### 2. Branch (Decision) Coverage
**Goal:** Every decision (if/else) evaluates both True and False outcomes.

For `grade_score()`, there are 7 decisions (D1–D7). Branch coverage requires each to be True at least once and False at least once.

**Example:**
| Decision | Condition | True Test | False Test |
|----------|-----------|-----------|------------|
| D1 | isinstance check | `"abc"` | `95` |
| D2 | 0 ≤ score ≤ 100 | `-5` or `101` | `95` |
| D3 | 90 ≤ score ≤ 100 | `100` | `85` |

### 3. Condition Coverage
**Goal:** Every atomic condition (sub-expression in a compound boolean) evaluates both True and False.

For `grade_score()`, there are 13 atomic conditions (C1–C13):
- `isinstance(score, (int, float))`
- `score < 0`, `score > 100`
- `score >= 90`, `score <= 100`
- `score >= 80`, `score < 90`
- `score >= 70`, `score < 80`
- `score >= 60`, `score < 70`
- `score >= 0`, `score < 60`

## Files

| File | Description |
|------|-------------|
| `conditional_logic.py` | Grade-scoring function with compound boolean conditions |
| `test_coverage.py` | Three test suites: statement, branch, and condition coverage |
| `generate_report.py` | Script to run Coverage.py and generate reports |
| `htmlcov/` | Generated HTML coverage report (interactive) |
| `README.md` | This file |

## Running Coverage Analysis

```bash
cd activity2-coverage
python generate_report.py
```

Or manually:
```bash
cd activity2-coverage
python -m pytest test_coverage.py -v --cov=conditional_logic.py --cov-report=term-missing --cov-report=html
```

## Results

| Coverage Type | Target | Achieved |
|---------------|--------|----------|
| Statement     | 100%   | 100% ✅  |
| Branch        | 100%   | 100% ✅  |
| Condition     | 100%   | 100% ✅  |

All three coverage levels are demonstrated with dedicated test suites. Each suite is clearly labeled and documented to show which coverage requirements it satisfies.

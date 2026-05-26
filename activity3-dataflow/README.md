# Activity 3: Data Flow Testing

## Overview

This activity demonstrates **data flow testing** — a white-box technique that tracks how variable values flow through a program from their definition points to their usage points. We use Euclid's GCD algorithm as our subject program.

## Key Concepts

### Definitions and Uses

- **Definition (d):** A point where a variable is assigned a value
  - Example: `x = 5` defines variable `x`
- **Computation Use (c-use):** A point where a variable's value is used in a computation
  - Example: `result = x + 3` uses `x` in computation
- **Predicate Use (p-use):** A point where a variable's value is used in a condition
  - Example: `if x > 0:` uses `x` in a predicate

### DU Pairs and DU Paths

- **DU Pair:** A pair `(d, u)` where variable `v` is defined at `d` and used at `u`, and there exists a def-clear path from `d` to `u` (no intervening redefinition of `v`)
- **DU Path:** A simple (non-looping) path through the CFG from a definition to a use

### Coverage Criteria

1. **All-Defs Coverage:** Every definition reaches at least one use
   - Minimum: 1 test per definition point
2. **All DU Pairs Coverage:** Every DU pair is exercised
   - Every definition reaches every possible use
3. **All DU Paths Coverage:** Every simple path from each definition to each use is exercised
   - Most thorough; accounts for different loop iterations

## Our Implementation

### Subject Program: `gcd(a, b)`

Euclid's GCD algorithm with three variables `x`, `y`, and `r`:

| Variable | Definitions | Uses (c-use) | Uses (p-use) |
|----------|-------------|--------------|--------------|
| x | d1_x (init), d2_x (loop) | c_x_mod, c_x_ret | — |
| y | d1_y (init), d2_y (loop) | c_y_mod, c_y_assign | p_y_while |
| r | d1_r (init), d2_r (loop) | c_r_assign | — |

**Total: 12 DU pairs**

### Test Design

| Coverage Criterion | Test Cases | Verification |
|--------------------|------------|--------------|
| All-defs | 6 tests | Each definition reaches ≥1 use |
| All DU pairs | 12 tests | Every DU pair exercised |
| All DU paths | 20+ tests | Multiple loop iteration counts |

## Files

| File | Description |
|------|-------------|
| `dataflow_program.py` | GCD function with `gcd()` and `gcd_with_steps()` |
| `du_analysis.py` | Programmatic data flow analysis with full report |
| `test_dataflow.py` | pytest tests for all-defs, all-DU-pairs, all-DU-paths |
| `du_diagram.md` | Mermaid diagram with annotated def/use points |
| `README.md` | This file |

## Running the Tests

```bash
cd activity3-dataflow
python -m pytest test_dataflow.py -v
```

## Results

All three data flow coverage criteria are satisfied:
- **All-Defs:** ✅ All 6 definition points reach at least one use
- **All DU Pairs:** ✅ All 12 DU pairs are exercised
- **All DU Paths:** ✅ All significant simple paths covered

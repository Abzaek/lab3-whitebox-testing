# Activity 4: Mutation Testing

## Overview

This activity demonstrates **mutation testing** — a fault-based testing technique where small changes (mutations) are introduced to the code to evaluate the quality of the test suite. A good test suite should "kill" (detect) these mutations.

## Key Concepts

### Mutation Testing Process

1. **Create Mutants:** Introduce small, deliberate faults into the code
2. **Run Tests:** Execute the test suite against each mutant
3. **Kill or Survive:** A mutant is "killed" if tests fail (mutation detected).
   A mutant "survives" if tests still pass (mutation undetected)
4. **Compute Score:** `Mutation Score = (Killed / Total) × 100%`

### Mutation Operators

Common mutation types include:
- **Arithmetic Operator Replacement:** `+` → `-`, `*` → `/`
- **Relational Operator Replacement:** `==` → `<=`, `<` → `>`
- **Off-by-One Changes:** `b` → `b + 1`, `i++` → `i--`
- **Condition Negation:** `if (x)` → `if (!x)`
- **Statement Deletion:** Remove a statement entirely

## Our Implementation

### Subject Program: Calculator Class

A `Calculator` class with 6 methods:
- `add(a, b)` — addition
- `subtract(a, b)` — subtraction
- `multiply(a, b)` — multiplication
- `divide(a, b)` — division (with zero check)
- `power(a, b)` — exponentiation
- `modulo(a, b)` — modulo (with zero check)

### Mutants Created

| # | File | Method | Mutation Type | Change |
|---|------|--------|---------------|--------|
| 1 | `mutant_1.py` | add | Operator change | `+` → `-` |
| 2 | `mutant_2.py` | multiply | Operator swap | `*` → `/` |
| 3 | `mutant_3.py` | power | Off-by-one | `b` → `b + 1` |
| 4 | `mutant_4.py` | divide | Relational | `==` → `<=` |
| 5 | `mutant_5.py` | modulo | Negation | `==` → `!=` |

### Expected Results

| Mutant | Would Test Detect? | Why? |
|--------|-------------------|------|
| 1 | ✅ Yes | `add(2,3) == -1` fails assertion for 5 |
| 2 | ✅ Yes | `multiply(4,3) ≈ 1.33` fails assertion for 12 |
| 3 | ✅ Yes | `power(2,3) == 16` fails assertion for 8 |
| 4 | ✅ Yes | `divide(10,-2)` raises error instead of returning -5 |
| 5 | ✅ Yes | `modulo(10,3)` raises error instead of returning 1 |

## Files

| File | Description |
|------|-------------|
| `calculator.py` | Original Calculator class under test |
| `test_mutation.py` | pytest tests designed to kill all mutants |
| `mutation_runner.py` | Script to automate mutation testing and compute score |
| `mutation_report.md` | Professional report with results and analysis |
| `mutants/mutant_1.py` | Mutant 1: add → subtract |
| `mutants/mutant_2.py` | Mutant 2: multiply → divide |
| `mutants/mutant_3.py` | Mutant 3: power off-by-one |
| `mutants/mutant_4.py` | Mutant 4: divide condition change |
| `mutants/mutant_5.py` | Mutant 5: modulo condition negation |
| `README.md` | This file |

## Running the Tests

```bash
cd activity4-mutation
python -m pytest test_mutation.py -v
```

## Running Mutation Testing

```bash
cd activity4-mutation
python mutation_runner.py
```

## Results

- **Mutants Killed:** 5 / 5
- **Mutation Score:** 100%
- **Test Suite Quality:** Excellent — all mutations detected

A 100% mutation score indicates that the test suite is thorough enough to
detect all 5 types of common programming faults.

# Mutation Testing Report — Calculator Class

## Overview

This report documents the mutation testing results for the `Calculator` class.
Five mutants were created, each introducing a single fault. The test suite was
run against each mutant to determine whether the mutation was detected ("killed").

## Mutant Details

| ID | Mutation Type | File | Original Code | Mutated Code |
|----|---------------|------|---------------|--------------|
| 1 | Arithmetic Operator Change | `mutant_1.py` | `a + b` (add) | `a - b` |
| 2 | Operator Swap | `mutant_2.py` | `a * b` (multiply) | `a / b` |
| 3 | Off-by-One / Boundary | `mutant_3.py` | `a ** b` (power) | `a ** (b + 1)` |
| 4 | Relational Operator Change | `mutant_4.py` | `if b == 0:` (divide) | `if b <= 0:` |
| 5 | Condition Negation | `mutant_5.py` | `if b == 0:` (modulo) | `if b != 0:` |

## Results

| ID | Mutation Type | Killed? | Test That Killed It | Notes |
|----|---------------|---------|---------------------|-------|
| 1 | Arithmetic Operator Change | ✅ YES | `test_add_positive_numbers` | `add(2,3)` returned -1 instead of 5 |
| 2 | Operator Swap | ✅ YES | `test_multiply_basic` | `multiply(4,3)` returned 1.33 instead of 12 |
| 3 | Off-by-One / Boundary | ✅ YES | `test_power_basic` | `power(2,3)` returned 16 instead of 8 |
| 4 | Relational Operator Change | ✅ YES | `test_divide_negative_divisor` | `divide(10,-2)` raised ZeroDivisionError |
| 5 | Condition Negation | ✅ YES | `test_modulo_basic` | `modulo(10,3)` raised ZeroDivisionError |

## Mutation Score Calculation

```
Mutation Score = (Killed Mutants / Total Mutants) × 100
               = (5 / 5) × 100
               = 100.0%
```

## Analysis

### Score: 100% — All mutants killed ✅

### Why each mutant was killed:

1. **Mutant 1 (add → subtract):** The test `test_add_positive_numbers` calls
   `add(2, 3)` and expects 5. The mutant returns `2 - 3 = -1`, which fails
   the assertion. Multiple other tests also detect this mutation.

2. **Mutant 2 (multiply → divide):** The test `test_multiply_basic` calls
   `multiply(4, 3)` and expects 12. The mutant returns `4 / 3 ≈ 1.33`,
   which fails the assertion. Tests with negative numbers also detect it.

3. **Mutant 3 (b → b+1 in exponent):** The test `test_power_basic` calls
   `power(2, 3)` and expects 8. The mutant returns `2^4 = 16`, which fails.
   The zero-exponent test (`power(5,0)` expecting 1, mutant gives 5) also
   detects it.

4. **Mutant 4 (== to <= in divide):** The test `test_divide_negative_divisor`
   calls `divide(10, -2)` and expects -5.0. The mutant raises
   `ZeroDivisionError` because `-2 <= 0` is True, which fails the test.

5. **Mutant 5 (== to != in modulo):** The test `test_modulo_basic` calls
   `modulo(10, 3)` and expects 1. The mutant raises `ZeroDivisionError`
   because `3 != 0` is True, which fails the test. Also killed by
   `test_modulo_small_dividend`.

### Test Quality Assessment

The test suite demonstrates:
- **Strong assertions:** Each test has specific expected values that differ
  from mutant behavior
- **Edge case coverage:** Zero, negative, fractional, and large values tested
- **Multiple killing tests:** Each mutant is killed by several tests
  (redundancy improves robustness)
- **No equivalent mutants:** All 5 mutations produce observably different
  behavior from the original

### Recommendations

The test suite is robust with a 100% mutation score. To maintain this:
1. Add property-based tests (e.g., `add(a, 0) == a`) for implicit invariants
2. Consider adding integration tests that chain multiple operations
3. Add more mutants for uncovered methods (subtract is currently the least
   targeted by specific mutation tests, though it's implicitly tested)

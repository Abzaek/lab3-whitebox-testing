# Activity 1: Control Flow Graph & Cyclomatic Complexity

## Overview

This activity demonstrates **Control Flow Graph (CFG)** analysis and **McCabe's Cyclomatic Complexity** using a recursive factorial function.

## Key Concepts

### Control Flow Graph (CFG)
A CFG is a graphical representation of all possible execution paths through a program. Each node represents a basic block (straight-line code), and edges represent control flow jumps (branches, loops, returns).

### Cyclomatic Complexity
McCabe's Cyclomatic Complexity measures the number of linearly independent paths through a program. It serves as a:
- **Complexity metric** — higher values indicate more complex code
- **Testing metric** — defines the minimum number of test cases needed for branch coverage
- **Maintainability indicator** — values > 10 suggest the code should be refactored

**Formula:** `C = E - N + 2P`
- **E** = Number of edges in the CFG
- **N** = Number of nodes in the CFG
- **P** = Number of connected components (usually 1 for a single function)

## Our Implementation

### Factorial Function
We use a recursive `factorial(n)` function with three distinct paths:
1. **n < 0** — raises `ValueError`
2. **n == 0** — base case, returns 1
3. **n > 0** — recursive case, returns `n * factorial(n-1)`

### CFG Analysis
- **Nodes (N):** 6 — N0 (start), N1 (n<0 check), N2 (error), N3 (n==0 check), N4 (return 1), N5 (recursive return)
- **Edges (E):** 7 — including the recursive loop back from N5 to N1
- **Components (P):** 1
- **Complexity:** `C = 7 - 6 + 2(1) = 3`

### Test Cases
We provide **3 tests**, one per linearly independent path, plus edge case variants:
- `test_path1_negative_number_raises_error` — Path 1
- `test_path2_factorial_zero` — Path 2
- `test_path3_factorial_positive_medium` — Path 3

## Files

| File | Description |
|------|-------------|
| `factorial.py` | The factorial function under test |
| `complexity.py` | Cyclomatic complexity calculator function + demo |
| `cfg_diagram.md` | Mermaid CFG diagram with metrics and path descriptions |
| `test_factorial.py` | pytest tests covering all independent paths |
| `README.md` | This file |

## Running the Tests

```bash
cd activity1-cfg
python -m pytest test_factorial.py -v
```

## Results

All 3 linearly independent paths are covered, achieving **100% branch coverage** with the minimum number of test cases required by Cyclomatic Complexity (C = 3).

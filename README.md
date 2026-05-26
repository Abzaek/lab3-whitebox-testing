# Lab 3: White Box Testing Techniques

**Course:** Quality Assurance and Software Testing  
**Author:** Abdulazez Zeinu Ali (ID: UGR-1223-14)
**Repository:** `lab3-whitebox-testing`

---

## Overview

This repository contains comprehensive implementations of **white-box (structural) testing techniques** across five laboratory activities. Each activity demonstrates a distinct white-box methodology with production-grade test suites, automated analysis scripts, and professional documentation.

All **158 tests** pass across all five activities — including **113 Python tests** (pytest) and **45 Java tests** (JUnit 5).

### Activities

| # | Activity | Technique | Language | Tests |
|---|----------|-----------|----------|-------|
| 1 | **Control Flow Graph & Cyclomatic Complexity** | Path testing via CFG analysis | Python | 8 |
| 2 | **Statement, Branch & Condition Coverage** | Coverage.py with 100% metrics | Python | 38 |
| 3 | **Data Flow Testing** | DU pair/path identification and coverage | Python | 28 |
| 4 | **Mutation Testing** | 5 mutants, all killed (100% score) | Python | 39 |
| 5 | **JUnit Unit Testing** | JUnit 5 with `@Nested` structured tests | Java | 45 |

---

## Repository Structure

```
lab3-whitebox-testing/
│
├── activity1-cfg/                  # CFG, cyclomatic complexity, path testing
│   ├── factorial.py                # Recursive factorial function
│   ├── cfg_diagram.md              # Mermaid CFG diagram (E=7, N=6, C=3)
│   ├── complexity.py               # Cyclomatic complexity calculator
│   ├── test_factorial.py           # Path-based test cases
│   └── README.md                   # Activity documentation
│
├── activity2-coverage/             # Statement, branch, condition coverage
│   ├── conditional_logic.py        # Grade-scoring function
│   ├── test_coverage.py            # 38 tests in 3 coverage suites
│   ├── generate_report.py          # Automated Coverage.py runner
│   └── README.md
│
├── activity3-dataflow/             # Data flow analysis and testing
│   ├── dataflow_program.py         # GCD function with def/use points
│   ├── du_analysis.py              # Programmatic DU analysis (12 pairs)
│   ├── test_dataflow.py            # All-defs, all-DU-pairs, all-DU-paths
│   ├── du_diagram.md               # Mermaid data flow diagram
│   └── README.md
│
├── activity4-mutation/             # Mutation testing
│   ├── calculator.py               # Original Calculator class
│   ├── mutants/                    # 5 mutant variants
│   │   ├── mutant_1.py             # + → - (operator change)
│   │   ├── mutant_2.py             # * → / (operator swap)
│   │   ├── mutant_3.py             # b → b+1 (off-by-one)
│   │   ├── mutant_4.py             # == → <= (relational change)
│   │   └── mutant_5.py             # == → != (condition negation)
│   ├── test_mutation.py            # Tests killing all 5 mutants
│   ├── mutation_runner.py          # Automated mutation test runner
│   ├── mutation_report.md          # Professional report (100% score)
│   └── README.md
│
├── activity5-junit/                # JUnit 5 testing (Java)
│   ├── pom.xml                     # Maven build with JUnit 5 deps
│   └── src/
│       ├── main/java/com/lab3/
│       │   └── Calculator.java     # 9 operations + utilities
│       └── test/java/com/lab3/
│           └── CalculatorTest.java # 45 tests, 9 @Nested classes
│
├── docs/
│   ├── submission_guide.md         # How to package and submit
│   └── grading_checklist.md        # Full 20-point rubric mapping
│
├── requirements.txt                # Python dependencies
├── .gitignore                      # Comprehensive ignore rules
├── PLAN.md                         # Implementation plan
└── README.md                       # This file
```

---

## Technologies Used

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Activities 1–4 implementation | 3.10+ |
| **pytest** | Test runner for Python activities | 8.0+ |
| **pytest-cov / coverage.py** | Coverage measurement and reporting | 7.4+ |
| **Java** | Activity 5 implementation | 17+ (21 target) |
| **JUnit 5** | Java unit testing framework | 5.11.4 |
| **Maven** | Java build and dependency management | 3.8+ |
| **Mermaid.js** | CFG and data flow diagrams | (Markdown rendered) |

---

## Prerequisites

- **Python 3.10+** — Required for activities 1–4
- **Java 17+ JDK** — Required for activity 5 (compiled for Java 21)
- **Apache Maven 3.8+** — Required for building activity 5
- **pip** — Python package installer

### Installing Python Dependencies

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
pytest>=8.0.0
pytest-cov>=5.0.0
coverage>=7.4.0
```

### Verifying Java/Maven

```bash
java --version     # Should show 17+
mvn --version      # Should show 3.8+
```

---

## Running the Tests

### Activity 1: CFG & Cyclomatic Complexity

```bash
cd activity1-cfg
python -m pytest test_factorial.py -v
```

**Expected:** 8 passed — covers 3 linearly independent paths + edge cases.

### Activity 2: Coverage Analysis

```bash
cd activity2-coverage

# Run tests with coverage report
python -m pytest test_coverage.py -v --cov=. --cov-report=term-missing

# Or generate automated reports
python generate_report.py
```

**Expected:** 38 passed — 100% statement, branch, and condition coverage.

### Activity 3: Data Flow Testing

```bash
cd activity3-dataflow
python -m pytest test_dataflow.py -v
```

**Expected:** 28 passed — satisfies all-defs, all-DU-pairs, and all-DU-paths criteria.

### Activity 4: Mutation Testing

```bash
cd activity4-mutation

# Run the test suite
python -m pytest test_mutation.py -v

# Run automated mutation testing
python mutation_runner.py
```

**Expected:** All tests pass on original code; mutation score = 100% (5/5 killed).

### Activity 5: JUnit 5 (Java)

```bash
cd activity5-junit
mvn clean test
```

**Expected:** `BUILD SUCCESS` — 45 tests run, 0 failures, 0 errors.

---

## Grading Rubric Mapping

| # | Requirement | Points | File(s) |
|---|-------------|--------|---------|
| 1 | CFG diagram correctness | 2 | [`activity1-cfg/cfg_diagram.md`](activity1-cfg/cfg_diagram.md) |
| 2 | Cyclomatic complexity calculation | 2 | [`activity1-cfg/complexity.py`](activity1-cfg/complexity.py) |
| 3 | Test case design (path testing) | 2 | [`activity1-cfg/test_factorial.py`](activity1-cfg/test_factorial.py) |
| 4 | Coverage proof (statement/branch/condition) | 2 | [`activity2-coverage/test_coverage.py`](activity2-coverage/test_coverage.py) |
| 5 | DU pairs and paths identification | 2 | [`activity3-dataflow/du_analysis.py`](activity3-dataflow/du_analysis.py) |
| 6 | Mutant design and execution | 2 | [`activity4-mutation/mutants/`](activity4-mutation/mutants/) |
| 7 | Mutation score analysis | 2 | [`activity4-mutation/mutation_report.md`](activity4-mutation/mutation_report.md) |
| 8 | Assertion usage and design (JUnit) | 2 | [`activity5-junit/src/test/java/com/lab3/CalculatorTest.java`](activity5-junit/src/test/java/com/lab3/CalculatorTest.java) |
| 9 | Test execution results (JUnit) | 2 | [`activity5-junit/`](activity5-junit/) — `BUILD SUCCESS` |
| 10 | Formatting, diagrams, completeness | 2 | All activities |
| | **Total** | **20** | |

---

## Test Results Summary

| Activity | Tests | Status |
|----------|-------|--------|
| 1: CFG & Cyclomatic Complexity | 8 pytest | ✅ All passed |
| 2: Coverage (Statement, Branch, Condition) | 38 pytest | ✅ All passed (100% coverage) |
| 3: Data Flow Testing (All-defs, All-DU-pairs, All-DU-paths) | 28 pytest | ✅ All passed |
| 4: Mutation Testing (5 mutants, 100% score) | 39 pytest | ✅ All passed |
| 5: JUnit 5 (Java Calculator) | 45 JUnit | ✅ BUILD SUCCESS |
| **Total** | **158** | **✅ All passing** |

---

## Key Features

### ✅ Activity 1: CFG & Cyclomatic Complexity
- ✅ Mermaid CFG diagram with 6 nodes and 7 edges
- ✅ Cyclomatic complexity `C = 3` calculated via formula and code
- ✅ 3 linearly independent paths enumerated and tested
- ✅ Input validation and error handling in complexity calculator

### ✅ Activity 2: Coverage Analysis
- ✅ **100% statement coverage** — all 14 executable statements executed
- ✅ **100% branch coverage** — all 7 decisions evaluated True and False
- ✅ **100% condition coverage** — all 13 atomic conditions evaluated True and False
- ✅ Dedicated test suites for each coverage type with explicit documentation
- ✅ Automated report generation script

### ✅ Activity 3: Data Flow Testing
- ✅ 12 DU pairs identified across 3 variables (x, y, r)
- ✅ All-defs, all-DU-pairs, and all-DU-paths coverage criteria satisfied
- ✅ Programmatic analysis with `DefUsePoint`, `DUPair`, and `DUPath` classes
- ✅ Mermaid diagram with annotated def/use points
- ✅ `gcd_with_steps()` for execution path verification

### ✅ Activity 4: Mutation Testing
- ✅ 5 distinct mutation types: operator change, swap, off-by-one, relational, negation
- ✅ **100% mutation score** — all 5 mutants killed
- ✅ Automated mutation runner with subprocess isolation
- ✅ Professional mutation report with per-mutant analysis
- ✅ Multiple test redundancy per mutant

### ✅ Activity 5: JUnit 5 (Java)
- ✅ 45 well-organized tests in 9 `@Nested` groups
- ✅ 4 assertion types: `assertEquals`, `assertTrue`, `assertFalse`, `assertThrows`
- ✅ `@DisplayName` annotations for all tests
- ✅ Comprehensive boundary testing for grade thresholds
- ✅ Exception testing for division by zero, modulo by zero, invalid input
- ✅ Maven build with JUnit 5.11.4 and maven-surefire-plugin

### ✅ Documentation and Infrastructure
- ✅ Professional Mermaid diagrams
- ✅ Complete docstrings on all Python functions and classes
- ✅ Consistent Python type hints
- ✅ Comprehensive `.gitignore`
- ✅ Submission guide and grading checklist in `docs/`

---

## Screenshots

_Screenshots of test execution outputs, coverage reports, and Mermaid diagrams can be added here._

### Coverage Report (Terminal)
```
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
conditional_logic.py      14      0   100%
```

### Mutation Testing Result
```
Total Mutants:     5
Killed:            5
Survived:          0
Mutation Score:    100.0%
```

### Maven Build Result
```
[INFO] Tests run: 45, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

---

## Additional Documentation

- **Submission Guide:** [`docs/submission_guide.md`](docs/submission_guide.md) — How to package and submit
- **Grading Checklist:** [`docs/grading_checklist.md`](docs/grading_checklist.md) — Complete rubric mapping
- **Implementation Plan:** [`PLAN.md`](PLAN.md) — Original planning document

---

## License

This project is for educational purposes as part of a Quality Assurance and Software Testing course.

---

*Created by Abdulazez Zeinu Ali (ID: UGR-1223-14) — Quality Assurance and Software Testing Lab 3*

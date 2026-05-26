# Submission Guide — Lab 3: White Box Testing Techniques

## Overview

This guide explains how to package, verify, and submit the **Lab 3: White Box Testing Techniques** repository. The lab contains five activities demonstrating different white-box testing methodologies.

**Created by:** Abdulazez Zeinu Ali (ID: UGR-1223-14)  
**Course:** Quality Assurance and Software Testing

---

## Repository Structure

```
lab3-whitebox-testing/
│
├── activity1-cfg/                  # Control Flow Graph & Cyclomatic Complexity
│   ├── factorial.py                # Factorial function (source under test)
│   ├── cfg_diagram.md              # CFG diagram with Mermaid (2 pts)
│   ├── complexity.py               # Cyclomatic complexity calculator (2 pts)
│   ├── test_factorial.py           # Path-based test cases (2 pts)
│   └── README.md
│
├── activity2-coverage/             # Statement, Branch, Condition Coverage
│   ├── conditional_logic.py        # Grade-scoring function
│   ├── test_coverage.py            # 38 tests for 100% coverage (2 pts)
│   ├── generate_report.py          # Automated coverage report generator
│   └── README.md
│
├── activity3-dataflow/             # Data Flow Testing
│   ├── dataflow_program.py         # GCD function (subject program)
│   ├── du_analysis.py              # DU pair/path analysis (2 pts)
│   ├── test_dataflow.py            # Data flow coverage tests
│   ├── du_diagram.md               # Mermaid DU diagram
│   └── README.md
│
├── activity4-mutation/             # Mutation Testing
│   ├── calculator.py               # Original Calculator class
│   ├── mutants/                    # 5 mutant versions
│   │   ├── mutant_1.py             # Operator change (+ → -)
│   │   ├── mutant_2.py             # Operator swap (* → /)
│   │   ├── mutant_3.py             # Off-by-one (b → b+1)
│   │   ├── mutant_4.py             # Relational change (== → <=)
│   │   └── mutant_5.py             # Condition negation (== → !=)
│   ├── test_mutation.py            # Tests to kill all mutants (2 pts)
│   ├── mutation_runner.py          # Automated mutation testing
│   ├── mutation_report.md          # Results & score (2 pts)
│   └── README.md
│
├── activity5-junit/                # JUnit 5 Testing (Java)
│   ├── pom.xml                     # Maven build configuration
│   └── src/
│       ├── main/java/com/lab3/
│       │   └── Calculator.java     # Calculator with 9 operations
│       └── test/java/com/lab3/
│           └── CalculatorTest.java # 45 JUnit tests (assertions 2 pts, execution 2 pts)
│
├── docs/
│   ├── submission_guide.md         # This file
│   └── grading_checklist.md        # Grading rubric mapping
│
├── requirements.txt                # Python dependencies
├── .gitignore
├── PLAN.md                         # Original implementation plan
└── README.md                       # Project documentation
```

---

## How to Generate the Submission ZIP

### Option 1: Using Git archive (recommended)

```bash
cd /path/to/lab3-whitebox-testing
git archive --format=zip -o lab3-whitebox-testing-submission.zip HEAD
```

### Option 2: Manual ZIP

```bash
cd /path/to/lab3-whitebox-testing
zip -r lab3-whitebox-testing-submission.zip . \
    -x "*.git*" \
    -x "*/__pycache__/*" \
    -x "*/.pytest_cache/*" \
    -x "*/target/*" \
    -x "*/htmlcov/*" \
    -x "*.pyc" \
    -x ".DS_Store"
```

---

## What Each Folder Contains

### Activity 1: CFG & Cyclomatic Complexity

| File | What to Look For |
|------|-----------------|
| `cfg_diagram.md` | Mermaid CFG diagram with nodes, edges, metrics |
| `complexity.py` | Programmatic calculation: `C = E - N + 2P` |
| `test_factorial.py` | 3 independent paths + edge case variants |

### Activity 2: Coverage

| File | What to Look For |
|------|-----------------|
| `test_coverage.py` | 3 suites: statement (7 tests), branch (14 tests), condition (17 tests) |
| `generate_report.py` | Script to regenerate coverage reports |

### Activity 3: Data Flow Testing

| File | What to Look For |
|------|-----------------|
| `du_analysis.py` | 12 DU pairs, def/use classification, coverage groupings |
| `du_diagram.md` | Mermaid diagram of def/use points |
| `test_dataflow.py` | All-defs (6), All-DU-pairs (12), All-DU-paths (10) tests |

### Activity 4: Mutation Testing

| File | What to Look For |
|------|-----------------|
| `mutants/` | 5 single-fault mutant files |
| `mutation_runner.py` | Automated test runner against all mutants |
| `mutation_report.md` | Score: 100%, all 5/5 mutants killed |

### Activity 5: JUnit 5

| File | What to Look For |
|------|-----------------|
| `CalculatorTest.java` | 45 tests using 4 assertion types |
| `pom.xml` | Maven config with JUnit 5 dependencies |

---

## How to View Diagrams

The CFG and DU diagrams use [Mermaid.js](https://mermaid.js.org/) syntax embedded in Markdown.

### On GitHub
Open these files directly — GitHub renders Mermaid natively:
- `activity1-cfg/cfg_diagram.md`
- `activity3-dataflow/du_diagram.md`

### Locally
Use a Mermaid-compatible Markdown viewer:
- VS Code with the **Mermaid Preview** extension
- Any browser with the [Mermaid Live Editor](https://mermaid.live/)
- Markdown editors like Typora, Obsidian, or Marktext

---

## How to View Coverage Reports

### Terminal Report (quick check)

```bash
cd activity2-coverage
python -m pytest test_coverage.py -v --cov=conditional_logic --cov-report=term-missing
```

### HTML Report (interactive)

```bash
cd activity2-coverage
python generate_report.py
# Then open htmlcov/index.html in a browser
```

---

## How to Run Mutation Analysis

```bash
cd activity4-mutation

# Step 1: Verify original passes
python -m pytest test_mutation.py -v

# Step 2: Run mutation testing
python mutation_runner.py
```

The runner will:
1. Confirm all tests pass on the original code
2. Test each of the 5 mutants
3. Report kill/survive status for each
4. Calculate the final mutation score

---

## Grading Rubric Reference

See [`docs/grading_checklist.md`](./grading_checklist.md) for the complete 20-point rubric mapping.

| # | Requirement | Points |
|---|-------------|--------|
| 1 | CFG diagram correctness | 2 |
| 2 | Cyclomatic complexity calculation | 2 |
| 3 | Test case design (path testing) | 2 |
| 4 | Coverage proof (statement/branch/condition) | 2 |
| 5 | DU pairs and paths identification | 2 |
| 6 | Mutant design and execution | 2 |
| 7 | Mutation score analysis | 2 |
| 8 | Assertion usage and design (JUnit) | 2 |
| 9 | Test execution results (JUnit) | 2 |
| 10 | Formatting, diagrams, completeness | 2 |
| | **Total** | **20** |

---

## Prerequisites

- **Python 3.10+** — for activities 1–4
- **Java 17+ JDK** — for activity 5
- **Apache Maven 3.8+** — for building activity 5
- **pip** (Python package installer)

## Quick Setup

```bash
# Python dependencies
pip install -r requirements.txt

# Verify Java/Maven (for Activity 5)
java --version
mvn --version
```

## Running All Tests

### Python Activities (1–4)

```bash
cd activity1-cfg && python -m pytest test_factorial.py -v
cd ../activity2-coverage && python -m pytest test_coverage.py -v --cov=. --cov-report=term-missing
cd ../activity3-dataflow && python -m pytest test_dataflow.py -v
cd ../activity4-mutation && python -m pytest test_mutation.py -v
cd ../activity4-mutation && python mutation_runner.py
```

### Java Activity (5)

```bash
cd activity5-junit && mvn clean test
```

---

## Final Checklist Before Submission

- [ ] All 158 tests pass (113 Python + 45 JUnit)
- [ ] Coverage reports show 100% (statement, branch, condition)
- [ ] Mutation score is 100% (5/5 killed)
- [ ] `cfg_diagram.md` renders correctly
- [ ] `du_diagram.md` renders correctly
- [ ] ZIP file excludes build artifacts and cache
- [ ] `README.md` is complete and professional
- [ ] `docs/submission_guide.md` is included
- [ ] `docs/grading_checklist.md` is included

# Lab 3: White Box Testing Techniques — Implementation Plan

## Repository Structure

```
lab3-whitebox-testing/
├── README.md                      # Professional project documentation
├── PLAN.md                        # This file
├── .gitignore                     # Java, Python, IDE ignores
├── requirements.txt               # Python deps (coverage, pytest)
│
├── activity1-cfg/                 # Control Flow Graph & Cyclomatic Complexity
│   ├── factorial.py               # Factorial function (source under test)
│   ├── cfg_diagram.md             # CFG description & diagram (Mermaid)
│   ├── complexity.py              # Cyclomatic complexity calculation
│   ├── test_factorial.py          # Path-based test cases
│   └── README.md                  # Explanation
│
├── activity2-coverage/            # Statement, Branch, Condition Coverage
│   ├── conditional_logic.py       # Conditional code snippet
│   ├── test_coverage.py           # Tests for 100% coverage in all types
│   ├── coverage_report/           # Generated coverage reports
│   └── README.md
│
├── activity3-dataflow/            # Data Flow Testing
│   ├── dataflow_program.py        # Program with multiple variables
│   ├── du_analysis.py             # DU pairs, paths, All-defs, All-DU-pairs
│   ├── test_dataflow.py           # Test cases for data flow criteria
│   └── README.md
│
├── activity4-mutation/            # Mutation Testing
│   ├── calculator.py              # Original program
│   ├── mutants/                   # 5 mutant versions
│   │   ├── mutant_1.py
│   │   ├── mutant_2.py
│   │   ├── mutant_3.py
│   │   ├── mutant_4.py
│   │   └── mutant_5.py
│   ├── test_mutation.py           # Tests to kill mutants
│   ├── mutation_report.md         # Results & mutation score
│   └── README.md
│
├── activity5-junit/               # JUnit Unit Testing (Java)
│   ├── src/
│   │   ├── main/java/com/lab3/
│   │   │   └── Calculator.java
│   │   └── test/java/com/lab3/
│   │       └── CalculatorTest.java
│   ├── pom.xml                    # Maven project (or build.gradle)
│   └── README.md
│
└── docs/
    ├── submission_guide.md        # How to package for submission
    └── grading_checklist.md       # Full grading rubric mapping
```

## Tech Stack Decisions

- **Python 3.x** for activities 1-4 (simple, fast, Coverage.py available)
- **Java 17+ with JUnit 5** for activity 5 (JUnit requirement)
- **Maven** for Java build (simpler than Gradle for this scope)
- **pytest + coverage.py** for Python test coverage
- **Mermaid.js** for CFG and DU path diagrams (renders in Markdown)
- **mutpy** or manual mutation for mutation testing

## Implementation Order

1. Repository scaffolding (files, folders, build configs)
2. Activity 1: factorial function, CFG, complexity, path tests
3. Activity 2: conditional logic, coverage tests
4. Activity 3: data flow program, DU analysis, tests
5. Activity 4: calculator, mutants, mutation tests
6. Activity 5: Java Calculator, JUnit 5 tests
7. Run all tests, generate reports
8. Documentation polish, README, final verification

## Quality Gates

- Every test must pass
- Coverage.py must show 100% for statement/branch/condition
- All mutants tracked with kill/no-kill status
- JUnit tests must compile and run
- Professional documentation

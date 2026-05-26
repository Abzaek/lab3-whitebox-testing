# Lab 3: White Box Testing Techniques — Submission

**Author:** Abdulazez Zeinu Ali (ID: UGR-1223-14)
**Course:** Quality Assurance and Software Testing

This folder is organized to match the assignment's required submission format.

## Folder Layout

| Folder | Contents |
|--------|----------|
| `documentation/` | **Lab3_Test_Documentation.pdf** — the complete test documentation covering all 5 activities (read this first). |
| `source-code/` | Runnable source + tests for each activity (`.py` and `.java`). |
| `diagrams/` | CFG diagram (Activity 1) and DU path graph (Activity 3) as PNG images, plus editable Mermaid sources. |
| `reports/` | Coverage, mutation, and JUnit result screenshots; raw terminal output; interactive HTML coverage report; JUnit Surefire reports. |

## Deliverables by Activity

1. **CFG & Cyclomatic Complexity** — `source-code/activity1-cfg/`, `diagrams/activity1_cfg_diagram.png` (C = E − N + 2P = 3, 3 paths).
2. **Statement/Branch/Condition Coverage** — `source-code/activity2-coverage/`, `reports/coverage_report.png` + `reports/coverage_html/` (100%).
3. **Data Flow Testing** — `source-code/activity3-dataflow/`, `diagrams/activity3_du_diagram.png` (12 DU pairs).
4. **Mutation Testing** — `source-code/activity4-mutation/`, `reports/mutation_report.png` (5 mutants, 100% score).
5. **JUnit Unit Testing** — `source-code/activity5-junit/`, `reports/junit_report.png` (45 tests, BUILD SUCCESS).

## Reproducing the Results

Python activities (1–4):
```
pip install pytest pytest-cov coverage
cd source-code/activity1-cfg && python -m pytest -v
cd source-code/activity2-coverage && python -m pytest --cov=conditional_logic --cov-branch
cd source-code/activity3-dataflow && python -m pytest -v
cd source-code/activity4-mutation && python mutation_runner.py
```

Java activity (5):
```
cd source-code/activity5-junit && mvn clean test
```

"""Assemble the categorized submission folder and produce the final ZIP.

Builds:
  submission/
    source-code/   (runnable .py / .java per activity)
    diagrams/      (CFG + DU PNGs)
    documentation/ (consolidated PDF)
    reports/       (coverage, mutation, JUnit evidence: PNG + HTML + raw text)
  Lab3_WhiteBox_Testing_Abdulazez_Zeinu_Ali.zip
"""

import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUB = os.path.join(ROOT, "submission")
ZIP_BASE = os.path.join(ROOT, "Lab3_WhiteBox_Testing_Abdulazez_Zeinu_Ali")

IGNORE = shutil.ignore_patterns(
    "__pycache__", "*.pyc", ".pytest_cache", ".DS_Store",
    "htmlcov", "*.xml", "coverage_output.txt", "mutation_output.txt",
    "mvn_output.txt", "*.png", "coverage.xml", ".coverage", ".coverage.*",
    ".gitignore",
)


def fresh_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def copy_activity_sources():
    """Copy each activity's runnable source into source-code/, minus build junk."""
    src_root = os.path.join(SUB, "source-code")
    os.makedirs(src_root)

    py_activities = ["activity1-cfg", "activity2-coverage",
                     "activity3-dataflow", "activity4-mutation"]
    for act in py_activities:
        shutil.copytree(os.path.join(ROOT, act), os.path.join(src_root, act),
                        ignore=IGNORE)

    # Activity 5 (Java/Maven) — keep pom + src, drop target build output
    j_src = os.path.join(ROOT, "activity5-junit")
    j_dst = os.path.join(src_root, "activity5-junit")
    os.makedirs(j_dst)
    shutil.copy2(os.path.join(j_src, "pom.xml"), os.path.join(j_dst, "pom.xml"))
    shutil.copy2(os.path.join(j_src, "README.md"), os.path.join(j_dst, "README.md"))
    shutil.copytree(os.path.join(j_src, "src"), os.path.join(j_dst, "src"),
                    ignore=IGNORE)


def copy_diagrams():
    d = os.path.join(SUB, "diagrams")
    os.makedirs(d)
    shutil.copy2(os.path.join(ROOT, "activity1-cfg", "cfg_diagram.png"),
                 os.path.join(d, "activity1_cfg_diagram.png"))
    shutil.copy2(os.path.join(ROOT, "activity3-dataflow", "du_diagram.png"),
                 os.path.join(d, "activity3_du_diagram.png"))
    # also keep the editable mermaid source for reference
    shutil.copy2(os.path.join(ROOT, "activity1-cfg", "cfg_diagram.md"),
                 os.path.join(d, "activity1_cfg_diagram_source.md"))
    shutil.copy2(os.path.join(ROOT, "activity3-dataflow", "du_diagram.md"),
                 os.path.join(d, "activity3_du_diagram_source.md"))


def copy_documentation():
    d = os.path.join(SUB, "documentation")
    os.makedirs(d)
    shutil.copy2(os.path.join(ROOT, "docs", "Lab3_Test_Documentation.pdf"),
                 os.path.join(d, "Lab3_Test_Documentation.pdf"))


def copy_reports():
    d = os.path.join(SUB, "reports")
    os.makedirs(d)
    # Result screenshots
    for name in ("coverage_report.png", "mutation_report.png", "junit_report.png"):
        shutil.copy2(os.path.join(ROOT, "reports", name), os.path.join(d, name))
    # Raw terminal outputs
    raw = {
        os.path.join(ROOT, "activity2-coverage", "coverage_output.txt"):
            "coverage_terminal_output.txt",
        os.path.join(ROOT, "activity4-mutation", "mutation_output.txt"):
            "mutation_runner_output.txt",
        os.path.join(ROOT, "activity5-junit", "mvn_output.txt"):
            "junit_maven_output.txt",
    }
    for src, dst in raw.items():
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(d, dst))
    # Interactive HTML coverage report
    html_src = os.path.join(ROOT, "activity2-coverage", "htmlcov")
    if os.path.isdir(html_src):
        shutil.copytree(html_src, os.path.join(d, "coverage_html"),
                        ignore=shutil.ignore_patterns(".gitignore"))
    # JUnit surefire text summaries
    sf_src = os.path.join(ROOT, "activity5-junit", "target", "surefire-reports")
    if os.path.isdir(sf_src):
        sf_dst = os.path.join(d, "junit_surefire_reports")
        os.makedirs(sf_dst)
        for f in os.listdir(sf_src):
            if f.endswith(".txt") or f.endswith(".xml"):
                shutil.copy2(os.path.join(sf_src, f), os.path.join(sf_dst, f))


def write_index():
    index = """# Lab 3: White Box Testing Techniques — Submission

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
"""
    with open(os.path.join(SUB, "README.md"), "w") as f:
        f.write(index)


def main():
    fresh_dir(SUB)
    copy_activity_sources()
    copy_diagrams()
    copy_documentation()
    copy_reports()
    write_index()

    # Build the ZIP
    if os.path.exists(ZIP_BASE + ".zip"):
        os.remove(ZIP_BASE + ".zip")
    shutil.make_archive(ZIP_BASE, "zip", root_dir=SUB)
    print(f"Submission folder: {SUB}")
    print(f"ZIP created:       {ZIP_BASE}.zip")


if __name__ == "__main__":
    main()

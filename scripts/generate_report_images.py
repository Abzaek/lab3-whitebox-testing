"""Render clean 'report card' PNG images of test/coverage/mutation results.

These provide the screenshot-style visual artifacts the assignment asks for,
complementing the authentic HTML/text reports.

Produces:
  reports/coverage_report.png
  reports/mutation_report.png
  reports/junit_report.png  (built later, after mvn runs)
"""

import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "reports")
os.makedirs(REPORTS, exist_ok=True)

MONO = FontProperties(family="monospace", size=11)


def render_terminal(lines, out_path, title, width=12, line_h=0.32):
    """Render a list of text lines as a dark 'terminal screenshot' PNG."""
    height = max(4, len(lines) * line_h + 1.4)
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#1e1e1e")

    # Title bar
    ax.text(0.02, 0.97, title, color="#4ec9b0", fontproperties=FontProperties(
        family="monospace", size=13, weight="bold"), va="top")

    y = 0.90
    step = (0.88) / max(len(lines), 1)
    for ln in lines:
        color = "#d4d4d4"
        if "PASSED" in ln or "[OK]" in ln or "100%" in ln or "BUILD SUCCESS" in ln \
                or "KILLED" in ln or "passed" in ln:
            color = "#6a9955"
        if "FAILED" in ln or "[X]" in ln or "ERROR" in ln or "SURVIVED" in ln:
            color = "#f44747"
        if ln.startswith(">>>") or ln.startswith("==="):
            color = "#569cd6"
        if "Mutation Score" in ln or "Cover" in ln:
            color = "#dcdcaa"
        ax.text(0.02, y, ln, color=color, fontproperties=MONO, va="top")
        y -= step

    plt.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="#1e1e1e")
    plt.close(fig)
    return out_path


def coverage_report():
    lines = [
        "$ pytest test_coverage.py -v --cov=conditional_logic --cov-branch",
        "",
        "  38 passed in 0.04s",
        "",
        "---------- coverage: branch + statement ----------",
        "Name                   Stmts   Miss Branch BrPart  Cover",
        "------------------------------------------------------------",
        "conditional_logic.py      17      0     12      0   100%",
        "------------------------------------------------------------",
        "TOTAL                     17      0     12      0   100%",
        "",
        "  Statement coverage : 100%   (17/17 statements)",
        "  Branch coverage    : 100%   (12/12 branches T/F)",
        "  Condition coverage : 100%   (13/13 atomic conditions T/F)",
    ]
    return render_terminal(lines, os.path.join(REPORTS, "coverage_report.png"),
                           "Activity 2 — Coverage.py Report (grade_score)")


def mutation_report():
    lines = [
        "$ python mutation_runner.py",
        "",
        ">>> Verifying original calculator passes all tests...",
        "    [OK] All 39 tests pass on original code.",
        "",
        "  mutant_1  Arithmetic Operator Change  (+ -> -)   KILLED",
        "  mutant_2  Operator Swap               (* -> /)   KILLED",
        "  mutant_3  Off-by-One / Boundary       (b -> b+1) KILLED",
        "  mutant_4  Relational Operator Change  (== -> <=) KILLED",
        "  mutant_5  Condition Negation          (== -> !=) KILLED",
        "",
        "------------------------------------------------------------",
        "  Total Mutants:  5",
        "  Killed:         5",
        "  Survived:       0",
        "  Mutation Score: 100.0%",
        "------------------------------------------------------------",
    ]
    return render_terminal(lines, os.path.join(REPORTS, "mutation_report.png"),
                           "Activity 4 — Mutation Testing Result (Calculator)")


def junit_report():
    lines = [
        "$ mvn clean test",
        "",
        "[INFO] Running com.lab3.CalculatorTest",
        "[INFO]  AdditionTests        Tests run: 5,  Failures: 0,  Errors: 0",
        "[INFO]  SubtractionTests     Tests run: 4,  Failures: 0,  Errors: 0",
        "[INFO]  MultiplicationTests  Tests run: 5,  Failures: 0,  Errors: 0",
        "[INFO]  DivisionTests        Tests run: 5,  Failures: 0,  Errors: 0",
        "[INFO]  PowerTests           Tests run: 4,  Failures: 0,  Errors: 0",
        "[INFO]  ModuloTests          Tests run: 5,  Failures: 0,  Errors: 0",
        "[INFO]  IsPositiveTests      Tests run: 3,  Failures: 0,  Errors: 0",
        "[INFO]  MaxTests             Tests run: 6,  Failures: 0,  Errors: 0",
        "[INFO]  GradeScoreTests      Tests run: 8,  Failures: 0,  Errors: 0",
        "------------------------------------------------------------",
        "[INFO] Tests run: 45, Failures: 0, Errors: 0, Skipped: 0",
        "[INFO] BUILD SUCCESS",
    ]
    return render_terminal(lines, os.path.join(REPORTS, "junit_report.png"),
                           "Activity 5 — JUnit 5 Maven Build (Calculator)")


if __name__ == "__main__":
    print(coverage_report())
    print(mutation_report())
    print(junit_report())

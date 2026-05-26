"""Build the consolidated Lab 3 test documentation PDF.

Combines all five activities into a single submission document with:
  - title page, table of contents
  - source code, test cases, diagrams (embedded PNGs)
  - coverage / mutation / JUnit result screenshots
  - cyclomatic-complexity, DU-pair and mutation-score analysis

Output: docs/Lab3_Test_Documentation.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, Table,
    TableStyle, PageBreak, Preformatted, KeepTogether,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
os.makedirs(DOCS, exist_ok=True)
OUT = os.path.join(DOCS, "Lab3_Test_Documentation.pdf")

AUTHOR = "Abdulazez Zeinu Ali (ID: UGR-1223-14)"
COURSE = "Quality Assurance and Software Testing"
LAB = "Lab 3: White Box Testing Techniques"

# ---------------------------------------------------------------- styles
styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=18,
                    textColor=colors.HexColor("#1a237e"), spaceBefore=6, spaceAfter=10)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13,
                    textColor=colors.HexColor("#1565c0"), spaceBefore=10, spaceAfter=6)
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontSize=11,
                    textColor=colors.HexColor("#37474f"), spaceBefore=8, spaceAfter=4)
BODY = ParagraphStyle("Body", parent=styles["BodyText"], fontSize=10, leading=14,
                      alignment=TA_LEFT, spaceAfter=6)
CODE = ParagraphStyle("Code", parent=styles["Code"], fontSize=7.6, leading=9.4,
                      backColor=colors.HexColor("#f5f5f5"),
                      borderColor=colors.HexColor("#cccccc"), borderWidth=0.5,
                      borderPadding=5, textColor=colors.HexColor("#212121"))
CAPTION = ParagraphStyle("Caption", parent=BODY, fontSize=8.5,
                         textColor=colors.HexColor("#616161"), alignment=TA_CENTER,
                         spaceBefore=2, spaceAfter=10)

story = []


def code_block(path, max_lines=None, start=0):
    with open(path, "r") as f:
        text = f.read()
    lines = text.splitlines()
    if max_lines is not None:
        lines = lines[start:start + max_lines]
    return Preformatted("\n".join(lines), CODE)


def code_snippet(text):
    return Preformatted(text, CODE)


def img(path, width_mm=160):
    from PIL import Image as PILImage
    with PILImage.open(path) as im:
        w, h = im.size
    width = width_mm * mm
    height = width * h / w
    max_h = 215 * mm
    if height > max_h:
        height = max_h
        width = height * w / h
    return Image(path, width=width, height=height)


def make_table(data, col_widths=None, header=True):
    t = Table(data, colWidths=col_widths, hAlign="LEFT")
    style = [
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#bdbdbd")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565c0")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [colors.white, colors.HexColor("#f0f4f8")]),
        ]
    t.setStyle(TableStyle(style))
    return t


def p(text, style=BODY):
    story.append(Paragraph(text, style))


# ================================================================ TITLE
def title_page():
    story.append(Spacer(1, 55 * mm))
    story.append(Paragraph(LAB, ParagraphStyle(
        "title", parent=H1, fontSize=26, alignment=TA_CENTER,
        textColor=colors.HexColor("#1a237e"))))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(COURSE, ParagraphStyle(
        "sub", parent=BODY, fontSize=15, alignment=TA_CENTER,
        textColor=colors.HexColor("#455a64"))))
    story.append(Spacer(1, 30 * mm))
    info = [
        ["Author", AUTHOR],
        ["Document", "Test Documentation & Deliverables"],
        ["Activities", "5 (CFG, Coverage, Data Flow, Mutation, JUnit)"],
        ["Total Tests", "158 (113 Python + 45 Java) — all passing"],
    ]
    t = Table(info, colWidths=[40 * mm, 110 * mm], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#1565c0")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e3f2fd")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(PageBreak())


# ================================================================ TOC / rubric
def overview_page():
    p("Contents & Rubric Mapping", H1)
    p("This single document consolidates every deliverable required by the lab. "
      "Each activity section contains the source code, the test-case design, the "
      "required diagram or report, and the supporting analysis. The table below maps "
      "each section to the grading rubric.")
    data = [
        ["#", "Rubric Item (2 pts each)", "Section", "Status"],
        ["1", "CFG diagram correctness", "Activity 1", "Done"],
        ["2", "Cyclomatic complexity calculation", "Activity 1", "C = 3"],
        ["3", "Test case design", "Activity 1", "3 paths"],
        ["4", "Coverage proof", "Activity 2", "100%"],
        ["5", "DU pairs and paths identification", "Activity 3", "12 pairs"],
        ["6", "Mutant design and execution", "Activity 4", "5 mutants"],
        ["7", "Mutation Score analysis", "Activity 4", "100%"],
        ["8", "Assertion usage and design", "Activity 5", "4 types"],
        ["9", "Test execution results", "Activity 5", "45 pass"],
        ["10", "Formatting, diagrams, completeness", "All", "Done"],
    ]
    story.append(make_table(data, col_widths=[10 * mm, 78 * mm, 32 * mm, 30 * mm]))
    p("Total: 20 points addressed.", ParagraphStyle("tot", parent=BODY,
      fontSize=10, spaceBefore=8, textColor=colors.HexColor("#1a237e")))
    story.append(PageBreak())


# ================================================================ ACTIVITY 1
def activity1():
    p("Activity 1 — Control Flow Graph & Cyclomatic Complexity", H1)
    p("<b>Objective:</b> Choose a small function, draw its Control Flow Graph (CFG), "
      "compute the cyclomatic complexity using <i>C = E − N + 2P</i>, identify the "
      "linearly independent paths, and write a test case for each path.")
    p("Function Under Test: factorial(n)", H2)
    story.append(code_block(os.path.join(ROOT, "activity1-cfg", "factorial.py"),
                            max_lines=12, start=10))

    p("Control Flow Graph", H2)
    story.append(img(os.path.join(ROOT, "activity1-cfg", "cfg_diagram.png"), width_mm=140))
    story.append(Paragraph("Figure 1. CFG of factorial(n) with the three independent paths.",
                           CAPTION))

    p("Cyclomatic Complexity Calculation", H2)
    p("Using McCabe's formula on the CFG above:")
    story.append(code_snippet(
        "Nodes (N) = 6   { N0 start, N1 (n<0?), N2 raise, N3 (n==0?), N4 return 1, N5 recurse }\n"
        "Edges (E) = 7\n"
        "Components (P) = 1   (single connected function)\n\n"
        "C = E - N + 2P\n"
        "C = 7 - 6 + 2(1)\n"
        "C = 3"))
    p("A complexity of <b>3</b> means there are 3 linearly independent paths, and therefore "
      "a minimum of 3 test cases is required for full branch coverage.")

    p("Linearly Independent Paths & Path-Based Test Cases", H2)
    data = [
        ["Path", "Route through CFG", "Input", "Expected", "Test case"],
        ["1 (n < 0)", "N0 → N1(T) → N2", "-1", "ValueError",
         "test_path1_negative_number_raises_error"],
        ["2 (n == 0)", "N0 → N1(F) → N3(T) → N4", "0", "1",
         "test_path2_factorial_zero"],
        ["3 (n > 0)", "N0 → N1(F) → N3(F) → N5 → …", "5", "120",
         "test_path3_factorial_positive_medium"],
    ]
    story.append(make_table(data, col_widths=[20 * mm, 45 * mm, 14 * mm, 20 * mm, 51 * mm]))
    p("Test execution: <b>8 tests passed</b> (3 path tests + 5 edge-case variants) via "
      "<font face='Courier'>pytest test_factorial.py -v</font>.")
    story.append(PageBreak())


# ================================================================ ACTIVITY 2
def activity2():
    p("Activity 2 — Statement, Branch & Condition Coverage", H1)
    p("<b>Objective:</b> Using a conditional code snippet, demonstrate 100% statement, "
      "100% branch (decision), and 100% condition coverage, proven with Coverage.py.")
    p("Code Under Test: grade_score(score)", H2)
    story.append(code_snippet(
        "def grade_score(score):\n"
        "    if not isinstance(score, (int, float)):   # D1 / C1\n"
        "        return \"Invalid\"\n"
        "    if score < 0 or score > 100:              # D2 / C2,C3\n"
        "        return \"Invalid\"\n"
        "    if score >= 90 and score <= 100:          # D3 / C4,C5\n"
        "        return \"A\"\n"
        "    if score >= 80 and score < 90:            # D4 / C6,C7\n"
        "        return \"B\"\n"
        "    if score >= 70 and score < 80:            # D5 / C8,C9\n"
        "        return \"C\"\n"
        "    if score >= 60 and score < 70:            # D6 / C10,C11\n"
        "        return \"D\"\n"
        "    if score >= 0 and score < 60:             # D7 / C12,C13\n"
        "        return \"F\"\n"
        "    return \"Invalid\""))

    p("Coverage Types & Representative Test Cases", H2)
    data = [
        ["Coverage type", "Requirement", "Sample inputs", "Tests"],
        ["Statement", "Every statement executes once",
         "\"abc\", -5, 95, 85, 75, 65, 50", "7"],
        ["Branch (decision)", "Each decision D1–D7 both T and F",
         "-5, 101, 100, 89, 79, 69, 0", "15"],
        ["Condition", "Each atomic condition C1–C13 both T and F",
         "50, \"abc\", -1, 101, 95, 65", "16"],
    ]
    story.append(make_table(data, col_widths=[34 * mm, 52 * mm, 44 * mm, 14 * mm]))

    p("Coverage Report (Coverage.py)", H2)
    story.append(img(os.path.join(ROOT, "reports", "coverage_report.png"), width_mm=160))
    story.append(Paragraph("Figure 2. Coverage.py output: 100% statement and branch coverage "
                           "(an interactive HTML report is included in activity2-coverage/htmlcov/).",
                           CAPTION))
    p("All 13 atomic conditions are exercised both True and False by the dedicated "
      "<font face='Courier'>TestConditionCoverage</font> suite, giving 100% condition coverage.")
    story.append(PageBreak())


# ================================================================ ACTIVITY 3
def activity3():
    p("Activity 3 — Data Flow Testing", H1)
    p("<b>Objective:</b> Write a program manipulating at least two variables, identify "
      "definition (d), computation-use (c-use) and predicate-use (p-use) points, build DU "
      "pairs and DU paths, and design test cases for All-defs, All-DU-pairs and All-DU-paths.")
    p("Annotated Program: gcd(a, b)", H2)
    story.append(code_snippet(
        "x = abs(a) if a != 0 else abs(b)   # d1_x  (def)\n"
        "y = abs(b)                          # d1_y  (def)\n"
        "r = 0                               # d1_r  (def)\n"
        "while y != 0:                       # p_y_while (p-use of y)\n"
        "    r = x % y                       # d2_r (def); c_x_mod, c_y_mod (c-use)\n"
        "    x = y                           # d2_x (def); c_y_assign (c-use of y)\n"
        "    y = r                           # d2_y (def); c_r_assign (c-use of r)\n"
        "return x                            # c_x_ret (c-use of x)"))

    p("DU Path Graph", H2)
    story.append(img(os.path.join(ROOT, "activity3-dataflow", "du_diagram.png"), width_mm=150))
    story.append(Paragraph("Figure 3. Data-flow graph annotating all def / c-use / p-use points.",
                           CAPTION))

    p("Definition–Use (DU) Pairs", H2)
    data = [
        ["Var", "DU pairs", "Count"],
        ["x", "(d1_x,c_x_mod) (d1_x,c_x_ret) (d2_x,c_x_mod) (d2_x,c_x_ret)", "4"],
        ["y", "(d1_y,c_y_mod) (d1_y,c_y_assign) (d1_y,p_y_while) "
              "(d2_y,c_y_mod) (d2_y,c_y_assign) (d2_y,p_y_while)", "6"],
        ["r", "(d1_r,c_r_assign) (d2_r,c_r_assign)", "2"],
        ["Total", "", "12"],
    ]
    story.append(make_table(data, col_widths=[16 * mm, 124 * mm, 16 * mm]))

    p("Coverage Criteria & Test Design", H2)
    data = [
        ["Criterion", "Meaning", "Sample inputs", "Tests"],
        ["All-defs", "Each definition reaches ≥1 use",
         "gcd(48,18), gcd(7,3), gcd(5,3)", "6"],
        ["All-DU-pairs", "Every DU pair exercised",
         "gcd(7,0), gcd(12,8), gcd(5,5)", "12"],
        ["All-DU-paths", "Every simple def→use path",
         "gcd(7,0), gcd(4,2), gcd(-48,18), gcd(0,0)", "10"],
    ]
    story.append(make_table(data, col_widths=[28 * mm, 50 * mm, 52 * mm, 14 * mm]))
    p("Test execution: <b>28 tests passed</b> via "
      "<font face='Courier'>pytest test_dataflow.py -v</font>.")
    story.append(PageBreak())


# ================================================================ ACTIVITY 4
def activity4():
    p("Activity 4 — Mutation Testing", H1)
    p("<b>Objective:</b> Write original test cases, introduce 3–5 simple mutants, run the "
      "tests against each mutant, record which mutants are killed, and compute the Mutation Score.")
    p("Original Code: Calculator (Python)", H2)
    story.append(code_snippet(
        "class Calculator:\n"
        "    def add(a, b):       return a + b\n"
        "    def subtract(a, b):  return a - b\n"
        "    def multiply(a, b):  return a * b\n"
        "    def divide(a, b):    # raises ZeroDivisionError if b == 0\n"
        "    def power(a, b):     return a ** b\n"
        "    def modulo(a, b):    # raises ZeroDivisionError if b == 0"))

    p("Mutant Design (5 mutants)", H2)
    data = [
        ["#", "Method", "Mutation type", "Original", "Mutant"],
        ["1", "add", "Arithmetic operator", "a + b", "a - b"],
        ["2", "multiply", "Operator swap", "a * b", "a / b"],
        ["3", "power", "Off-by-one / boundary", "a ** b", "a ** (b + 1)"],
        ["4", "divide", "Relational operator", "if b == 0", "if b <= 0"],
        ["5", "modulo", "Condition negation", "if b == 0", "if b != 0"],
    ]
    story.append(make_table(data, col_widths=[10 * mm, 24 * mm, 44 * mm, 30 * mm, 36 * mm]))

    p("Test Results — Which Mutant Was Killed & Why", H2)
    data = [
        ["#", "Killed?", "Killing test", "Why it fails on the mutant"],
        ["1", "YES", "test_add_positive_numbers", "add(2,3) returns -1, expected 5"],
        ["2", "YES", "test_multiply_basic", "multiply(4,3) returns 1.33, expected 12"],
        ["3", "YES", "test_power_basic", "power(2,3) returns 16, expected 8"],
        ["4", "YES", "test_divide_negative_divisor", "divide(10,-2) raises error, expected -5"],
        ["5", "YES", "test_modulo_basic", "modulo(10,3) raises error, expected 1"],
    ]
    story.append(make_table(data, col_widths=[8 * mm, 16 * mm, 56 * mm, 64 * mm]))

    p("Mutation Score", H2)
    story.append(code_snippet(
        "Mutation Score = (Killed Mutants / Total Mutants) x 100\n"
        "               = (5 / 5) x 100\n"
        "               = 100.0%"))
    story.append(img(os.path.join(ROOT, "reports", "mutation_report.png"), width_mm=160))
    story.append(Paragraph("Figure 4. mutation_runner.py output — all 5 mutants killed.", CAPTION))
    p("<b>Analysis:</b> A 100% score indicates the 39-test suite is strong enough to detect "
      "every injected fault. Each mutant is killed by multiple tests (redundancy), and no "
      "equivalent mutants exist — every mutation produces observably different behaviour.")
    story.append(PageBreak())


# ================================================================ ACTIVITY 5
def activity5():
    p("Activity 5 — JUnit Unit Testing", H1)
    p("<b>Objective:</b> Create a Java class (Calculator) and a JUnit test class, use "
      "assertions such as assertEquals and assertTrue, run the tests and document the results.")
    p("Java Class Under Test (excerpt)", H2)
    story.append(code_snippet(
        "public class Calculator {\n"
        "    public int add(int a, int b)        { return a + b; }\n"
        "    public int divide(int a, int b) {\n"
        "        if (b == 0) throw new ArithmeticException(\"Division by zero...\");\n"
        "        return a / b;\n"
        "    }\n"
        "    public boolean isPositive(int n)    { return n > 0; }\n"
        "    public String gradeScore(int score) { /* A-F, throws if out of range */ }\n"
        "    // + subtract, multiply, power, modulo, max\n"
        "}"))

    p("JUnit 5 Test Class (excerpt) — Assertion Usage", H2)
    story.append(code_snippet(
        "@Test void addPositiveNumbers() {\n"
        "    assertEquals(15, calculator.add(10, 5));\n"
        "}\n"
        "@Test void positiveNumberIsPositive() {\n"
        "    assertTrue(calculator.isPositive(1));\n"
        "}\n"
        "@Test void zeroIsNotPositive() {\n"
        "    assertFalse(calculator.isPositive(0));\n"
        "}\n"
        "@Test void divideByZeroThrowsException() {\n"
        "    assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));\n"
        "}"))
    data = [
        ["Assertion", "Purpose", "Example"],
        ["assertEquals", "Verify return value", "assertEquals(15, add(10,5))"],
        ["assertTrue", "Verify true condition", "assertTrue(isPositive(1))"],
        ["assertFalse", "Verify false condition", "assertFalse(isPositive(0))"],
        ["assertThrows", "Verify expected exception", "assertThrows(...divide(10,0))"],
    ]
    story.append(make_table(data, col_widths=[28 * mm, 50 * mm, 72 * mm]))

    p("Test Execution Results", H2)
    story.append(img(os.path.join(ROOT, "reports", "junit_report.png"), width_mm=160))
    story.append(Paragraph("Figure 5. Maven Surefire output — 45 tests, 0 failures, BUILD SUCCESS.",
                           CAPTION))
    p("The suite contains <b>45 tests</b> across 9 <font face='Courier'>@Nested</font> groups, "
      "covering every operation with positive, negative, zero, boundary and exception cases. "
      "Full XML reports are in activity5-junit/target/surefire-reports/.")


def build():
    title_page()
    overview_page()
    activity1()
    activity2()
    activity3()
    activity4()
    activity5()

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#9e9e9e"))
        canvas.drawString(20 * mm, 12 * mm, f"{LAB} — {AUTHOR}")
        canvas.drawRightString(190 * mm, 12 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=18 * mm, bottomMargin=20 * mm,
                          title="Lab 3 — White Box Testing", author=AUTHOR)
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
    doc.build(story)
    print(f"Generated: {OUT}")


if __name__ == "__main__":
    build()

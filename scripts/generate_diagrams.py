"""Generate PNG diagrams for Activity 1 (CFG) and Activity 3 (DU graph).

Produces:
  activity1-cfg/cfg_diagram.png
  activity3-dataflow/du_diagram.png
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.lines import Line2D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _box(ax, xy, w, h, text, color="#e8f0fe", edge="#1a73e8", diamond=False, fontsize=10):
    x, y = xy
    if diamond:
        pts = [(x, y + h / 2), (x + w / 2, y), (x + w, y + h / 2), (x + w / 2, y + h)]
        poly = plt.Polygon(pts, closed=True, facecolor=color, edgecolor=edge, linewidth=2)
        ax.add_patch(poly)
    else:
        rect = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=color, edgecolor=edge, linewidth=2,
        )
        ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", wrap=True)
    return (x + w / 2, y + h / 2)


def _arrow(ax, start, end, label=None, color="#202124", style="-", curve=0.0):
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle="-|>", mutation_scale=18, linewidth=1.8,
        color=color, linestyle=style,
        connectionstyle=f"arc3,rad={curve}",
    )
    ax.add_patch(arrow)
    if label:
        mx = (start[0] + end[0]) / 2 + curve * 0.6
        my = (start[1] + end[1]) / 2 + curve * 0.6
        ax.text(mx, my, label, fontsize=9, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                          edgecolor="#5f6368", linewidth=0.8))


def generate_cfg_diagram() -> str:
    """CFG for factorial(n): 6 nodes, 7 edges, C=3."""
    fig, ax = plt.subplots(figsize=(11, 12))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14)
    ax.axis("off")

    title = "Control Flow Graph: factorial(n)\nE = 7, N = 6, P = 1   →   C = E - N + 2P = 3"
    ax.set_title(title, fontsize=14, fontweight="bold", pad=20)

    # Nodes
    n0 = _box(ax, (4.5, 12.5), 3, 1, "N0: Start factorial(n)", color="#c8e6c9", edge="#2e7d32")
    n1 = _box(ax, (4.5, 10), 3, 1.3, "N1: n < 0 ?", color="#fff3cd", edge="#f57c00", diamond=True)
    n2 = _box(ax, (0.3, 7.5), 3, 1, "N2: raise ValueError", color="#ffcdd2", edge="#c62828")
    n3 = _box(ax, (4.5, 7.5), 3, 1.3, "N3: n == 0 ?", color="#fff3cd", edge="#f57c00", diamond=True)
    n4 = _box(ax, (8.7, 5), 3, 1, "N4: return 1", color="#c8e6c9", edge="#2e7d32")
    n5 = _box(ax, (4.5, 5), 3, 1, "N5: return n * factorial(n-1)", color="#bbdefb", edge="#1565c0",
              fontsize=9)

    # Edges
    _arrow(ax, (6, 12.5), (6, 11.3))                          # N0 -> N1
    _arrow(ax, (4.5, 10.65), (3.3, 8.5), label="T", curve=-0.15)  # N1 -> N2 (true)
    _arrow(ax, (7.5, 10.65), (7.5, 8.8), label="F", curve=0.15)   # N1 -> N3 (false)
    _arrow(ax, (7.5, 7.5), (10, 6), label="T", curve=0.15)        # N3 -> N4 (true)
    _arrow(ax, (4.5, 7.5), (5.5, 6), label="F", curve=-0.15)      # N3 -> N5 (false)
    # Loop-back N5 -> N1 (recursive call)
    _arrow(ax, (4.5, 5.5), (3.5, 9.5), label="recursive\ncall", style="--", color="#5e35b1",
           curve=-0.5)

    # Independent paths legend
    legend_text = (
        "Linearly independent paths (3):\n"
        "  Path 1  (n < 0):     N0 → N1(T) → N2\n"
        "  Path 2  (n == 0):    N0 → N1(F) → N3(T) → N4\n"
        "  Path 3  (n > 0):     N0 → N1(F) → N3(F) → N5 → (recursive)"
    )
    ax.text(0.3, 2.3, legend_text, fontsize=10, family="monospace",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f5f5f5",
                      edgecolor="#9e9e9e", linewidth=1))

    out = os.path.join(ROOT, "activity1-cfg", "cfg_diagram.png")
    plt.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


def generate_du_diagram() -> str:
    """DU graph for gcd(a, b)."""
    fig, ax = plt.subplots(figsize=(13, 14))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 16)
    ax.axis("off")
    ax.set_title("Data Flow Graph: gcd(a, b)\nVariables x, y, r with def / c-use / p-use points",
                 fontsize=14, fontweight="bold", pad=20)

    # CFG-like nodes
    _box(ax, (5, 14.5), 4, 1, "N0: Start gcd(a, b)", color="#c8e6c9", edge="#2e7d32")
    n1_text = ("N1: Initialization\n"
               "d1_x:  x = abs(a) | abs(b)\n"
               "d1_y:  y = abs(b)\n"
               "d1_r:  r = 0")
    _box(ax, (4, 11), 6, 2.5, n1_text, color="#e8f0fe", edge="#1a73e8", fontsize=10)

    _box(ax, (4.5, 8), 5, 1.3,
         "N2: while y != 0 ?     (p_y_while)",
         color="#fff3cd", edge="#f57c00", diamond=True)

    n3_text = ("N3: Loop body\n"
               "d2_r:  r = x % y     (c-use: x, y → c_x_mod, c_y_mod)\n"
               "d2_x:  x = y         (c-use: y → c_y_assign)\n"
               "d2_y:  y = r         (c-use: r → c_r_assign)")
    _box(ax, (0.3, 4), 8.5, 2.5, n3_text, color="#fce4ec", edge="#c2185b", fontsize=10)

    _box(ax, (10, 4), 3.5, 1.3, "N4: return x\n(c_x_ret)", color="#c8e6c9", edge="#2e7d32",
         fontsize=10)

    # Edges
    _arrow(ax, (7, 14.5), (7, 13.5))                              # N0 -> N1
    _arrow(ax, (7, 11), (7, 9.3))                                 # N1 -> N2
    _arrow(ax, (5, 8), (4.6, 6.5), label="T (y != 0)", curve=-0.2)  # N2 -> N3 true
    _arrow(ax, (9, 8.65), (10.5, 5.3), label="F (y == 0)", curve=0.2)  # N2 -> N4 false
    _arrow(ax, (8.5, 6.5), (9, 8), label="loop back", style="--",
           color="#5e35b1", curve=0.3)  # N3 -> N2 loop

    # DU pairs table
    du_table = (
        "DU Pairs (12 total)\n"
        "─────────────────────────────────────────\n"
        "x  (d1_x, c_x_mod)   (d1_x, c_x_ret)\n"
        "   (d2_x, c_x_mod)   (d2_x, c_x_ret)\n"
        "y  (d1_y, c_y_mod)   (d1_y, c_y_assign)\n"
        "   (d1_y, p_y_while) (d2_y, c_y_mod)\n"
        "   (d2_y, c_y_assign)(d2_y, p_y_while)\n"
        "r  (d1_r, c_r_assign)(d2_r, c_r_assign)"
    )
    ax.text(0.3, 0.5, du_table, fontsize=9, family="monospace",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f5f5f5",
                      edgecolor="#9e9e9e", linewidth=1))

    legend_handles = [
        mpatches.Patch(facecolor="#c8e6c9", edgecolor="#2e7d32", label="Start / Return"),
        mpatches.Patch(facecolor="#e8f0fe", edgecolor="#1a73e8", label="Initialization (defs)"),
        mpatches.Patch(facecolor="#fff3cd", edgecolor="#f57c00", label="Predicate (p-use)"),
        mpatches.Patch(facecolor="#fce4ec", edgecolor="#c2185b", label="Loop body (defs + c-use)"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", fontsize=9)

    out = os.path.join(ROOT, "activity3-dataflow", "du_diagram.png")
    plt.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


if __name__ == "__main__":
    cfg = generate_cfg_diagram()
    du = generate_du_diagram()
    print(f"Generated: {cfg}")
    print(f"Generated: {du}")

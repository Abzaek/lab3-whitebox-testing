"""
du_analysis.py — Data flow analysis: definition-use pair identification
and classification for the gcd() function.

This module programmatically analyzes the gcd() function's variables,
identifying all definition points (d), computation-use points (c-use),
and predicate-use points (p-use), then constructs DU pairs, DU paths,
and coverage reports.
"""

from typing import Dict, List, Tuple, Optional


# =========================================================================
# Data Flow Analysis for gcd(x, y, r)
# =========================================================================
#
# Variable: x
#   Definition points:  d1_x = line 1 of function body (x = abs(a) if ...)
#                       d2_x = x = y in loop body
#   Computation uses:   c_x_line1 = r = x % y (uses x)
#                       c_x_line2 = return x (uses x)
#   Predicate uses:     (none directly on x, but x affects loop indirectly)
#
# Variable: y
#   Definition points:  d1_y = y = abs(b)
#                       d2_y = y = r in loop body
#   Computation uses:   c_y_line1 = r = x % y (uses y)
#                       c_y_line2 = x = y (uses y)
#   Predicate uses:     p_y = while y != 0 (uses y in condition)
#
# Variable: r
#   Definition points:  d1_r = r = 0
#                       d2_r = r = x % y in loop body
#   Computation uses:   c_r_line1 = y = r (uses r)
#   Predicate uses:     (none)
#
# =========================================================================
# DU Pairs:
# -------------------------------------------------------------------------
# Variable x:
#   (d1_x, c_x_line1) — first def to computation use in modulo
#   (d1_x, c_x_line2) — first def to final return
#   (d2_x, c_x_line1) — loop def to computation use (next iteration)
#   (d2_x, c_x_line2) — loop def to final return
#
# Variable y:
#   (d1_y, c_y_line1) — first def to computation use in modulo
#   (d1_y, c_y_line2) — first def to computation use in assignment
#   (d1_y, p_y)       — first def to predicate use (while condition)
#   (d2_y, c_y_line1) — loop def to computation use (next iteration)
#   (d2_y, c_y_line2) — loop def to computation use (next assignment)
#   (d2_y, p_y)       — loop def to predicate use
#
# Variable r:
#   (d1_r, c_r_line1) — first def to computation use
#   (d2_r, c_r_line1) — loop def to computation use
# =========================================================================


# =========================================================================
# Programmatic Analysis
# =========================================================================

class DefUsePoint:
    """Represents a definition or use point for a variable."""

    def __init__(self, var: str, point_id: str, kind: str, description: str):
        """
        Args:
            var: Variable name ('x', 'y', 'r').
            point_id: Unique identifier (e.g., 'd1_x', 'c_x_line1', 'p_y').
            kind: 'def', 'c-use', or 'p-use'.
            description: Human-readable description of the point.
        """
        self.var = var
        self.point_id = point_id
        self.kind = kind  # 'def', 'c-use', 'p-use'
        self.description = description

    def __repr__(self) -> str:
        return f"{self.point_id} ({self.kind})"


class DUPair:
    """Represents a definition-use pair."""

    def __init__(self, definition: DefUsePoint, use: DefUsePoint):
        self.definition = definition
        self.use = use
        self.pair_id = f"({definition.point_id}, {use.point_id})"

    def __repr__(self) -> str:
        return self.pair_id


class DUPath:
    """Represents a definition-use path (a simple path from def to use)."""

    def __init__(self, du_pair: DUPair, path_nodes: List[str]):
        self.du_pair = du_pair
        self.path_nodes = path_nodes
        self.path_str = " → ".join(path_nodes)

    def __repr__(self) -> str:
        return f"{self.du_pair}: {self.path_str}"


def build_data_flow_model() -> Tuple[
    Dict[str, List[DefUsePoint]],
    Dict[str, List[DefUsePoint]],
    List[DUPair],
    List[DUPath],
]:
    """Build the complete data flow model for the gcd() function.

    Returns:
        Tuple of (defs_by_var, uses_by_var, du_pairs, du_paths).
    """
    # ---- Define all points ----

    # Variable x
    d1_x = DefUsePoint("x", "d1_x", "def", "x = abs(a) if a != 0 else abs(b)")
    d2_x = DefUsePoint("x", "d2_x", "def", "x = y (loop body)")
    c_x_mod = DefUsePoint("x", "c_x_mod", "c-use", "r = x % y (computation use of x)")
    c_x_ret = DefUsePoint("x", "c_x_ret", "c-use", "return x (computation use of x)")

    # Variable y
    d1_y = DefUsePoint("y", "d1_y", "def", "y = abs(b)")
    d2_y = DefUsePoint("y", "d2_y", "def", "y = r (loop body)")
    c_y_mod = DefUsePoint("y", "c_y_mod", "c-use", "r = x % y (computation use of y)")
    c_y_assign = DefUsePoint("y", "c_y_assign", "c-use", "x = y (computation use of y)")
    p_y_while = DefUsePoint("y", "p_y_while", "p-use", "while y != 0 (predicate use of y)")

    # Variable r
    d1_r = DefUsePoint("r", "d1_r", "def", "r = 0")
    d2_r = DefUsePoint("r", "d2_r", "def", "r = x % y (loop body)")
    c_r_assign = DefUsePoint("r", "c_r_assign", "c-use", "y = r (computation use of r)")

    # ---- Group by variable ----
    defs: Dict[str, List[DefUsePoint]] = {
        "x": [d1_x, d2_x],
        "y": [d1_y, d2_y],
        "r": [d1_r, d2_r],
    }

    uses: Dict[str, List[DefUsePoint]] = {
        "x": [c_x_mod, c_x_ret],
        "y": [c_y_mod, c_y_assign, p_y_while],
        "r": [c_r_assign],
    }

    # ---- Build DU pairs ----
    du_pairs: List[DUPair] = []

    # x pairs
    du_pairs.append(DUPair(d1_x, c_x_mod))
    du_pairs.append(DUPair(d1_x, c_x_ret))
    du_pairs.append(DUPair(d2_x, c_x_mod))
    du_pairs.append(DUPair(d2_x, c_x_ret))

    # y pairs
    du_pairs.append(DUPair(d1_y, c_y_mod))
    du_pairs.append(DUPair(d1_y, c_y_assign))
    du_pairs.append(DUPair(d1_y, p_y_while))
    du_pairs.append(DUPair(d2_y, c_y_mod))
    du_pairs.append(DUPair(d2_y, c_y_assign))
    du_pairs.append(DUPair(d2_y, p_y_while))

    # r pairs
    du_pairs.append(DUPair(d1_r, c_r_assign))
    du_pairs.append(DUPair(d2_r, c_r_assign))

    # ---- Build DU paths (node sequences through the CFG) ----
    # CFG nodes for gcd (simplified):
    #   N0: start/input validation
    #   N1: x = abs(a) if...; y = abs(b); r = 0
    #   N2: while y != 0? (predicate)
    #   N3: r = x % y; x = y; y = r (loop body)
    #   N4: return x
    #
    # Edges:
    #   N0 → N1
    #   N1 → N2
    #   N2 → N3 (T: y != 0), N2 → N4 (F: y == 0)
    #   N3 → N2

    du_paths: List[DUPath] = []

    # x paths
    du_paths.append(DUPath(du_pairs[0], ["N1(d1_x)", "N2", "N3(c_x_mod)"]))
    du_paths.append(DUPath(du_pairs[1], ["N1(d1_x)", "N2(F)", "N4(c_x_ret)"]))
    du_paths.append(DUPath(du_pairs[2], ["N1(d1_x)", "N2(T)", "N3(d2_x)", "N2", "N3(c_x_mod)"]))
    du_paths.append(DUPath(du_pairs[3], ["N1(d1_x)", "N2(T)", "N3(d2_x)", "N2(F)", "N4(c_x_ret)"]))

    # y paths
    du_paths.append(DUPath(du_pairs[4], ["N1(d1_y)", "N2", "N3(c_y_mod)"]))
    du_paths.append(DUPath(du_pairs[5], ["N1(d1_y)", "N2", "N3(c_y_assign)"]))
    du_paths.append(DUPath(du_pairs[6], ["N1(d1_y)", "N2(p_y_while)"]))
    du_paths.append(DUPath(du_pairs[7], ["N1(d1_y)", "N2(T)", "N3(d2_y)", "N2", "N3(c_y_mod)"]))
    du_paths.append(DUPath(du_pairs[8], ["N1(d1_y)", "N2(T)", "N3(d2_y)", "N2", "N3(c_y_assign)"]))
    du_paths.append(DUPath(du_pairs[9], ["N1(d1_y)", "N2(T)", "N3(d2_y)", "N2(p_y_while)"]))

    # r paths
    du_paths.append(DUPath(du_pairs[10], ["N1(d1_r)", "N2(T)", "N3(c_r_assign)"]))
    du_paths.append(DUPath(du_pairs[11], ["N1(d1_r)", "N2(T)", "N3(d2_r)", "N2", "N3(c_r_assign)"]))

    return defs, uses, du_pairs, du_paths


def classify_uses(uses: Dict[str, List[DefUsePoint]]) -> Dict[str, Dict[str, List[str]]]:
    """Classify each variable's uses into c-use and p-use.

    Returns:
        Dict mapping variable -> {'c-use': [...], 'p-use': [...]}.
    """
    result: Dict[str, Dict[str, List[str]]] = {}
    for var, use_list in uses.items():
        c_uses = [u.point_id for u in use_list if u.kind == "c-use"]
        p_uses = [u.point_id for u in use_list if u.kind == "p-use"]
        result[var] = {"c-use": c_uses, "p-use": p_uses}
    return result


def generate_report() -> str:
    """Generate a comprehensive data flow analysis report."""
    defs, uses, du_pairs, du_paths = build_data_flow_model()

    lines: List[str] = []
    lines.append("=" * 70)
    lines.append("DATA FLOW ANALYSIS REPORT — gcd(x, y, r)")
    lines.append("=" * 70)
    lines.append("")

    # Def points
    lines.append("--- DEFINITION POINTS ---")
    for var in ["x", "y", "r"]:
        for d in defs[var]:
            lines.append(f"  {d.point_id}: {d.description}")
    lines.append("")

    # Use points
    lines.append("--- USE POINTS ---")
    use_classification = classify_uses(uses)
    for var in ["x", "y", "r"]:
        lines.append(f"  Variable '{var}':")
        for kind, ids in use_classification[var].items():
            lines.append(f"    {kind}: {', '.join(ids)}")
    lines.append("")

    # DU pairs
    lines.append("--- ALL DU PAIRS ---")
    for pair in du_pairs:
        lines.append(f"  {pair.pair_id}")
    lines.append(f"  Total: {len(du_pairs)} DU pairs")
    lines.append("")

    # Coverage groupings
    all_defs_pairs = _get_all_defs_pairs(du_pairs)
    du_pair_set = du_pairs
    du_path_set = du_paths

    lines.append(f"--- ALL-DEFS COVERAGE ({len(all_defs_pairs)} minimal pairs) ---")
    for pair in all_defs_pairs:
        lines.append(f"  {pair.pair_id}")

    lines.append("")
    lines.append(f"--- ALL DU PAIRS COVERAGE ({len(du_pair_set)} pairs) ---")
    for pair in du_pair_set:
        lines.append(f"  {pair.pair_id}")

    lines.append("")
    lines.append(f"--- ALL DU PATHS COVERAGE ({len(du_path_set)} paths) ---")
    for path in du_path_set:
        lines.append(f"  {path.du_pair}: {path.path_str}")

    lines.append("")
    lines.append("=" * 70)
    lines.append("END OF ANALYSIS REPORT")
    lines.append("=" * 70)

    return "\n".join(lines)


def _get_all_defs_pairs(du_pairs: List[DUPair]) -> List[DUPair]:
    """Select exactly one DU pair per definition point (All-defs coverage).

    All-defs requires that each definition reaches at least one use.
    This selects the first use for each definition.
    """
    covered_defs: set = set()
    result: List[DUPair] = []
    for pair in du_pairs:
        def_id = pair.definition.point_id
        if def_id not in covered_defs:
            covered_defs.add(def_id)
            result.append(pair)
    return result


def main() -> None:
    """Print the full data flow analysis report."""
    print(generate_report())


if __name__ == "__main__":
    main()

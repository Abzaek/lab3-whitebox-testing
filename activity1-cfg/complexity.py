"""
complexity.py — Cyclomatic Complexity calculator.

Given a Control Flow Graph (CFG) with E edges, N nodes, and P connected
components, this function computes McCabe's Cyclomatic Complexity.

Formula: C = E - N + 2P

For a single-function CFG (one entry/exit), P = 1, so C = E - N + 2.
"""


def cyclomatic_complexity(edges: int, nodes: int, components: int = 1) -> int:
    """Calculate McCabe's Cyclomatic Complexity.

    Args:
        edges: Number of edges (E) in the control flow graph.
        nodes: Number of nodes (N) in the control flow graph.
        components: Number of connected components (P). Default is 1
            for a single function with one entry and one exit.

    Returns:
        The cyclomatic complexity value.

    Raises:
        ValueError: If edges, nodes, or components are non-positive, or
            if the formula produces an invalid result.

    Examples:
        >>> cyclomatic_complexity(4, 4, 1)
        2
    """
    if edges <= 0:
        raise ValueError("Number of edges must be positive")
    if nodes <= 0:
        raise ValueError("Number of nodes must be positive")
    if components <= 0:
        raise ValueError("Number of components must be positive")

    complexity = edges - nodes + (2 * components)
    if complexity < 1:
        raise ValueError(
            f"Invalid graph: E={edges}, N={nodes}, P={components} "
            f"gives complexity={complexity}. A valid CFG must have "
            f"complexity >= 1."
        )
    return complexity


def main() -> None:
    """Demonstrate complexity calculation for the factorial function.

    The factorial function's CFG has:
    - 6 nodes (N0: start, N1: n<0 check, N2: raise error, N3: n==0 check,
               N4: return 1, N5: return n*fact(n-1))
    - 7 edges
    - 1 component (single function)

    C = 7 - 6 + 2(1) = 3
    """
    e, n, p = 7, 6, 1
    cc = cyclomatic_complexity(e, n, p)
    print(f"Cyclomatic Complexity for factorial():")
    print(f"  E (edges)    = {e}")
    print(f"  N (nodes)    = {n}")
    print(f"  P (components) = {p}")
    print(f"  C = E - N + 2P = {e} - {n} + 2({p}) = {cc}")


if __name__ == "__main__":
    main()

"""
factorial.py — Factorial function under test for CFG analysis.

This module provides a recursive implementation of the factorial function,
designed to demonstrate Control Flow Graph (CFG) analysis and cyclomatic
complexity calculation. The function handles edge cases like n=0 and
negative inputs.
"""


def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer n.

    The factorial of n (written as n!) is the product of all positive
    integers less than or equal to n. By definition, 0! = 1.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

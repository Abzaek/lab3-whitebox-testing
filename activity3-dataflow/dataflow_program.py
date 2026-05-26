"""
dataflow_program.py — A program with clear def/use points for data flow analysis.

This function finds the greatest common divisor (GCD) of two integers using
Euclid's algorithm. It has well-defined variable definitions (d) and uses
(c-use: computation-use, p-use: predicate-use) suitable for data flow testing.

Variable analysis:
------------------
a (first input):
  - d1: parameter definition (line marked as def)
  - d2: reassignment in loop body: a = b (def)
  - p-use: condition `a != 0` (predicate use in while)
  - p-use: condition `a < b` or equivalent (predicate use)
  - c-use: computation `b = b % a` uses a's current value

b (second input):
  - d1: parameter definition
  - d2: reassignment: b = b % a (def)
  - c-use: used in computation `a = b` (when swapping)
  - p-use: condition checks involving b

temp (swap variable):
  - d1: temp = a (def)
  - c-use: a = b (uses temp... wait, let me simplify)

Simplified implementation for cleaner data flow:
We use a non-swapping version of Euclid's algorithm.
"""

from typing import Tuple


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor using Euclid's algorithm.

    Euclid's algorithm: gcd(a, b) = gcd(b, a mod b) until b == 0.
    Returns the original a when done.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        GCD of a and b.

    Raises:
        ValueError: If both a and b are 0.

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(0, 5)
        5
        >>> gcd(7, 0)
        7
        >>> gcd(0, 0)
        Traceback (most recent call last):
        ...
        ValueError: gcd(0, 0) is undefined
    """
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")

    # Normalize: ensure we work with the right assignment order
    # Use three variables to create more def/use points
    x: int = abs(a) if a != 0 else abs(b)      # d1_x
    y: int = abs(b)                              # d1_y
    r: int = 0                                   # d1_r (remainder)

    while y != 0:                                # p-use: y
        r = x % y                                # d2_r, c-use: x, y
        x = y                                    # d2_x, c-use: y
        y = r                                    # d2_y, c-use: r

    return x                                     # c-use: x


def gcd_with_steps(a: int, b: int) -> Tuple[int, list]:
    """Compute GCD and return it along with intermediate steps for analysis.

    Useful for verifying DU paths in test cases.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Tuple of (gcd_value, list_of_intermediate_states).

    Raises:
        ValueError: If both a and b are 0.
    """
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")

    x: int = abs(a) if a != 0 else abs(b)
    y: int = abs(b)
    r: int = 0
    steps: list = [(x, y, r)]

    while y != 0:
        r = x % y
        x = y
        y = r
        steps.append((x, y, r))

    return x, steps

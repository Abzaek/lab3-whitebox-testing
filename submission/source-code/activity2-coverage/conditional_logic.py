"""
conditional_logic.py — Conditional logic with compound boolean conditions.

This function determines a letter grade based on a numerical score.
It uses compound boolean expressions (AND/OR), nested if-else structures,
and includes edge cases for invalid inputs. This module is designed for
statement, branch, and condition coverage analysis.

Statements: 14 executable statements total
- 1: validate input type
- 2: validate score range
- 3-4: return 'A' if score >= 90 and score <= 100
- 5-6: return 'B' if score >= 80 and score < 90
- 7-8: return 'C' if score >= 70 and score < 80
- 9-10: return 'D' if score >= 60 and score < 70
- 11-12: return 'F' if score >= 0 and score < 60
- 13-14: return 'Invalid' else

Compound conditions (for condition coverage):
- if isinstance(score, (int, float)) and (0 <= score <= 100):
- score >= 90 and score <= 100
- score >= 80 and score < 90
- score >= 70 and score < 80
- score >= 60 and score < 70
- score >= 0 and score < 60
"""

from typing import Union


Numeric = Union[int, float]


def grade_score(score: Numeric) -> str:
    """Determine the letter grade for a given numerical score.

    Args:
        score: A numeric value (int or float) representing the test score.

    Returns:
        A string letter grade: 'A', 'B', 'C', 'D', 'F', or 'Invalid'.

    Examples:
        >>> grade_score(95)
        'A'
        >>> grade_score(83)
        'B'
        >>> grade_score(72)
        'C'
        >>> grade_score(65)
        'D'
        >>> grade_score(45)
        'F'
        >>> grade_score(-5)
        'Invalid'
        >>> grade_score("abc")
        'Invalid'
    """
    # Statement 1: type check
    if not isinstance(score, (int, float)):
        return "Invalid"

    # Statement 2: range check
    if score < 0 or score > 100:
        return "Invalid"

    # A: 90-100
    if score >= 90 and score <= 100:
        return "A"

    # B: 80-89
    if score >= 80 and score < 90:
        return "B"

    # C: 70-79
    if score >= 70 and score < 80:
        return "C"

    # D: 60-69
    if score >= 60 and score < 70:
        return "D"

    # F: 0-59
    if score >= 0 and score < 60:
        return "F"

    # Fallback (should not be reached — all valid scores are caught above)
    # but we include a test that passes a score that somehow gets here
    # by having the F check not trigger
    return "Invalid"  # pragma: no cover

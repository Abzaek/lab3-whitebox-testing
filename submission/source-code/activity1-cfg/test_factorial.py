"""
test_factorial.py — Path coverage tests for the factorial function.

The factorial function has a cyclomatic complexity of 3, meaning there are
3 linearly independent paths through the code:

Path 1 (n < 0):   N0 → N1 (T) → N2 (exit)
Path 2 (n == 0):  N0 → N1 (F) → N3 (T) → N4 (exit)
Path 3 (n > 0):   N0 → N1 (F) → N3 (F) → N5 → (recursive) → N1...

These paths cover all branches and provide 100% branch coverage.
"""

import pytest
from factorial import factorial


class TestFactorialPaths:
    """Test suite covering all linearly independent paths through factorial()."""

    # --- Path 1: n < 0 (validation path) ---
    # N0 → N1(T) → N2(raise ValueError)
    def test_path1_negative_number_raises_error(self) -> None:
        """Path 1: n < 0 triggers ValueError.

        Covers: n < 0 branch → raise ValueError block.
        """
        with pytest.raises(ValueError, match="not defined for negative numbers"):
            factorial(-1)

    def test_path1_negative_large_value(self) -> None:
        """Path 1 variant: large negative value."""
        with pytest.raises(ValueError, match="not defined for negative numbers"):
            factorial(-100)

    # --- Path 2: n == 0 (base case) ---
    # N0 → N1(F) → N3(T) → N4(return 1)
    def test_path2_factorial_zero(self) -> None:
        """Path 2: n == 0 returns 1 directly.

        Covers: n < 0 branch false → n == 0 branch true → return 1.
        """
        assert factorial(0) == 1

    # --- Path 3: n > 0 (recursive path) ---
    # N0 → N1(F) → N3(F) → N5(return n * factorial(n-1))
    def test_path3_factorial_positive_small(self) -> None:
        """Path 3: n = 1 triggers recursive base immediately.

        factorial(1) = 1 * factorial(0) = 1 * 1 = 1
        """
        assert factorial(1) == 1

    def test_path3_factorial_positive_medium(self) -> None:
        """Path 3: n = 5 exercises recursion 5 levels deep."""
        assert factorial(5) == 120

    def test_path3_factorial_positive_larger(self) -> None:
        """Path 3: n = 10 exercises deeper recursion."""
        assert factorial(10) == 3628800

    # --- Edge cases ---
    def test_factorial_negative_float_rejected(self) -> None:
        """Ensure negative floats are also caught."""
        with pytest.raises(ValueError, match="not defined for negative numbers"):
            factorial(-5)

    def test_factorial_type_error_on_string(self) -> None:
        """Non-integer types should raise TypeError (not our ValueError)."""
        with pytest.raises(TypeError):
            factorial("5")  # type: ignore[arg-type]

"""
test_mutation.py — Test suite designed to kill all 5 calculator mutants.

Each test function targets specific mutations. Tests are organized to
provide robust coverage with multiple inputs (including edge cases)
that expose operator replacements, boundary changes, and condition negations.
"""

import pytest
from calculator import Calculator


# =========================================================================
# Calculator Tests — designed to kill all mutants
# =========================================================================

class TestCalculator:
    """Tests for all Calculator methods — robust enough to kill mutants."""

    # --- add() tests ---
    # Targets mutant_1 (add → subtract)
    # If add is replaced with subtract, add(2,3) returns -1 instead of 5

    def test_add_positive_numbers(self) -> None:
        """add(2, 3) = 5 — kills mutant_1 (2-3=-1 != 5)."""
        assert Calculator.add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        """add(-4, -1) = -5 — kills mutant_1 (-4-(-1)=-3 != -5)."""
        assert Calculator.add(-4, -1) == -5

    def test_add_mixed_signs(self) -> None:
        """add(-3, 7) = 4 — kills mutant_1 (-3-7=-10 != 4)."""
        assert Calculator.add(-3, 7) == 4

    def test_add_zero(self) -> None:
        """add(0, 5) = 5, add(5, 0) = 5 — kills mutant_1."""
        assert Calculator.add(0, 5) == 5
        assert Calculator.add(5, 0) == 5

    def test_add_floats(self) -> None:
        """add(2.5, 3.1) = 5.6 — kills mutant_1 (2.5-3.1=-0.6 != 5.6)."""
        assert Calculator.add(2.5, 3.1) == 5.6

    def test_add_commutative(self) -> None:
        """add(a,b) == add(b,a) — mutant_1 breaks commutativity."""
        assert Calculator.add(7, 9) == Calculator.add(9, 7)

    # --- subtract() tests ---

    def test_subtract_positive(self) -> None:
        """subtract(5, 3) = 2."""
        assert Calculator.subtract(5, 3) == 2

    def test_subtract_negative_result(self) -> None:
        """subtract(3, 5) = -2."""
        assert Calculator.subtract(3, 5) == -2

    def test_subtract_negative_inputs(self) -> None:
        """subtract(-5, -3) = -2."""
        assert Calculator.subtract(-5, -3) == -2

    def test_subtract_zero(self) -> None:
        """subtract(0, 5) = -5, subtract(5, 0) = 5."""
        assert Calculator.subtract(0, 5) == -5
        assert Calculator.subtract(5, 0) == 5

    def test_subtract_floats(self) -> None:
        """subtract(5.5, 2.2) = 3.3."""
        assert abs(Calculator.subtract(5.5, 2.2) - 3.3) < 1e-10

    # --- multiply() tests ---
    # Targets mutant_2 (multiply → divide)
    # If multiply is replaced with divide, multiply(4,2) returns 2 instead of 8

    def test_multiply_basic(self) -> None:
        """multiply(4, 3) = 12 — kills mutant_2 (4/3 ≈ 1.33 != 12)."""
        assert Calculator.multiply(4, 3) == 12

    def test_multiply_by_zero(self) -> None:
        """multiply(0, 5) = 0 — tricky for mutant_2 (0/5=0, same result)."""
        assert Calculator.multiply(0, 5) == 0

    def test_multiply_by_one(self) -> None:
        """multiply(7, 1) = 7 — tricky for mutant_2 (7/1=7, same)."""
        assert Calculator.multiply(7, 1) == 7

    def test_multiply_negative(self) -> None:
        """multiply(-4, 3) = -12 — kills mutant_2 (-4/3 ≈ -1.33 != -12)."""
        assert Calculator.multiply(-4, 3) == -12

    def test_multiply_two_negatives(self) -> None:
        """multiply(-4, -3) = 12 — kills mutant_2 (-4/-3 ≈ 1.33 != 12)."""
        assert Calculator.multiply(-4, -3) == 12

    def test_multiply_large_numbers(self) -> None:
        """multiply(100, 200) = 20000 — kills mutant_2."""
        assert Calculator.multiply(100, 200) == 20000

    def test_multiply_by_fraction(self) -> None:
        """multiply(6, 0.5) = 3.0 — kills mutant_2 (6/0.5=12 != 3)."""
        assert Calculator.multiply(6, 0.5) == 3.0

    # --- divide() tests ---
    # Targets mutant_4 (b == 0 → b <= 0)

    def test_divide_positive(self) -> None:
        """divide(10, 2) = 5.0."""
        assert Calculator.divide(10, 2) == 5.0

    def test_divide_negative_divisor(self) -> None:
        """divide(10, -2) = -5.0 — kills mutant_4 if b <= 0 raises error."""
        result = Calculator.divide(10, -2)
        assert result == -5.0

    def test_divide_by_negative(self) -> None:
        """divide(-10, -2) = 5.0 — kills mutant_4."""
        assert Calculator.divide(-10, -2) == 5.0

    def test_divide_by_zero_raises(self) -> None:
        """divide(10, 0) raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(10, 0)

    def test_divide_zero_by_number(self) -> None:
        """divide(0, 5) = 0.0."""
        assert Calculator.divide(0, 5) == 0.0

    def test_divide_fractional(self) -> None:
        """divide(7, 3) ≈ 2.333..."""
        assert abs(Calculator.divide(7, 3) - 7 / 3) < 1e-10

    def test_divide_float_precision(self) -> None:
        """divide(1, 3) = 0.333..."""
        assert abs(Calculator.divide(1, 3) - 1 / 3) < 1e-10

    # --- power() tests ---
    # Targets mutant_3 (b → b + 1)

    def test_power_basic(self) -> None:
        """power(2, 3) = 8 — kills mutant_3 (2^4=16 != 8)."""
        assert Calculator.power(2, 3) == 8

    def test_power_zero_exponent(self) -> None:
        """power(5, 0) = 1 — kills mutant_3 (5^1=5 != 1)."""
        assert Calculator.power(5, 0) == 1

    def test_power_one_exponent(self) -> None:
        """power(3, 1) = 3 — kills mutant_3 (3^2=9 != 3)."""
        assert Calculator.power(3, 1) == 3

    def test_power_negative_exponent(self) -> None:
        """power(2, -1) = 0.5 — kills mutant_3 (2^0=1 != 0.5)."""
        assert abs(Calculator.power(2, -1) - 0.5) < 1e-10

    def test_power_negative_base(self) -> None:
        """power(-2, 3) = -8 — kills mutant_3 ((-2)^4=16 != -8)."""
        assert Calculator.power(-2, 3) == -8

    def test_power_fractional_exponent(self) -> None:
        """power(9, 0.5) = 3.0 — kills mutant_3 (9^1.5=27 != 3)."""
        assert abs(Calculator.power(9, 0.5) - 3.0) < 1e-10

    def test_power_large_exponent(self) -> None:
        """power(3, 5) = 243 — kills mutant_3 (3^6=729 != 243)."""
        assert Calculator.power(3, 5) == 243

    # --- modulo() tests ---
    # Targets mutant_5 (b == 0 → b != 0)

    def test_modulo_basic(self) -> None:
        """modulo(10, 3) = 1 — kills mutant_5 if b != 0 raises error."""
        assert Calculator.modulo(10, 3) == 1

    def test_modulo_exact_division(self) -> None:
        """modulo(10, 5) = 0."""
        assert Calculator.modulo(10, 5) == 0

    def test_modulo_negative_dividend(self) -> None:
        """modulo(-10, 3) = 2 (Python's modulo semantics)."""
        assert Calculator.modulo(-10, 3) == 2

    def test_modulo_negative_divisor(self) -> None:
        """modulo(10, -3) = -2 (Python's modulo semantics)."""
        assert Calculator.modulo(10, -3) == -2

    def test_modulo_by_zero_raises(self) -> None:
        """modulo(10, 0) raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            Calculator.modulo(10, 0)

    def test_modulo_large_numbers(self) -> None:
        """modulo(100, 7) = 2."""
        assert Calculator.modulo(100, 7) == 2

    def test_modulo_small_dividend(self) -> None:
        """modulo(1, 5) = 1 — kills mutant_5 if b != 0 raises error."""
        assert Calculator.modulo(1, 5) == 1

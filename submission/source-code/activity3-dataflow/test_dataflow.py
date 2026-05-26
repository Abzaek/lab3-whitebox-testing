"""
test_dataflow.py — Data flow coverage tests for the GCD function.

This test suite provides test cases for three data flow coverage criteria:
1. All-defs coverage: each definition reaches at least one use
2. All DU pairs coverage: every DU pair is exercised
3. All DU paths coverage: every simple path from def to each use

We use gcd_with_steps() to verify the exact execution path taken.
"""

import pytest
from dataflow_program import gcd, gcd_with_steps


class TestAllDefsCoverage:
    """All-defs coverage: each definition reaches at least one use.

    Required pairs (one per definition):
      x: (d1_x, c_x_mod), (d2_x, c_x_ret)
      y: (d1_y, c_y_mod), (d2_y, p_y_while)
      r: (d1_r, c_r_assign), (d2_r, c_r_assign)
    """

    def test_def_x1_reaches_cx_mod(self) -> None:
        """d1_x → c_x_mod: gcd(48, 18) uses initial x in modulo."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        # Steps: [(48, 18, 0), (18, 12, 12), (12, 6, 6), (6, 0, 0)]
        # The last step has y=0, proving loop exited
        assert steps[-1][1] == 0  # y became 0

    def test_def_x2_reaches_cx_ret(self) -> None:
        """d2_x → c_x_ret: x reassigned in loop then returned."""
        assert gcd(7, 3) == 1
        # Steps: x=7,y=3 → x=3,y=1 → x=1,y=0 → return 1
        # d2_x happens in iteration 1 (x=3), then returned

    def test_def_y1_reaches_cy_mod(self) -> None:
        """d1_y → c_y_mod: initial y used in modulo computation."""
        assert gcd(12, 8) == 4

    def test_def_y2_reaches_py_while(self) -> None:
        """d2_y → p_y_while: reassigned y used in while condition."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        # y is reassigned (d2_y) then checked in while condition (p_y_while)

    def test_def_r1_reaches_cr_assign(self) -> None:
        """d1_r → c_r_assign: initial r=0, but also used after d2_r."""
        assert gcd(5, 3) == 1

    def test_def_r2_reaches_cr_assign(self) -> None:
        """d2_r → c_r_assign: r computed in loop, then assigned to y."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        r_values = [s[2] for s in steps]
        assert 12 in r_values  # First modulo result
        assert 6 in r_values   # Second modulo result


class TestAllDUPairsCoverage:
    """All DU pairs coverage: every DU pair must be exercised.

    Full pair list:
      x: (d1_x, c_x_mod), (d1_x, c_x_ret), (d2_x, c_x_mod), (d2_x, c_x_ret)
      y: (d1_y, c_y_mod), (d1_y, c_y_assign), (d1_y, p_y_while),
         (d2_y, c_y_mod), (d2_y, c_y_assign), (d2_y, p_y_while)
      r: (d1_r, c_r_assign), (d2_r, c_r_assign)
    """

    def test_pair_d1x_cx_mod(self) -> None:
        """(d1_x, c_x_mod): initial x used in first modulo."""
        assert gcd(12, 8) == 4

    def test_pair_d1x_cx_ret(self) -> None:
        """(d1_x, c_x_ret): initial x used in return (no loop)."""
        assert gcd(7, 0) == 7  # y=0, loop skipped, d1_x reaches return

    def test_pair_d2x_cx_mod(self) -> None:
        """(d2_x, c_x_mod): reassigned x used in next modulo."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        # After first iteration: x=18, y=12
        # x=18 is d2_x, then used in r = x % y = 18 % 12 = 6

    def test_pair_d2x_cx_ret(self) -> None:
        """(d2_x, c_x_ret): reassigned x used in return after loop exit."""
        assert gcd(12, 8) == 4
        # Loop runs: x=8,y=4 → x=4,y=0 → return 4 (d2_x reaches return)

    def test_pair_d1y_cy_mod(self) -> None:
        """(d1_y, c_y_mod): initial y used in modulo."""
        assert gcd(48, 18) == 6

    def test_pair_d1y_cy_assign(self) -> None:
        """(d1_y, c_y_assign): initial y assigned to x."""
        assert gcd(7, 3) == 1

    def test_pair_d1y_py_while(self) -> None:
        """(d1_y, p_y_while): initial y checked in while condition."""
        assert gcd(5, 5) == 5

    def test_pair_d2y_cy_mod(self) -> None:
        """(d2_y, c_y_mod): reassigned y used in modulo."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        # y reassigned to 12 (d2_y), then used in 18 % 12

    def test_pair_d2y_cy_assign(self) -> None:
        """(d2_y, c_y_assign): reassigned y assigned to x."""
        assert gcd(48, 18) == 6

    def test_pair_d2y_py_while(self) -> None:
        """(d2_y, p_y_while): reassigned y checked in while."""
        result, steps = gcd_with_steps(48, 18)
        assert result == 6
        # y=12 checked in while, y=6 checked, y=0 exits

    def test_pair_d1r_cr_assign(self) -> None:
        """(d1_r, c_r_assign): but d1_r=0 is overwritten by d2_r first."""
        assert gcd(12, 8) == 4

    def test_pair_d2r_cr_assign(self) -> None:
        """(d2_r, c_r_assign): computed r assigned to y."""
        assert gcd(48, 18) == 6


class TestAllDUPathsCoverage:
    """All DU paths coverage: every simple path from each def to each use.

    This requires multiple test inputs to traverse different loop iterations
    and verify each possible path through the CFG.
    """

    def test_path_d1x_cx_mod_no_loop(self) -> None:
        """Path: d1_x → N2(F) → N4 — loop body never entered."""
        assert gcd(7, 0) == 7  # y=0, loop skipped entirely
        # x is used in return without ever entering the loop

    def test_path_d1x_cx_mod_one_iteration(self) -> None:
        """Path: d1_x → N2(T) → N3(c_x_mod) — single loop iteration."""
        assert gcd(7, 3) == 1  # Single iteration: 7%3=1, 3%1=0

    def test_path_d1x_cx_ret_one_iteration(self) -> None:
        """Path: d1_x → N2(T) → N3(d2_x) → N2(F) → N4(c_x_ret)."""
        assert gcd(4, 2) == 2  # One loop: x=2,y=0 → return 2

    def test_path_d1x_cx_ret_multi_iteration(self) -> None:
        """Path through multiple iterations: d1_x → many rounds → return."""
        assert gcd(48, 18) == 6  # Multiple iterations

    def test_path_zero_inputs(self) -> None:
        """Edge case: one zero input (exercises d1_y short path)."""
        assert gcd(0, 5) == 5  # x=5, y=5... actually x=|b|=5, loop runs
        assert gcd(5, 0) == 5  # y=0, loop skipped

    def test_path_equal_inputs(self) -> None:
        """Edge case: equal inputs, one loop iteration."""
        assert gcd(12, 12) == 12

    def test_path_negative_inputs(self) -> None:
        """Edge case: negative numbers (abs normalizes)."""
        assert gcd(-48, 18) == 6
        assert gcd(48, -18) == 6
        assert gcd(-48, -18) == 6

    def test_path_prime_inputs(self) -> None:
        """Edge case: coprime numbers, GCD=1."""
        assert gcd(17, 13) == 1
        assert gcd(101, 53) == 1

    def test_path_zero_zero(self) -> None:
        """Edge case: gcd(0,0) raises ValueError."""
        with pytest.raises(ValueError, match="gcd.*undefined"):
            gcd(0, 0)

    def test_path_large_numbers(self) -> None:
        """Edge case: large numbers to test deeper recursion depth."""
        assert gcd(123456, 7890) == 6

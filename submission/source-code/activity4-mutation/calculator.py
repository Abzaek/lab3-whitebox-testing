"""
calculator.py — A Calculator class with arithmetic operations.

This module provides a Calculator class with methods that serve as the
subject for mutation testing. Each method has clear semantics and edge
cases to enable robust test design.
"""


class Calculator:
    """A simple calculator with arithmetic operations.

    All methods are static/instance methods that accept numeric inputs.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of a and b.

        >>> Calculator.add(2, 3)
        5
        >>> Calculator.add(-1, 1)
        0
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return a minus b.

        >>> Calculator.subtract(5, 3)
        2
        >>> Calculator.subtract(3, 5)
        -2
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of a and b.

        >>> Calculator.multiply(4, 3)
        12
        >>> Calculator.multiply(0, 5)
        0
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return a divided by b.

        Args:
            a: Dividend.
            b: Divisor.

        Returns:
            Quotient as a float.

        Raises:
            ZeroDivisionError: If b is zero.

        >>> Calculator.divide(10, 2)
        5.0
        >>> Calculator.divide(7, 3)
        2.333...
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Return a raised to the power b.

        >>> Calculator.power(2, 3)
        8
        >>> Calculator.power(5, 0)
        1
        >>> Calculator.power(4, 0.5)
        2.0
        """
        return a ** b

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Return a modulo b (remainder of a / b).

        Args:
            a: Dividend.
            b: Divisor.

        Returns:
            Remainder.

        Raises:
            ZeroDivisionError: If b is zero.

        >>> Calculator.modulo(10, 3)
        1
        >>> Calculator.modulo(10, 5)
        0
        """
        if b == 0:
            raise ZeroDivisionError("Cannot compute modulo with zero")
        return a % b

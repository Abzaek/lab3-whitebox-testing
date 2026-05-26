"""
mutant_3.py — MUTATION: Off-by-one / boundary change in power().

Original:    return a ** b
Mutation:    return a ** (b + 1)

This adds 1 to the exponent, changing the result for all non-zero,
non-one exponent values. Tests like Calculator.power(2, 3) == 8
will see 2^4 == 16 instead, killing this mutant.
"""

# MUTATION: Changed exponent to b + 1 in power()
# Original: return a ** b


class Calculator:
    """MUTATED: Power exponent is incremented by 1."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Unchanged addition."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Unchanged subtraction."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Unchanged multiplication."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Unchanged division."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """MUTATED: Returns a ** (b + 1) instead of a ** b."""
        return a ** (b + 1)  # MUTATION: b changed to b + 1

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Unchanged modulo."""
        if b == 0:
            raise ZeroDivisionError("Cannot compute modulo with zero")
        return a % b

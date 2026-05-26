"""
mutant_4.py — MUTATION: Relational operator change in divide().

Original:    if b == 0:
Mutation:    if b <= 0:

This changes the zero-division check from equality (==) to
less-than-or-equal (<=). Negative divisors will now raise
ZeroDivisionError incorrectly. Tests dividing by negative numbers
should kill this mutant.
"""

# MUTATION: Changed 'b == 0' to 'b <= 0' in divide()
# Original: if b == 0:


class Calculator:
    """MUTATED: Divide raises error for b <= 0 instead of b == 0."""

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
        """MUTATED: Raises ZeroDivisionError for b <= 0 instead of b == 0."""
        if b <= 0:  # MUTATION: == changed to <=
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Unchanged power."""
        return a ** b

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Unchanged modulo."""
        if b == 0:
            raise ZeroDivisionError("Cannot compute modulo with zero")
        return a % b

"""
mutant_1.py — MUTATION: Changed arithmetic operator in add().

Original:    return a + b
Mutation:    return a - b

This changes the addition operator to subtraction, so add() now
behaves like subtract(). Tests that verify sum results should kill
this mutant.
"""

# MUTATION: Changed '+' to '-' in add()
# Original: return a + b


class Calculator:
    """MUTATED: Add is replaced with subtract."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """MUTATED: Returns a - b instead of a + b."""
        return a - b  # MUTATION: + changed to -

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
        """Unchanged power."""
        return a ** b

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Unchanged modulo."""
        if b == 0:
            raise ZeroDivisionError("Cannot compute modulo with zero")
        return a % b

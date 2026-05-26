"""
mutant_2.py — MUTATION: Swapped operator in multiply().

Original:    return a * b
Mutation:    return a / b

This changes multiplication to division. Tests using non-zero values
where a * b != a / b will kill this mutant.
"""

# MUTATION: Changed '*' to '/' in multiply()
# Original: return a * b


class Calculator:
    """MUTATED: Multiply is replaced with divide."""

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
        """MUTATED: Returns a / b instead of a * b."""
        return a / b  # MUTATION: * changed to /

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

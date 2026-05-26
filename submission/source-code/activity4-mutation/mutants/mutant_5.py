"""
mutant_5.py — MUTATION: Negated condition in modulo().

Original:    if b == 0:
Mutation:    if b != 0:   (or removed the condition entirely)

This negates the zero-check condition. When b != 0, the function
raises ZeroDivisionError, and when b == 0, it proceeds to compute
a % 0 which would also raise ZeroDivisionError (naturally from Python).
The key difference is that normal usage with b != 0 now fails.
"""

# MUTATION: Changed 'if b == 0:' to 'if b != 0:' in modulo()
# Original: if b == 0:


class Calculator:
    """MUTATED: Modulo condition is negated (b != 0 instead of b == 0)."""

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
        """Unchanged power."""
        return a ** b

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """MUTATED: Negated condition — raises error when b != 0 instead of b == 0."""
        if b != 0:  # MUTATION: == changed to !=
            raise ZeroDivisionError("Cannot compute modulo with zero")
        return a % b

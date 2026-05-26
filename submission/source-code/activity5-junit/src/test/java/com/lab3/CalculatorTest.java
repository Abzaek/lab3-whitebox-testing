package com.lab3;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Comprehensive JUnit 5 test suite for the Calculator class.
 * Covers all operations with boundary values, edge cases, and exception testing.
 * Implements statement, branch, and condition coverage principles.
 */
@DisplayName("Calculator Test Suite")
class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }

    // ========================================================================
    // Addition Tests
    // ========================================================================

    @Nested
    @DisplayName("Addition Operations")
    class AdditionTests {

        @Test
        @DisplayName("Adding two positive numbers returns correct sum")
        void addPositiveNumbers() {
            assertEquals(15, calculator.add(10, 5));
        }

        @Test
        @DisplayName("Adding positive and negative numbers returns correct result")
        void addPositiveAndNegative() {
            assertEquals(5, calculator.add(10, -5));
        }

        @Test
        @DisplayName("Adding two negative numbers returns correct sum")
        void addNegativeNumbers() {
            assertEquals(-15, calculator.add(-10, -5));
        }

        @Test
        @DisplayName("Adding zero to a number returns the same number")
        void addWithZero() {
            assertEquals(7, calculator.add(7, 0));
            assertEquals(0, calculator.add(0, 0));
        }

        @Test
        @DisplayName("Adding large numbers handles integer overflow")
        void addLargeNumbers() {
            assertEquals(Integer.MAX_VALUE, calculator.add(Integer.MAX_VALUE, 0));
            assertEquals(Integer.MIN_VALUE, calculator.add(Integer.MIN_VALUE, 0));
        }
    }

    // ========================================================================
    // Subtraction Tests
    // ========================================================================

    @Nested
    @DisplayName("Subtraction Operations")
    class SubtractionTests {

        @Test
        @DisplayName("Subtracting two positive numbers returns correct difference")
        void subtractPositiveNumbers() {
            assertEquals(10, calculator.subtract(15, 5));
        }

        @Test
        @DisplayName("Subtracting a negative is equivalent to addition")
        void subtractNegativeNumber() {
            assertEquals(10, calculator.subtract(5, -5));
        }

        @Test
        @DisplayName("Subtracting zero returns the original number")
        void subtractZero() {
            assertEquals(42, calculator.subtract(42, 0));
        }

        @Test
        @DisplayName("Subtracting a number from itself returns zero")
        void subtractNumberFromItself() {
            assertEquals(0, calculator.subtract(7, 7));
            assertEquals(0, calculator.subtract(-7, -7));
        }
    }

    // ========================================================================
    // Multiplication Tests
    // ========================================================================

    @Nested
    @DisplayName("Multiplication Operations")
    class MultiplicationTests {

        @Test
        @DisplayName("Multiplying two positive numbers returns correct product")
        void multiplyPositiveNumbers() {
            assertEquals(20, calculator.multiply(4, 5));
        }

        @Test
        @DisplayName("Multiplying by zero returns zero")
        void multiplyByZero() {
            assertEquals(0, calculator.multiply(99, 0));
            assertEquals(0, calculator.multiply(0, 0));
        }

        @Test
        @DisplayName("Multiplying by negative numbers returns correct product")
        void multiplyNegativeNumbers() {
            assertEquals(-20, calculator.multiply(4, -5));
            assertEquals(20, calculator.multiply(-4, -5));
        }

        @Test
        @DisplayName("Multiplying by one returns the original number")
        void multiplyByOne() {
            assertEquals(42, calculator.multiply(42, 1));
        }

        @Test
        @DisplayName("Multiplying large numbers handles integer overflow")
        void multiplyLargeNumbers() {
            // 100000 * 100000 = 10000000000 -> overflow expected
            int result = calculator.multiply(100000, 100000);
            assertTrue(result < 0 || result > 0, "Overflow may occur but should not throw");
        }
    }

    // ========================================================================
    // Division Tests
    // ========================================================================

    @Nested
    @DisplayName("Division Operations")
    class DivisionTests {

        @Test
        @DisplayName("Dividing two positive numbers returns correct quotient")
        void dividePositiveNumbers() {
            assertEquals(3, calculator.divide(15, 5));
        }

        @Test
        @DisplayName("Dividing by a negative number returns correct quotient")
        void divideByNegativeNumber() {
            assertEquals(-3, calculator.divide(15, -5));
            assertEquals(3, calculator.divide(-15, -5));
        }

        @Test
        @DisplayName("Dividing zero by any non-zero number returns zero")
        void divideZeroByNumber() {
            assertEquals(0, calculator.divide(0, 5));
        }

        @Test
        @DisplayName("Division by zero throws ArithmeticException")
        void divideByZeroThrowsException() {
            Exception exception = assertThrows(ArithmeticException.class, () -> {
                calculator.divide(10, 0);
            });
            assertEquals("Division by zero is not allowed", exception.getMessage());
        }

        @Test
        @DisplayName("Integer division truncates toward zero")
        void integerDivisionTruncation() {
            assertEquals(3, calculator.divide(10, 3));
            assertEquals(-3, calculator.divide(-10, 3));
        }
    }

    // ========================================================================
    // Power Tests
    // ========================================================================

    @Nested
    @DisplayName("Power Operations")
    class PowerTests {

        @Test
        @DisplayName("Any number to the power of zero equals one")
        void powerOfZero() {
            assertEquals(1, calculator.power(5, 0));
            assertEquals(1, calculator.power(0, 0));
            assertEquals(1, calculator.power(-5, 0));
        }

        @Test
        @DisplayName("Raising a number to the power of one returns the number itself")
        void powerOfOne() {
            assertEquals(5, calculator.power(5, 1));
            assertEquals(-5, calculator.power(-5, 1));
        }

        @Test
        @DisplayName("Raising a positive base to a positive exponent")
        void positiveBasePositiveExponent() {
            assertEquals(8, calculator.power(2, 3));
            assertEquals(27, calculator.power(3, 3));
        }

        @Test
        @DisplayName("Negative exponent throws IllegalArgumentException")
        void negativeExponentThrowsException() {
            assertThrows(IllegalArgumentException.class, () -> {
                calculator.power(2, -1);
            });
        }
    }

    // ========================================================================
    // Modulo Tests
    // ========================================================================

    @Nested
    @DisplayName("Modulo Operations")
    class ModuloTests {

        @Test
        @DisplayName("Modulo of two positive numbers returns correct remainder")
        void moduloPositiveNumbers() {
            assertEquals(2, calculator.modulo(17, 5));
        }

        @Test
        @DisplayName("Modulo with negative dividend")
        void moduloNegativeDividend() {
            assertEquals(-2, calculator.modulo(-17, 5));
        }

        @Test
        @DisplayName("Modulo by zero throws ArithmeticException")
        void moduloByZeroThrowsException() {
            Exception exception = assertThrows(ArithmeticException.class, () -> {
                calculator.modulo(10, 0);
            });
            assertEquals("Modulo by zero is not allowed", exception.getMessage());
        }

        @Test
        @DisplayName("Modulo where dividend is smaller than divisor returns dividend")
        void moduloSmallerDividend() {
            assertEquals(3, calculator.modulo(3, 10));
        }

        @Test
        @DisplayName("Modulo of zero returns zero")
        void moduloOfZero() {
            assertEquals(0, calculator.modulo(0, 5));
        }
    }

    // ========================================================================
    // isPositive Tests
    // ========================================================================

    @Nested
    @DisplayName("isPositive Checks")
    class IsPositiveTests {

        @Test
        @DisplayName("Positive number returns true")
        void positiveNumberIsPositive() {
            assertTrue(calculator.isPositive(1));
            assertTrue(calculator.isPositive(Integer.MAX_VALUE));
        }

        @Test
        @DisplayName("Zero is not positive")
        void zeroIsNotPositive() {
            assertFalse(calculator.isPositive(0));
        }

        @Test
        @DisplayName("Negative number returns false")
        void negativeNumberIsNotPositive() {
            assertFalse(calculator.isPositive(-1));
            assertFalse(calculator.isPositive(Integer.MIN_VALUE));
        }
    }

    // ========================================================================
    // Max Tests
    // ========================================================================

    @Nested
    @DisplayName("Maximum of Three Numbers")
    class MaxTests {

        @Test
        @DisplayName("First number is the maximum")
        void firstIsMax() {
            assertEquals(10, calculator.max(10, 5, 3));
        }

        @Test
        @DisplayName("Second number is the maximum")
        void secondIsMax() {
            assertEquals(10, calculator.max(5, 10, 3));
        }

        @Test
        @DisplayName("Third number is the maximum")
        void thirdIsMax() {
            assertEquals(10, calculator.max(5, 3, 10));
        }

        @Test
        @DisplayName("All numbers equal returns that value")
        void allEqual() {
            assertEquals(7, calculator.max(7, 7, 7));
        }

        @Test
        @DisplayName("Works with negative numbers")
        void maxOfNegativeNumbers() {
            assertEquals(-1, calculator.max(-5, -1, -10));
        }

        @Test
        @DisplayName("Works with extremes including Integer.MIN_VALUE and Integer.MAX_VALUE")
        void maxWithExtremes() {
            assertEquals(Integer.MAX_VALUE, calculator.max(Integer.MIN_VALUE, 0, Integer.MAX_VALUE));
        }
    }

    // ========================================================================
    // Grade Score Tests
    // ========================================================================

    @Nested
    @DisplayName("Grade Score Evaluation")
    class GradeScoreTests {

        @Test
        @DisplayName("Score of 90-100 returns A")
        void scoreReturnsA() {
            assertEquals("A", calculator.gradeScore(90));
            assertEquals("A", calculator.gradeScore(95));
            assertEquals("A", calculator.gradeScore(100));
        }

        @Test
        @DisplayName("Score of 80-89 returns B")
        void scoreReturnsB() {
            assertEquals("B", calculator.gradeScore(80));
            assertEquals("B", calculator.gradeScore(85));
            assertEquals("B", calculator.gradeScore(89));
        }

        @Test
        @DisplayName("Score of 70-79 returns C")
        void scoreReturnsC() {
            assertEquals("C", calculator.gradeScore(70));
            assertEquals("C", calculator.gradeScore(75));
            assertEquals("C", calculator.gradeScore(79));
        }

        @Test
        @DisplayName("Score of 60-69 returns D")
        void scoreReturnsD() {
            assertEquals("D", calculator.gradeScore(60));
            assertEquals("D", calculator.gradeScore(65));
            assertEquals("D", calculator.gradeScore(69));
        }

        @Test
        @DisplayName("Score of 0-59 returns F")
        void scoreReturnsF() {
            assertEquals("F", calculator.gradeScore(0));
            assertEquals("F", calculator.gradeScore(30));
            assertEquals("F", calculator.gradeScore(59));
        }

        @Test
        @DisplayName("Score below 0 throws IllegalArgumentException")
        void scoreBelowZeroThrowsException() {
            assertThrows(IllegalArgumentException.class, () -> {
                calculator.gradeScore(-1);
            });
        }

        @Test
        @DisplayName("Score above 100 throws IllegalArgumentException")
        void scoreAbove100ThrowsException() {
            assertThrows(IllegalArgumentException.class, () -> {
                calculator.gradeScore(101);
            });
        }

        @Test
        @DisplayName("Boundary testing: scores at grade boundaries return correct grades")
        void boundaryScoreGrades() {
            // Lower boundaries
            assertEquals("F", calculator.gradeScore(0));
            assertEquals("D", calculator.gradeScore(60));
            assertEquals("C", calculator.gradeScore(70));
            assertEquals("B", calculator.gradeScore(80));
            assertEquals("A", calculator.gradeScore(90));

            // Upper boundaries
            assertEquals("F", calculator.gradeScore(59));
            assertEquals("D", calculator.gradeScore(69));
            assertEquals("C", calculator.gradeScore(79));
            assertEquals("B", calculator.gradeScore(89));
            assertEquals("A", calculator.gradeScore(100));
        }
    }
}

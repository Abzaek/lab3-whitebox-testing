package com.lab3;

/**
 * A robust calculator class providing basic arithmetic operations and utility functions.
 * Used for demonstrating white-box testing techniques with JUnit 5.
 */
public class Calculator {

    /**
     * Adds two integers.
     *
     * @param a first operand
     * @param b second operand
     * @return the sum of a and b
     */
    public int add(int a, int b) {
        return a + b;
    }

    /**
     * Subtracts the second integer from the first.
     *
     * @param a first operand
     * @param b second operand
     * @return the result of a - b
     */
    public int subtract(int a, int b) {
        return a - b;
    }

    /**
     * Multiplies two integers.
     *
     * @param a first operand
     * @param b second operand
     * @return the product of a and b
     */
    public int multiply(int a, int b) {
        return a * b;
    }

    /**
     * Divides the first integer by the second.
     *
     * @param a dividend
     * @param b divisor
     * @return the integer quotient of a / b
     * @throws ArithmeticException if b is zero
     */
    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        return a / b;
    }

    /**
     * Computes base raised to the power of exp (base^exp).
     * Only supports non-negative exponents.
     *
     * @param base the base value
     * @param exp  the exponent (must be >= 0)
     * @return base raised to the power of exp
     * @throws IllegalArgumentException if exp is negative
     */
    public int power(int base, int exp) {
        if (exp < 0) {
            throw new IllegalArgumentException("Negative exponent not supported: " + exp);
        }
        int result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }

    /**
     * Computes the modulo (remainder) of a divided by b.
     *
     * @param a dividend
     * @param b divisor
     * @return the remainder of a / b
     * @throws ArithmeticException if b is zero
     */
    public int modulo(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Modulo by zero is not allowed");
        }
        return a % b;
    }

    /**
     * Checks if a number is positive (greater than zero).
     *
     * @param n the number to check
     * @return true if n > 0, false otherwise
     */
    public boolean isPositive(int n) {
        return n > 0;
    }

    /**
     * Returns the maximum of three integers.
     *
     * @param a first number
     * @param b second number
     * @param c third number
     * @return the largest value among a, b, and c
     */
    public int max(int a, int b, int c) {
        int max = a;
        if (b > max) {
            max = b;
        }
        if (c > max) {
            max = c;
        }
        return max;
    }

    /**
     * Converts a numeric score to a letter grade.
     * <ul>
     *   <li>A: 90-100</li>
     *   <li>B: 80-89</li>
     *   <li>C: 70-79</li>
     *   <li>D: 60-69</li>
     *   <li>F: 0-59</li>
     * </ul>
     *
     * @param score the numeric score (0-100)
     * @return the letter grade as a String
     * @throws IllegalArgumentException if score is outside the range 0-100
     */
    public String gradeScore(int score) {
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("Score must be between 0 and 100: " + score);
        }
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else if (score >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}

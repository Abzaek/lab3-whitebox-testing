# Activity 5: JUnit 5 Calculator

## Overview

This activity demonstrates **white-box testing techniques** using JUnit 5. A robust `Calculator` class provides basic arithmetic and utility operations, and a comprehensive test suite achieves statement, branch, and condition coverage.

## Project Structure

```
activity5-junit/
├── pom.xml                          # Maven build configuration
├── README.md                        # This file
└── src/
    ├── main/java/com/lab3/
    │   └── Calculator.java          # Calculator class with 9 operations
    └── test/java/com/lab3/
        └── CalculatorTest.java      # JUnit 5 test suite (38 tests)
```

## Calculator Operations

| Method | Signature | Description |
|--------|-----------|-------------|
| `add` | `int add(int a, int b)` | Returns a + b |
| `subtract` | `int subtract(int a, int b)` | Returns a - b |
| `multiply` | `int multiply(int a, int b)` | Returns a * b |
| `divide` | `int divide(int a, int b)` | Returns a / b, throws on zero divisor |
| `power` | `int power(int base, int exp)` | Returns base^exp (exp >= 0) |
| `modulo` | `int modulo(int a, int b)` | Returns a % b, throws on zero divisor |
| `isPositive` | `boolean isPositive(int n)` | Returns true if n > 0 |
| `max` | `int max(int a, int b, int c)` | Returns the largest of three ints |
| `gradeScore` | `String gradeScore(int score)` | Returns A/B/C/D/F, throws on invalid score |

## Test Methodology

### Testing Approach

- **Organized by operation** using `@Nested` inner classes for logical grouping
- **Descriptive test names and `@DisplayName` annotations** for readability
- **`@BeforeEach` setup** creates a fresh `Calculator` instance per test
- **Coverage principles** applied:
  - **Statement coverage:** Every line of code in `Calculator.java` is executed
  - **Branch coverage:** Every branch (if/else) is tested with both true/false conditions
  - **Condition coverage:** Each boolean condition is evaluated to both true and false

### Assertion Usage

| Assertion | Purpose | Example |
|-----------|---------|---------|
| `assertEquals(expected, actual)` | Verify correct return values | `assertEquals(15, calculator.add(10, 5))` |
| `assertTrue(condition)` | Verify true conditions | `assertTrue(calculator.isPositive(1))` |
| `assertFalse(condition)` | Verify false conditions | `assertFalse(calculator.isPositive(0))` |
| `assertThrows(Exception.class, () -> ...)` | Verify expected exceptions | `assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0))` |

### Test Coverage Summary

| Category | Tests | Coverage Focus |
|----------|-------|---------------|
| Addition | 5 | Positive, negative, zero, large numbers |
| Subtraction | 4 | Positive, negative, zero, identity |
| Multiplication | 5 | Positive, zero, negative, identity, overflow |
| Division | 5 | Positive, negative, zero dividend, by-zero exception, truncation |
| Power | 4 | Zero exponent, one exponent, positive, negative exponent exception |
| Modulo | 5 | Positive, negative dividend, by-zero exception, smaller dividend, zero |
| isPositive | 3 | Positive, zero, negative |
| Max | 6 | Each position max, equal values, negatives, extremes |
| Grade Score | 8 | Each grade range, boundary testing, invalid score exceptions |
| **Total** | **45** | |

## How to Run

### Prerequisites

- Java 21 (OpenJDK)
- Apache Maven 3.8+

### Running Tests

```bash
cd activity5-junit
mvn clean test
```

### Expected Output

```
[INFO] Tests run: 45, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

## Test Results

The test suite consists of **45 test methods** that all pass:

- ✅ All calculator operations verified with multiple input combinations
- ✅ Boundary testing for `gradeScore` at every grade threshold (0, 59, 60, 69, 70, 79, 80, 89, 90, 100)
- ✅ Exception testing: `ArithmeticException` for division/modulo by zero, `IllegalArgumentException` for invalid scores and negative exponents
- ✅ Edge cases: zero values, negative numbers, integer extremes (`Integer.MAX_VALUE`, `Integer.MIN_VALUE`)

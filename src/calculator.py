"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import math

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

def power(base, exponent):
    """Raise base to the given exponent with input validation."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Power requires numeric inputs")

    return base ** exponent


def sqrt(number):
    """Return the square root of a non-negative number."""
    if not isinstance(number, (int, float)):
        raise TypeError("Square root requires a numeric input")
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")

    return math.sqrt(number)

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

def test_add_negative_numbers(self):
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2
def test_subtract_negative_numbers(self):
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2    
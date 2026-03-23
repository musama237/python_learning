"""
Challenge: Temperature Converter
Difficulty: ⭐ Easy
Topic: Functions, Math, Conditionals

Write functions to convert between Celsius and Fahrenheit.
Round results to 2 decimal places.

Formula: F = C * 9/5 + 32

Example:
    celsius_to_fahrenheit(0) -> 32.0
    fahrenheit_to_celsius(212) -> 100.0
"""


def celsius_to_fahrenheit(c: float) -> float:
    # YOUR CODE HERE
    pass


def fahrenheit_to_celsius(f: float) -> float:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(-40) == -40.0
    assert celsius_to_fahrenheit(37) == 98.6
    print("✅ All tests passed!")

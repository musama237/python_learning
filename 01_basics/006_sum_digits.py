"""
Challenge: Sum of Digits
Difficulty: ⭐ Easy
Topic: Loops, Math, Type Conversion

Calculate the sum of all digits in a non-negative integer.

Example:
    sum_digits(123) -> 6  (1 + 2 + 3)
    sum_digits(9999) -> 36
"""


def sum_digits(n: int) -> int:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert sum_digits(123) == 6
    assert sum_digits(9999) == 36
    assert sum_digits(0) == 0
    assert sum_digits(5) == 5
    assert sum_digits(10001) == 2
    print("✅ All tests passed!")

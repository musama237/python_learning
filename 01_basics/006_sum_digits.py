"""
Challenge: Sum of Digits
Difficulty: ⭐ Easy
Topic: Loops, Math, Type Conversion

Calculate the sum of all digits in a non-negative integer.

Example:
    sum_digits(123) -> 6  (1 + 2 + 3)
    sum_digits(9999) -> 36

Hints:
    1. There are two approaches: treat the number as a string, or use math to extract digits.
    2. String approach: convert to str and iterate, converting each char back to int. Math approach: use % 10 to get the last digit and // 10 to remove it.
    3. With math: loop while n > 0, add n % 10 to a running sum, then set n = n // 10. Repeat until n is 0.
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

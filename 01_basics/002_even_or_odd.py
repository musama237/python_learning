"""
Challenge: Even or Odd
Difficulty: ⭐ Easy
Topic: Conditionals, Modulo Operator

Write a function that returns "even" if a number is even, "odd" if odd.

Example:
    even_or_odd(4) -> "even"
    even_or_odd(7) -> "odd"

Hints:
    1. What does the remainder of a division tell you about a number?
    2. The modulo operator (%) gives the remainder — even numbers have remainder 0 when divided by 2.
    3. Check if n % 2 == 0 and return "even" or "odd" accordingly.
"""


def even_or_odd(n: int) -> str:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert even_or_odd(4) == "even"
    assert even_or_odd(7) == "odd"
    assert even_or_odd(0) == "even"
    assert even_or_odd(-3) == "odd"
    assert even_or_odd(-2) == "even"
    print("✅ All tests passed!")

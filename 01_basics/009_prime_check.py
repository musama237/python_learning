"""
Challenge: Prime Number Check
Difficulty: ⭐ Easy
Topic: Loops, Math, Optimization

Write a function that checks if a number is prime.
A prime number is greater than 1 and divisible only by 1 and itself.

Hint: You only need to check up to the square root of n.

Example:
    is_prime(7) -> True
    is_prime(4) -> False
"""


def is_prime(n: int) -> bool:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(7) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    assert is_prime(97) is True
    assert is_prime(100) is False
    print("✅ All tests passed!")

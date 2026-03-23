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

Hints:
    1. Think about which numbers to immediately rule out before doing any divisibility checks.
    2. Numbers less than 2 are not prime. You only need to check divisors up to the square root of n.
    3. Return False for n < 2. Loop from 2 to int(n**0.5) + 1; if any divides n evenly, return False. Otherwise return True.
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

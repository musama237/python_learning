"""
Challenge: Greatest Common Divisor (GCD)
Difficulty: ⭐ Easy
Topic: Math, Loops (Euclidean Algorithm)

Find the greatest common divisor of two positive integers.
Do NOT use math.gcd. Implement the Euclidean algorithm.

Euclidean algorithm: gcd(a, b) = gcd(b, a % b) until b == 0

Example:
    gcd(12, 8) -> 4
    gcd(17, 5) -> 1
"""


def gcd(a: int, b: int) -> int:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert gcd(100, 25) == 25
    assert gcd(7, 7) == 7
    assert gcd(48, 18) == 6
    assert gcd(1, 100) == 1
    print("✅ All tests passed!")

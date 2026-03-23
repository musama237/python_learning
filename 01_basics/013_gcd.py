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

Hints:
    1. The Euclidean algorithm repeatedly replaces the larger number — think about what operation reduces the problem.
    2. The key insight: gcd(a, b) = gcd(b, a % b). The process stops when b becomes 0, and a is the answer.
    3. Loop while b != 0: set a, b = b, a % b. When b is 0, return a.

Learn:
    # Euclidean algorithm step by step:
    # gcd(48, 18):
    #   48 % 18 = 12  -> gcd(18, 12)
    #   18 % 12 = 6   -> gcd(12, 6)
    #   12 % 6 = 0    -> gcd(6, 0) -> answer is 6

    # While loop with multiple assignment:
    a, b = 48, 18
    while b != 0:
        a, b = b, a % b
    # a is now the GCD
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

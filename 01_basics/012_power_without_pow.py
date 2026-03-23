"""
Challenge: Power Without pow()
Difficulty: ⭐ Easy
Topic: Loops, Math

Calculate base^exponent without using ** operator or pow().
Assume exponent is a non-negative integer.

Example:
    power(2, 10) -> 1024
    power(5, 0) -> 1

Hints:
    1. Exponentiation is just repeated multiplication — how many times do you multiply?
    2. Multiply the base by itself exponent times. Remember that anything raised to the power 0 is 1.
    3. Start result = 1, loop exponent times, multiply result *= base each iteration. Return result.

Learn:
    # Repeated multiplication:
    result = 1
    for _ in range(3):
        result *= 2  # 1*2=2, 2*2=4, 4*2=8
    # result is 2^3 = 8

    # The underscore _ means "I don't need this variable":
    for _ in range(5):  # just repeat 5 times
        pass
"""


def power(base: int, exponent: int) -> int:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert power(2, 10) == 1024
    assert power(5, 0) == 1
    assert power(3, 3) == 27
    assert power(1, 100) == 1
    assert power(0, 5) == 0
    assert power(7, 2) == 49
    print("✅ All tests passed!")

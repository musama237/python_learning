"""
Challenge: Fibonacci Sequence
Difficulty: ⭐ Easy
Topic: Loops, Sequences

Return the first n numbers of the Fibonacci sequence.
Fibonacci: each number is the sum of the two preceding ones.
Starts with 0, 1.

Example:
    fibonacci(5) -> [0, 1, 1, 2, 3]
    fibonacci(1) -> [0]
"""


def fibonacci(n: int) -> list[int]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert fibonacci(0) == []
    print("✅ All tests passed!")

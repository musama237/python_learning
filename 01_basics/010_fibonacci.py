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

Hints:
    1. Each Fibonacci number depends on the two numbers before it — think about what state you need to track.
    2. Keep two variables for the previous two values. Handle edge cases for n=0 (empty list) and n=1 ([0]).
    3. Start a list with [0, 1], then loop from index 2 to n, appending the sum of the last two elements each time.

Learn:
    # Multiple assignment to track two values:
    a, b = 0, 1
    a, b = b, a + b  # a becomes 1, b becomes 1

    # Building a list with append:
    result = []
    result.append(0)  # [0]
    result.append(1)  # [0, 1]

    # List slicing for edge cases:
    [0, 1][:0]  # -> []  (first 0 elements)
    [0, 1][:1]  # -> [0] (first 1 element)
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

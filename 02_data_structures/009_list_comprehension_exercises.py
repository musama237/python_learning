"""
Challenge: List Comprehension Exercises
Difficulty: ⭐ Easy
Topic: List Comprehensions

Solve each function using a SINGLE list comprehension (one line).

Example:
    squares(5) -> [0, 1, 4, 9, 16]
"""


def squares(n: int) -> list[int]:
    """Return squares of 0 to n-1."""
    # YOUR CODE HERE (one line)
    pass


def even_squares(n: int) -> list[int]:
    """Return squares of even numbers from 0 to n-1."""
    # YOUR CODE HERE (one line)
    pass


def flatten_2d(matrix: list[list]) -> list:
    """Flatten a 2D list using a comprehension."""
    # YOUR CODE HERE (one line)
    pass


def filter_long_words(words: list[str], min_length: int) -> list[str]:
    """Return words longer than min_length."""
    # YOUR CODE HERE (one line)
    pass


def string_lengths(words: list[str]) -> list[int]:
    """Return the length of each word."""
    # YOUR CODE HERE (one line)
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert squares(5) == [0, 1, 4, 9, 16]
    assert squares(0) == []
    assert even_squares(10) == [0, 4, 16, 36, 64]
    assert flatten_2d([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert filter_long_words(["hi", "hello", "hey", "python"], 3) == ["hello", "python"]
    assert string_lengths(["hi", "hello", "a"]) == [2, 5, 1]
    print("✅ All tests passed!")

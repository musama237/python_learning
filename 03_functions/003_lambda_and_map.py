"""
Challenge: Lambda, Map, Filter, Reduce
Difficulty: ⭐⭐ Medium
Topic: Functional Programming

Solve each using lambda with map/filter/reduce (one line each).
"""

from functools import reduce


def double_all(nums: list[int]) -> list[int]:
    """Double every number in the list using map + lambda."""
    # YOUR CODE HERE (one line)
    pass


def filter_positives(nums: list[int]) -> list[int]:
    """Keep only positive numbers using filter + lambda."""
    # YOUR CODE HERE (one line)
    pass


def product_of_all(nums: list[int]) -> int:
    """Multiply all numbers together using reduce + lambda. Return 1 for empty list."""
    # YOUR CODE HERE
    pass


def sort_by_last_char(words: list[str]) -> list[str]:
    """Sort strings by their last character using sorted + lambda."""
    # YOUR CODE HERE (one line)
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert double_all([1, 2, 3]) == [2, 4, 6]
    assert double_all([]) == []
    assert filter_positives([-1, 2, -3, 4, 0]) == [2, 4]
    assert product_of_all([1, 2, 3, 4]) == 24
    assert product_of_all([]) == 1
    assert sort_by_last_char(["hello", "hi", "hey"]) == ["hi", "hello", "hey"]
    print("✅ All tests passed!")

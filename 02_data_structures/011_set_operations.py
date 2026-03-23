"""
Challenge: Set Operations from Scratch
Difficulty: ⭐⭐ Medium
Topic: Sets, Logic

Implement set operations WITHOUT using Python's built-in set operations
(no &, |, -, ^). Use loops only.

Example:
    my_union([1, 2], [2, 3]) -> [1, 2, 3]
"""


def my_union(lst1: list, lst2: list) -> list:
    """Return sorted union of two lists."""
    # YOUR CODE HERE
    pass


def my_intersection(lst1: list, lst2: list) -> list:
    """Return sorted intersection of two lists."""
    # YOUR CODE HERE
    pass


def my_difference(lst1: list, lst2: list) -> list:
    """Return sorted elements in lst1 but not in lst2."""
    # YOUR CODE HERE
    pass


def my_symmetric_difference(lst1: list, lst2: list) -> list:
    """Return sorted elements in either list but not both."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert my_union([1, 2], [2, 3]) == [1, 2, 3]
    assert my_union([], [1]) == [1]
    assert my_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert my_intersection([1, 2], [3, 4]) == []
    assert my_difference([1, 2, 3], [2, 4]) == [1, 3]
    assert my_difference([1, 2], [1, 2]) == []
    assert my_symmetric_difference([1, 2, 3], [2, 3, 4]) == [1, 4]
    print("✅ All tests passed!")

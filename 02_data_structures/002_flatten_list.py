"""
Challenge: Flatten a Nested List
Difficulty: ⭐⭐ Medium
Topic: Lists, Recursion

Flatten a nested list of arbitrary depth into a single flat list.

Example:
    flatten([1, [2, [3, 4], 5], 6]) -> [1, 2, 3, 4, 5, 6]
"""


def flatten(lst: list) -> list:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[[[1]]]]) == [1]
    assert flatten([1, [2], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]
    print("✅ All tests passed!")

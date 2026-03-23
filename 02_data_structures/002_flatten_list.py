"""
Challenge: Flatten a Nested List
Difficulty: ⭐⭐ Medium
Topic: Lists, Recursion

Flatten a nested list of arbitrary depth into a single flat list.

Example:
    flatten([1, [2, [3, 4], 5], 6]) -> [1, 2, 3, 4, 5, 6]

Hints:
    1. Not every element is the same type — some are lists themselves.
    2. Use isinstance(element, list) to check if an element needs further flattening.
    3. For each element: if it's a list, recursively flatten it and extend your result; otherwise, append it directly.
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

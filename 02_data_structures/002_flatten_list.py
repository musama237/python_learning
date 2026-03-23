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

Learn:
    # Check if something is a list:
    isinstance([1, 2], list)  # -> True
    isinstance(5, list)       # -> False

    # Extend vs append:
    result = [1]
    result.append([2, 3])  # [1, [2, 3]] - adds list as element
    result.extend([2, 3])  # [1, 2, 3]   - adds each element

    # Recursion pattern:
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))  # recurse
            else:
                result.append(item)
        return result
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

"""
Challenge: Remove Duplicates (Preserve Order)
Difficulty: ⭐ Easy
Topic: Lists, Sets, Order

Remove duplicates from a list while preserving the original order.
Do NOT use dict.fromkeys() or set — use a loop.

Example:
    remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]

Hints:
    1. Think about how you could remember which items you've already encountered.
    2. A set gives O(1) lookup — use it to track what you've already seen.
    3. Iterate through the list; for each element, if it's not in your "seen" set, add it to the result and the set.

Learn:
    # Sets for O(1) lookup:
    seen = set()
    seen.add(1)
    1 in seen  # -> True (very fast)

    # Pattern: filter while preserving order:
    result = []
    seen = set()
    for item in [1, 2, 2, 3]:
        if item not in seen:
            result.append(item)
            seen.add(item)
"""


def remove_duplicates(lst: list) -> list:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    print("✅ All tests passed!")

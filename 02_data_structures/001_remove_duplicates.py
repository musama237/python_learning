"""
Challenge: Remove Duplicates (Preserve Order)
Difficulty: ⭐ Easy
Topic: Lists, Sets, Order

Remove duplicates from a list while preserving the original order.
Do NOT use dict.fromkeys() or set — use a loop.

Example:
    remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
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

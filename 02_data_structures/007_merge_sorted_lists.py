"""
Challenge: Merge Two Sorted Lists
Difficulty: ⭐⭐ Medium
Topic: Lists, Two Pointers

Merge two sorted lists into one sorted list. Do NOT use sort() or sorted().

Example:
    merge_sorted([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
"""


def merge_sorted(lst1: list[int], lst2: list[int]) -> list[int]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1, 2], []) == [1, 2]
    assert merge_sorted([], []) == []
    assert merge_sorted([1, 1], [1, 1]) == [1, 1, 1, 1]
    assert merge_sorted([1, 5, 9], [2, 3, 7, 10]) == [1, 2, 3, 5, 7, 9, 10]
    print("✅ All tests passed!")

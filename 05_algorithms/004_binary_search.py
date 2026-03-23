"""
Challenge: Binary Search Variants
Difficulty: ⭐⭐ Medium
Topic: Searching, Binary Search

Implement multiple binary search variants:
1. Standard binary search
2. Find first occurrence
3. Find last occurrence
4. Find insertion point (like bisect_left)

All inputs are sorted lists.
"""


def binary_search(arr: list[int], target: int) -> int:
    """Return index of target, or -1 if not found."""
    # YOUR CODE HERE
    pass


def find_first(arr: list[int], target: int) -> int:
    """Return index of FIRST occurrence of target, or -1."""
    # YOUR CODE HERE
    pass


def find_last(arr: list[int], target: int) -> int:
    """Return index of LAST occurrence of target, or -1."""
    # YOUR CODE HERE
    pass


def insertion_point(arr: list[int], target: int) -> int:
    """Return the index where target should be inserted to keep sorted order."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([], 1) == -1

    assert find_first([1, 2, 2, 2, 3], 2) == 1
    assert find_first([1, 1, 1], 1) == 0
    assert find_first([1, 2, 3], 4) == -1

    assert find_last([1, 2, 2, 2, 3], 2) == 3
    assert find_last([1, 1, 1], 1) == 2

    assert insertion_point([1, 3, 5, 7], 4) == 2
    assert insertion_point([1, 3, 5, 7], 0) == 0
    assert insertion_point([1, 3, 5, 7], 8) == 4
    assert insertion_point([1, 3, 5, 7], 3) == 1
    print("✅ All tests passed!")

"""
Challenge: Merge Sort
Difficulty: ⭐⭐ Medium
Topic: Sorting, Divide and Conquer, Recursion

Implement merge sort — a classic O(n log n) sorting algorithm.
Split the array in half, sort each half, then merge.

Example:
    merge_sort([38, 27, 43, 3, 9, 82, 10]) -> [3, 9, 10, 27, 38, 43, 82]
"""


def merge_sort(arr: list) -> list:
    """Sort using merge sort. Return a new sorted list."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([1, 1, 1]) == [1, 1, 1]
    import random
    big = random.sample(range(1000), 100)
    assert merge_sort(big) == sorted(big)
    print("✅ All tests passed!")

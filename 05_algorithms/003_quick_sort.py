"""
Challenge: Quick Sort
Difficulty: ⭐⭐ Medium
Topic: Sorting, Divide and Conquer, Partitioning

Implement quick sort. Pick the last element as pivot.

Example:
    quick_sort([10, 7, 8, 9, 1, 5]) -> [1, 5, 7, 8, 9, 10]
"""


def quick_sort(arr: list) -> list:
    """Sort using quick sort. Return a new sorted list."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([3, 3, 3]) == [3, 3, 3]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    import random
    big = random.sample(range(1000), 100)
    assert quick_sort(big) == sorted(big)
    print("✅ All tests passed!")

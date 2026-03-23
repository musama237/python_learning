"""
Challenge: Bubble Sort
Difficulty: ⭐ Easy
Topic: Sorting, Algorithms

Implement bubble sort. Optimize: stop early if no swaps occur in a pass.

Example:
    bubble_sort([5, 3, 8, 1, 2]) -> [1, 2, 3, 5, 8]
"""


def bubble_sort(arr: list) -> list:
    """Sort a list using bubble sort. Return a new sorted list."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([5, 5, 5]) == [5, 5, 5]
    print("✅ All tests passed!")

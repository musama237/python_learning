"""
Challenge: Recursive Functions
Difficulty: ⭐⭐ Medium
Topic: Recursion

Solve each problem using RECURSION only (no loops).

Example:
    sum_nested([1, [2, [3]], 4]) -> 10
"""


def sum_nested(lst) -> int:
    """Sum all numbers in a nested list structure using recursion."""
    # YOUR CODE HERE
    pass


def power_recursive(base: int, exp: int) -> int:
    """Calculate base^exp recursively. exp >= 0."""
    # YOUR CODE HERE
    pass


def reverse_string_recursive(s: str) -> str:
    """Reverse a string recursively."""
    # YOUR CODE HERE
    pass


def count_occurrences(lst: list, target) -> int:
    """Count how many times target appears in list, recursively."""
    # YOUR CODE HERE
    pass


def binary_search_recursive(arr: list[int], target: int, low: int = 0, high: int = None) -> int:
    """Return index of target in sorted arr, or -1. Use recursion."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert sum_nested([1, [2, [3]], 4]) == 10
    assert sum_nested([]) == 0
    assert sum_nested([[[5]]]) == 5

    assert power_recursive(2, 10) == 1024
    assert power_recursive(5, 0) == 1

    assert reverse_string_recursive("hello") == "olleh"
    assert reverse_string_recursive("") == ""

    assert count_occurrences([1, 2, 3, 2, 2], 2) == 3
    assert count_occurrences([], 1) == 0

    assert binary_search_recursive([1, 3, 5, 7, 9], 5) == 2
    assert binary_search_recursive([1, 3, 5, 7, 9], 4) == -1
    assert binary_search_recursive([], 1) == -1
    print("✅ All tests passed!")

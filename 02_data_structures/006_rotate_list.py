"""
Challenge: Rotate a List
Difficulty: ⭐ Easy
Topic: Lists, Slicing

Rotate a list by k positions to the right.

Example:
    rotate([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    rotate([1, 2, 3], 1) -> [3, 1, 2]
"""


def rotate(lst: list, k: int) -> list:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3], 1) == [3, 1, 2]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([], 5) == []
    assert rotate([1], 10) == [1]
    print("✅ All tests passed!")

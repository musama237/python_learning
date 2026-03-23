"""
Challenge: Rotate a List
Difficulty: ⭐ Easy
Topic: Lists, Slicing

Rotate a list by k positions to the right.

Example:
    rotate([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    rotate([1, 2, 3], 1) -> [3, 1, 2]

Hints:
    1. What happens if k is larger than the length of the list?
    2. Use modulo (k % len) to handle cases where k >= len; this gives the effective rotation.
    3. Split the list into two parts at position (len - k) and concatenate them in reverse order.
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

"""
Challenge: Matrix Transpose
Difficulty: ⭐⭐ Medium
Topic: Lists, Nested Loops, 2D Arrays

Transpose a matrix (list of lists). Rows become columns.

Example:
    transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
"""


def transpose(matrix: list[list]) -> list[list]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1]]) == [[1]]
    assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("✅ All tests passed!")

"""
Challenge: Matrix Transpose
Difficulty: ⭐⭐ Medium
Topic: Lists, Nested Loops, 2D Arrays

Transpose a matrix (list of lists). Rows become columns.

Example:
    transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]

Hints:
    1. In a transpose, the new row i is the old column i.
    2. Iterate over column indices, then collect each row's value at that column index.
    3. Build each new row as [matrix[row][col] for row in range(rows)] for each col, or use zip(*matrix).

Learn:
    # Access column values across rows:
    matrix = [[1, 2], [3, 4]]
    matrix[0][1]  # -> 2 (row 0, col 1)

    # zip unpacks rows into columns:
    list(zip(*[[1, 2], [3, 4]]))  # -> [(1, 3), (2, 4)]

    # Nested list comprehension:
    [[row[col] for row in matrix] for col in range(2)]
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

"""
Challenge: Backtracking
Difficulty: ⭐⭐⭐ Hard
Topic: Backtracking, Recursion, Combinatorics

1. Generate all permutations of a list.
2. Generate all combinations of size k.
3. Solve N-Queens problem.

Example:
    permutations([1, 2, 3]) -> [[1,2,3], [1,3,2], [2,1,3], ...]

Hints:
    1. Build the solution step by step; at each step try all valid options
    2. Backtrack (undo the last choice) if the current path cannot lead to a valid solution
    3. N-queens: place one queen per row, checking column and diagonal conflicts before placing

Learn:
    # Backtracking template:
    def backtrack(path, choices):
        if is_complete(path):
            results.append(path.copy())
            return
        for choice in choices:
            path.append(choice)         # make choice
            backtrack(path, remaining)   # explore
            path.pop()                  # undo choice

    # N-Queens: check conflicts:
    # Same column: col == placed_col
    # Same diagonal: abs(row - placed_row) == abs(col - placed_col)
"""


def permutations(arr: list) -> list[list]:
    """Return all permutations. Order doesn't matter."""
    # YOUR CODE HERE
    pass


def combinations(arr: list, k: int) -> list[list]:
    """Return all combinations of size k. Order doesn't matter."""
    # YOUR CODE HERE
    pass


def n_queens(n: int) -> int:
    """Return the NUMBER of valid N-Queens solutions."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    perms = permutations([1, 2, 3])
    assert len(perms) == 6
    assert sorted(perms) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

    combs = combinations([1, 2, 3, 4], 2)
    assert len(combs) == 6
    assert sorted(combs) == sorted([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

    assert n_queens(4) == 2
    assert n_queens(8) == 92
    assert n_queens(1) == 1
    print("✅ All tests passed!")

"""
Challenge: itertools Mastery
Difficulty: ⭐⭐ Medium
Topic: itertools, Lazy Evaluation, Combinatorics

Solve each using itertools functions. Import what you need.

Example:
    running_totals([1, 2, 3, 4]) -> [1, 3, 6, 10]

Hints:
    1. Use accumulate for running totals — it yields cumulative results by default
    2. chain.from_iterable flattens one level of nesting without unpacking
    3. groupby groups consecutive equal elements — perfect for group_consecutive
    4. Build the powerset by combining combinations of every possible length

Learn:
    from itertools import accumulate, chain, groupby, combinations, permutations
    list(accumulate([1,2,3]))  # -> [1, 3, 6]
    list(chain.from_iterable([[1,2],[3]]))  # -> [1, 2, 3]
    [(k, list(g)) for k, g in groupby([1,1,2,2])]  # groups consecutive
    list(combinations([1,2,3], 2))  # -> [(1,2), (1,3), (2,3)]
"""

import itertools


def running_totals(nums: list[int]) -> list[int]:
    """Cumulative sums using itertools.accumulate."""
    # YOUR CODE HERE (one line)
    pass


def flatten_itertools(nested: list[list]) -> list:
    """Flatten 2D list using itertools.chain."""
    # YOUR CODE HERE (one line)
    pass


def group_consecutive(data: list[int]) -> list[list[int]]:
    """Group consecutive equal elements.
    [1,1,2,2,2,3,1,1] -> [[1,1],[2,2,2],[3],[1,1]]
    """
    # YOUR CODE HERE
    pass


def powerset(s: list) -> list[tuple]:
    """Return all subsets (the power set) of s.
    powerset([1,2,3]) -> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
    """
    # YOUR CODE HERE
    pass


def nth_permutation(iterable, n: int) -> tuple:
    """Return the nth permutation (0-indexed) using itertools."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert running_totals([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_totals([]) == []
    assert flatten_itertools([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert group_consecutive([1, 1, 2, 2, 2, 3, 1, 1]) == [[1, 1], [2, 2, 2], [3], [1, 1]]
    assert powerset([1, 2, 3]) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    assert nth_permutation([1, 2, 3], 0) == (1, 2, 3)
    assert nth_permutation([1, 2, 3], 5) == (3, 2, 1)
    print("✅ All tests passed!")

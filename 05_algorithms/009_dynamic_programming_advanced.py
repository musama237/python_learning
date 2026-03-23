"""
Challenge: Dynamic Programming - Advanced
Difficulty: ⭐⭐⭐ Hard
Topic: DP, Knapsack, Subsequences

1. 0/1 Knapsack problem
2. Longest increasing subsequence
3. Edit distance (Levenshtein distance)

Example:
    knapsack(capacity=7, weights=[1,3,4,5], values=[1,4,5,7]) -> 9

Hints:
    1. Knapsack: build a 2D table dp[item][capacity] deciding to include or skip each item
    2. LIS: dp[i] = length of longest increasing subsequence ending at index i; check all j < i
    3. Edit distance: build a 2D table where each cell considers insert, delete, or replace operations

Learn:
    # 0/1 Knapsack:
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # skip item
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                    dp[i-1][w - weights[i-1]] + values[i-1])

    # Edit distance: dp[i][j] = min of 3 operations
    # insert: dp[i][j-1] + 1
    # delete: dp[i-1][j] + 1
    # replace: dp[i-1][j-1] + (0 if match else 1)
"""


def knapsack(capacity: int, weights: list[int], values: list[int]) -> int:
    """0/1 Knapsack: maximize value without exceeding capacity."""
    # YOUR CODE HERE
    pass


def longest_increasing_subsequence(arr: list[int]) -> int:
    """Return LENGTH of longest strictly increasing subsequence."""
    # YOUR CODE HERE
    pass


def edit_distance(s1: str, s2: str) -> int:
    """Minimum edit operations (insert, delete, replace) to convert s1 to s2."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7]) == 9
    assert knapsack(0, [1, 2], [10, 20]) == 0
    assert knapsack(10, [5, 5, 5], [10, 20, 30]) == 50

    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
    assert longest_increasing_subsequence([3, 2, 1]) == 1
    assert longest_increasing_subsequence([1, 2, 3]) == 3
    assert longest_increasing_subsequence([]) == 0

    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("horse", "ros") == 3
    print("✅ All tests passed!")

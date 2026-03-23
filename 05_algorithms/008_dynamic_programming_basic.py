"""
Challenge: Dynamic Programming - Basics
Difficulty: ⭐⭐ Medium
Topic: DP, Memoization, Tabulation

Solve classic DP problems:
1. Climbing stairs (1 or 2 steps at a time)
2. Coin change (minimum coins)
3. Longest common subsequence

Example:
    climb_stairs(5) -> 8
    coin_change([1, 5, 10], 11) -> 2 (10+1)

Hints:
    1. Climbing stairs: dp[i] = dp[i-1] + dp[i-2] (like Fibonacci)
    2. Coin change: dp[amount] = min(dp[amount - coin] + 1) for each coin
    3. LCS: build a 2D table where matching characters extend the diagonal value by 1

Learn:
    # DP with array (climbing stairs):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    # Coin change DP:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # 2D DP table (LCS):
    dp = [[0] * (m+1) for _ in range(n+1)]
"""


def climb_stairs(n: int) -> int:
    """How many distinct ways to climb n stairs (1 or 2 steps at a time)?"""
    # YOUR CODE HERE
    pass


def coin_change(coins: list[int], amount: int) -> int:
    """Minimum number of coins to make amount. Return -1 if impossible."""
    # YOUR CODE HERE
    pass


def longest_common_subsequence(s1: str, s2: str) -> int:
    """Return length of longest common subsequence."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89

    assert coin_change([1, 5, 10], 11) == 2
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2, 5], 11) == 3

    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("", "abc") == 0
    print("✅ All tests passed!")

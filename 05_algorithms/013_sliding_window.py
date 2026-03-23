"""
Challenge: Sliding Window Technique
Difficulty: ⭐⭐ Medium
Topic: Arrays, Two Pointers, Sliding Window

1. Maximum sum subarray of size k
2. Longest substring without repeating characters
3. Minimum window substring

Example:
    max_sum_subarray([2, 1, 5, 1, 3, 2], 3) -> 9

Hints:
    1. Fixed window: add the new right element and remove the old left element as the window slides
    2. Variable window: expand right to include more; shrink left when the window condition breaks
    3. For minimum window substring, use a character frequency map and track how many required chars are satisfied

Learn:
    # Fixed window sum:
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide
        max_sum = max(max_sum, window_sum)

    # Variable window (two pointers):
    left = 0
    for right in range(len(s)):
        # expand window
        while condition_broken:
            # shrink from left
            left += 1
"""


def max_sum_subarray(arr: list[int], k: int) -> int:
    """Return maximum sum of any contiguous subarray of size k."""
    # YOUR CODE HERE
    pass


def longest_unique_substring(s: str) -> int:
    """Return length of longest substring without repeating characters."""
    # YOUR CODE HERE
    pass


def min_window_substring(s: str, t: str) -> str:
    """Return minimum window in s that contains all characters of t.
    Return "" if no such window exists.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray([1, 2, 3], 1) == 3
    assert max_sum_subarray([1, 2, 3], 3) == 6

    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0

    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("a", "aa") == ""
    print("✅ All tests passed!")

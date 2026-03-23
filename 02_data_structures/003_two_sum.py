"""
Challenge: Two Sum
Difficulty: ⭐⭐ Medium
Topic: Lists, Dicts (Hash Maps)

Given a list of integers and a target, return the indices of two numbers
that add up to the target. Each input has exactly one solution.
You may not use the same element twice.

Example:
    two_sum([2, 7, 11, 15], 9) -> (0, 1)

Hints:
    1. A brute-force nested loop works, but there's a faster way using a lookup structure.
    2. Use a dict to store {value: index} as you iterate through the list.
    3. For each number, check if (target - num) already exists in your dict; if so, return both indices.
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([1, 5, 3, 7], 8) == (1, 2)
    print("✅ All tests passed!")

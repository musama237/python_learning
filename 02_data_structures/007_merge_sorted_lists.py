"""
Challenge: Merge Two Sorted Lists
Difficulty: ⭐⭐ Medium
Topic: Lists, Two Pointers

Merge two sorted lists into one sorted list. Do NOT use sort() or sorted().

Example:
    merge_sorted([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]

Hints:
    1. Since both lists are already sorted, you can build the result in one pass.
    2. Use two pointers (indices), one for each list, and always take the smaller front element.
    3. Compare lst1[i] and lst2[j]; append the smaller one and advance that pointer. After the loop, append any remaining elements.

Learn:
    # Two-pointer technique:
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    # Append remaining elements:
    result.extend(lst1[i:])  # any remaining from lst1
    result.extend(lst2[j:])  # any remaining from lst2
"""


def merge_sorted(lst1: list[int], lst2: list[int]) -> list[int]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1, 2], []) == [1, 2]
    assert merge_sorted([], []) == []
    assert merge_sorted([1, 1], [1, 1]) == [1, 1, 1, 1]
    assert merge_sorted([1, 5, 9], [2, 3, 7, 10]) == [1, 2, 3, 5, 7, 9, 10]
    print("✅ All tests passed!")

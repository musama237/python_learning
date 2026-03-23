"""
Challenge: Group Anagrams
Difficulty: ⭐⭐ Medium
Topic: Dicts, Strings, Sorting

Group a list of strings into anagram groups.
Return a list of groups (each group is a sorted list of words).
Sort the groups by their first element.

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

Hints:
    1. Anagrams share the same letters — how could you create a common identifier for them?
    2. Sorting a word's characters gives a canonical key (e.g., sorted("eat") -> "aet").
    3. Use a dict with the sorted-character tuple/string as key; append each word to its group, then sort and return the groups.
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert result == expected
    assert group_anagrams([]) == []
    assert group_anagrams(["a"]) == [["a"]]
    print("✅ All tests passed!")

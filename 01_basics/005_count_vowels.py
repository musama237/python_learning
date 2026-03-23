"""
Challenge: Count Vowels
Difficulty: ⭐ Easy
Topic: Strings, Loops, Conditionals

Count the number of vowels (a, e, i, o, u) in a string. Case-insensitive.

Example:
    count_vowels("Hello World") -> 3
"""


def count_vowels(s: str) -> int:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert count_vowels("Hello World") == 3
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0
    assert count_vowels("Python Programming") == 4
    print("✅ All tests passed!")

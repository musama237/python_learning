"""
Challenge: Count Vowels
Difficulty: ⭐ Easy
Topic: Strings, Loops, Conditionals

Count the number of vowels (a, e, i, o, u) in a string. Case-insensitive.

Example:
    count_vowels("Hello World") -> 3

Hints:
    1. How can you check if a character belongs to a set of characters? Think about the "in" operator.
    2. Convert the string to lowercase first so you only need to check against lowercase vowels "aeiou".
    3. Iterate through each character, check if it is in "aeiou" (after lowering), and keep a running count.
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

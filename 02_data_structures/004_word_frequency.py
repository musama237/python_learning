"""
Challenge: Word Frequency Counter
Difficulty: ⭐ Easy
Topic: Dicts, Strings, Loops

Count the frequency of each word in a string. Convert to lowercase.
Return a dictionary.

Example:
    word_frequency("the cat and the dog") -> {"the": 2, "cat": 1, "and": 1, "dog": 1}

Hints:
    1. You need to break the string into individual words first.
    2. Use str.split() to get words, and str.lower() to normalize case.
    3. Iterate over the lowercase words; for each word, increment its count in a dict (defaulting to 0).
"""


def word_frequency(text: str) -> dict[str, int]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert word_frequency("the cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert word_frequency("") == {}
    assert word_frequency("hello") == {"hello": 1}
    assert word_frequency("Hello hello HELLO") == {"hello": 3}
    print("✅ All tests passed!")

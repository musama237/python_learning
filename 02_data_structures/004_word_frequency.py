"""
Challenge: Word Frequency Counter
Difficulty: ⭐ Easy
Topic: Dicts, Strings, Loops

Count the frequency of each word in a string. Convert to lowercase.
Return a dictionary.

Example:
    word_frequency("the cat and the dog") -> {"the": 2, "cat": 1, "and": 1, "dog": 1}
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

"""
Challenge: Number to Words (0-99)
Difficulty: ⭐⭐ Medium
Topic: Conditionals, Strings, Mapping

Convert an integer (0-99) to its English word representation.

Example:
    number_to_words(0) -> "zero"
    number_to_words(15) -> "fifteen"
    number_to_words(42) -> "forty two"
    number_to_words(99) -> "ninety nine"

Hints:
    1. Numbers have different naming patterns — ones (0-9), teens (10-19), and tens (20-90). Think about using lookup dictionaries.
    2. Create separate mappings for ones, teens (11-19), and tens (20, 30, ..., 90). The teens are special cases that don't follow the normal pattern.
    3. Check if n < 10 (use ones dict), if n < 20 (use teens dict), otherwise combine tens[n // 10] with ones[n % 10] if the remainder is non-zero.
"""


def number_to_words(n: int) -> str:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert number_to_words(0) == "zero"
    assert number_to_words(5) == "five"
    assert number_to_words(11) == "eleven"
    assert number_to_words(15) == "fifteen"
    assert number_to_words(20) == "twenty"
    assert number_to_words(42) == "forty two"
    assert number_to_words(99) == "ninety nine"
    assert number_to_words(10) == "ten"
    print("✅ All tests passed!")

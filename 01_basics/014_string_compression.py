"""
Challenge: Basic String Compression
Difficulty: ⭐⭐ Medium
Topic: Strings, Loops, Counting

Compress a string by counting consecutive repeated characters.
If the compressed string is not shorter, return the original.

Example:
    compress("aabcccccaaa") -> "a2b1c5a3"
    compress("abc") -> "abc"  (compressed "a1b1c1" is longer)
"""


def compress(s: str) -> str:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("abc") == "abc"
    assert compress("") == ""
    assert compress("aaa") == "a3"
    assert compress("aabb") == "aabb"
    assert compress("aaabba") == "a3b2a1"
    print("✅ All tests passed!")

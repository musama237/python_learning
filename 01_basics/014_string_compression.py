"""
Challenge: Basic String Compression
Difficulty: ⭐⭐ Medium
Topic: Strings, Loops, Counting

Compress a string by counting consecutive repeated characters.
If the compressed string is not shorter, return the original.

Example:
    compress("aabcccccaaa") -> "a2b1c5a3"
    compress("abc") -> "abc"  (compressed "a1b1c1" is longer)

Hints:
    1. Think about tracking the current character and how many times it appears consecutively.
    2. Walk through the string keeping a current character and a count. When the character changes, append the char and count to your result.
    3. Build a compressed string by tracking runs of identical characters. After the loop, compare len(compressed) vs len(original) and return the shorter one.
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

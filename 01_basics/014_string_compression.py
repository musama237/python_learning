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

Learn:
    # Tracking consecutive characters:
    s = "aaabb"
    current = s[0]  # 'a'
    count = 1
    for char in s[1:]:     # iterate from 2nd char
        if char == current:
            count += 1
        else:
            # char changed, process current run
            current = char
            count = 1

    # f-string formatting:
    f"{char}{count}"  # e.g., "a3"

    # Compare lengths:
    compressed = "a3b2"
    original = "aaabb"
    shorter = compressed if len(compressed) < len(original) else original
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

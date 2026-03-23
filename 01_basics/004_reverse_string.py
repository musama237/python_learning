"""
Challenge: Reverse a String
Difficulty: ⭐ Easy
Topic: Strings, Loops

Reverse a string WITHOUT using slicing ([::-1]) or reversed().
Use a loop.

Example:
    reverse_string("hello") -> "olleh"
"""


def reverse_string(s: str) -> str:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("12345") == "54321"
    print("✅ All tests passed!")

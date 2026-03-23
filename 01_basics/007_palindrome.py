"""
Challenge: Palindrome Check
Difficulty: ⭐ Easy
Topic: Strings, Logic

Check if a string is a palindrome (reads the same forwards and backwards).
Ignore case and non-alphanumeric characters.

Example:
    is_palindrome("racecar") -> True
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("hello") -> False
"""


def is_palindrome(s: str) -> bool:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("No lemon, no melon") is True
    print("✅ All tests passed!")

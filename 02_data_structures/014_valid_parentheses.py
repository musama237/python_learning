"""
Challenge: Valid Parentheses
Difficulty: ⭐⭐ Medium
Topic: Stacks, Strings

Given a string containing just '(', ')', '{', '}', '[', ']',
determine if the input string has valid (balanced) brackets.

Example:
    is_valid("()[]{}") -> True
    is_valid("(]") -> False
    is_valid("([)]") -> False
    is_valid("{[]}") -> True
"""


def is_valid(s: str) -> bool:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(") is False
    assert is_valid("((()))") is True
    assert is_valid("({[()]})") is True
    print("✅ All tests passed!")

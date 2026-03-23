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

Hints:
    1. Think about what data structure lets you match the most recent opening bracket with a closing one.
    2. Use a stack: push opening brackets, and when you see a closing bracket, pop and check if it matches.
    3. Create a mapping of closing-to-opening brackets; for each char, push if opening, pop and compare if closing. At the end, the stack should be empty.

Learn:
    # Mapping closing to opening brackets:
    pairs = {")": "(", "]": "[", "}": "{"}

    # Stack-based matching:
    stack = []
    char = "("
    if char in "({[":
        stack.append(char)    # push opening bracket
    elif char in ")}]":
        if stack and stack[-1] == pairs[char]:
            stack.pop()       # matched!
        else:
            return False      # mismatch
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

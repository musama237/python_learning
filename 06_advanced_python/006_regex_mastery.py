"""
Challenge: Regular Expressions
Difficulty: ⭐⭐ Medium
Topic: regex, Pattern Matching, Text Processing

Write functions that use regex to solve text processing problems.
"""

import re


def validate_email(email: str) -> bool:
    """Check if email is valid. Basic rules:
    - Has exactly one @
    - Local part: alphanumeric, dots, underscores, hyphens
    - Domain: alphanumeric and hyphens, at least one dot
    """
    # YOUR CODE HERE
    pass


def extract_dates(text: str) -> list[str]:
    """Extract all dates in DD/MM/YYYY or DD-MM-YYYY format from text."""
    # YOUR CODE HERE
    pass


def camel_to_snake(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case.
    'myVariableName' -> 'my_variable_name'
    'HTTPResponse' -> 'http_response'
    """
    # YOUR CODE HERE
    pass


def find_repeated_words(text: str) -> list[str]:
    """Find words that appear consecutively repeated (case-insensitive).
    'the the cat' -> ['the']
    """
    # YOUR CODE HERE
    pass


def mask_credit_cards(text: str) -> str:
    """Replace credit card numbers (16 digits, possibly with spaces/dashes)
    with masked version showing only last 4 digits.
    '1234 5678 9012 3456' -> '****-****-****-3456'
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert validate_email("user@example.com") is True
    assert validate_email("user.name@domain.co.uk") is True
    assert validate_email("invalid@") is False
    assert validate_email("@domain.com") is False
    assert validate_email("no-at-sign.com") is False

    text = "Born on 15/03/1990 and graduated 20-06-2015."
    assert extract_dates(text) == ["15/03/1990", "20-06-2015"]

    assert camel_to_snake("myVariableName") == "my_variable_name"
    assert camel_to_snake("HTTPResponse") == "http_response"
    assert camel_to_snake("simpleTest") == "simple_test"

    assert find_repeated_words("the the cat sat on on the mat") == ["the", "on"]
    assert find_repeated_words("no repeats here") == []

    assert mask_credit_cards("Card: 1234 5678 9012 3456") == "Card: ****-****-****-3456"
    assert mask_credit_cards("Card: 1234-5678-9012-3456") == "Card: ****-****-****-3456"
    print("✅ All tests passed!")

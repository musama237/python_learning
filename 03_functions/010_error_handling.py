"""
Challenge: Error Handling
Difficulty: ⭐⭐ Medium
Topic: Exceptions, Try/Except, Custom Exceptions

1. Write a safe_divide that returns None on division errors.
2. Write a function that validates and parses user input.
3. Create a custom exception hierarchy.

Example:
    safe_divide(10, 3) -> 3.333...
    safe_divide(10, 0) -> None

Hints:
    1. Wrap risky operations in try/except and return a safe default when things go wrong.
    2. Use isinstance() to check types before operating; raise your custom exceptions with descriptive messages for validation.
    3. safe_divide: try a/b, except (ZeroDivisionError, TypeError) return None. validate_age: check isinstance(value, int) first (raise TypeValidationError), then check 0 <= value <= 150 (raise RangeValidationError).

Learn:
    # try/except catches errors:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        result = None

    # Catch multiple exception types:
    except (ValueError, TypeError):
        pass

    # Custom exceptions:
    class MyError(Exception):
        pass
    raise MyError("something went wrong")

    # isinstance for type checking:
    isinstance(42, int)     # -> True
    isinstance("hi", int)   # -> False
"""


def safe_divide(a, b) -> float | None:
    """Divide a by b. Return None if b is zero or inputs aren't numbers."""
    # YOUR CODE HERE
    pass


class ValidationError(Exception):
    """Base validation error."""
    pass


class TypeValidationError(ValidationError):
    """Raised when type is wrong."""
    pass


class RangeValidationError(ValidationError):
    """Raised when value is out of range."""
    pass


def validate_age(value) -> int:
    """Validate that value is an integer between 0 and 150.
    Raise TypeValidationError if not an int.
    Raise RangeValidationError if out of range.
    Return the value if valid.
    """
    # YOUR CODE HERE
    pass


def safe_parse_int(s: str, default: int = 0) -> int:
    """Try to parse string to int. Return default if it fails."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert safe_divide(10, 3) == 10 / 3
    assert safe_divide(10, 0) is None
    assert safe_divide("a", 1) is None

    assert validate_age(25) == 25
    try:
        validate_age("25")
        assert False
    except TypeValidationError:
        pass
    try:
        validate_age(-1)
        assert False
    except RangeValidationError:
        pass
    try:
        validate_age(200)
        assert False
    except RangeValidationError:
        pass

    assert safe_parse_int("42") == 42
    assert safe_parse_int("abc") == 0
    assert safe_parse_int("abc", -1) == -1
    print("✅ All tests passed!")

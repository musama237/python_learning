"""
Challenge: Dict Comprehension Exercises
Difficulty: ⭐ Easy
Topic: Dict Comprehensions

Solve each function using a SINGLE dict comprehension.

Hints:
    1. Dict comprehensions follow the pattern: {key: value for item in iterable}.
    2. You can add conditions with if, and iterate over .items() to access both keys and values.
    3. For merge: collect all keys from both dicts using a set union, then sum values with dict.get(key, 0) for each dict.
"""


def invert_dict(d: dict) -> dict:
    """Swap keys and values.
    Example: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    # YOUR CODE HERE (one line)
    pass


def count_chars(s: str) -> dict[str, int]:
    """Count character frequencies in a string.
    Example: "aab" -> {"a": 2, "b": 1}
    """
    # YOUR CODE HERE
    pass


def filter_dict(d: dict, threshold: int) -> dict:
    """Keep only entries where value > threshold.
    Example: {"a": 1, "b": 5, "c": 3}, 2 -> {"b": 5, "c": 3}
    """
    # YOUR CODE HERE (one line)
    pass


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dicts. If key exists in both, sum the values.
    Example: {"a": 1}, {"a": 2, "b": 3} -> {"a": 3, "b": 3}
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}
    assert count_chars("aab") == {"a": 2, "b": 1}
    assert count_chars("") == {}
    assert filter_dict({"a": 1, "b": 5, "c": 3}, 2) == {"b": 5, "c": 3}
    assert merge_dicts({"a": 1}, {"a": 2, "b": 3}) == {"a": 3, "b": 3}
    assert merge_dicts({}, {"x": 1}) == {"x": 1}
    print("✅ All tests passed!")

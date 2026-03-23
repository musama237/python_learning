"""
Challenge: *args and **kwargs
Difficulty: ⭐ Easy
Topic: Functions, Unpacking

Write a function that takes any number of positional and keyword arguments
and returns a tuple of (sum_of_positional_args, dict_of_kwargs).
All positional args will be numbers.

Example:
    flexible(1, 2, 3, name="Alice", age=30)
    -> (6, {"name": "Alice", "age": 30})
"""


def flexible(*args, **kwargs) -> tuple:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert flexible(1, 2, 3, name="Alice") == (6, {"name": "Alice"})
    assert flexible() == (0, {})
    assert flexible(10) == (10, {})
    assert flexible(x=1, y=2) == (0, {"x": 1, "y": 2})
    assert flexible(1, 2, 3, 4, 5) == (15, {})
    print("✅ All tests passed!")

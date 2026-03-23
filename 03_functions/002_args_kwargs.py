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

Hints:
    1. Consider what built-in function can add up a collection of numbers, and what kwargs already is.
    2. sum() works directly on the args tuple; kwargs is already a dict you can return as-is.
    3. Return a tuple of (sum(args), kwargs) -- that handles empty args (sum returns 0) and empty kwargs (empty dict).

Learn:
    # *args collects positional args as a tuple:
    def f(*args):
        print(args)  # (1, 2, 3)
    f(1, 2, 3)

    # **kwargs collects keyword args as a dict:
    def f(**kwargs):
        print(kwargs)  # {"name": "Alice", "age": 30}
    f(name="Alice", age=30)

    # sum() works on tuples:
    sum((1, 2, 3))  # -> 6
    sum(())          # -> 0
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

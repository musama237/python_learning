"""
Challenge: Closures
Difficulty: ⭐⭐ Medium
Topic: Functions, Closures, State

A closure is a function that remembers variables from its enclosing scope.

1. Write a counter factory that returns an increment function.
2. Write a multiplier factory.

Example:
    count = make_counter(10)
    count() -> 11
    count() -> 12

    double = make_multiplier(2)
    double(5) -> 10
"""


def make_counter(start: int = 0):
    """Return a function that returns the next count each time it's called."""
    # YOUR CODE HERE
    pass


def make_multiplier(factor: int):
    """Return a function that multiplies its argument by factor."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    count = make_counter(10)
    assert count() == 11
    assert count() == 12
    assert count() == 13

    count2 = make_counter()
    assert count2() == 1
    assert count2() == 2

    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(5) == 10
    assert triple(5) == 15
    assert double(0) == 0
    print("✅ All tests passed!")

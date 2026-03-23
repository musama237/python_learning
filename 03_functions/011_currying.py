"""
Challenge: Currying and Partial Application
Difficulty: ⭐⭐⭐ Hard
Topic: Functional Programming, Closures

1. Write a curry function that converts a multi-arg function to a chain of single-arg functions.
2. Write a partial function (like functools.partial but from scratch).

Example:
    @curry
    def add(a, b, c):
        return a + b + c

    add(1)(2)(3) -> 6
    add(1, 2)(3) -> 6

Hints:
    1. Currying transforms f(a, b, c) into f(a)(b)(c) -- you need to collect arguments until you have enough.
    2. Use inspect.signature to count how many args the function expects. Return a new function that accumulates args until enough are collected.
    3. Inside curry, define an inner function that takes *args, appends to accumulated args, and if len(accumulated) >= expected param count calls the original func, otherwise returns another accumulating function.
"""

import inspect


def curry(func):
    """Decorator that curries a function. Supports partial application.
    add(1)(2)(3) and add(1, 2)(3) and add(1, 2, 3) should all work.
    """
    # YOUR CODE HERE
    pass


def my_partial(func, *partial_args, **partial_kwargs):
    """Return a new function with some arguments pre-filled.
    Do NOT use functools.partial.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    @curry
    def add(a, b, c):
        return a + b + c

    assert add(1)(2)(3) == 6
    assert add(1, 2)(3) == 6
    assert add(1, 2, 3) == 6
    assert add(1)(2, 3) == 6

    def multiply(a, b):
        return a * b

    double = my_partial(multiply, 2)
    assert double(5) == 10
    assert double(3) == 6

    def greet(greeting, name, punct="!"):
        return f"{greeting}, {name}{punct}"

    hello = my_partial(greet, "Hello")
    assert hello("World") == "Hello, World!"
    assert hello("World", punct=".") == "Hello, World."
    print("✅ All tests passed!")

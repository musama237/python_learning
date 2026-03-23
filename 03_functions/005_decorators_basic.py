"""
Challenge: Basic Decorators
Difficulty: ⭐⭐ Medium
Topic: Decorators, Higher-Order Functions

1. Write a decorator that logs function calls (name + args).
2. Write a decorator that times function execution.

The timer decorator should add an attribute 'last_time' to the function.
The logger should store logs in a list attribute 'logs' on the function.

Hints:
    1. A decorator is a function that takes a function and returns a new wrapper function that adds behavior.
    2. Use functools.wraps on your wrapper; you can store state as attributes on the wrapper function itself (e.g., wrapper.logs = []).
    3. For logger: define wrapper(*args, **kwargs), format args into a string, append to wrapper.logs, then call and return func(*args, **kwargs). For timer: record time.time() before and after the call, store the difference in wrapper.last_time.
"""

import time


def logger(func):
    """Decorator that records each call as 'func_name(args, kwargs)' string
    in func.logs list.

    Example log entry: "add(1, 2)" or "greet(name='Alice')"
    """
    # YOUR CODE HERE
    pass


def timer(func):
    """Decorator that times each call and stores elapsed seconds
    in func.last_time.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    @logger
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    assert add(3, 4) == 7
    assert len(add.logs) == 2
    assert "add(1, 2)" in add.logs[0]

    @timer
    def slow():
        time.sleep(0.1)
        return "done"

    result = slow()
    assert result == "done"
    assert slow.last_time >= 0.05
    print("✅ All tests passed!")

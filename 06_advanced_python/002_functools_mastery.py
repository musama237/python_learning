"""
Challenge: functools Mastery
Difficulty: ⭐⭐ Medium
Topic: functools, Caching, Partial

Explore functools: lru_cache, partial, reduce, singledispatch.
"""

import functools


def fibonacci_cached(n: int) -> int:
    """Compute fibonacci using @lru_cache for O(n) performance.
    fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
    """
    # YOUR CODE HERE - use @functools.lru_cache
    pass


def create_power_functions() -> dict:
    """Return dict of {'square': fn, 'cube': fn, 'fourth': fn}
    using functools.partial with a single base power function.
    """
    # YOUR CODE HERE
    pass


@functools.singledispatch
def format_value(value) -> str:
    """Format different types differently:
    - str: return as-is in quotes
    - int: return with commas (1000 -> "1,000")
    - float: return with 2 decimal places
    - list: return comma-separated
    - Default: str(value)
    """
    return str(value)


# Register your singledispatch implementations below:
# YOUR CODE HERE


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert fibonacci_cached(50) == 12586269025
    assert fibonacci_cached(0) == 0
    assert fibonacci_cached(1) == 1

    powers = create_power_functions()
    assert powers["square"](5) == 25
    assert powers["cube"](3) == 27
    assert powers["fourth"](2) == 16

    assert format_value("hello") == '"hello"'
    assert format_value(1000000) == "1,000,000"
    assert format_value(3.14159) == "3.14"
    assert format_value([1, 2, 3]) == "1, 2, 3"
    print("✅ All tests passed!")

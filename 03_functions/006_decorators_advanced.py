"""
Challenge: Advanced Decorators
Difficulty: ⭐⭐⭐ Hard
Topic: Decorators, Parameterized Decorators

1. Write a retry decorator that retries a function up to n times on exception.
2. Write a memoize decorator that caches results.

Example:
    @retry(max_attempts=3)
    def unstable():
        ...

    @memoize
    def fib(n):
        ...

Hints:
    1. retry needs a decorator factory (function returning a decorator); memoize needs a dict to remember previous results.
    2. For retry: loop max_attempts times with try/except, re-raise on the last attempt. For memoize: use a dict with args as key, store it on func.cache.
    3. retry: for i in range(max_attempts) try calling func, except on the last iteration re-raise. memoize: check if args in cache dict, if not compute and store, then return cached value.
"""


def retry(max_attempts: int = 3):
    """Decorator factory. Retry the function up to max_attempts times.
    If all attempts fail, raise the last exception.
    """
    # YOUR CODE HERE
    pass


def memoize(func):
    """Decorator that caches function results based on arguments.
    Store cache in func.cache dict.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test retry
    call_count = 0

    @retry(max_attempts=3)
    def flaky():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("Not yet")
        return "success"

    assert flaky() == "success"
    assert call_count == 3

    fail_count = 0

    @retry(max_attempts=2)
    def always_fails():
        nonlocal fail_count
        fail_count += 1
        raise RuntimeError("fail")

    try:
        always_fails()
        assert False, "Should have raised"
    except RuntimeError:
        assert fail_count == 2

    # Test memoize
    fib_calls = 0

    @memoize
    def fib(n):
        nonlocal fib_calls
        fib_calls += 1
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(10) == 55
    assert fib_calls == 11  # Each value computed only once
    assert fib(10) == 55  # From cache, no extra calls
    assert fib_calls == 11
    print("✅ All tests passed!")

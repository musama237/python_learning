"""
Challenge: Context Manager Protocol
Difficulty: ⭐⭐ Medium
Topic: __enter__, __exit__, with statement

1. Create a Timer context manager that measures elapsed time.
2. Create a FileTransaction that writes to a temp file first,
   then replaces the original only if no exception occurred.

Example:
    with Timer() as t:
        time.sleep(0.1)
    t.elapsed >= 0.1  # True

Hints:
    1. __enter__ starts timer, returns self
    2. __exit__ computes elapsed
    3. SuppressErrors returns True from __exit__ to suppress

Learn:
    # Context manager protocol:
    class MyContext:
        def __enter__(self):
            # setup code
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            # cleanup code
            return False  # True = suppress exception

    # Timer pattern:
    import time
    self._start = time.time()       # in __enter__
    self.elapsed = time.time() - self._start  # in __exit__

    # Suppress specific exceptions:
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.suppressed:
            return True  # swallow exception
        return False      # let it propagate
"""

import time
import os
import tempfile


class Timer:
    """Context manager that measures elapsed time in seconds."""

    def __init__(self):
        self.elapsed = 0.0

    def __enter__(self):
        # YOUR CODE HERE
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        pass


class SuppressErrors:
    """Context manager that suppresses specified exception types.

    Example:
        with SuppressErrors(ValueError, TypeError):
            raise ValueError("ignored")
        # No error raised outside
    """

    def __init__(self, *exceptions):
        # YOUR CODE HERE
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE - return True to suppress, False otherwise
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    with Timer() as t:
        time.sleep(0.1)
    assert t.elapsed >= 0.05

    with Timer() as t2:
        pass
    assert t2.elapsed < 0.1

    with SuppressErrors(ValueError):
        raise ValueError("should be suppressed")

    with SuppressErrors(ValueError, TypeError):
        raise TypeError("also suppressed")

    try:
        with SuppressErrors(ValueError):
            raise RuntimeError("not suppressed")
        assert False
    except RuntimeError:
        pass
    print("✅ All tests passed!")

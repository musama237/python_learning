"""
Challenge: Advanced Context Managers
Difficulty: ⭐⭐⭐ Hard
Topic: contextlib, Generator-based CMs, Nested CMs

1. Write context managers using @contextmanager decorator.
2. Create a database transaction simulator.
3. Create a temporary directory context manager.
"""

from contextlib import contextmanager
import tempfile
import os
from pathlib import Path


@contextmanager
def redirect_stdout_to_list():
    """Context manager that captures all print() output into a list.
    Yields the list that accumulates printed strings.

    Example:
        with redirect_stdout_to_list() as output:
            print("hello")
            print("world")
        output -> ["hello", "world"]
    """
    # YOUR CODE HERE
    pass


@contextmanager
def transaction(data: dict):
    """Simulate a database transaction on a dict.
    If an exception occurs inside the block, rollback all changes.
    If no exception, commit (keep changes).

    Example:
        d = {"a": 1}
        with transaction(d):
            d["b"] = 2
            raise ValueError()  # d is still {"a": 1}
    """
    # YOUR CODE HERE
    pass


@contextmanager
def temp_workspace():
    """Create a temporary directory, cd into it, yield the Path,
    then cd back and clean up the directory.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test redirect
    with redirect_stdout_to_list() as output:
        print("hello")
        print("world")
    assert output == ["hello", "world"]

    # Test transaction - success
    data = {"x": 1, "y": 2}
    with transaction(data):
        data["z"] = 3
    assert data == {"x": 1, "y": 2, "z": 3}

    # Test transaction - rollback
    data = {"x": 1, "y": 2}
    try:
        with transaction(data):
            data["z"] = 3
            data["x"] = 999
            raise ValueError("abort!")
    except ValueError:
        pass
    assert data == {"x": 1, "y": 2}  # Rolled back

    # Test temp_workspace
    original_dir = os.getcwd()
    with temp_workspace() as tmp:
        assert Path(tmp).exists()
        assert os.getcwd() == str(tmp)
        (tmp / "test.txt").write_text("hello")
    assert os.getcwd() == original_dir
    assert not Path(tmp).exists()  # Cleaned up
    print("✅ All tests passed!")

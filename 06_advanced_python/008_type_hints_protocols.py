"""
Challenge: Type Hints & Protocols
Difficulty: ⭐⭐ Medium
Topic: typing, Protocol, Generic, TypeVar

Use advanced type hints to create well-typed code.
All code should pass mypy strict checking.

Hints:
    1. For SortedList: use the bisect module to find the O(log n) insertion point
    2. For Result: store both value and error, then check which one is set for is_ok/unwrap
"""

from typing import TypeVar, Generic, Protocol, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...


class SortedList(Generic[T]):
    """A list that maintains sorted order on insertion.
    Only accepts items that implement Comparable.
    """

    def __init__(self):
        # YOUR CODE HERE
        pass

    def insert(self, item: T) -> None:
        """Insert item in sorted position."""
        # YOUR CODE HERE
        pass

    def remove(self, item: T) -> None:
        """Remove first occurrence. Raise ValueError if not found."""
        # YOUR CODE HERE
        pass

    def __contains__(self, item: T) -> bool:
        """Use binary search for O(log n) lookup."""
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass

    def __getitem__(self, index: int) -> T:
        # YOUR CODE HERE
        pass

    def to_list(self) -> list[T]:
        # YOUR CODE HERE
        pass


class Result(Generic[T]):
    """A Result type that holds either a value (Ok) or an error message (Err).
    Similar to Rust's Result type.
    """

    def __init__(self, value: T | None = None, error: str | None = None):
        # YOUR CODE HERE
        pass

    @classmethod
    def ok(cls, value: T) -> "Result[T]":
        # YOUR CODE HERE
        pass

    @classmethod
    def err(cls, error: str) -> "Result[T]":
        # YOUR CODE HERE
        pass

    def is_ok(self) -> bool:
        # YOUR CODE HERE
        pass

    def unwrap(self) -> T:
        """Return value if Ok, raise ValueError if Err."""
        # YOUR CODE HERE
        pass

    def unwrap_or(self, default: T) -> T:
        """Return value if Ok, default if Err."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    sl = SortedList()
    sl.insert(5)
    sl.insert(1)
    sl.insert(3)
    sl.insert(2)
    sl.insert(4)
    assert sl.to_list() == [1, 2, 3, 4, 5]
    assert 3 in sl
    assert 6 not in sl
    assert len(sl) == 5
    assert sl[0] == 1
    sl.remove(3)
    assert sl.to_list() == [1, 2, 4, 5]

    r1 = Result.ok(42)
    assert r1.is_ok() is True
    assert r1.unwrap() == 42

    r2 = Result.err("something went wrong")
    assert r2.is_ok() is False
    assert r2.unwrap_or(0) == 0
    try:
        r2.unwrap()
        assert False
    except ValueError:
        pass
    print("✅ All tests passed!")

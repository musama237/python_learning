"""
Challenge: Iterator Protocol
Difficulty: ⭐⭐ Medium
Topic: __iter__, __next__, Custom Iterables

1. Create a Range class that mimics Python's range() — make it iterable.
2. Create a Cycle class that endlessly cycles through elements.

Example:
    for i in Range(1, 5):
        print(i)  # 1, 2, 3, 4

    c = Cycle([1, 2, 3])
    [next(c) for _ in range(7)] -> [1, 2, 3, 1, 2, 3, 1]
"""


class Range:
    """Mimics range(start, stop, step). Must be iterable."""

    def __init__(self, start: int, stop: int = None, step: int = 1):
        # Handle Range(5) -> Range(0, 5)
        # YOUR CODE HERE
        pass

    def __iter__(self):
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass


class Cycle:
    """Endlessly cycles through elements of an iterable."""

    def __init__(self, iterable):
        # YOUR CODE HERE
        pass

    def __iter__(self):
        return self

    def __next__(self):
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert list(Range(5)) == [0, 1, 2, 3, 4]
    assert list(Range(1, 5)) == [1, 2, 3, 4]
    assert list(Range(0, 10, 2)) == [0, 2, 4, 6, 8]
    assert list(Range(5, 0, -1)) == [5, 4, 3, 2, 1]
    assert len(Range(10)) == 10
    assert len(Range(0, 10, 3)) == 4

    c = Cycle([1, 2, 3])
    result = [next(c) for _ in range(7)]
    assert result == [1, 2, 3, 1, 2, 3, 1]

    c2 = Cycle("ab")
    result2 = [next(c2) for _ in range(5)]
    assert result2 == ["a", "b", "a", "b", "a"]
    print("✅ All tests passed!")

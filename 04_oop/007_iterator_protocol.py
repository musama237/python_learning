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

Hints:
    1. __iter__ returns self or a new iterator
    2. __next__ returns next value or raises StopIteration
    3. Range: track current position

Learn:
    # Iterator protocol: __iter__ + __next__
    class Counter:
        def __init__(self, n):
            self.n = n
            self.current = 0
        def __iter__(self):
            return self  # iterator returns itself
        def __next__(self):
            if self.current >= self.n:
                raise StopIteration
            val = self.current
            self.current += 1
            return val

    list(Counter(3))  # -> [0, 1, 2]

    # Cycle: use modulo index
    self.index = (self.index + 1) % len(self.items)
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

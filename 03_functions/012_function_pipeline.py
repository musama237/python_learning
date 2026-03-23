"""
Challenge: Function Pipeline
Difficulty: ⭐⭐⭐ Hard
Topic: Functional Programming, Composition

Build a Pipeline class that chains transformations on data.
Should support adding functions, running the pipeline, and branching.

Example:
    result = (Pipeline([1, 2, 3, 4, 5])
              .filter(lambda x: x > 2)
              .map(lambda x: x * 10)
              .reduce(lambda a, b: a + b))
    # result == 120

Hints:
    1. Store the data inside the object and have each method transform it, returning self for chaining.
    2. Each method (map, filter, sort, take) should update self.data and return self. reduce iterates through self.data to produce a single value.
    3. In __init__, store data as a list. map: self.data = [func(x) for x in self.data]; return self. filter: self.data = [x for x in self.data if func(x)]; return self. reduce: iterate with an accumulator, using initial or self.data[0] as the starting value.
"""


class Pipeline:
    def __init__(self, data):
        # YOUR CODE HERE
        pass

    def map(self, func) -> "Pipeline":
        """Apply func to each element."""
        # YOUR CODE HERE
        pass

    def filter(self, func) -> "Pipeline":
        """Keep elements where func returns True."""
        # YOUR CODE HERE
        pass

    def reduce(self, func, initial=None):
        """Reduce to a single value."""
        # YOUR CODE HERE
        pass

    def sort(self, key=None, reverse=False) -> "Pipeline":
        """Sort the data."""
        # YOUR CODE HERE
        pass

    def take(self, n: int) -> "Pipeline":
        """Keep only first n elements."""
        # YOUR CODE HERE
        pass

    def collect(self) -> list:
        """Return the data as a list."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    result = (Pipeline([1, 2, 3, 4, 5])
              .filter(lambda x: x > 2)
              .map(lambda x: x * 10)
              .reduce(lambda a, b: a + b))
    assert result == 120

    result2 = (Pipeline([5, 1, 3, 2, 4])
               .sort()
               .take(3)
               .collect())
    assert result2 == [1, 2, 3]

    result3 = (Pipeline(["hello", "world", "hi"])
               .filter(lambda s: len(s) > 2)
               .map(str.upper)
               .collect())
    assert result3 == ["HELLO", "WORLD"]

    assert Pipeline([]).collect() == []
    print("✅ All tests passed!")

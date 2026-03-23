"""
Challenge: collections Module
Difficulty: ⭐⭐ Medium
Topic: Counter, defaultdict, deque, namedtuple, OrderedDict

Use the collections module to solve each problem efficiently.

Hints:
    1. Counter.most_common(k) gives the top-k elements by frequency
    2. defaultdict(list) auto-creates empty lists on first access — great for grouping
    3. Use a deque to maintain a sliding window with O(1) append and popleft
    4. namedtuple creates a lightweight Point class with named x, y fields
"""

from collections import Counter, defaultdict, deque, namedtuple


def top_k_frequent(words: list[str], k: int) -> list[str]:
    """Return the k most frequent words, sorted by frequency (desc),
    then alphabetically for ties.
    """
    # YOUR CODE HERE
    pass


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by their length using defaultdict.
    Values should be sorted alphabetically.
    """
    # YOUR CODE HERE
    pass


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Return max of each sliding window of size k using deque."""
    # YOUR CODE HERE
    pass


def create_point_system():
    """Create a Point namedtuple with x, y fields.
    Add a class method 'from_string' that parses "x,y" format.
    Return the Point class.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert top_k_frequent(["the", "day", "is", "sunny", "the", "the", "sunny"], 2) == ["the", "sunny"]
    assert top_k_frequent(["a", "b", "c"], 1) == ["a"]

    grouped = group_by_length(["hi", "hello", "hey", "go", "python"])
    assert grouped[2] == ["go", "hi"]
    assert grouped[5] == ["hello"]

    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    Point = create_point_system()
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2
    p2 = Point.from_string("3,4")
    assert p2.x == 3 and p2.y == 4
    print("✅ All tests passed!")

"""
Challenge: Lambda, Map, Filter, Reduce
Difficulty: ⭐⭐ Medium
Topic: Functional Programming

Solve each using lambda with map/filter/reduce (one line each).

Hints:
    1. Remember that map and filter return iterators in Python 3, not lists.
    2. Wrap map() and filter() calls in list(); filter keeps items where the lambda returns True; reduce needs an initial value to handle empty lists.
    3. For double_all: list(map(lambda x: x*2, nums)); for product_of_all: reduce(lambda a,b: a*b, nums, 1) -- the third arg to reduce is the initial value for empty lists.

Learn:
    # Lambda: anonymous one-line function:
    double = lambda x: x * 2
    double(5)  # -> 10

    # map applies function to each element:
    list(map(lambda x: x * 2, [1, 2, 3]))  # -> [2, 4, 6]

    # filter keeps items where function returns True:
    list(filter(lambda x: x > 0, [-1, 2, -3, 4]))  # -> [2, 4]

    # reduce combines all elements:
    from functools import reduce
    reduce(lambda a, b: a + b, [1, 2, 3], 0)  # -> 6
    # 0 is the initial value (important for empty lists!)

    # sorted with key:
    sorted(["hello", "hi"], key=lambda s: s[-1])
"""

from functools import reduce


def double_all(nums: list[int]) -> list[int]:
    """Double every number in the list using map + lambda."""
    # YOUR CODE HERE (one line)
    pass


def filter_positives(nums: list[int]) -> list[int]:
    """Keep only positive numbers using filter + lambda."""
    # YOUR CODE HERE (one line)
    pass


def product_of_all(nums: list[int]) -> int:
    """Multiply all numbers together using reduce + lambda. Return 1 for empty list."""
    # YOUR CODE HERE
    pass


def sort_by_last_char(words: list[str]) -> list[str]:
    """Sort strings by their last character using sorted + lambda."""
    # YOUR CODE HERE (one line)
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert double_all([1, 2, 3]) == [2, 4, 6]
    assert double_all([]) == []
    assert filter_positives([-1, 2, -3, 4, 0]) == [2, 4]
    assert product_of_all([1, 2, 3, 4]) == 24
    assert product_of_all([]) == 1
    assert sort_by_last_char(["hello", "hi", "hey"]) == ["hi", "hello", "hey"]
    print("✅ All tests passed!")

"""
Challenge: Higher-Order Functions
Difficulty: ⭐⭐ Medium
Topic: Functions as Arguments, Composition

Write your own versions of map, filter, and reduce.
Then write a compose function that chains functions together.

Example:
    my_map(lambda x: x*2, [1,2,3]) -> [2, 4, 6]
    compose(str, lambda x: x+1)(5) -> "6"

Hints:
    1. Higher-order functions take or return functions -- my_map just needs a loop applying func to each item.
    2. For my_map: loop and append func(item). For compose: apply functions right-to-left on the input value.
    3. my_map: return [func(x) for x in iterable]. compose: return a lambda that uses reduce or a loop to chain funcs from right to left, e.g., for f in reversed(funcs): val = f(val).

Learn:
    # Functions are values -- pass them around:
    def apply(func, value):
        return func(value)
    apply(str, 42)  # -> "42"

    # Building your own map:
    def my_map(func, items):
        return [func(x) for x in items]

    # Composing functions (right to left):
    def compose(f, g):
        return lambda x: f(g(x))
    add1_str = compose(str, lambda x: x + 1)
    add1_str(5)  # -> "6"
"""


def my_map(func, iterable) -> list:
    """Apply func to each element. Do NOT use built-in map."""
    # YOUR CODE HERE
    pass


def my_filter(func, iterable) -> list:
    """Keep elements where func returns True. Do NOT use built-in filter."""
    # YOUR CODE HERE
    pass


def my_reduce(func, iterable, initial=None):
    """Reduce iterable using func. Do NOT use functools.reduce."""
    # YOUR CODE HERE
    pass


def compose(*funcs):
    """Return a function that applies funcs right-to-left.
    compose(f, g, h)(x) == f(g(h(x)))
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert my_map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert my_map(str, [1, 2]) == ["1", "2"]
    assert my_filter(lambda x: x > 0, [-1, 2, -3, 4]) == [2, 4]
    assert my_reduce(lambda a, b: a + b, [1, 2, 3, 4]) == 10
    assert my_reduce(lambda a, b: a + b, [1, 2, 3], 10) == 16

    add_one_then_str = compose(str, lambda x: x + 1)
    assert add_one_then_str(5) == "6"

    double_add_str = compose(str, lambda x: x + 1, lambda x: x * 2)
    assert double_add_str(3) == "7"  # 3*2=6, 6+1=7, str(7)="7"
    print("✅ All tests passed!")

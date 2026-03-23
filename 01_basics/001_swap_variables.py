"""
Challenge: Swap Two Variables
Difficulty: ⭐ Easy
Topic: Variables, Assignment

Swap the values of two variables WITHOUT using a temporary variable.

Example:
    a = 5, b = 10 -> a = 10, b = 5

Hints:
    1. Think about how Python handles multiple values on both sides of an assignment.
    2. Python can pack and unpack tuples in a single line — no temporary variable needed.
    3. Use simultaneous assignment: a, b = b, a — Python evaluates the right side fully before assigning.

Learn:
    # Tuple unpacking allows swapping without temp variable:
    x, y = y, x

    # Functions can return multiple values as a tuple:
    def example():
        return 10, 20
    a, b = example()  # a=10, b=20
"""


def swap(a, b):
    # YOUR CODE HERE
    pass



if __name__ == "__main__":
    assert swap(5, 10) == (10, 5)
    assert swap("hello", "world") == ("world", "hello")
    assert swap(0, 0) == (0, 0)
    assert swap(-1, 1) == (1, -1)
    print("✅ All tests passed!")

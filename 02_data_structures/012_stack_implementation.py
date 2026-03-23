"""
Challenge: Implement a Stack
Difficulty: ⭐⭐ Medium
Topic: Data Structures, Classes

Implement a Stack class with push, pop, peek, is_empty, and size.
Raise IndexError when popping/peeking an empty stack.

Example:
    s = Stack()
    s.push(1)
    s.push(2)
    s.peek()  -> 2
    s.pop()   -> 2
    s.size()  -> 1

Hints:
    1. Think about which built-in Python data structure naturally supports LIFO behavior.
    2. A list works perfectly — append() adds to top, pop() removes from top, [-1] peeks.
    3. Store items in a list internally; use len() for size, check length for is_empty, and raise IndexError when operating on an empty stack.
"""


class Stack:
    def __init__(self):
        # YOUR CODE HERE
        pass

    def push(self, item):
        # YOUR CODE HERE
        pass

    def pop(self):
        # YOUR CODE HERE
        pass

    def peek(self):
        # YOUR CODE HERE
        pass

    def is_empty(self) -> bool:
        # YOUR CODE HERE
        pass

    def size(self) -> int:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    s = Stack()
    assert s.is_empty() is True
    assert s.size() == 0
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.size() == 1
    assert s.is_empty() is False
    s.pop()
    assert s.is_empty() is True
    try:
        s.pop()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass
    print("✅ All tests passed!")

"""
Challenge: Mixin Classes and Multiple Inheritance
Difficulty: ⭐⭐⭐ Hard
Topic: Multiple Inheritance, Mixins, MRO

Create mixin classes that add functionality:
1. JsonMixin - adds to_json() and from_json() methods
2. ComparableMixin - adds comparison operators from a key() method
3. ValidatableMixin - adds validate() that checks type hints

Example:
    class User(JsonMixin, ComparableMixin):
        ...

Hints:
    1. to_json: json.dumps(self.__dict__)
    2. from_json: create instance and set attributes
    3. ComparableMixin uses self.key() for comparisons

Learn:
    # Mixin: a class that adds behavior:
    import json
    class JsonMixin:
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, s):
            obj = cls.__new__(cls)       # create without __init__
            obj.__dict__ = json.loads(s)  # restore attributes
            return obj

    # Comparison mixin:
    def __lt__(self, other):
        return self.key() < other.key()
"""

import json


class JsonMixin:
    """Adds to_json() and from_json() based on __dict__."""

    def to_json(self) -> str:
        # YOUR CODE HERE
        pass

    @classmethod
    def from_json(cls, json_str: str):
        # YOUR CODE HERE
        pass


class ComparableMixin:
    """Adds <, <=, >, >= based on a key() method that subclasses define."""

    def key(self):
        raise NotImplementedError

    def __lt__(self, other):
        # YOUR CODE HERE
        pass

    def __le__(self, other):
        # YOUR CODE HERE
        pass

    def __gt__(self, other):
        # YOUR CODE HERE
        pass

    def __ge__(self, other):
        # YOUR CODE HERE
        pass

    def __eq__(self, other):
        # YOUR CODE HERE
        pass


class Employee(JsonMixin, ComparableMixin):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def key(self):
        return self.salary


# --- Tests (do not modify) ---
if __name__ == "__main__":
    e1 = Employee("Alice", 90000)
    e2 = Employee("Bob", 80000)

    # JSON
    json_str = e1.to_json()
    data = json.loads(json_str)
    assert data["name"] == "Alice"
    assert data["salary"] == 90000

    e3 = Employee.from_json(json_str)
    assert e3.name == "Alice"
    assert e3.salary == 90000

    # Comparison
    assert e2 < e1
    assert e1 > e2
    assert e1 >= e1
    assert e2 <= e1
    assert Employee("X", 50000) == Employee("Y", 50000)
    print("✅ All tests passed!")

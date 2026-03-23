"""
Challenge: Descriptor Protocol
Difficulty: ⭐⭐⭐ Hard
Topic: Descriptors, __get__, __set__, Validation

Create descriptors for automatic validation:
1. TypeChecked - ensures a field is of a specific type
2. RangeChecked - ensures a numeric field is within bounds
3. Use them to build a validated model

Example:
    class Product:
        name = TypeChecked(str)
        price = RangeChecked(0, 10000)
"""


class TypeChecked:
    """Descriptor that enforces type on assignment."""

    def __init__(self, expected_type):
        # YOUR CODE HERE
        pass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        # YOUR CODE HERE - raise TypeError if wrong type
        pass


class RangeChecked:
    """Descriptor that enforces numeric range on assignment."""

    def __init__(self, min_val: float, max_val: float):
        # YOUR CODE HERE
        pass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        # YOUR CODE HERE - raise ValueError if out of range
        pass


class Product:
    name = TypeChecked(str)
    price = RangeChecked(0, 10000)
    quantity = RangeChecked(0, 1000000)

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


# --- Tests (do not modify) ---
if __name__ == "__main__":
    p = Product("Widget", 9.99, 100)
    assert p.name == "Widget"
    assert p.price == 9.99
    assert p.quantity == 100

    try:
        p.name = 123  # Not a string
        assert False
    except TypeError:
        pass

    try:
        p.price = -1  # Below 0
        assert False
    except ValueError:
        pass

    try:
        p.price = 20000  # Above 10000
        assert False
    except ValueError:
        pass

    p.price = 19.99
    assert p.price == 19.99
    print("✅ All tests passed!")

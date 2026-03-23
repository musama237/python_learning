"""
Challenge: Metaclass Basics
Difficulty: 💀 Extreme
Topic: Metaclasses, Class Creation, __init_subclass__

1. Create a metaclass that automatically adds a 'registry' of all subclasses.
2. Create a metaclass that enforces all methods have docstrings.

Example:
    class Animal(metaclass=RegistryMeta):
        pass
    class Dog(Animal): pass
    class Cat(Animal): pass
    Animal.registry -> {'Dog': Dog, 'Cat': Cat}

Hints:
    1. __new__ in metaclass runs at class creation
    2. Add registry dict to base class
    3. Check methods for __doc__ attribute

Learn:
    # Metaclass: a class that creates classes:
    class Meta(type):
        def __new__(mcs, name, bases, namespace):
            cls = super().__new__(mcs, name, bases, namespace)
            # modify cls here
            return cls

    # Registry pattern:
    if not hasattr(cls, 'registry'):
        cls.registry = {}      # base class gets registry
    else:
        for base in bases:
            if hasattr(base, 'registry'):
                base.registry[name] = cls

    # Check if callable has docstring:
    for key, val in namespace.items():
        if callable(val) and not key.startswith('_'):
            if not val.__doc__:
                raise TypeError(f"{key} needs a docstring")
"""


class RegistryMeta(type):
    """Metaclass that maintains a registry of all subclasses."""

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # YOUR CODE HERE - add registry dict and track subclasses
        pass
        return cls


class DocstringMeta(type):
    """Metaclass that requires all public methods have docstrings.
    Raises TypeError at class creation if a public method lacks a docstring.
    """

    def __new__(mcs, name, bases, namespace):
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    class Animal(metaclass=RegistryMeta):
        pass

    class Dog(Animal):
        pass

    class Cat(Animal):
        pass

    class GoldenRetriever(Dog):
        pass

    assert "Dog" in Animal.registry
    assert "Cat" in Animal.registry
    assert "GoldenRetriever" in Dog.registry

    # DocstringMeta test
    try:
        class BadClass(metaclass=DocstringMeta):
            def my_method(self):
                pass  # No docstring!
        assert False, "Should have raised TypeError"
    except TypeError:
        pass

    class GoodClass(metaclass=DocstringMeta):
        def my_method(self):
            """This has a docstring."""
            pass

        def _private(self):
            pass  # Private methods don't need docstrings

    print("✅ All tests passed!")

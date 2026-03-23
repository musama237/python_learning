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

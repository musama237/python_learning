"""
Challenge: Design Pattern - Singleton & Factory
Difficulty: ⭐⭐⭐ Hard
Topic: Design Patterns, Metaclasses

1. Implement a Singleton class (only one instance can exist).
2. Implement a Factory pattern for creating different types of objects.

Example:
    a = Singleton()
    b = Singleton()
    a is b -> True

Hints:
    1. Override __new__
    2. Check if instance exists (cls._instance)
    3. Factory uses dict mapping type string to class
"""


class Singleton:
    """Only one instance of this class can exist.
    Subsequent calls to Singleton() return the same instance.
    """
    # YOUR CODE HERE
    pass


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


class Fish(Animal):
    def speak(self) -> str:
        return f"{self.name} says ..."


class AnimalFactory:
    """Factory that creates animals by type string.
    Supports registering new animal types dynamically.
    """

    def __init__(self):
        # YOUR CODE HERE
        pass

    def register(self, animal_type: str, cls):
        """Register a new animal type."""
        # YOUR CODE HERE
        pass

    def create(self, animal_type: str, name: str) -> Animal:
        """Create an animal. Raise ValueError for unknown types."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    assert a is b

    factory = AnimalFactory()
    factory.register("dog", Dog)
    factory.register("cat", Cat)
    factory.register("fish", Fish)

    dog = factory.create("dog", "Rex")
    cat = factory.create("cat", "Whiskers")
    assert dog.speak() == "Rex says Woof!"
    assert cat.speak() == "Whiskers says Meow!"
    assert isinstance(dog, Dog)

    try:
        factory.create("bird", "Tweety")
        assert False
    except ValueError:
        pass
    print("✅ All tests passed!")

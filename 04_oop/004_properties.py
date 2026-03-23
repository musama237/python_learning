"""
Challenge: Properties and Descriptors
Difficulty: ⭐⭐ Medium
Topic: Properties, Getters/Setters, Validation

Create a Temperature class that stores temperature in Celsius internally
but can get/set in both Celsius and Fahrenheit using properties.

Also create a Person class with validated name and age properties.

Example:
    t = Temperature(100)
    t.fahrenheit -> 212.0
    t.fahrenheit = 32
    t.celsius -> 0.0

Hints:
    1. Use @property for getter, @name.setter for setter
    2. Store internal value as _celsius
    3. Convert in fahrenheit property
"""


class Temperature:
    def __init__(self, celsius: float = 0):
        # YOUR CODE HERE
        pass

    @property
    def celsius(self) -> float:
        # YOUR CODE HERE
        pass

    @celsius.setter
    def celsius(self, value: float):
        # YOUR CODE HERE (raise ValueError if below absolute zero: -273.15)
        pass

    @property
    def fahrenheit(self) -> float:
        # YOUR CODE HERE
        pass

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        # YOUR CODE HERE
        pass


class Person:
    def __init__(self, name: str, age: int):
        self.name = name  # Should use the property setter
        self.age = age

    @property
    def name(self) -> str:
        # YOUR CODE HERE
        pass

    @name.setter
    def name(self, value: str):
        """Must be a non-empty string. Raise ValueError otherwise."""
        # YOUR CODE HERE
        pass

    @property
    def age(self) -> int:
        # YOUR CODE HERE
        pass

    @age.setter
    def age(self, value: int):
        """Must be int between 0 and 150. Raise ValueError otherwise."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    t = Temperature(100)
    assert t.celsius == 100
    assert t.fahrenheit == 212.0
    t.fahrenheit = 32
    assert t.celsius == 0.0
    t.celsius = -40
    assert t.fahrenheit == -40.0
    try:
        t.celsius = -300
        assert False
    except ValueError:
        pass

    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30
    p.name = "Bob"
    assert p.name == "Bob"
    try:
        p.name = ""
        assert False
    except ValueError:
        pass
    try:
        p.age = -1
        assert False
    except ValueError:
        pass
    print("✅ All tests passed!")

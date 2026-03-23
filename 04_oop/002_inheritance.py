"""
Challenge: Inheritance - Shape Hierarchy
Difficulty: ⭐⭐ Medium
Topic: Inheritance, Abstract Methods, Polymorphism

Create a shape hierarchy:
- Shape (base): abstract area() and perimeter()
- Rectangle(width, height)
- Square(side) - inherits from Rectangle
- Circle(radius)

Use math.pi for circle calculations.

Hints:
    1. Square.__init__ calls super().__init__(side, side)
    2. Circle uses math.pi
    3. ABC forces subclasses to implement methods
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        # YOUR CODE HERE
        pass


class Square(Rectangle):
    def __init__(self, side: float):
        # YOUR CODE HERE
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14

    s = Square(5)
    assert s.area() == 25
    assert s.perimeter() == 20
    assert isinstance(s, Rectangle)

    c = Circle(10)
    assert abs(c.area() - math.pi * 100) < 0.001
    assert abs(c.perimeter() - 2 * math.pi * 10) < 0.001

    # Polymorphism
    shapes = [Rectangle(2, 3), Square(4), Circle(1)]
    areas = [s.area() for s in shapes]
    assert areas[0] == 6
    assert areas[1] == 16
    assert abs(areas[2] - math.pi) < 0.001
    print("✅ All tests passed!")

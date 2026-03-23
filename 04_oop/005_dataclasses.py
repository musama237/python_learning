"""
Challenge: Dataclasses
Difficulty: ⭐⭐ Medium
Topic: Dataclasses, Type Hints, Comparison

Use @dataclass to create clean data models.

1. Point3D with x, y, z coordinates and a distance_to method.
2. Student with name, grades list, and computed GPA property.
3. Inventory Item with auto-computed total_cost.
"""

from dataclasses import dataclass, field
import math


@dataclass
class Point3D:
    # YOUR CODE HERE
    pass

    def distance_to(self, other: "Point3D") -> float:
        """Euclidean distance to another point."""
        # YOUR CODE HERE
        pass


@dataclass
class Student:
    name: str
    grades: list[float] = field(default_factory=list)

    @property
    def gpa(self) -> float:
        """Average of grades. Return 0.0 if no grades."""
        # YOUR CODE HERE
        pass

    def add_grade(self, grade: float) -> None:
        """Add a grade (0.0 - 4.0). Raise ValueError if out of range."""
        # YOUR CODE HERE
        pass


@dataclass(order=True)
class InventoryItem:
    """Sortable by total_cost. Implement sort_index for ordering."""
    name: str = field(compare=False)
    unit_price: float = field(compare=False)
    quantity: int = field(compare=False, default=0)
    sort_index: float = field(init=False, repr=False)

    def __post_init__(self):
        # YOUR CODE HERE - set sort_index to total_cost
        pass

    @property
    def total_cost(self) -> float:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(1, 2, 2)
    assert abs(p1.distance_to(p2) - 3.0) < 0.001
    assert p1 != p2

    s = Student("Alice")
    assert s.gpa == 0.0
    s.add_grade(3.5)
    s.add_grade(4.0)
    assert s.gpa == 3.75
    try:
        s.add_grade(5.0)
        assert False
    except ValueError:
        pass

    item1 = InventoryItem("Widget", 10.0, 5)
    item2 = InventoryItem("Gadget", 25.0, 3)
    assert item1.total_cost == 50.0
    assert item2.total_cost == 75.0
    assert item1 < item2  # sorted by total_cost
    print("✅ All tests passed!")

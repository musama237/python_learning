"""
Challenge: Magic Methods - Vector Class
Difficulty: ⭐⭐ Medium
Topic: Dunder Methods, Operator Overloading

Create a Vector class that supports:
- Addition (+), Subtraction (-), Scalar multiplication (*)
- Equality (==), String representation
- Dot product method
- len() returns dimension

Example:
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v1 + v2 -> Vector(5, 7, 9)
    v1 * 2 -> Vector(2, 4, 6)

Hints:
    1. Store components as tuple
    2. __add__ creates new Vector with zipped sums
    3. magnitude = sqrt(sum of squares)

Learn:
    # Operator overloading:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # zip pairs up elements:
    list(zip([1, 2], [3, 4]))  # -> [(1, 3), (2, 4)]

    # __rmul__ handles: 3 * vector (when 3 doesn't know how):
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # __repr__ for developer-friendly string:
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    # Magnitude: sqrt(x^2 + y^2 + z^2)
    import math
    math.sqrt(sum(c**2 for c in self.components))
"""


class Vector:
    def __init__(self, *components):
        # YOUR CODE HERE
        pass

    def __add__(self, other):
        # YOUR CODE HERE
        pass

    def __sub__(self, other):
        # YOUR CODE HERE
        pass

    def __mul__(self, scalar):
        # YOUR CODE HERE
        pass

    def __rmul__(self, scalar):
        # YOUR CODE HERE
        pass

    def __eq__(self, other):
        # YOUR CODE HERE
        pass

    def __len__(self):
        # YOUR CODE HERE
        pass

    def __repr__(self):
        """Return 'Vector(1, 2, 3)'"""
        # YOUR CODE HERE
        pass

    def dot(self, other) -> float:
        """Dot product of two vectors."""
        # YOUR CODE HERE
        pass

    def magnitude(self) -> float:
        """Return the magnitude (length) of the vector."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    assert v1 + v2 == Vector(5, 7, 9)
    assert v2 - v1 == Vector(3, 3, 3)
    assert v1 * 2 == Vector(2, 4, 6)
    assert 3 * v1 == Vector(3, 6, 9)
    assert len(v1) == 3
    assert repr(v1) == "Vector(1, 2, 3)"
    assert v1.dot(v2) == 32
    assert abs(Vector(3, 4).magnitude() - 5.0) < 0.001
    assert v1 != v2
    print("✅ All tests passed!")

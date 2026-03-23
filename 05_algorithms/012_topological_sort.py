"""
Challenge: Topological Sort
Difficulty: ⭐⭐⭐ Hard
Topic: Graphs, DAG, Ordering

Given a directed acyclic graph (DAG), return a valid topological ordering.
Detect cycles (return empty list if cycle exists).

Example:
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    topological_sort(graph) -> [0, 1, 2, 3] or [0, 2, 1, 3]
"""


def topological_sort(graph: dict[int, list[int]]) -> list[int]:
    """Return a topological ordering. Empty list if cycle detected."""
    # YOUR CODE HERE
    pass


def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Given n courses and prerequisite pairs [course, prereq],
    return True if all courses can be finished (no circular dependency).

    Example: can_finish_courses(2, [[1, 0]]) -> True (take 0 then 1)
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = topological_sort(graph)
    assert len(result) == 4
    assert result.index(0) < result.index(1)
    assert result.index(0) < result.index(2)
    assert result.index(1) < result.index(3)

    # Cycle detection
    cyclic = {0: [1], 1: [2], 2: [0]}
    assert topological_sort(cyclic) == []

    assert can_finish_courses(2, [[1, 0]]) is True
    assert can_finish_courses(2, [[1, 0], [0, 1]]) is False
    assert can_finish_courses(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    print("✅ All tests passed!")

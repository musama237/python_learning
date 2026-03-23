"""
Challenge: Graph Traversal - BFS & DFS
Difficulty: ⭐⭐⭐ Hard
Topic: Graphs, BFS, DFS, Adjacency List

Implement BFS and DFS on a graph represented as an adjacency list (dict).

Example:
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    bfs(graph, 'A') -> ['A', 'B', 'C', 'D']
    dfs(graph, 'A') -> ['A', 'B', 'D', 'C']

Hints:
    1. BFS uses a queue (deque), DFS uses a stack (or recursion)
    2. Always track a visited set to avoid revisiting nodes in graphs with cycles
    3. For shortest path, track the parent of each node during BFS and reconstruct the path backward

Learn:
    # BFS with deque:
    from collections import deque
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # DFS with stack (iterative):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
"""

from collections import deque


def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """Breadth-first traversal. Return visited nodes in order."""
    # YOUR CODE HERE
    pass


def dfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """Depth-first traversal (iterative). Return visited nodes in order."""
    # YOUR CODE HERE
    pass


def has_path(graph: dict[str, list[str]], start: str, end: str) -> bool:
    """Return True if there's a path from start to end."""
    # YOUR CODE HERE
    pass


def shortest_path(graph: dict[str, list[str]], start: str, end: str) -> list[str]:
    """Return shortest path from start to end. Empty list if no path."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D']
    assert dfs(graph, 'A') == ['A', 'B', 'D', 'C']
    assert has_path(graph, 'A', 'D') is True
    assert has_path(graph, 'D', 'A') is False
    assert shortest_path(graph, 'A', 'D') == ['A', 'B', 'D']
    assert shortest_path(graph, 'D', 'A') == []

    graph2 = {'A': ['B'], 'B': ['C'], 'C': ['A']}  # Cycle
    assert has_path(graph2, 'A', 'C') is True
    print("✅ All tests passed!")

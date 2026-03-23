"""
Challenge: Dijkstra's Shortest Path
Difficulty: 💀 Extreme
Topic: Graphs, Shortest Path, Priority Queue

Implement Dijkstra's algorithm for finding shortest paths in a weighted graph.

Graph format: dict of {node: [(neighbor, weight), ...]}

Example:
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dijkstra(graph, 'A') -> {'A': 0, 'B': 1, 'C': 3, 'D': 4}

Hints:
    1. Use a min-heap (heapq) seeded with (0, start); greedily visit the closest unvisited node
    2. For each visited node, update its neighbors if a shorter path is found through the current node
    3. Skip nodes already finalized (already popped with a shorter distance); track parents to reconstruct paths

Learn:
    # Min-heap for shortest distances:
    import heapq
    heap = [(0, start)]  # (distance, node)
    distances = {start: 0}

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances.get(node, float('inf')):
            continue  # already found shorter path
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
"""

import heapq


def dijkstra(graph: dict, start: str) -> dict[str, float]:
    """Return shortest distances from start to all reachable nodes."""
    # YOUR CODE HERE
    pass


def shortest_path_dijkstra(graph: dict, start: str, end: str) -> tuple[float, list[str]]:
    """Return (distance, path) for shortest path. (inf, []) if unreachable."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    distances = dijkstra(graph, 'A')
    assert distances == {'A': 0, 'B': 1, 'C': 3, 'D': 4}

    dist, path = shortest_path_dijkstra(graph, 'A', 'D')
    assert dist == 4
    assert path == ['A', 'B', 'C', 'D']

    dist2, path2 = shortest_path_dijkstra(graph, 'D', 'A')
    assert dist2 == float('inf')
    assert path2 == []
    print("✅ All tests passed!")

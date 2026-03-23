"""
Challenge: K-Means Clustering from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Clustering, Unsupervised Learning

Implement K-Means clustering algorithm.

Hints:
    1. Initialize centroids by randomly selecting k data points from the dataset
    2. Assign each point to its nearest centroid using argmin of distances
    3. Update each centroid as the mean of all points assigned to it; repeat until convergence

Learn:
    # Random initialization:
    indices = np.random.choice(n, self.k, replace=False)
    self.centroids = X[indices]

    # Assign clusters (distances):
    distances = np.sqrt(((X[:, None] - self.centroids[None]) ** 2).sum(axis=2))
    self.labels = distances.argmin(axis=1)

    # Update centroids:
    for i in range(self.k):
        self.centroids[i] = X[self.labels == i].mean(axis=0)
"""

import numpy as np


class KMeans:
    def __init__(self, k: int = 3, max_iterations: int = 100, random_seed: int = 42):
        self.k = k
        self.max_iterations = max_iterations
        self.random_seed = random_seed
        self.centroids = None
        self.labels = None

    def fit(self, X: np.ndarray) -> "KMeans":
        """Fit K-Means:
        1. Initialize centroids randomly from data points
        2. Assign each point to nearest centroid
        3. Update centroids as mean of assigned points
        4. Repeat until convergence or max_iterations
        """
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Assign cluster labels to new data points."""
        # YOUR CODE HERE
        pass

    def inertia(self, X: np.ndarray) -> float:
        """Compute sum of squared distances to nearest centroid."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)

    # Create 3 clear clusters
    c1 = np.random.randn(50, 2) + np.array([0, 0])
    c2 = np.random.randn(50, 2) + np.array([10, 0])
    c3 = np.random.randn(50, 2) + np.array([5, 10])
    X = np.vstack([c1, c2, c3])

    km = KMeans(k=3)
    km.fit(X)

    assert km.centroids.shape == (3, 2)
    assert km.labels.shape == (150,)
    assert len(set(km.labels)) == 3

    # Each cluster should have roughly 50 points
    counts = [np.sum(km.labels == i) for i in range(3)]
    assert all(30 < c < 70 for c in counts)

    # Inertia should be relatively low for well-separated clusters
    assert km.inertia(X) < 500
    print("✅ All tests passed!")

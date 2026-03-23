"""
Challenge: K-Nearest Neighbors from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Distance Metrics, Classification

Implement KNN for classification and regression.

Hints:
    1. Compute Euclidean distances from the query point to all training points
    2. Use argsort to find the k nearest neighbors by index
    3. For classification use majority vote (Counter.most_common); for regression take the mean of k neighbors
"""

import numpy as np
from collections import Counter


class KNN:
    def __init__(self, k: int = 3, task: str = "classification"):
        """task: 'classification' or 'regression'"""
        self.k = k
        self.task = task
        self.X_train = None
        self.y_train = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "KNN":
        """Store training data."""
        # YOUR CODE HERE
        pass

    def _euclidean_distance(self, x1: np.ndarray, x2: np.ndarray) -> float:
        # YOUR CODE HERE
        pass

    def _predict_single(self, x: np.ndarray):
        """Predict for a single sample."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict for multiple samples."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)

    # Classification test
    X_train = np.array([[1, 1], [1, 2], [2, 1], [5, 5], [5, 6], [6, 5]])
    y_train = np.array([0, 0, 0, 1, 1, 1])

    knn = KNN(k=3, task="classification")
    knn.fit(X_train, y_train)
    assert knn.predict(np.array([[1.5, 1.5]]))[0] == 0
    assert knn.predict(np.array([[5.5, 5.5]]))[0] == 1

    # Regression test
    X_reg = np.array([[1], [2], [3], [4], [5]])
    y_reg = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
    knn_reg = KNN(k=2, task="regression")
    knn_reg.fit(X_reg, y_reg)
    pred = knn_reg.predict(np.array([[2.5]]))[0]
    assert abs(pred - 5.0) < 1.0  # Average of neighbors
    print("✅ All tests passed!")

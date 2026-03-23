"""
Challenge: Decision Tree from Scratch
Difficulty: ⭐⭐⭐ Hard
Topic: ML, Trees, Information Gain, Entropy

Implement a decision tree classifier using information gain (entropy).

Hints:
    1. Entropy is -sum(p * log2(p)) where p is the proportion of each class
    2. Try all features and all unique thresholds; pick the split with highest information gain
    3. Recurse on left/right subsets until max_depth is reached or the node is pure
"""

import numpy as np
from collections import Counter


class DecisionTree:
    def __init__(self, max_depth: int = 10, min_samples_split: int = 2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def entropy(self, y: np.ndarray) -> float:
        """Compute entropy of label array."""
        # YOUR CODE HERE
        pass

    def information_gain(self, y: np.ndarray, left_y: np.ndarray, right_y: np.ndarray) -> float:
        """Compute information gain from a split."""
        # YOUR CODE HERE
        pass

    def best_split(self, X: np.ndarray, y: np.ndarray) -> tuple:
        """Find best feature and threshold to split on.
        Return (feature_index, threshold, info_gain).
        """
        # YOUR CODE HERE
        pass

    def fit(self, X: np.ndarray, y: np.ndarray) -> "DecisionTree":
        """Build the decision tree recursively."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class for each sample."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)

    # Simple XOR-like problem
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1],
                   [0, 0.1], [0.1, 1], [1, 0.1], [0.9, 1]])
    y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

    tree = DecisionTree(max_depth=5)
    tree.fit(X, y)
    preds = tree.predict(X)
    accuracy = (preds == y).mean()
    assert accuracy >= 0.75, f"Accuracy too low: {accuracy}"

    # Test entropy
    assert abs(tree.entropy(np.array([0, 0, 1, 1])) - 1.0) < 0.01
    assert abs(tree.entropy(np.array([0, 0, 0, 0])) - 0.0) < 0.01
    print(f"✅ All tests passed! Accuracy = {accuracy:.4f}")

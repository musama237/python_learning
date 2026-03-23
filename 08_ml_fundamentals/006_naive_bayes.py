"""
Challenge: Naive Bayes Classifier from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Probability, Bayes Theorem

Implement Gaussian Naive Bayes classifier.
"""

import numpy as np


class GaussianNaiveBayes:
    def __init__(self):
        self.classes = None
        self.priors = None  # P(class)
        self.means = None   # Mean of each feature per class
        self.vars = None    # Variance of each feature per class

    def fit(self, X: np.ndarray, y: np.ndarray) -> "GaussianNaiveBayes":
        """Learn class priors and feature statistics."""
        # YOUR CODE HERE
        pass

    def _gaussian_pdf(self, x: float, mean: float, var: float) -> float:
        """Compute Gaussian probability density."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class for each sample using Bayes theorem."""
        # YOUR CODE HERE
        pass

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return class probabilities for each sample. Shape: (n, n_classes)"""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)

    # Two well-separated Gaussian clusters
    X0 = np.random.randn(50, 2) + np.array([0, 0])
    X1 = np.random.randn(50, 2) + np.array([4, 4])
    X = np.vstack([X0, X1])
    y = np.array([0] * 50 + [1] * 50)

    nb = GaussianNaiveBayes()
    nb.fit(X, y)
    preds = nb.predict(X)
    accuracy = (preds == y).mean()
    assert accuracy > 0.90, f"Accuracy too low: {accuracy}"

    proba = nb.predict_proba(X)
    assert proba.shape == (100, 2)
    assert np.allclose(proba.sum(axis=1), 1.0, atol=0.01)
    print(f"✅ All tests passed! Accuracy = {accuracy:.4f}")

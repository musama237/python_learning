"""
Challenge: Naive Bayes Classifier from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Probability, Bayes Theorem

Implement Gaussian Naive Bayes classifier.

Hints:
    1. P(class|X) is proportional to P(class) * product(P(x_i|class)) for each feature
    2. Use the Gaussian PDF for continuous features: (1/sqrt(2*pi*var)) * exp(-(x-mean)^2 / (2*var))
    3. Predict by taking argmax over classes of the log-posterior (use log to avoid underflow)

Learn:
    # Gaussian PDF:
    def gaussian(x, mean, var):
        return (1 / np.sqrt(2 * np.pi * var)) * np.exp(-(x - mean)**2 / (2 * var))

    # Per-class statistics:
    for c in classes:
        mask = (y == c)
        self.means[c] = X[mask].mean(axis=0)
        self.vars[c] = X[mask].var(axis=0)
        self.priors[c] = mask.sum() / len(y)
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

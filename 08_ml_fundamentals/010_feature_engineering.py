"""
Challenge: Feature Engineering
Difficulty: ⭐⭐ Medium
Topic: ML, Preprocessing, Feature Scaling

Implement common feature engineering techniques from scratch.

Hints:
    1. StandardScaler: (X - mean) / std; store mean and std from fit for transform and inverse_transform
    2. MinMaxScaler: (X - min) / (max - min); store min and max from fit
    3. Polynomial features: use itertools.combinations_with_replacement on column indices for all degree combinations

Learn:
    # StandardScaler:
    self.mean = X.mean(axis=0)
    self.std = X.std(axis=0)
    X_scaled = (X - self.mean) / self.std

    # MinMaxScaler:
    self.min = X.min(axis=0)
    self.max = X.max(axis=0)
    X_scaled = (X - self.min) / (self.max - self.min)

    # Polynomial features:
    from itertools import combinations_with_replacement
    combos = combinations_with_replacement(range(n_features), degree)
"""

import numpy as np


class StandardScaler:
    """Standardize features to zero mean and unit variance."""

    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, X: np.ndarray) -> "StandardScaler":
        # YOUR CODE HERE
        pass

    def transform(self, X: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

    def inverse_transform(self, X: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass


class MinMaxScaler:
    """Scale features to [0, 1] range."""

    def __init__(self):
        self.min = None
        self.max = None

    def fit(self, X: np.ndarray) -> "MinMaxScaler":
        # YOUR CODE HERE
        pass

    def transform(self, X: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)


def polynomial_features(X: np.ndarray, degree: int = 2) -> np.ndarray:
    """Generate polynomial features up to given degree.
    For X with columns [a, b] and degree=2:
    Return [a, b, a^2, ab, b^2]
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    X = np.array([[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]], dtype=float)

    ss = StandardScaler()
    X_std = ss.fit_transform(X)
    assert np.allclose(X_std.mean(axis=0), 0, atol=1e-10)
    assert np.allclose(X_std.std(axis=0), 1, atol=1e-10)
    X_inv = ss.inverse_transform(X_std)
    assert np.allclose(X_inv, X)

    mms = MinMaxScaler()
    X_mm = mms.fit_transform(X)
    assert np.allclose(X_mm.min(axis=0), 0)
    assert np.allclose(X_mm.max(axis=0), 1)

    X_poly = polynomial_features(np.array([[2, 3]]), degree=2)
    # Should contain: 2, 3, 4, 6, 9
    assert 4 in X_poly[0]
    assert 6 in X_poly[0]
    assert 9 in X_poly[0]
    print("✅ All tests passed!")

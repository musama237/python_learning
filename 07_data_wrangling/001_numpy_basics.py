"""
Challenge: NumPy Basics
Difficulty: ⭐ Easy
Topic: NumPy, Arrays, Vectorization

Solve each using NumPy operations (no Python loops).

Hints:
    1. normalize: (arr - arr.min()) / (arr.max() - arr.min())
    2. moving_average: np.convolve with np.ones(window)/window
    3. softmax: subtract max for stability then exp/sum
    4. euclidean: use broadcasting with (X[:,None,:] - X[None,:,:])

Learn:
    import numpy as np
    # Vectorized operations (no loops):
    arr = np.array([1, 2, 3])
    arr * 2  # -> [2, 4, 6]
    arr.min(), arr.max(), arr.mean()

    # Softmax with stability trick:
    x = x - x.max()  # subtract max for numerical stability
    exp_x = np.exp(x)
    softmax = exp_x / exp_x.sum()

    # Broadcasting for pairwise distances:
    diff = X[:, None, :] - X[None, :, :]  # (n, n, d)
    dist = np.sqrt((diff**2).sum(axis=-1))  # (n, n)
"""

import numpy as np


def normalize(arr: np.ndarray) -> np.ndarray:
    """Normalize array to range [0, 1]. (x - min) / (max - min)
    Return zeros array if max == min.
    """
    # YOUR CODE HERE
    pass


def moving_average(arr: np.ndarray, window: int) -> np.ndarray:
    """Compute moving average with given window size.
    Use np.convolve. Output length = len(arr) - window + 1.
    """
    # YOUR CODE HERE
    pass


def outer_product(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Compute outer product of two 1D arrays without np.outer."""
    # YOUR CODE HERE (hint: broadcasting)
    pass


def euclidean_distances(X: np.ndarray) -> np.ndarray:
    """Compute pairwise Euclidean distance matrix for rows of X.
    X has shape (n, d). Return (n, n) matrix.
    Use vectorized operations (no loops).
    """
    # YOUR CODE HERE
    pass


def softmax(x: np.ndarray) -> np.ndarray:
    """Compute softmax along last axis. Handle numerical stability.
    softmax(x_i) = exp(x_i) / sum(exp(x_j))
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert np.allclose(normalize(np.array([1, 2, 3, 4, 5])), [0, 0.25, 0.5, 0.75, 1.0])
    assert np.allclose(normalize(np.array([5, 5, 5])), [0, 0, 0])

    ma = moving_average(np.array([1, 2, 3, 4, 5]), 3)
    assert np.allclose(ma, [2, 3, 4])

    op = outer_product(np.array([1, 2, 3]), np.array([4, 5]))
    assert op.shape == (3, 2)
    assert np.allclose(op, [[4, 5], [8, 10], [12, 15]])

    X = np.array([[0, 0], [3, 4], [1, 0]])
    D = euclidean_distances(X)
    assert D.shape == (3, 3)
    assert np.allclose(D[0, 1], 5.0)
    assert np.allclose(D[0, 0], 0.0)

    s = softmax(np.array([1.0, 2.0, 3.0]))
    assert np.allclose(s.sum(), 1.0)
    assert s[2] > s[1] > s[0]

    # Test numerical stability with large numbers
    s2 = softmax(np.array([1000.0, 1001.0, 1002.0]))
    assert np.allclose(s2.sum(), 1.0)
    print("✅ All tests passed!")

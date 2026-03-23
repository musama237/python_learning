"""
Challenge: Linear Algebra with NumPy
Difficulty: ⭐⭐⭐ Hard
Topic: NumPy, Linear Algebra, Matrix Operations

Implement linear algebra operations from scratch (no np.linalg where noted).
"""

import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Matrix multiplication WITHOUT using np.dot, np.matmul, or @.
    Use loops or broadcasting.
    """
    # YOUR CODE HERE
    pass


def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve Ax = b using np.linalg.solve."""
    # YOUR CODE HERE
    pass


def compute_eigenvalues(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (eigenvalues, eigenvectors) sorted by eigenvalue descending."""
    # YOUR CODE HERE
    pass


def pca_manual(X: np.ndarray, n_components: int) -> np.ndarray:
    """Perform PCA on X (n_samples, n_features).
    Return transformed data with n_components dimensions.
    Steps: center data, compute covariance, eigendecompose, project.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = matrix_multiply(A, B)
    expected = np.array([[19, 22], [43, 50]])
    assert np.allclose(result, expected)

    # Solve: 2x + y = 5, x + 3y = 7
    A2 = np.array([[2, 1], [1, 3]])
    b2 = np.array([5, 7])
    x = solve_linear_system(A2, b2)
    assert np.allclose(A2 @ x, b2)

    # Eigenvalues
    sym = np.array([[4, 2], [2, 3]])
    vals, vecs = compute_eigenvalues(sym)
    assert vals[0] > vals[1]  # Sorted descending

    # PCA
    np.random.seed(42)
    X = np.random.randn(100, 5)
    X_pca = pca_manual(X, 2)
    assert X_pca.shape == (100, 2)
    print("✅ All tests passed!")

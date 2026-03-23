"""
Challenge: NumPy Advanced
Difficulty: ⭐⭐ Medium
Topic: NumPy, Broadcasting, Linear Algebra

Advanced NumPy operations — all without Python loops.

Hints:
    1. batch_dot: (A * B).sum(axis=1)
    2. one_hot: create zeros array, use fancy indexing to set 1s
    3. convolution: nested loops sliding kernel over image

Learn:
    # Element-wise multiply and sum:
    (A * B).sum(axis=1)  # batch dot product

    # One-hot encoding:
    one_hot = np.zeros((n, num_classes))
    one_hot[np.arange(n), labels] = 1  # fancy indexing

    # Boolean mask with broadcasting:
    result = image * mask[:, :, None]  # (H,W) -> (H,W,1)
"""

import numpy as np


def batch_dot_product(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Compute dot product for each pair of rows.
    A shape: (n, d), B shape: (n, d) -> output shape: (n,)
    """
    # YOUR CODE HERE
    pass


def one_hot_encode(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """Convert integer labels to one-hot vectors.
    labels shape: (n,) -> output shape: (n, num_classes)
    """
    # YOUR CODE HERE
    pass


def apply_mask(image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Apply a boolean mask to an image.
    Set masked pixels (where mask is False) to 0.
    image shape: (H, W, C), mask shape: (H, W) -> output shape: (H, W, C)
    """
    # YOUR CODE HERE
    pass


def convolution_2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Apply 2D convolution (valid mode, no padding).
    image shape: (H, W), kernel shape: (kH, kW)
    output shape: (H-kH+1, W-kW+1)
    You CAN use loops for this one since it's about understanding convolution.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    assert np.allclose(batch_dot_product(A, B), [17, 53])

    ohe = one_hot_encode(np.array([0, 2, 1, 0]), 3)
    expected = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])
    assert np.allclose(ohe, expected)

    img = np.ones((3, 3, 3))
    mask = np.array([[True, False, True],
                     [False, True, False],
                     [True, False, True]])
    result = apply_mask(img, mask)
    assert result[0, 0, 0] == 1  # Masked in
    assert result[0, 1, 0] == 0  # Masked out

    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    kernel = np.array([[1, 0], [0, 1]], dtype=float)
    conv = convolution_2d(image, kernel)
    assert conv.shape == (2, 2)
    assert conv[0, 0] == 6  # 1*1 + 5*1
    print("✅ All tests passed!")

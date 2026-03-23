"""
Challenge: Cross-Validation & Model Evaluation
Difficulty: ⭐⭐ Medium
Topic: ML, Evaluation, Train/Test Split

Implement model evaluation tools from scratch.
"""

import numpy as np


def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2,
                     random_seed: int = 42) -> tuple:
    """Split data into train and test sets.
    Return (X_train, X_test, y_train, y_test).
    """
    # YOUR CODE HERE
    pass


def k_fold_indices(n_samples: int, k: int = 5, random_seed: int = 42) -> list[tuple]:
    """Generate k-fold cross-validation indices.
    Return list of (train_indices, test_indices) tuples.
    """
    # YOUR CODE HERE
    pass


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """Compute confusion matrix. Return 2x2 array:
    [[TN, FP], [FN, TP]]
    """
    # YOUR CODE HERE
    pass


def classification_report(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Compute precision, recall, f1-score, accuracy.
    Return dict with these keys.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(100, 3)
    y = np.random.randint(0, 2, 100)

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)
    assert X_tr.shape[0] == 80
    assert X_te.shape[0] == 20
    assert y_tr.shape[0] == 80

    folds = k_fold_indices(100, k=5)
    assert len(folds) == 5
    for train_idx, test_idx in folds:
        assert len(train_idx) == 80
        assert len(test_idx) == 20
        assert len(set(train_idx) & set(test_idx)) == 0

    y_true = np.array([1, 1, 0, 0, 1, 0, 1, 0])
    y_pred = np.array([1, 0, 0, 0, 1, 1, 1, 0])
    cm = confusion_matrix(y_true, y_pred)
    assert cm[1, 1] == 3  # TP
    assert cm[0, 0] == 3  # TN
    assert cm[1, 0] == 1  # FN
    assert cm[0, 1] == 1  # FP

    report = classification_report(y_true, y_pred)
    assert "precision" in report
    assert "recall" in report
    assert "f1" in report
    assert report["accuracy"] == 0.75
    print("✅ All tests passed!")

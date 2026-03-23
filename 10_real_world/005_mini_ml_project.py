"""
Challenge: Mini ML Project — End to End
Difficulty: 💀 Extreme
Topic: ML Pipeline, Feature Engineering, Model Selection

Build a complete ML pipeline from scratch that:
1. Generates synthetic data
2. Preprocesses features
3. Trains multiple models
4. Evaluates and selects the best one
5. Makes predictions

This is the capstone challenge — use everything you've learned!
"""

import numpy as np
from dataclasses import dataclass


@dataclass
class ExperimentResult:
    model_name: str
    accuracy: float
    precision: float
    recall: float
    f1: float


class MLPipeline:
    """End-to-end ML pipeline."""

    def __init__(self, random_seed: int = 42):
        self.seed = random_seed
        np.random.seed(random_seed)
        self.models = {}
        self.results = []
        self.best_model = None
        self.scaler_mean = None
        self.scaler_std = None

    def generate_data(self, n_samples: int = 1000, n_features: int = 10,
                      noise: float = 0.1) -> tuple[np.ndarray, np.ndarray]:
        """Generate synthetic binary classification data.
        Features should have different scales (some *100, some *0.01).
        Labels should depend on a non-trivial combination of features.
        Return (X, y).
        """
        # YOUR CODE HERE
        pass

    def preprocess(self, X_train: np.ndarray, X_test: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Standardize features using training set statistics.
        Store mean/std for future use.
        """
        # YOUR CODE HERE
        pass

    def train_test_split(self, X: np.ndarray, y: np.ndarray,
                         test_ratio: float = 0.2) -> tuple:
        """Split into train/test. Return (X_train, X_test, y_train, y_test)."""
        # YOUR CODE HERE
        pass

    def add_model(self, name: str, model) -> None:
        """Register a model (must have fit and predict methods)."""
        # YOUR CODE HERE
        pass

    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
        """Compute accuracy, precision, recall, f1."""
        # YOUR CODE HERE
        pass

    def run(self, n_samples: int = 1000) -> list[ExperimentResult]:
        """Run the full pipeline:
        1. Generate data
        2. Split
        3. Preprocess
        4. Train each model
        5. Evaluate each model
        6. Select best by F1 score
        Return sorted results (best first).
        """
        # YOUR CODE HERE
        pass


# Simple models to use in the pipeline
class SimpleLogistic:
    """Logistic regression with gradient descent."""
    def __init__(self, lr=0.1, epochs=200):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = None

    def fit(self, X, y):
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        for _ in range(self.epochs):
            z = X @ self.w + self.b
            pred = 1 / (1 + np.exp(-np.clip(z, -500, 500)))
            error = pred - y
            self.w -= self.lr * (X.T @ error) / n
            self.b -= self.lr * error.mean()

    def predict(self, X):
        z = X @ self.w + self.b
        return (1 / (1 + np.exp(-np.clip(z, -500, 500))) >= 0.5).astype(int)


class SimpleKNN:
    """K-Nearest Neighbors."""
    def __init__(self, k=5):
        self.k = k
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        preds = []
        for x in X:
            dists = np.sqrt(((self.X - x) ** 2).sum(axis=1))
            idx = dists.argsort()[:self.k]
            counts = np.bincount(self.y[idx].astype(int))
            preds.append(counts.argmax())
        return np.array(preds)


# --- Tests (do not modify) ---
if __name__ == "__main__":
    pipeline = MLPipeline(random_seed=42)

    # Add models
    pipeline.add_model("logistic", SimpleLogistic(lr=0.1, epochs=300))
    pipeline.add_model("knn_3", SimpleKNN(k=3))
    pipeline.add_model("knn_7", SimpleKNN(k=7))

    # Run pipeline
    results = pipeline.run(n_samples=500)

    assert len(results) == 3
    assert all(isinstance(r, ExperimentResult) for r in results)
    assert results[0].f1 >= results[-1].f1  # Sorted by F1

    # At least one model should do reasonably well
    best = results[0]
    assert best.accuracy > 0.6, f"Best accuracy too low: {best.accuracy}"
    assert best.f1 > 0.5, f"Best F1 too low: {best.f1}"

    print(f"\n{'Model':<15} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1':<10}")
    print("-" * 55)
    for r in results:
        print(f"{r.model_name:<15} {r.accuracy:<10.4f} {r.precision:<10.4f} {r.recall:<10.4f} {r.f1:<10.4f}")

    print(f"\n🏆 Best model: {results[0].model_name} (F1={results[0].f1:.4f})")
    print("✅ All tests passed!")

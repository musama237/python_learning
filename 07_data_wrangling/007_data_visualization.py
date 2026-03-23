"""
Challenge: Data Visualization Functions
Difficulty: ⭐⭐ Medium
Topic: Matplotlib, Data Viz, Statistics

Write functions that create publication-quality plots.
Each function should save the plot and return the figure.

Hints:
    1. plt.hist() for distribution plots
    2. plt.imshow() for heatmap visualization
    3. plt.plot() for training curves
    4. fig.savefig(path) to save; always plt.close(fig) when done
"""

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for testing
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import tempfile


def plot_distribution(data: np.ndarray, title: str, save_path: Path) -> plt.Figure:
    """Create a histogram with KDE overlay.
    Include: title, mean/median lines, legend, grid.
    """
    # YOUR CODE HERE
    pass


def plot_correlation_matrix(data: np.ndarray, labels: list[str], save_path: Path) -> plt.Figure:
    """Create a heatmap of the correlation matrix.
    Include: title, colorbar, annotations.
    """
    # YOUR CODE HERE
    pass


def plot_training_curves(
    train_losses: list[float],
    val_losses: list[float],
    save_path: Path
) -> plt.Figure:
    """Plot training and validation loss curves.
    Include: title, legend, grid, axis labels.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Test distribution plot
        np.random.seed(42)
        data = np.random.normal(0, 1, 1000)
        fig1 = plot_distribution(data, "Normal Distribution", tmp / "dist.png")
        assert fig1 is not None
        assert (tmp / "dist.png").exists()

        # Test correlation matrix
        data2 = np.random.randn(100, 4)
        fig2 = plot_correlation_matrix(data2, ["A", "B", "C", "D"], tmp / "corr.png")
        assert fig2 is not None
        assert (tmp / "corr.png").exists()

        # Test training curves
        train = [1.0, 0.8, 0.6, 0.4, 0.3, 0.25]
        val = [1.1, 0.9, 0.7, 0.55, 0.5, 0.48]
        fig3 = plot_training_curves(train, val, tmp / "curves.png")
        assert fig3 is not None
        assert (tmp / "curves.png").exists()

    plt.close("all")
    print("✅ All tests passed!")

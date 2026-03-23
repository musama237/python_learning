"""
Challenge: Time Series Processing
Difficulty: ⭐⭐⭐ Hard
Topic: Pandas, Time Series, Resampling

Work with time series data using Pandas.

Hints:
    1. dt accessor for date parts (df.date.dt.year, .dt.month, etc.)
    2. resample().agg({'price': ['first','max','min','last']}) for OHLCV
    3. rolling mean +/- n*rolling std for anomaly detection

Learn:
    # Date features from datetime column:
    df["year"] = df["date"].dt.year
    df["is_weekend"] = df["date"].dt.dayofweek >= 5

    # Resample OHLCV:
    resampled = df.resample("1h").agg({"price": ["first","max","min","last"], "volume": "sum"})

    # Anomaly detection:
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    anomalies = (series - rolling_mean).abs() > n_std * rolling_std
"""

import pandas as pd
import numpy as np


def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """Given df with a 'date' column (datetime), add:
    - year, month, day, day_of_week, is_weekend, quarter
    Return modified df.
    """
    # YOUR CODE HERE
    pass


def resample_ohlcv(df: pd.DataFrame, freq: str) -> pd.DataFrame:
    """Given df with 'date' (index), 'price', 'volume' at minute level,
    resample to given frequency ('1H', '1D', etc.) returning:
    - open (first), high (max), low (min), close (last) for price
    - volume (sum)
    """
    # YOUR CODE HERE
    pass


def detect_anomalies(series: pd.Series, window: int, n_std: float) -> pd.Series:
    """Detect anomalies using rolling mean +/- n_std * rolling_std.
    Return boolean Series (True = anomaly).
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test date features
    df = pd.DataFrame({
        "date": pd.to_datetime(["2024-01-15", "2024-03-20", "2024-07-04"]),
        "value": [1, 2, 3]
    })
    result = create_date_features(df)
    assert "year" in result.columns
    assert "is_weekend" in result.columns
    assert result["month"].tolist() == [1, 3, 7]

    # Test resample
    dates = pd.date_range("2024-01-01", periods=120, freq="1min")
    ohlcv = pd.DataFrame({
        "price": np.random.randn(120).cumsum() + 100,
        "volume": np.random.randint(100, 1000, 120)
    }, index=dates)
    hourly = resample_ohlcv(ohlcv, "1h")
    assert "open" in hourly.columns
    assert "high" in hourly.columns
    assert len(hourly) == 2

    # Test anomaly detection
    np.random.seed(42)
    normal = pd.Series(np.random.randn(100))
    normal.iloc[50] = 10  # Inject anomaly
    anomalies = detect_anomalies(normal, window=10, n_std=2)
    assert anomalies.iloc[50] is True or anomalies.iloc[50] == True
    assert anomalies.sum() < 10  # Not too many false positives
    print("✅ All tests passed!")

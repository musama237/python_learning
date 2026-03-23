"""
Challenge: Pandas Advanced
Difficulty: ⭐⭐ Medium
Topic: Pandas, Merging, Pivoting, Window Functions

Advanced Pandas data manipulation.

Hints:
    1. pd.merge(left, right, on=col, how='left').dropna() for joining
    2. pd.pivot_table() for reshaping data
    3. df['col'].rolling(window) for rolling statistics
    4. drop_duplicates, fillna, str.strip for cleaning
"""

import pandas as pd
import numpy as np


def merge_datasets(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """Left join orders with customers on 'customer_id'.
    Drop rows where customer info is missing.
    Return sorted by order_date.
    """
    # YOUR CODE HERE
    pass


def pivot_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Given df with columns: date, product, revenue,
    create a pivot table with dates as rows, products as columns,
    values are sum of revenue. Fill NaN with 0.
    """
    # YOUR CODE HERE
    pass


def rolling_stats(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """Given df with 'date' and 'value' columns (sorted by date),
    add columns: rolling_mean, rolling_std (using given window size).
    """
    # YOUR CODE HERE
    pass


def clean_messy_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a messy DataFrame:
    1. Drop duplicate rows
    2. Fill numeric NaN with column median
    3. Fill string NaN with 'Unknown'
    4. Strip whitespace from string columns
    5. Convert 'date' column to datetime if it exists
    Return cleaned df.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test merge
    orders = pd.DataFrame({
        "order_id": [1, 2, 3],
        "customer_id": [101, 102, 103],
        "order_date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "amount": [100, 200, 300]
    })
    customers = pd.DataFrame({
        "customer_id": [101, 102],
        "name": ["Alice", "Bob"]
    })
    merged = merge_datasets(orders, customers)
    assert len(merged) == 2
    assert "name" in merged.columns

    # Test pivot
    sales = pd.DataFrame({
        "date": ["2024-01", "2024-01", "2024-02", "2024-02"],
        "product": ["A", "B", "A", "B"],
        "revenue": [100, 200, 150, 250]
    })
    pivoted = pivot_sales(sales)
    assert pivoted.loc["2024-01", "A"] == 100
    assert pivoted.loc["2024-02", "B"] == 250

    # Test rolling
    ts = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=10),
        "value": range(10)
    })
    rolled = rolling_stats(ts, 3)
    assert "rolling_mean" in rolled.columns
    assert "rolling_std" in rolled.columns
    assert np.isnan(rolled["rolling_mean"].iloc[0])  # Not enough data
    assert rolled["rolling_mean"].iloc[2] == 1.0  # mean(0,1,2)

    # Test clean
    messy = pd.DataFrame({
        "name": ["Alice ", " Bob", None, "Alice "],
        "age": [30, None, 25, 30],
        "score": [90.0, 85.0, None, 90.0]
    })
    clean = clean_messy_data(messy)
    assert len(clean) == 3  # Duplicate removed
    assert clean["name"].iloc[0] == "Alice"  # Stripped
    assert not clean["age"].isna().any()  # NaN filled
    print("✅ All tests passed!")

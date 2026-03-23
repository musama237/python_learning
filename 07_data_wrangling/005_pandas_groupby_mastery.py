"""
Challenge: Pandas GroupBy Mastery
Difficulty: ⭐⭐ Medium
Topic: Pandas, GroupBy, Aggregation, Transform

Master the groupby operation — the most powerful Pandas tool.

Hints:
    1. groupby().agg() with named aggregations for multi_agg
    2. groupby().rank(ascending=False) for ranking within groups
    3. groupby().cumsum() for cumulative totals per group
    4. groupby().apply(lambda g: g.nlargest(n)) for top-n per group

Learn:
    # Named aggregation:
    df.groupby("cat").agg(value_mean=("value", "mean"), value_count=("value", "count"))

    # Rank within group:
    df["rank"] = df.groupby("dept")["salary"].rank(ascending=False)

    # Cumulative sum per group (sort first):
    df = df.sort_values(["user_id", "date"])
    df["cumsum"] = df.groupby("user_id")["amount"].cumsum()
"""

import pandas as pd
import numpy as np


def multi_agg(df: pd.DataFrame) -> pd.DataFrame:
    """Given df with 'category' and 'value' columns,
    group by category and compute:
    - count, mean, median, std, min, max
    Return with flat column names like 'value_mean', 'value_count', etc.
    """
    # YOUR CODE HERE
    pass


def group_rank(df: pd.DataFrame) -> pd.DataFrame:
    """Given df with 'department' and 'salary' columns,
    add 'salary_rank' column: rank within each department (highest=1).
    """
    # YOUR CODE HERE
    pass


def cumulative_sum_by_group(df: pd.DataFrame) -> pd.DataFrame:
    """Given df with 'user_id', 'date', 'amount',
    add 'cumulative_amount': running total per user, ordered by date.
    """
    # YOUR CODE HERE
    pass


def top_n_per_group(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """Given df with 'category' and 'score',
    return top n rows per category by score.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test multi_agg
    df1 = pd.DataFrame({
        "category": ["A", "A", "B", "B", "B"],
        "value": [10, 20, 30, 40, 50]
    })
    agg = multi_agg(df1)
    assert "value_mean" in agg.columns
    assert agg.loc[agg.index == "A", "value_mean"].values[0] == 15.0
    assert agg.loc[agg.index == "B", "value_count"].values[0] == 3

    # Test group_rank
    df2 = pd.DataFrame({
        "department": ["A", "A", "A", "B", "B"],
        "salary": [50, 70, 60, 80, 90]
    })
    ranked = group_rank(df2)
    assert ranked.loc[ranked["salary"] == 70, "salary_rank"].values[0] == 1

    # Test cumulative sum
    df3 = pd.DataFrame({
        "user_id": [1, 1, 2, 1, 2],
        "date": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-03", "2024-01-02"],
        "amount": [10, 20, 100, 30, 200]
    })
    cum = cumulative_sum_by_group(df3)
    # User 1: 10, 30, 60 | User 2: 100, 300
    user1 = cum[cum["user_id"] == 1].sort_values("date")
    assert list(user1["cumulative_amount"]) == [10, 30, 60]

    # Test top_n_per_group
    df4 = pd.DataFrame({
        "category": ["A", "A", "A", "B", "B", "B"],
        "score": [10, 30, 20, 50, 40, 60]
    })
    top2 = top_n_per_group(df4, 2)
    assert len(top2) == 4
    a_scores = sorted(top2[top2["category"] == "A"]["score"].tolist(), reverse=True)
    assert a_scores == [30, 20]
    print("✅ All tests passed!")

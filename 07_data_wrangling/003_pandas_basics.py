"""
Challenge: Pandas Basics
Difficulty: ⭐ Easy
Topic: Pandas, DataFrames, Series

Solve each using Pandas operations.

Hints:
    1. pd.DataFrame(dict) to create
    2. df[df.col >= val].sort_values() for filtering and sorting
    3. df.apply or np.where for conditional column
    4. groupby().agg() for group statistics
"""

import pandas as pd
import numpy as np


def create_student_df() -> pd.DataFrame:
    """Create a DataFrame with columns: name, age, grade, city
    with at least 5 rows of sample data.
    """
    # YOUR CODE HERE
    pass


def filter_and_sort(df: pd.DataFrame, min_age: int) -> pd.DataFrame:
    """Filter rows where age >= min_age, sort by grade descending.
    Reset index after filtering.
    """
    # YOUR CODE HERE
    pass


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Given a df with 'price' and 'quantity' columns, add:
    - 'total': price * quantity
    - 'category': 'expensive' if price > 50 else 'cheap'
    Return the modified df.
    """
    # YOUR CODE HERE
    pass


def group_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Given a df with 'department' and 'salary' columns,
    return a df with: department, mean_salary, max_salary, count
    Sorted by mean_salary descending.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test create
    df = create_student_df()
    assert len(df) >= 5
    assert set(["name", "age", "grade", "city"]).issubset(df.columns)

    # Test filter_and_sort
    test_df = pd.DataFrame({
        "name": ["A", "B", "C", "D"],
        "age": [20, 25, 18, 30],
        "grade": [85, 90, 95, 80]
    })
    result = filter_and_sort(test_df, 20)
    assert len(result) == 3
    assert result.iloc[0]["grade"] == 90  # Highest grade first

    # Test add_computed_columns
    shop_df = pd.DataFrame({"price": [100, 30, 60], "quantity": [2, 5, 1]})
    result2 = add_computed_columns(shop_df)
    assert list(result2["total"]) == [200, 150, 60]
    assert list(result2["category"]) == ["expensive", "cheap", "expensive"]

    # Test group_statistics
    emp_df = pd.DataFrame({
        "department": ["A", "A", "B", "B", "B"],
        "salary": [50000, 60000, 70000, 80000, 90000]
    })
    stats = group_statistics(emp_df)
    assert stats.iloc[0]["department"] == "B"  # Higher mean
    assert stats.iloc[0]["count"] == 3
    print("✅ All tests passed!")

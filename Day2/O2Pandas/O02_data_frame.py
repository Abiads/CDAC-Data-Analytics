"""
Concepts used in this example:
1. DataFrame Data Structure: 2D heterogeneous tabular data with labeled row and column axes.
2. Construction from Dict of Lists: Creating tabular datasets from key-value lists.
3. Structural Inspection via .info(): Non-null counts, column dtypes, and memory consumption.
4. Column Extraction: Accessing individual columns as 1D pd.Series objects.
5. Parametric Summary Statistics via .describe(): Computing count, mean, std, and 5-number summaries.
"""

import pandas as pd

# 1. DataFrame Construction
df_cricket = pd.DataFrame({
    "name": ["sachin", "virat", "rahul", "ms dhoni", "rohit",
             "mithali", "anjali", "priya", "neha"],
    "age": [50, 36, 32, 41, 34, 40, 28, 25, 30],
    "gender": ["male", "male", "male", "male", "male", 
               "female", "female", "female", "female"]
})
print("Cricket DataFrame:\n", df_cricket)
print("=" * 60)

# 2. Structural Inspection via info()
print("DataFrame Info:")
df_cricket.info()
print("=" * 60)

# 3. Column Extraction (Series extraction)
age_series = df_cricket["age"]
print("Extracted 'age' Column:\n", age_series)
print("\nType of extracted column:", type(age_series))
print("\nSummary of 'age' Column:\n", age_series.describe())
print("=" * 60)

# 4. Parametric Summary of entire DataFrame
print("Summary of Numeric Features in DataFrame (Transposed):\n", df_cricket.describe().T)
print("=" * 60)

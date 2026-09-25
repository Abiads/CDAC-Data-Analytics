"""
Concepts used in this example:
1. Pandas Series Architecture: 1D labeled array with homogeneous data types and explicit index mapping.
2. Series Construction: Creating Series from Python lists, custom integer indices, and key-value dictionaries.
3. Index Re-alignment & Missing Values: Handling missing keys during re-indexing (NaN generation).
4. Vectorized Arithmetic: Scalar math, aggregations (.sum(), .mean(), .std(), .var(), .median(), .mode(), .prod()).
5. Series Metadata Inspection: Accessing .values, .index, .dtype, .shape, .ndim, .size, and .memory_usage().
"""

import pandas as pd

# 1. Basic Series Construction
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Basic Series:\n", series)
print("-" * 60)

players = ["sachin", "virat", "rahul", "ms dhoni", "rohit"]
players_series = pd.Series(players, name="Players")
print("Players Series:\n", players_series)
print("-" * 60)

# 2. Custom Indices
integer_series = pd.Series([10, 20, 30, 40, 50], name="Integers")
print("Integer Series:\n", integer_series)
print("-" * 60)

col_index = [100, 200, 300, 400, 500]
players_1_series = pd.Series(players, index=col_index, name="Players Custom Index")
print("Players with Custom Index:\n", players_1_series)
print("-" * 60)

# 3. Series from Dictionaries
players_role = {
    "sachin": "batsman",
    "virat": "captain",
    "rahul": "batsman",
    "dhoni": "wicketkeeper",
    "rohit": "batsman"
}
players_role_series = pd.Series(players_role, name="Players Role")
print("Players Role Series:\n", players_role_series)
print("-" * 60)

# Re-indexing with a dictionary (introduces NaN for missing keys)
data_dict = {'a': 100, 'b': 200, 'c': 300}
data_dict_series = pd.Series(data_dict, name="Data Dict", index=['b', 'a', 'c', 'd'])
print("Data Dict Series with Re-indexing (NaN for 'd'):\n", data_dict_series)
print("-" * 60)

# 4. Vectorized Operations & Statistical Summaries
vector_series = pd.Series([1, 2, 3, 4, 5], name="Vector")
print("Original Vector Series:\n", vector_series)
print("Vector + 10:\n", vector_series + 10)
print("Vector * 2:\n", vector_series * 2)
print("Vector - 3:\n", vector_series - 3)
print("Vector / 2:\n", vector_series / 2)
print("Sum:               ", vector_series.sum())
print("Mean (1st moment): ", vector_series.mean())
print("Max:               ", vector_series.max())
print("Min:               ", vector_series.min())
print("Std (2nd moment):  ", vector_series.std())
print("Variance:          ", vector_series.var())
print("Median:            ", vector_series.median())
print("Mode:              ", vector_series.mode().values)
print("Product:           ", vector_series.prod())
print("-" * 60)

# 5. Metadata and Attribute Inspection
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
fruits_day = pd.Series(fruits, index=weekdays, name="Fruits Day")
print("Fruits Day Series:\n", fruits_day)
print("-" * 60)
print("Values Array:       ", fruits_day.values)
print("Index Array:        ", fruits_day.index)
print("Data type:          ", fruits_day.dtype)
print("Shape:              ", fruits_day.shape)
print("Dimensions (ndim):  ", fruits_day.ndim)
print("Element count:      ", fruits_day.size)
print("Memory usage (bytes):", fruits_day.memory_usage())

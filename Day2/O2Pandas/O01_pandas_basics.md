# Pandas Core Architecture: Series & DataFrames

## 1. What is Pandas?
Pandas is Python's primary data manipulation and tabular analysis library built directly on top of NumPy. It provides two foundational data structures:
- **`pd.Series` (1D):** Labeled homogeneous 1D array.
- **`pd.DataFrame` (2D):** Labeled heterogeneous 2D table composed of multiple Series sharing an index.

## 2. Key Differences: Series vs. DataFrame

| Dimension | `pd.Series` | `pd.DataFrame` |
| :--- | :--- | :--- |
| **Dimensionality** | 1D (vector) | 2D (matrix / tabular) |
| **Axes** | Single axis (index) | Two axes (rows `index`, columns `columns`) |
| **Types** | Single `dtype` | Heterogeneous (`dtype` per column) |
| **Analogy** | Single column or single record | Full spreadsheet / SQL database table |

## 3. Essential Inspection Methods
- **`df.info()`:** Provides a concise structural summary including:
  - Total row and column dimensions.
  - Non-null counts per column (crucial for finding missing data).
  - Data types (`int64`, `float64`, `object`, `category`).
  - Total memory footprint in RAM.
- **`df.describe()`:** Generates parametric statistics for numeric columns:
  - Count, Mean (1st statistical moment).
  - Standard Deviation (2nd statistical moment).
  - 5-number summary: Min, 25% ($Q_1$), 50% (Median), 75% ($Q_3$), Max.

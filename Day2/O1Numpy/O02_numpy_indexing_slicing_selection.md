# NumPy Indexing, Slicing & Selection

## 1. Core Principles
- **Zero-Copy Slicing:** Basic slicing (`array[start:stop:step]`) creates a **view** referencing the original memory buffer. Modifications to a slice mutate the original array directly, eliminating memory duplication and maximizing speed.
- **Rank Preservation vs. Dimension Dropping:**
  - Indexing with a scalar integer drops rank (e.g., `matrix_2d[0]` yields a 1D vector).
  - Indexing with a slice preserves rank (e.g., `matrix_2d[0:1]` yields a 2D matrix of shape `(1, N)`).
- **Fancy / Integer Array Indexing:**
  - Passing arrays of integer coordinates (e.g., `matrix[row_indices, col_indices]`) selects specific arbitrary elements.
  - **Crucial Rule:** Fancy indexing always creates a **copy**, not a view.
- **Boolean Indexing (Masking):**
  - Filtering elements based on conditional logical expressions (e.g., `data[data > 50]`).
  - Produces a 1D flattened copy containing only elements where the boolean mask evaluates to `True`.

## 2. Quick Reference

| Slicing Syntax | Operation | Result Type | Shares Memory? |
| :--- | :--- | :--- | :---: |
| `arr[2:6]` | 1D range slice | Sub-array view | Yes (`View`) |
| `arr[::-1]` | Array reversal | Reversed view | Yes (`View`) |
| `arr[:2, 2:]` | 2D block slice | Sub-matrix view | Yes (`View`) |
| `arr[[0, 2], [1, 3]]` | Integer coordinate indexing | Extracted elements | No (`Copy`) |
| `arr[arr > 0.5]` | Boolean mask filtering | Filtered 1D array | No (`Copy`) |
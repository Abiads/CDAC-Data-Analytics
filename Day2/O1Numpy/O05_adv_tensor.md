# Advanced Tensor Operations: Einstein Summation (`einsum`)

## 1. What is Einstein Summation?
`np.einsum` provides a concise index-based representation for multidimensional array transformations, inner products, traces, and tensor contractions without explicit loops or intermediate copies.

## 2. Einsum Indexing Grammar
- Repeating an index across inputs means multiplication.
- Omitting an index in the output implies summation (contraction) along that axis.
- Specifying an index in the output determines the output axis arrangement.

## 3. Common Operations Table

| Operation | Einsum Notation | Equivalent NumPy Call |
| :--- | :--- | :--- |
| **Matrix Multiplication** | `'ij,jk->ik'` | `A @ B` or `np.matmul(A, B)` |
| **Inner / Dot Product** | `'i,i->'` | `np.dot(a, b)` |
| **Matrix Transpose** | `'ij->ji'` | `A.T` |
| **Matrix Trace (Diagonal Sum)**| `'ii->'` | `np.trace(A)` |
| **Sum across Columns** | `'ij->j'` | `np.sum(A, axis=0)` |
| **Sum across Rows** | `'ij->i'` | `np.sum(A, axis=1)` |
| **Batch Matrix Multiplication**| `'bij,bjk->bik'` | Batched `@` across 3D tensors |

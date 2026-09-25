"""
Concepts used in this example:
1. Einstein Summation Convention (einsum): Compact index-based tensor contraction notation.
2. Index Grammar: Repeated indices indicate element-wise multiplication; omitted indices imply summation.
3. Equivalent Operations: Demonstrating matrix multiplication, transposition, and trace via einsum vs standard NumPy operators.
"""

import numpy as np

A = np.array([[1, 2], [4, 5]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# 1. Matrix multiplication: C_ik = sum_j (A_ij * B_jk)
mat_mul_einsum = np.einsum('ij,jk->ik', A, B)
print("\n1. Matrix multiplication using einsum ('ij,jk->ik'):\n", mat_mul_einsum)
print("Standard @ operator comparison:\n", A @ B)

# 2. Transposition: A^T
transpose_einsum = np.einsum('ij->ji', A)
print("\n2. Transpose using einsum ('ij->ji'):\n", transpose_einsum)

# 3. Trace (sum of diagonal elements)
trace_einsum = np.einsum('ii->', A)
print("\n3. Trace using einsum ('ii->'):", trace_einsum)
print("np.trace comparison:", np.trace(A))

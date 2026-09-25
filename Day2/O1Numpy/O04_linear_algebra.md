# NumPy Linear Algebra & Broadcasting Mechanics

## 1. Matrix Operations & Multiplication
- **Dot Product:** 
  - For 1D vectors, computes inner product: $\mathbf{a} \cdot \mathbf{b} = \sum a_i b_i$.
  - Executed via `np.dot(a, b)` or the infix `@` operator.
- **Matrix Multiplication:**
  - For 2D matrices, computes linear algebraic product $C_{ik} = \sum_j A_{ij} B_{jk}$.
  - Requires inner dimensions to match: $(M \times K) \times (K \times N) \rightarrow (M \times N)$.
  - Executed via `A @ B` (preferred in modern Python 3.5+) or `np.matmul(A, B)`.

## 2. Transposition & Dimension Expansion
- **Transposition (`.T`):** Reverses matrix axes.
- **1D Caveat:** A 1D array of shape `(N,)` has only one axis; `.T` has no effect.
- **Rank Expansion (`np.newaxis`):**
  - Converts a 1D vector `(N,)` into a 2D column vector of shape `(N, 1)`: `arr[:, np.newaxis]`.
  - Converts a 1D vector `(N,)` into a 2D row vector of shape `(1, N)`: `arr[np.newaxis, :]`.

## 3. General Broadcasting Rules
NumPy compares shapes element-wise, starting from the trailing (rightmost) dimensions:
Two dimensions are compatible if:
1. They are equal, OR
2. One of them is $1$.

### Example: Outer Grid Expansion
```
vec_x_col shape: (3, 1)
vec_y     shape:    (2)   -> aligned as (1, 2)
Result    shape: (3, 2)
```
NumPy automatically stretches dimension 1 of `vec_x_col` and dimension 0 of `vec_y` across memory without duplicating physical data.

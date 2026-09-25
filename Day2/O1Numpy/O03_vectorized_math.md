# NumPy Vectorized Mathematics & Statistical Moments

## 1. Vectorized Computation & Ufuncs
- **Universal Functions (`ufuncs`):** Fast, element-by-element operations compiled in C (`np.add`, `np.subtract`, `np.multiply`, `np.divide`, `np.power`, `np.sqrt`, `np.exp`, `np.log`).
- **Elimination of Python Loops:** Operations execute over contiguous memory blocks in hardware registers without Python interpreter overhead.

## 2. Memory Buffer Optimization (`out=` Parameter)
- By default, operations like `a * 2.5` allocate a new temporary array in RAM.
- Using the `out=` parameter (e.g., `np.multiply(source, scalar, out=destination_buffer)`) reuses pre-allocated memory buffers, avoiding expensive memory allocation and garbage collection overhead during large-scale data processing.
- Verify buffer sharing using `np.may_share_memory(a, b)`.

## 3. Statistical Reductions & Moments
- **Axis Reductions:**
  - Global: `np.sum(arr)`, `np.mean(arr)`
  - Column-wise (`axis=0`): Computes statistics down each column across rows (per-feature).
  - Row-wise (`axis=1`): Computes statistics across each row across columns (per-sample).

- **1st Statistical Moment (Mean / Central Tendency):**
  $$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$

- **2nd Statistical Moment (Variance & Standard Deviation / Dispersion):**
  $$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2, \quad \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

- **Z-Score Normalization (Standardization):**
  Transforming arbitrary continuous feature distributions to standard normal scale ($\mu = 0, \sigma = 1$):
  $$z = \frac{x - \mu}{\sigma}$$
  *Validation:*
  - Mean of Z-normalized data $\approx 0$
  - Standard deviation of Z-normalized data $\approx 1$

# NumPy Architecture: Memory, Layout & Data Types

## 1. Core Architecture
- **Computational Engine:** Numerical Python (NumPy) is the foundational library for scientific computing and high-performance data processing in Python.
- **`ndarray` Storage:** A homogeneous, contiguous block of allocated memory (C-contiguous or Fortran-contiguous).
- **Hardware Acceleration:** Contiguous memory layout maximizes CPU cache line locality (L1/L2/L3 cache hits) and leverages modern CPU vector SIMD instructions (AVX-512, SSE). This achieves 50x–100x execution speedups over native Python `for` loops.
- **Zero-Copy Views:** Basic slicing returns a view rather than allocating new memory buffers, drastically reducing RAM overhead for massive arrays.
- **Type Precision (`dtype`):** Using explicit fixed-width data types (`int32`, `int64`, `float32`, `float64`) avoids Python's dynamic type-checking overhead and object boxing/unboxing.
- **Structured Arrays:** Heterogeneous column schemas using compound dtypes, mapped to low-level C `struct` representations in memory.

## 2. Memory Comparison: Python List vs. NumPy `ndarray`

| Feature | Standard Python `list` | NumPy `ndarray` |
| :--- | :--- | :--- |
| **Memory Allocation** | Non-contiguous array of pointers to `PyObject`s | Single contiguous flat buffer in RAM |
| **Element Types** | Heterogeneous (any object) | Homogeneous (fixed `dtype`) |
| **Cache Locality** | Poor (cache misses due to pointer dereferencing) | Optimal (sequential memory pre-fetching) |
| **Memory Overhead** | ~8 bytes per pointer + 28 bytes per integer | Exactly the size of the datatype (e.g. 4 or 8 bytes) |
| **Vectorization** | Requires Python interpreter bytecode loops | Direct C/Fortran compiled vector instructions |

## 3. Factory Tensor Initializers
- `np.zeros(shape, dtype)`: Pre-allocates buffer initialized to 0.
- `np.ones(shape, dtype)`: Pre-allocates buffer initialized to 1.
- `np.full(shape, fill_value)`: Pre-allocates buffer filled with a constant.
- `np.eye(N)`: Generates an identity matrix of dimension $N \times N$.
- `np.arange(start, stop, step)`: Evenly spaced intervals within a range.
- `np.random.default_rng(seed)`: Modern high-performance Mersenne Twister / PCG64 random generator.

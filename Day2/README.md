# Day 2: Scientific Python, NumPy Architecture & Pandas Foundations

> **Course:** Data Analytics (PGCP-AI, C-DAC ACTS)  
> **Module Mapping:** Module 1 (Session 2: Environment Setup, Computational Core & Statistical Foundations)  
> **Prerequisites:** Python 3.10+, Virtual Environment (`venv`)

---

## 📌 Overview

Day 2 focuses on high-performance scientific computing in Python. We transition from native Python object structures to contiguous C-level memory buffers using **NumPy**, dive into vectorized arithmetic and statistical moments, and introduce structured tabular analysis with **Pandas**.

---

## 📂 Directory Structure & Module Index

```
Day2/
├── minutes.txt                           # Lecture minutes and agenda
├── requirements.txt                      # Pinned Python package dependencies
├── README.md                             # Day 2 master index and guide
├── O1Numpy/                              # NumPy architecture, vectorization & linear algebra
│   ├── O01_NumpyBasic.md                 # Architecture, C-buffers, cache locality & dtypes
│   ├── O01_simple_ndarray.py             # ndarray creation, buffer inspection, factory initializers
│   ├── O02_numpy_indexing_slicing_selection.md # Zero-copy slicing, views vs copies, rank rules
│   ├── O02_numpy_indexing_slicing_selection.py # 1D/2D slicing, boolean masks, fancy indexing
│   ├── O03_vectorized_math.md            # Ufuncs, memory recycling ('out='), moments formulas
│   ├── O03_vectorized_math.py            # Reductions, Z-Score normalization, statistical moments
│   ├── O04_linear_algebra.md             # Dot product, matmul (@), transposition, broadcasting
│   ├── O04_linear_algebra.py             # Linear algebra workflows & broadcasting grid examples
│   ├── O05_adv_tensor.md                 # Einstein summation notation ('einsum') reference
│   └── O05_adv_tensor.py                 # Advanced tensor contractions using np.einsum
└── O2Pandas/                             # Pandas tabular data structures & exploratory inspection
    ├── O01_pandas_basics.md              # Series vs DataFrame architecture, inspection methods
    ├── O01_series.py                     # pd.Series construction, re-indexing, summary statistics
    └── O02_data_frame.py                 # pd.DataFrame creation, .info(), and .describe()
```

---

## ⚡ Key Topics & Mathematical Formulas Covered

### 1. NumPy ndarray Memory Architecture
- **Contiguous Memory Buffers:** Maximizes L1/L2/L3 CPU cache locality and SIMD vector register instructions (AVX-512/SSE).
- **Views vs Copies:** Basic slicing returns a zero-copy memory view (`np.may_share_memory() == True`), whereas fancy integer/boolean indexing allocates a new copy.

### 2. Statistical Moments & Standardization
- **1st Moment (Mean):**
  $$\mu = \frac{1}{N}\sum_{i=1}^N x_i$$
- **2nd Moment (Variance & Standard Deviation):**
  $$\sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2, \quad \sigma = \sqrt{\sigma^2}$$
- **Z-Score Normalization:**
  $$z = \frac{x - \mu}{\sigma} \quad (\text{rescales to } \mu = 0, \, \sigma = 1)$$

### 3. Broadcasting Compatibility Rule
Two dimensions are compatible for automatic broadcasting when:
1. They are equal, OR
2. One of them is $1$.

---

## 💻 Running the Code

### 1. Virtual Environment Setup
```bash
# Create and activate virtual environment
python -m venv cdacvenv

# Windows
.\cdacvenv\Scripts\activate

# Linux / macOS
source cdacvenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running NumPy Scripts
```bash
python O1Numpy/O01_simple_ndarray.py
python O1Numpy/O02_numpy_indexing_slicing_selection.py
python O1Numpy/O03_vectorized_math.py
python O1Numpy/O04_linear_algebra.py
python O1Numpy/O05_adv_tensor.py
```

### 3. Running Pandas Scripts
```bash
python O2Pandas/O01_series.py
python O2Pandas/O02_data_frame.py
```

---

## 🔗 Related Notes
- Comprehensive theoretical guide: [notes/01_foundations_and_eda.md](../notes/01_foundations_and_eda.md#session-2-environment-setup-computational-core--statistical-foundations-numpy--pandas)
- Master formula card: [notes/README.md](../notes/README.md)

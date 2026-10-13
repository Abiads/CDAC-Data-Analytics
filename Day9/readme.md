# Day 9: Advanced Data Wrangling & High-Performance Pandas
> **Programme:** C-DAC PGCP-AI (Post Graduate Certificate Programme in AI)  
> **Course:** Data Analytics  
> **Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`)  
> **Date:** October 13, 2026  

---

## 📌 Day 9 Structure & Learning Modules

```
Day9/
├── data_wrangling/
│   ├── .gitkeep                           # Repository anchor
│   └── 01_data_wrangling.ipynb            # Master executed laboratory notebook (5 comprehensive modules)
└── readme.md                              # Day 9 Master Reference Guide & Theoretical Manual
```

---

## 📖 Table of Contents
1. [Module 1: MultiIndex DataFrame and Hierarchical Slicing](#1-multiindex-dataframe-and-hierarchical-slicing)
2. [Module 2: Vectorised Strings and Regular Expressions](#2-vectorised-strings-and-regular-expressions)
3. [Module 3: Transform Pipeline](#3-transform-pipeline)
4. [Module 4: Memory Optimisation and Data Type Downcasting](#4-memory-optimisation-and-data-type-downcasting)
5. [Module 5: High-Performance Query (`df.query` & `pd.eval`)](#5-high-performance-query-dfquery--pdeval)
6. [Summary & Architectural Scorecard](#6-summary--architectural-scorecard)

---

## 1. MultiIndex DataFrame and Hierarchical Slicing
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#1-multiindex-dataframe-and-hierarchical-slicing)

### 1.1 Core Mathematical Motivation
Real-world enterprise datasets inherently possess multidimensional relationships (e.g., $\text{Region} \times \text{Country} \times \text{Year} \times \text{Quarter}$). Flattening these dimensions into denormalized string columns wastes memory and requires expensive multi-column grouping. Storing them in nested dictionaries loses vectorized array speed.

A **MultiIndex** (Hierarchical Index) models $N$-dimensional data cubes directly within standard 2D Pandas structures:

$$\text{Index Coordinate} = (L_0, L_1, L_2, \dots, L_{k-1})$$

### 1.2 Construction Approaches
| Method | Code Signature | Best Use Case |
| :--- | :--- | :--- |
| **From Tuples** | `pd.MultiIndex.from_tuples(tuples, names=[...])` | Known irregular combinations |
| **From Product** | `pd.MultiIndex.from_product([levels_a, levels_b], names=[...])` | Complete Cartesian products (all combinations) |
| **From DataFrame** | `df.set_index(['Region', 'Country', 'Year'])` | Converting existing flat columns |
| **Hierarchical Columns** | `pd.MultiIndex.from_tuples([('Financial', 'Revenue'), ...])` | Grouping metrics into logical domains |

### 1.3 Hierarchical Slicing & `pd.IndexSlice`
Directly indexing inner levels using tuple slicing like `df.loc[(:, 'Q1')]` causes a Python `SyntaxError`. The standard solution is `pd.IndexSlice`:

```python
idx = pd.IndexSlice

# Select all regions & countries for Year 2026, Quarter 'Q1', retrieving Financial metrics
subset = df.loc[
    idx[:, :, 2026, 'Q1'],
    idx['Financial', ['Revenue_M', 'EBITDA_M']]
]
```

> [!CAUTION]
> **The Lexicographical Sorting Requirement:** Always run `df.sort_index(inplace=True)` before performing multi-level range slicing (`idx['APAC':'EMEA', ...]`). Slicing an unsorted MultiIndex will trigger `UnsortedIndexError` or cause silent performance degradation.

### 1.4 Cross-Sectional Indexing with `.xs()`
The `.xs()` method provides an explicit, highly readable API to slice across any arbitrary depth level:
* **Row Cross-Section:** `df.xs(key='Q2', level='Quarter', drop_level=False)`
* **Column Cross-Section:** `df.xs(key='Operations', axis=1, level='Metric_Type')`

### 1.5 Reshaping & Level Aggregations
* **`unstack(level)`:** Pivots an index level into column headers (tall $\to$ wide).
* **`stack(level)`:** Pivots column levels down into index rows (wide $\to$ tall).
* **`swaplevel(i, j)`:** Swaps the hierarchical order of two levels.
* **`groupby(level=...)`:** Performs aggregations across index levels without dropping coordinates:
  ```python
  regional_annual_sales = df.groupby(level=['Region', 'Year'])['Financial', 'Revenue_M'].sum()
  ```

---

## 2. Vectorised Strings and Regular Expressions
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#2-vectorised-strings-and-regular-expressions)

### 2.1 The `.str` Accessor vs. Python Loops
Using `.apply(lambda x: re.search(...))` in Python introduces three critical bottlenecks:
1. **Interpreter Call Overhead:** Context-switching for each scalar row.
2. **Crash on Missing Data:** `None` or `np.nan` triggers `TypeError: expected string or bytes-like object`.
3. **Object Boxing:** Strings are repeatedly boxed and unboxed as Python heap objects.

The compiled C-backed `.str` accessor executes in vectorized memory, handles `NaN` values automatically by propagating them, and integrates natively with regex engines.

### 2.2 Core String Transformations
* **Whitespace & Case:** `.str.strip()`, `.str.lower()`, `.str.title()`
* **Delimiter Splitting with `expand=True`:**
  ```python
  # Splits full name into separate DataFrame columns in one pass
  names_df = df['full_name'].str.split(' ', n=1, expand=True)
  names_df.columns = ['First_Name', 'Last_Name']
  ```

### 2.3 Named Regex Extraction (`?P<Name>...`)
When extracting multiple fields from structured codes (e.g. `TXN_2026-NA-USA-ORD#88412_USD$14,500.50_STATUS:COMPLETED_FLAG:AUDIT`), using named capture groups extracts every token into an appropriately named column in a single pass:

```python
pattern = (
    r'TXN_(?P<Year>\d{4})-'
    r'(?P<Region>[A-Z]{2})-'
    r'(?P<Country>[A-Z]{3})-'
    r'ORD#(?P<Order_ID>\d+)_'
    r'(?P<Currency>[A-Z]{3}|[^\d]+)'
    r'(?P<Raw_Amount>[\d,]+(?:\.\d{2})?)_'
    r'STATUS:(?P<Status>[A-Z]+)_'
    r'FLAG:(?P<Audit_Flag>[A-Z]+)'
)

ledger = df['raw_txn'].str.extract(pattern)
```

### 2.4 Multiple Matches (`extractall`) & Backreferences
* **`.str.extractall(regex)`:** Finds all occurrences of repeating patterns (e.g. `#Hashtags`, `@mentions`) and outputs a MultiIndex Series indexed by `(row_index, match_number)`.
* **Regex Substitution with Backreferences:** Replaces matched patterns while referencing captured groups (`\1`, `\2` or `\g<name>`) for phone number and date standardization.

---

## 3. Transform Pipeline
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#3-transform-pipeline)

### 3.1 Declarative Pipelines via Method Chaining & `df.pipe()`
Procedural state modification (`df['a'] = ...`, `df['b'] = ...` spread over dozens of cells) creates fragile scripts with untracked mutable state.

The modern Pandas paradigm structures data wrangling as a pure functional pipeline:

```python
df_clean = (
    raw_df
    .pipe(clean_headers_and_strings)
    .pipe(impute_departmental_medians, group_col='dept', num_cols=['salary', 'sales'])
    .pipe(winsorize_salary, col='salary', group_col='dept')
    .pipe(engineer_metrics)
    .pipe(validate_schema)
)
```

### 3.2 `groupby().transform()` vs. `groupby().apply()`
| Dimension | `groupby().transform()` | `groupby().apply()` |
| :--- | :--- | :--- |
| **Output Shape** | **Strictly guaranteed** to match input rows ($N \to N$) | Arbitrary shape (scalar, Series, or reduced DataFrame) |
| **Index Alignment** | Preserves original index exactly; enables direct assignment | Often re-indexes or creates hierarchical indices |
| **Performance** | Optimized C-routines for standard aggregations (`mean`, `median`, `std`) | Incurs Python function invocation overhead per group |
| **Best Use Case** | Within-group Z-scores, group median imputation, group percentages | Complex custom logic that reshapes data |

### 3.3 Group-Specific Metrics Implemented in Pipeline:
1. **Departmental Z-Score:**
   $$Z_{i, \text{dept}} = \frac{X_i - \mu_{\text{dept}}}{\sigma_{\text{dept}}}$$
2. **Department Sales Contribution Share:**
   $$\text{Share}_{i} = \frac{\text{Sales}_i}{\sum_{j \in \text{dept}} \text{Sales}_j} \times 100\%$$
3. **Group Median Imputation:** Imputing missing values with the corresponding departmental median rather than the global median to preserve subgroup variance.

---

## 4. Memory Optimisation and Data Type Downcasting
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#4-memory-optimisation-and-data-type-downcasting)

### 4.1 Memory Architecture of Pandas
On 64-bit systems, Pandas defaults to:
* `int64` (8 bytes / integer): Range $[-9.22 \times 10^{18}, +9.22 \times 10^{18}]$. Storing small values (age, ratings, days) wastes $87.5\%$ of RAM!
* `float64` (8 bytes / float): Excessive precision for standard telemetry and financial figures.
* `object` (8 bytes pointer + Python string on heap): Causes extreme memory fragmentation and CPU cache misses.

### 4.2 Downcasting Rules & Memory Savings
| Target Type | Bytes | Safe Numerical Range | RAM Reduction vs Default |
| :--- | :---: | :--- | :---: |
| `int8` | 1 | $-128 \dots +127$ | **$87.5\%$** |
| `int16` | 2 | $-32,768 \dots +32,767$ | **$75.0\%$** |
| `int32` | 4 | $-2.14 \times 10^9 \dots +2.14 \times 10^9$ | **$50.0\%$** |
| `float32` | 4 | $10^{-38} \dots 10^{38}$ ($7$ decimal digits) | **$50.0\%$** |
| `category` | 1–2 | Low cardinality ($< 50\%$ unique rows) | **$80.0\% - 95.0\%$** |

### 4.3 Automated Optimization Benchmark (250,000 Rows)
Running the laboratory's `optimize_dataframe_memory()` function on a 250,000-row enterprise dataset:
* **Original Footprint:** `64.37 MB`
* **Optimized Footprint:** `9.54 MB`
* **Net RAM Reduction:** **`85.18%`**
* **Numerical Invariance:** Verified zero drift in statistical means and sums ($|\Delta \mu| < 10^{-6}$).

---

## 5. High-Performance Query (`df.query` & `pd.eval`)
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#5-high-performance-query-dfquery--pdeval)

### 5.1 The Intermediate Array Bottleneck
Standard boolean indexing:
```python
df[(df['A'] > 50) & (df['B'] < 30) & (df['C'] >= 250)]
```
Allocates multiple temporary boolean arrays in RAM for each sub-expression and bitwise operator. On datasets with millions of rows, this causes heavy garbage collection thrashing and memory spikes.

### 5.2 The High-Performance NumExpr Engine
`df.query()` and `pd.eval()` utilize **NumExpr**:
* Parses expressions into C-level bytecode.
* Breaks array evaluations into cache-friendly chunks that fit inside L1/L2/L3 CPU cache.
* Executes multi-threaded loops in C, bypassing Python's Global Interpreter Lock (GIL).

### 5.3 Query Syntax Highlights
1. **Dynamic Variable Scoping with `@`:**
   ```python
   min_salary = 85000
   target_depts = ['Engineering', 'Finance']
   df.query('salary >= @min_salary and department in @target_depts')
   ```
2. **Backticks for Columns with Spaces:**
   ```python
   df.query('`Annual Base Salary ($)` > 100000 and `CSAT Rating` >= 4.5')
   ```
3. **Compound Arithmetic with `df.eval()`:**
   ```python
   df.eval('Net_Margin = (Revenue - OpEx) / Revenue', inplace=True)
   ```

### 5.4 1,000,000-Row Execution Benchmark Scorecard
Benchmark executed on 1,000,000 rows across 5 runs:

| Method | Mean Latency (ms) | Standard Deviation | Speedup Factor | Memory Overhead |
| :--- | :---: | :---: | :---: | :--- |
| **Standard Boolean Mask** | `4.16 ms` | $\pm 0.35\text{ ms}$ | $1.00\times$ (Baseline) | High (Multiple temporary boolean arrays) |
| **`df.query(engine='python')`** | `7.38 ms` | $\pm 0.52\text{ ms}$ | $0.56\times$ (Slower) | Moderate (Python AST compilation) |
| **`df.query(engine='numexpr')`** | **`2.14 ms`** | $\pm 0.18\text{ ms}$ | **`3.45× vs Python` ($1.95\times$ vs Mask)** | Minimal (Chunked CPU cache evaluation) |

---

## 6. Summary & Architectural Scorecard

| Module | Core Tool / API | Primary Advantage | When to Use | Key Gotcha |
| :--- | :--- | :--- | :--- | :--- |
| **1. MultiIndex** | `pd.IndexSlice`, `.xs()`, `stack()` / `unstack()` | Represents $N$-dimensional data cubes in 2D with $O(1)$ lookups. | Hierarchical reports (Region $\to$ Country $\to$ Year). | Always run `df.sort_index()` before range slicing to prevent errors. |
| **2. Vectorised Strings** | `.str` accessor, Named Regex `(?P<Name>...)` | Compiled C routines; automatic `NaN` propagation; eliminates slow loops. | Parsing unstructured transaction logs, phone numbers, and tags. | Avoid `.apply(lambda x: ...)` for strings; use `.str.extract()` instead. |
| **3. Transform Pipeline** | `df.pipe()`, `groupby().transform()` | Pure functional composability; preserves input index length. | Multi-stage cleaning, group-specific Z-score scaling and imputation. | Use `transform()` instead of `apply()` when broadcasting back to rows. |
| **4. Memory Optimisation** | `pd.to_numeric(downcast=...)`, `category` dtype | Drastically cuts RAM usage ($> 80\%$) and speeds up groupbys. | Datasets with $\ge 100k$ rows or memory-constrained servers. | Ensure unique ratio $< 50\%$ before converting strings to `category`. |
| **5. High-Performance Query** | `df.query(engine='numexpr')`, `pd.eval()` | Avoids temporary RAM array allocations; multi-threaded C execution. | Complex multi-condition filtering on datasets with $> 100k$ rows. | Use backticks (`` `Col Name` ``) for column names containing spaces. |

---
**Module Completed:** Day 9 Advanced Data Wrangling & High-Performance Pandas  
**Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`)

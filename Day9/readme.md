# Day 9: Advanced Data Wrangling & High-Performance Pandas
> **Programme:** C-DAC PGCP-AI (Post Graduate Certificate Programme in AI)  
> **Course:** Data Analytics  
> **Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`) | **Instructor Notes:** Mohamed Ali (`alilog`)  
> **Date:** October 13, 2026  

---

## 📌 Day 9 Structure & Learning Modules

```
Day9/
├── Analytics/                             # Official upstream classroom notebooks (Ali Sir)
│   ├── 00_python_basics/
│   │   ├── 01_pandas_indexing.ipynb       # Series creation, indexing, string series & dicts
│   │   └── 02_df.ipynb                    # DataFrame construction, info, describe & reshape
│   └── O1_data_wrangling/
│       └── 01_indexing_vectorize.ipynb    # MultiIndex, regex, transform pipeline, downcasting, query
├── data_wrangling/
│   ├── .gitkeep                           # Repository anchor
│   ├── 01_data_wrangling.ipynb            # Master executed laboratory notebook (interactive help + 5 modules)
│   └── 02_missing_malformed_data.ipynb    # Executed notebook: Missing Data (MCAR/MAR/MNAR), Imputation (KNN/MICE/Rolling), Outlier Capping, Duplicate Resolution
├── readme.md                              # Unified Day 9 Master Guide + Ali Sir's 6-Phase Curriculum Blueprint
├── readme_detail.md                       # Ali Sir's Granular 6-Phase Analytical Workflows
└── test.py                                # Test script placeholder
```

---

## 📖 Table of Contents
- [🏛️ Enterprise Analytics Curriculum Blueprint (Phases 1 – 6 Notes)](#-enterprise-analytics-curriculum-blueprint-phases-1--6-notes)
  - [Phase 1: Ingestion & Foundation (Wrangling & SQL)](#phase-1-ingestion--foundation-wrangling--sql)
  - [Phase 2: Auditing & Profiling (EDA)](#phase-2-auditing--profiling-eda)
  - [Phase 3: Feature Engineering & Economic Alignment (KPIs)](#phase-3-feature-engineering--economic-alignment-kpis)
  - [Phase 4: Communication & Storytelling (Visualization)](#phase-4-communication--storytelling-visualization)
  - [Phase 5: Advanced Intelligence (Unsupervised & Predictive Modeling)](#phase-5-advanced-intelligence-unsupervised--predictive-modeling)
  - [Phase 6: Validation & Causal Impact (Experimentation)](#phase-6-validation--causal-impact-experimentation)
- [🛠️ Day 9 Practical Modules (Part 1: High-Performance Pandas)](#️-day-9-practical-modules-part-1-high-performance-pandas)
  - [0. 💡 Jupyter Auto-Suggestion & Inline Help Shortcuts](#0--jupyter-auto-suggestion--inline-help-shortcuts)
  - [1. Module 1: MultiIndex DataFrame and Hierarchical Slicing (North Region Sales)](#1-multiindex-dataframe-and-hierarchical-slicing-north-region-sales)
  - [2. Module 2: Vectorised Strings and Regular Expressions](#2-vectorised-strings-and-regular-expressions)
  - [3. Module 3: Transform Pipeline (HR & IT Salary)](#3-transform-pipeline-hr--it-salary-analysis)
  - [4. Module 4: Memory Optimisation and Data Type Downcasting](#4-memory-optimisation-and-data-type-downcasting)
  - [5. Module 5: High-Performance Query (`df.query` & `pd.eval`)](#5-high-performance-query-dfquery--pdeval)
  - [6. Summary & Architectural Scorecard](#6-summary--architectural-scorecard)
  - [7. ⚠️ Critical Interview Traps & Viva Hacks (Punchy & Direct)](#7--critical-interview-traps--viva-hacks-punchy--direct)
- [🔬 Day 9 Practical Modules (Part 2: Missing Data, Imputation, Outliers & Entity Resolution)](#-day-9-practical-modules-part-2-missing-data-imputation-outliers--entity-resolution)
  - [8. Missing Data Taxonomy (MCAR, MAR, MNAR)](#8-missing-data-taxonomy-mcar-mar-mnar)
  - [9. Advanced Imputation Strategies (KNN, Iterative / MICE, Rolling)](#9-advanced-imputation-strategies-knn-iterative--mice-rolling)
  - [10. Outlier Handling via Winsorization & Clipping](#10-outlier-handling-via-winsorization--clipping)
  - [11. Duplicate Detection & Entity Resolution Basics](#11-duplicate-detection--entity-resolution-basics)
  - [12. ⚠️ Part 2 Interview Traps & Viva Hacks](#12-️-part-2-interview-traps--viva-hacks)

---

## 🏛️ Enterprise Analytics Curriculum Blueprint (Phases 1 – 6 Notes)
> **Reference Document:** For deep granular step-by-step workflows, see [`Day9/readme_detail.md`](readme_detail.md).

### Phase 1: Ingestion & Foundation (Wrangling & SQL)
* **Core Nomenclature:** Data Ingestion, Relational Extraction, Schema Normalization, Memory Downcasting, Hierarchical Slicing, Vectorized Parsing.
* **Granular Scenarios Handled:**
  * **Memory Optimization:** Ingesting multi-gigabyte transactional logs using streaming chunk sizes (`chunksize=N`) and downcasting data types (e.g., converting 64-bit integers to 8-bit integers to reduce RAM footprints).
  * **Data Sanitization:** Standardizing string columns via `snake_casing`, stripping whitespace, and parsing ISO-8601 date formats.
  * **Relational Aggregation:** Executing conditional metrics via SQL `CASE WHEN` clauses, partition-based row ranking (`ROW_NUMBER() OVER`), and multi-level hierarchy traversal using recursive Common Table Expressions (CTEs).
  * **Multidimensional Panel Wrangling:** Setting multi-index axes (`set_index([L1, L2])`) to execute hierarchical slicing and melting wide-format tables into long-format structures.

---

### Phase 2: Auditing & Profiling (EDA)
* **Core Nomenclature:** Automated Profiling, Schema Enforcement, Missing Data Taxonomy, Collinearity Diagnostics, Non-Linear Association, Confounding Identification.
* **Granular Scenarios Handled:**
  * **Automated Data Quality Audits:** Generating instant HTML profiling reports (via YData-Profiling or Sweetviz) to inspect missingness percentages, duplicate entity keys, and memory allocations.
  * **Missing Data Classification:** Systematically diagnosing whether missing values follow MCAR (Missing Completely at Random), MAR (Missing at Random), or MNAR (Missing Not at Random) patterns.
  * **Multicollinearity Isolation:** Calculating Variance Inflation Factors (VIF) to detect and eliminate redundant predictor features that inflate regression coefficient variances.
  * **Confounding & Bias Detection:** Identifying Simpson’s Paradox where aggregate trends reverse or distort when data is segmented across localized cohorts.

---

### Phase 3: Feature Engineering & Economic Alignment (KPIs)
* **Core Nomenclature:** Categorical Encoding, Bayesian Smoothing, Power Transformation, Cyclical Feature Extraction, Unit Economics, Cohort Retention.
* **Granular Scenarios Handled:**
  * **High-Cardinality Handling:** Applying smoothed Target (Mean) Encoding to high-cardinality strings (like postal codes) by blending category means with global averages using smoothing parameters.
  * **Distribution Normalization:** Mitigating extreme skewness in financial distributions using Log, Box-Cox, and Yeo-Johnson power transformations.
  * **Temporal Boundary Resolution:** Applying Sine and Cosine cyclical transformations to hours of the day or months of the year to ensure continuous circular distance metrics without boundary jumps.
  * **Monetization & Retention Modeling:** Calculating Customer Acquisition Cost (CAC), historical versus predictive Customer Lifetime Value (LTV), logo/revenue churn, and period-over-period cohort retention matrices.

---

### Phase 4: Communication & Storytelling (Visualization)
* **Core Nomenclature:** Multi-Plot Faceting, Accessibility Standardization, Responsive GridSpec Layouts, Spatial Choropleth Aggregation, The Pyramid Principle.
* **Granular Scenarios Handled:**
  * **Multi-Variable Comparison:** Building complex panel visualizations using Seaborn `FacetGrid` and `PairGrid` structures to contrast distributions across segments.
  * **Interactive Drill-Down Exploration:** Designing responsive Plotly dashboards with hover tooltips, sunburst hierarchies, and financial waterfall charts for stakeholders.
  * **Geospatial Density Mapping:** Plotting geographic coordinate scatter points and aggregating metrics across regional state polygons using choropleth maps.
  * **Cognitive Load Reduction:** Structuring executive presentations using the Pyramid Principle (conclusion first, supporting evidence second) to bridge technical metrics with business outcomes.

---

### Phase 5: Advanced Intelligence (Unsupervised & Predictive Modeling)
* **Core Nomenclature:** Inertia Minimization, Silhouette Optimization, Orthogonal Projection, Additive Explanations, Stratified K-Fold Cross-Validation.
* **Granular Scenarios Handled:**
  * **Unsupervised Behavioral Segmentation:** Grouping customers into actionable RFM (Recency, Frequency, Monetary) tiers using K-Means inertia minimization, elbow plots, and DBSCAN density-based noise handling.
  * **Dimensionality Compression:** Projecting correlated features onto orthogonal axes via Principal Component Analysis (PCA) to capture maximum variance and reduce visual clutter.
  * **Supervised Predictive Classification & Forecasting:** Training logistic regressions and gradient models while evaluating performance via Precision-Recall curves, F1-scores, and MAPE metrics.
  * **Black-Box Interpretability:** Decomposing complex model predictions into cooperative game theory Shapley values (SHAP) to explain individual predictions to regulatory auditors.

---

### Phase 6: Validation & Causal Impact (Experimentation)
* **Core Nomenclature:** Power Analysis, Minimum Detectable Effect (MDE), Family-Wise Error Rate (FWER), Multi-Armed Bandit Allocation, Difference-in-Differences (DiD).
* **Granular Scenarios Handled:**
  * **Rigorous Experiment Sizing:** Calculating statistical power, significance thresholds ($\alpha$), and sample size durations to prevent underpowered tests.
  * **Multi-Testing Correction:** Applying Bonferroni and False Discovery Rate (FDR) corrections when evaluating multiple secondary guardrail metrics simultaneously.
  * **Adaptive Traffic Routing:** Deploying Multi-Armed Bandit algorithms (such as Thompson Sampling) to dynamically route user traffic toward winning variant arms in real time.
  * **Quasi-Experimental Causal Inference:** Estimating true causal impact in observational settings using Propensity Score Matching (PSM) and Difference-in-Differences (DiD) estimators to eliminate omitted variable bias.

---

## 🛠️ Day 9 Practical Modules & High-Performance Pandas

## 0. 💡 Jupyter Auto-Suggestion & Inline Help Shortcuts
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#0--jupyter-auto-suggestion--inline-help-shortcuts)

| Action | Shortcut / Syntax | Purpose & Behavior |
| :--- | :---: | :--- |
| **Auto-Suggest / Completion** | `Tab` | Triggers drop-down auto-completion for methods, attributes, and DataFrame column names (e.g., `df_sales.str.<Tab>`). |
| **Docstring / Signature Tooltip** | `Shift + Tab` | Pops up function signature & docstring while typing inside parentheses (press 2x for full docstring, 4x to pin to bottom). |
| **Quick Docstring Inspection** | `object?` (e.g. `pd.IndexSlice?`) | Displays object summary, parameters, and docstrings in a pop-up pager. |
| **Source Code Inspection** | `object??` (e.g. `optimize_dataframe_memory??`) | Displays the full Python source code of any user-defined function. |
| **IPython Quick Reference** | `%quickref` | Displays IPython cheatsheet and available magic commands. |

### Built-in Interactive Helper: `suggest_wrangling_help(topic)`
The laboratory notebook includes an interactive auto-suggestion helper function providing instant templates:
```python
suggest_wrangling_help('multiindex')    # Instant syntax templates for hierarchical indexing
suggest_wrangling_help('regex')          # Regex patterns for named groups & extraction
suggest_wrangling_help('pipeline')       # Transform pipeline & groupby transform templates
suggest_wrangling_help('downcasting')    # Memory downcasting decision rules & code snippets
suggest_wrangling_help('query')          # High-performance query syntax & numexpr templates
```

---

## 1. MultiIndex DataFrame and Hierarchical Slicing (North Region Sales)
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#1-multiindex-dataframe-and-hierarchical-slicing-north-region-sales)

### 1.1 Core Mathematical Motivation
Real-world enterprise datasets inherently possess multidimensional relationships (e.g., $\text{Region} \times \text{State} \times \text{Year} \times \text{Quarter}$). Flattening these dimensions into denormalized string columns wastes memory and requires expensive multi-column grouping. Storing them in nested dictionaries loses vectorized array speed.

A **MultiIndex** (Hierarchical Index) models $N$-dimensional data cubes directly within standard 2D Pandas structures:

$$\text{Index Coordinate} = (\text{Region}, \text{State}, \text{Year}, \text{Quarter})$$

### 1.2 Construction: Regional Sales Performance
* **Primary Case Scenario:** Enterprise sales tracking across 4 geographical regions (**North**, **South**, **West**, **East**), featuring **North region sales** across states (**Delhi**, **Punjab**, **UP**).
* **Multi-Tier Metrics:**
  * `Financial`: `Sales_Revenue_Lakhs`, `OpEx_Lakhs`, `Profit_Lakhs`
  * `Operations`: `Units_Sold`, `CSAT_Score`

### 1.3 Hierarchical Slicing: First Example (North Region Sales)
Directly indexing inner levels using tuple slicing like `df_sales.loc[(:, 'Q1')]` causes a Python `SyntaxError`. The standard solution is `pd.IndexSlice`:

```python
idx = pd.IndexSlice

# First Example: Slice outer level directly -> North Region Sales
north_region_sales = df_sales.loc['North']

# Precise Multi-Level Slice via IndexSlice:
# North Region, All States, Year 2026, Quarter 'Q1', Financial Metrics
north_q1_sales = df_sales.loc[
    idx['North', :, 2026, 'Q1'],
    idx['Financial', ['Sales_Revenue_Lakhs', 'Profit_Lakhs']]
]
```

> [!WARNING]
> **⚠️ Interview Trap (MultiIndex):** Slicing inner levels of an unsorted MultiIndex (`df.loc[idx[:, 'Q1'], :]`) raises `UnsortedIndexError`. Always run `df_sales.sort_index(inplace=True)` before slicing with `pd.IndexSlice`.

> [!CAUTION]
> **The Lexicographical Sorting Requirement:** Always run `df_sales.sort_index(inplace=True)` before performing multi-level range slicing (`idx['East':'North', ...]`). Slicing an unsorted MultiIndex will trigger `UnsortedIndexError` or cause silent performance degradation.

### 1.4 Cross-Sectional Indexing with `.xs()`
The `.xs()` method provides an explicit, highly readable API to slice across any arbitrary depth level:
* **Row Cross-Section:** `df_sales.xs(key='Q2', level='Quarter', drop_level=False)`
* **Column Cross-Section:** `df_sales.xs(key='Operations', axis=1, level='Metric_Type')`

---

## 2. Vectorised Strings and Regular Expressions
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#2-vectorised-strings-and-regular-expressions)

### 2.1 The Vectorization Performance Advantage
Standard Python string manipulation on lists or via `.apply(lambda x: ...)` forces the Python virtual machine to iterate through every row as an individual object pointer, incurring severe function call overhead:

$$\text{Loop Overhead} = \mathcal{O}(N \times \text{Interpreter Bytecode Frame Cost})$$

Pandas `.str` accessor methods delegate string evaluations directly to underlying C/Cython implementations, operating over continuous memory blocks while natively propagating missing values (`NaN`) without throwing `TypeError`.

### 2.2 Enterprise Messy String Sanitation
The module cleans enterprise data containing:
1. **Padded Whitespace & Case Inconsistencies:** `Emp_001 `, `finance`
2. **Compound Corporate Email Addresses:** `firstname.lastname+tag@subdomain.org.in`
3. **Multi-Format Contact Phone Numbers:** `+91-98765-43210`, `(022) 2410-1234`, `800.555.0199`
4. **Alphanumeric Project Identifiers:** `PROJ-ENG-2026-X09`

### 2.3 Regular Expression Extraction with Named Capture Groups
Instead of fragile positional indexing, we leverage named capturing groups `(?P<group_name>pattern)`:

```python
email_regex = r'^(?P<username>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$'
extracted_email_parts = df['Email'].str.extract(email_regex)
```

> [!WARNING]
> **⚠️ Interview Trap (Vectorized Regex):** `.str.extract()` requires capturing parentheses `(...)` and extracts only the first match. Use `.str.extractall()` for multiple matches per string. For quick true/false filtering, prefer `.str.contains(pat, regex=True, na=False)`.

---

## 3. Transform Pipeline (HR & IT Salary Analysis)
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#3-transform-pipeline)

### 3.1 Pipeline Design Principles
Enterprise data wrangling must be **declarative**, **reproducible**, and **immutable**. Traditional procedural Pandas scripts mutate state across multiple loose variables, making testing and DAG orchestration difficult.

We leverage method chaining anchored by Pandas `.pipe()`:

$$\text{Raw Dataset} \xrightarrow{\text{Sanitize}} \text{DF}_1 \xrightarrow{\text{Impute}} \text{DF}_2 \xrightarrow{\text{Winsorize}} \text{DF}_3 \xrightarrow{\text{Feature Eng}} \text{Clean Output}$$

### 3.2 Simplified HR and IT Focus & Per-Group Boxplot
To maximize clarity without unnecessary complexity, the pipeline focuses on **HR and IT Salary Distributions**:
* Standardizes department representations to strictly **`HR`** and **`IT`**.
* Handles missing salary records via department-specific median imputation.
* Computes intra-department relative metrics (Group Z-Scores and Percent of Department Median).
* Visualizes the distributions via **comparative per-group boxplots** to clearly contrast pay bands and anomalies.

```python
# Intra-Group Standardized Salary (Group Z-Score)
df['salary_zscore'] = df.groupby('dept')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

> [!WARNING]
> **⚠️ Interview Trap (Transform vs Apply):** `apply()` returns a reduced scalar or aggregated Series when used with aggregation functions, altering the DataFrame's shape. `transform()` **guarantees** $N \to N$ row preservation aligned with the original index, making it essential for broadcast group imputation and group normalization.

---

## 4. Memory Optimisation and Data Type Downcasting
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#4-memory-optimisation-and-data-type-downcasting)

### 4.1 Memory Mechanics of Pandas DataFrames
By default, Pandas allocates conservative 64-bit data types:
* `int64`: 8 bytes per cell ($\pm 9.22 \times 10^{18}$)
* `float64`: 8 bytes per cell (15–17 decimal digits)
* `object`: 8 bytes per cell for memory pointer + external Python string heap allocation (50–80 bytes per string)

Calling `df.info()` or `df.memory_usage()` without `deep=True` only counts the 8-byte pointer references, hiding up to **90%** of actual memory usage!

### 4.2 Integer and Float Downcasting Decision Matrix

| Data Type | Target Sub-Type | Dynamic Range | Memory Savings vs 64-bit |
| :--- | :--- | :--- | :---: |
| **Integer (Unsigned)** | `uint8` | $0 \dots 255$ | **87.5%** |
| **Integer (Signed)** | `int8` | $-128 \dots 127$ | **87.5%** |
| **Integer (Unsigned)** | `uint16` | $0 \dots 65,535$ | **75.0%** |
| **Integer (Signed)** | `int16` | $-32,768 \dots 32,767$ | **75.0%** |
| **Integer (Signed)** | `int32` | $-2.14 \times 10^9 \dots 2.14 \times 10^9$ | **50.0%** |
| **Float** | `float32` | 7 decimal digits (IEEE 754) | **50.0%** |

> [!WARNING]
> **⚠️ Interview Trap (Float16):** Never downcast financial metrics to `float16`. `float16` only supports 3–4 decimal digits of precision, creating catastrophic rounding errors, and lacks hardware SIMD acceleration on most CPUs. Always stop at `float32`.

### 4.3 Categorical Encoding: The Cardinality Rule
Converting string `object` columns to `category` replaces repetitive string allocations with an integer lookup table (dictionary codes + unique categories).

$$\text{Category Memory} = \text{Unique Strings} \times \text{Size} + N_{\text{rows}} \times \text{Code Size (1, 2, or 4 bytes)}$$

* **Cardinality Rule:** Only convert columns where $\frac{\text{Unique Count}}{N_{\text{total}}} < 0.50$ (ideally $< 0.05$). For unique identifier strings (e.g., UUIDs), `category` **increases** memory usage.

---

## 5. High-Performance Query (`df.query` & `pd.eval`)
* **Laboratory Location:** [`Day9/data_wrangling/01_data_wrangling.ipynb`](data_wrangling/01_data_wrangling.ipynb#5-high-performance-query-dfquery--pdeval)

### 5.1 Why Boolean Indexing Creates Memory Bottlenecks
Standard Pandas boolean compound filtering:
```python
filtered = df[(df['A'] > 100) & (df['B'] < 50) & (df['C'] == 'Active')]
```
forces Python to create **3 intermediate boolean Series** in RAM before computing the bitwise AND:
1. `mask1 = df['A'] > 100` (Temporary Series in RAM)
2. `mask2 = df['B'] < 50` (Temporary Series in RAM)
3. `mask3 = mask1 & mask2` (Temporary Series in RAM)
4. `mask4 = df['C'] == 'Active'` (Temporary Series in RAM)
5. `final_mask = mask3 & mask4` (Final Series in RAM)

For datasets with 10M+ rows, these intermediate memory allocations trigger CPU cache misses, RAM thrashing, and out-of-memory (OOM) crashes.

### 5.2 The NumExpr Acceleration Engine
`pd.eval()` and `df.query(engine='numexpr')` parse Python expressions into an Abstract Syntax Tree (AST), compile them to optimized C bytecode, and evaluate operations in **chunked CPU cache (L1/L2)** without allocating temporary full-length arrays.

Furthermore, `NumExpr` automatically leverages **all available CPU cores** for multi-threaded parallel execution.

### 5.3 Syntax Rules for `df.query()`
* **External Python Variables:** Prefix with `@` (e.g., `df.query('salary > @threshold')`).
* **Column Names with Spaces/Symbols:** Wrap in backticks (e.g., `df.query('`Annual Salary ($)` > 100000')`).
* **In-place Column Assignment via `pd.eval`:** `df.eval('Bonus = Salary * 0.15', inplace=True)`.

> [!WARNING]
> **⚠️ Interview Trap (Query Overhead):** `df.query()` has string parsing overhead. On small DataFrames ($< 10,000$ rows), traditional boolean indexing is faster. `df.query()` dominates on large datasets ($> 100,000$ rows).

---

## 6. Summary & Architectural Scorecard

| Technique | Core Advantage | Overhead / Limitation | Best Suited For |
| :--- | :--- | :--- | :--- |
| **MultiIndex (`pd.IndexSlice`)** | Models multidimensional cubes in 2D Pandas; zero redundant strings | Requires lexicographical sorting (`sort_index`) before slicing | Time-series panels, financial cohorts, geographic hierarchies |
| **Vectorized `.str` Regex** | C-vectorized execution; natively propagates `NaN` without crashing | Slightly higher initial regex compile overhead | Mass data sanitization, log parsing, phone/email extraction |
| **Transform Pipelines** | Guarantees strict $N \to N$ row preservation for broadcasting | Slower than simple vectorized arithmetic if using Python lambdas | Group Z-score, group median imputation, standardized KPI metrics |
| **Memory Downcasting** | Reduces RAM footprint by 50%–85%; speeds up cache locality | Risk of integer overflow or precision loss if thresholds are wrong | Big data ingestion, ETL pipelines, preventing VM OOM crashes |
| **`df.query` + `pd.eval`** | Multi-threaded C bytecode via `NumExpr`; avoids intermediate arrays | Expression parsing latency on small tables ($< 10\text{k}$ rows) | Filtering and column math on datasets exceeding 100k rows |

---

## 7. ⚠️ Critical Interview Traps & Viva Hacks (Punchy & Direct)

### ⚠️ Trap 1: The Unsorted MultiIndex Slicing Crash
* **The Trap:** Running `df.loc[idx[:, 'Q1'], :]` on a newly created MultiIndex.
* **Why It Fails:** Raises `UnsortedIndexError`. Pandas requires keys in lexicographical order to perform logarithmic $O(\log N)$ binary search.
* **Viva Rule:** Always call `df.sort_index(inplace=True)` before slicing with `pd.IndexSlice`.

### ⚠️ Trap 2: `transform()` vs `apply()`
* **The Trap:** Using `df.groupby('dept')['salary'].apply(lambda x: x - x.mean())`.
* **Why It Fails:** `apply()` may alter the DataFrame's index or return a reduced dimension Series, causing index mismatch errors during assignment.
* **Viva Rule:** `transform()` strictly guarantees $N \to N$ output aligned with the original index. Always use `transform()` for broadcasting group metrics!

### ⚠️ Trap 3: The `.apply(lambda x: ...)` String Bottleneck
* **The Trap:** Using `.apply(lambda s: s.strip().lower())` or standard Python `re.search()` on string columns.
* **Why It Fails:** Up to $50\times$ slower, creates Python VM interpreter overhead on every row, and crashes on `None`/`np.nan` with `TypeError`.
* **Viva Rule:** Always use compiled `.str` accessor methods (`df['col'].str.strip()`, `.str.extract()`); they natively propagate `NaN` without crashing.

### ⚠️ Trap 4: The Blind `float16` Downcasting Disaster
* **The Trap:** Downcasting `float64` to `float16` to save maximum memory.
* **Why It Fails:** `float16` only has 3–4 decimal digits of precision (causes severe numerical truncation) and lacks hardware SIMD vectorization on most CPUs (runs in slow software emulation).
* **Viva Rule:** Only downcast floats to `float32` (7 decimal digits, full hardware SIMD support).

### ⚠️ Trap 5: The "Categorical Always Saves RAM" Myth
* **The Trap:** Believing `df['col'].astype('category')` always reduces memory.
* **The Reality:** For high-cardinality columns (UUIDs, transaction hashes, unique names where cardinality $> 50\%$), `category` **increases** memory due to dictionary table overhead plus integer codes!
* **Viva Rule:** Only convert to `category` when unique values make up $< 50\%$ (ideally $< 5\%$) of total rows.

### ⚠️ Trap 6: Is `df.query()` Always Faster Than Boolean Indexing?
* **The Trap:** Claiming `df.query()` is always faster than `df[(col1 > x) & (col2 < y)]`.
* **The Reality:** On small DataFrames ($< 10,000$ rows), boolean indexing is faster due to `query()`'s expression parsing/compilation overhead. `query(engine='numexpr')` only wins on large DataFrames ($> 100,000$ rows) where it eliminates temporary intermediate array allocations in RAM.

### ⚠️ Trap 7: The `inplace=True` Fallacy
* **The Trap:** Believing `inplace=True` prevents memory copies and is faster.
* **The Reality:** In almost all Pandas methods (e.g., `dropna`, `reset_index`, `query`), Pandas creates an internal copy anyway and merely reassigns the pointer. `inplace=True` also breaks method chaining pipelines and is deprecated/discouraged in modern Pandas.
* **Viva Rule:** Avoid `inplace=True`; prefer declarative method chaining.

---

### ⚡ Quick-Fire Interview Flashcards
| Interview Question | 1-Line Punchy Answer |
| :--- | :--- |
| **Why use `pd.IndexSlice` over standard slices?** | Standard Python slice `:` is invalid syntax inside tuples for inner MultiIndex levels. |
| **How does `.xs()` differ from `.loc`?** | `.xs()` allows selecting inner levels without specifying outer level wildcards. |
| **What does `expand=True` do in `.str.split()`?** | Returns a multi-column DataFrame instead of a Series of Python lists. |
| **Why is `pipe()` preferred over procedural assignment?** | Enables pure functional method chaining without intermediate mutable global variables. |
| **What engine makes `df.query()` multi-threaded?** | `NumExpr` (evaluates C bytecode in CPU cache chunks). |

---

## 🔬 Day 9 Practical Modules (Part 2: Missing Data, Imputation, Outliers & Entity Resolution)
* **Master Laboratory Location:** [`Day9/data_wrangling/02_missing_malformed_data.ipynb`](data_wrangling/02_missing_malformed_data.ipynb)

---

### 8. Missing Data Taxonomy (MCAR, MAR, MNAR)

Formulated by statistician Donald Rubin (1976), missingness is governed by 3 distinct stochastic processes:

```
┌──────────────┬───────────────────────────────┬──────────────────────────────────┬─────────────────────────────┐
│ Type         │ Mathematical Condition        │ Real-World Scenario              │ Production Pipeline Impact  │
├──────────────┼───────────────────────────────┼──────────────────────────────────┼─────────────────────────────┤
│ **MCAR**     │ P(M | Y_obs, Y_mis) = P(M)    │ Dropped test vial; sensor packet │ Deletion (dropna) causes no │
│              │ (Independent of all features) │ dropped on uniform coin flip.    │ bias; only loses power.     │
├──────────────┼───────────────────────────────┼──────────────────────────────────┼─────────────────────────────┤
│ **MAR**      │ P(M | Y_obs, Y_mis)           │ Younger people rarely report     │ Deletion creates SEVERE     │
│              │ = P(M | Y_obs)                │ income; explained by Age (obs).  │ bias! Imputation required.  │
├──────────────┼───────────────────────────────┼──────────────────────────────────┼─────────────────────────────┤
│ **MNAR**     │ P(M) depends directly         │ Severely depressed patients skip │ Standard imputation fails!  │
│              │ on the unobserved value Y_mis │ survey; millionaires hide wealth.│ Needs Heckman / bounds.     │
└──────────────┴───────────────────────────────┴──────────────────────────────────┴─────────────────────────────┘
```

* **Mathematical Condition for Unbiased Deletion:** Only MCAR satisfies unbiased parameter recovery under listwise deletion (`df.dropna()`). Under MAR, listwise deletion distorts regression slopes $\beta$ and sample means $\mu$.

---

### 9. Advanced Imputation Strategies (KNN, Iterative / MICE, Rolling)

#### 9.1 Why Mean / Median Imputation Fails
* **Variance Deflation:** Replacing missing values with a central constant artificially shrinks sample variance:
  $$\text{Var}(X_{\text{mean\_imp}}) < \text{Var}(X_{\text{true}})$$
* **Covariance Collapse:** Mean imputation adds points aligned parallel to coordinate axes, dragging correlation $r_{X, Y}$ toward zero.

#### 9.2 The Modern Imputation Toolkit

1. **KNN Imputation (`KNNImputer`):**
   * Computes NaN-Euclidean distance: $d(x, y) = \sqrt{\frac{p}{p_{\text{present}}} \sum_{i \in \text{present}} (x_i - y_i)^2}$.
   * Imputes missing coordinates as the distance-weighted average of $K$ nearest geometric neighbors.
   * **Mandatory Prerequisite:** Features must be scaled (e.g. `StandardScaler`) first.
2. **Iterative Imputation / MICE (`IterativeImputer`):**
   * Fits a series of chained round-robin regressions (Bayesian Ridge): each feature is modeled as a function of all remaining features in cyclic iterations.
   * **Core Advantage:** Preserves multivariate covariance matrix $\Sigma$ and collinearities.
3. **Rolling Window Imputation (Sequential / Time-Series):**
   * Uses temporal proximity (`ffill()`, `bfill()`, moving median).
   * **Production Rule:** Never use `bfill()` or centered windows in financial or forecasting models—this introduces **Lookahead Bias** by leaking future observations into past training states!

---

### 10. Outlier Handling via Winsorization & Clipping

#### 10.1 Outlier Taxonomy: Errors vs. True Black Swans
* **Measurement Glitches / Typos:** Sensor reading $999^\circ\text{C}$ or salary entered with extra zero. Must be capped or cleaned.
* **Genuine Extremes:** Billionaire net worth, financial flash crashes, insurance claims. Must NOT be deleted in anomaly/fraud detection models!

#### 10.2 Trimming vs. Clipping vs. Winsorization
* **Trimming:** Drops observations outside $[Q_1 - 1.5 \text{IQR}, Q_3 + 1.5 \text{IQR}]$. Loses sample size $N$ and introduces selection truncation.
* **Clipping (`df['col'].clip(lower, upper)`):** Clamps numerical extremes to hard upper and lower constants.
* **Winsorization (`scipy.stats.mstats.winsorize(limits=[0.05, 0.05])`):**
  * Replaces values below the $5^{\text{th}}$ percentile with $P_{05}$, and above the $95^{\text{th}}$ percentile with $P_{95}$.
  * **Mathematical Properties:** Preserves exact sample size $N$, leaves the **median strictly unchanged**, and bounds variance.

---

### 11. Duplicate Detection & Entity Resolution Basics

#### 11.1 The Deduplication Hierarchy
1. **Exact Row Deduplication:** All columns match $\rightarrow$ `df.drop_duplicates()`.
2. **Subset Key Deduplication:** Unique natural key matches (e.g., Email, PAN) $\rightarrow$ `df.drop_duplicates(subset=['email'])`.
3. **Fuzzy Entity Resolution:** Typographical errors (`"Google"` vs `"Gooogle"`), word inversions (`"Sundar Pichai"` vs `"Pichai, Sundar"`), and abbreviations (`"Apple Inc"` vs `"Apple"`).

#### 11.2 Entity Resolution Pipeline
1. **String Normalization:** Lowercase $\rightarrow$ Strip punctuation $\rightarrow$ Remove corporate suffixes (`inc`, `corp`, `llc`) $\rightarrow$ Token sort.
2. **Similarity Scoring:** SequenceMatcher Gestalt ratio $\frac{2M}{T}$ or Levenshtein edit distance.
3. **Clustering & Canonical ID Assignment:** Connected components graph algorithm groups records above a similarity threshold (e.g. $\ge 0.72$) into unique canonical entity IDs.
4. **The $O(N^2)$ Scalability Trap & The "Blocking" Solution:**
   * Comparing 1M records pairwise requires $\approx 5 \times 10^{11}$ evaluations ($\approx 57$ days!).
   * **Blocking Technique:** Hashes records by a coarse key (e.g., `State + Soundex(Last_Name)`), running fuzzy matching **only within matching blocks**.

---

### 12. ⚠️ Part 2 Interview Traps & Viva Hacks

#### ⚠️ Trap 8: Testing for MNAR in Observational Data
* **The Trap:** Claiming you can run a statistical test to prove data is MNAR.
* **The Reality:** MNAR means missingness depends on the unobserved value itself. Because you never observe the missing values, you cannot mathematically prove MNAR from the dataset alone! It requires domain knowledge or external audit re-sampling.

#### ⚠️ Trap 9: Unscaled KNN Imputation
* **The Trap:** Calling `KNNImputer().fit_transform(df)` directly on raw unscaled tabular features.
* **The Reality:** A feature with large scale (e.g. `Salary` in lakhs) dwarfs features with small scale (e.g. `Age` or `CSAT`). Nearest neighbors will be selected purely based on Salary! Always standardize features with `StandardScaler` first.

#### ⚠️ Trap 10: Lookahead Bias in Time-Series Imputation
* **The Trap:** Using backward fill (`bfill()`) or centered moving averages in financial or predictive forecasting models.
* **The Reality:** `bfill()` leaks future price or sensor information into historical timestamps. In backtests, model accuracy appears unrealistically high, but it catastrophically fails in live forward production. Always use causal trailing windows (`ffill()` or trailing rolling mean).

#### ⚠️ Trap 11: Does Winsorization Alter the Median?
* **The Trap:** Believing Winsorization distorts the central tendency median.
* **The Reality:** As long as symmetric trimming fraction $\alpha < 0.50$ (e.g. 5% top and bottom), the $50^{\text{th}}$ percentile (median) remains **strictly unchanged**!

#### ⚠️ Trap 12: Pairwise Matching on Large Datasets ($O(N^2)$ Complexity)
* **The Trap:** Running pairwise fuzzy matching loops on 500,000 CRM records.
* **The Reality:** $500,000^2 / 2 = 1.25 \times 10^{11}$ comparisons, which crashes the server. Always apply a **Blocking Index** (e.g., Zip Code, First Letter Hash, or LSH) to restrict candidate pairs before scoring.

---

### ⚡ Part 2 Quick-Fire Viva Flashcards
| Interview Question | 1-Line Punchy Answer |
| :--- | :--- |
| **Under which taxonomy is listwise deletion unbiased?** | Strictly MCAR (Missing Completely at Random). |
| **Why is MICE preferred over Mean Imputation?** | Preserves multivariate covariance $\Sigma$ and correlations by modeling inter-feature regression chains. |
| **What is the mathematical definition of MAR?** | $P(M \mid Y_{\text{obs}}, Y_{\text{mis}}) = P(M \mid Y_{\text{obs}})$ (missingness explained entirely by observed features). |
| **When should you NEVER winsorize or clip outliers?** | In fraud detection, cyber-security, and insurance claim models where outliers represent the target signal. |
| **Why must text normalization precede deduplication?** | Ensures case, whitespace, and punctuation variations (`'IBM'` vs `'ibm '`) are unified before exact matching. |
| **How does Blocking speed up entity resolution?** | Filters candidates into coarse buckets, avoiding the global $\mathcal{O}(N^2)$ comparison bottleneck. |

---
**Module Completed:** Day 9 Advanced Data Wrangling, Cleaning & Entity Resolution Suite  
**Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`)

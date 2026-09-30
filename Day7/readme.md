# Day 7: Statistical Measures, Data Population & Bivariate Relationships
> **Programme:** C-DAC PGCP-AI (Post Graduate Certificate Programme in AI)  
> **Course:** Data Analytics  
> **Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`)  
> **Date:** September 30, 2026  

---

## 📌 Day 7 Structure & Learning Modules

```
Day7/
├── 01_statistical_measure/
│   ├── 01_measures_of_central_tendency_updated.ipynb   # Mean, median, mode, geometric, harmonic, trimmed & Winsorized mean
│   ├── 02_measures_of_dispersion_variability_spread.ipynb # Range, IQR, variance (s² vs σ²), std dev, MAD, and CV (%)
│   ├── 03_measures_of_positions.ipynb                  # Percentiles, quartiles, deciles, percentile ranks, Z-scores, modified Z-scores
│   ├── 04_measures_of_shape_and_distribution_geometry.ipynb # Skewness, Kurtosis, Moments, and Log/Power transformations
│   └── 01_statistical_measures.ipynb                   # Integrated end-to-end laboratory notebook
├── 02_data_population/
│   └── 02_data_population.ipynb                       # Multi-modal mixture models, sampling & anomaly injection
├── 03_bivariate_relationship/
│   └── 03_bivariate_relationship.ipynb                 # Covariance, Pearson vs Spearman, and the r≈0 non-linear trap
└── readme.md                                           # Day 7 Master Reference Guide
```

*(Note: Companion files also available under `Day6/02_statistical_measure/`)*

---

## 📖 Module Overviews

### 1. `01_statistical_measure` — Central Tendency, Dispersion & Outlier Handling
* **Location:** [`Day7/01_statistical_measure/01_statistical_measures.ipynb`](01_statistical_measure/01_statistical_measures.ipynb)
* **Topics Covered:**
  * **Central Tendency:**
    * Arithmetic Mean vs. Median (50th percentile)
    * Mode (most frequent observation)
    * Geometric Mean ($\sqrt[n]{\prod x_i}$) & Harmonic Mean ($\frac{n}{\sum 1/x_i}$)
    * **Trimmed Mean:** Trimming extreme $\alpha\%$ from both tails (drops sample size $N$).
    * **Winsorized Mean:** Capping extreme tails at percentiles (e.g., $P_{5\%}$ and $P_{95\%}$) while preserving **100% of sample size ($N$)**.
  * **Dispersion & Spread:**
    * Range ($Max - Min$), Interquartile Range ($IQR = Q_3 - Q_1$).
    * Sample Variance ($s^2$ with Bessel's correction $n-1$) vs. Population Variance ($\sigma^2$ with $N$).
    * Standard Deviation ($s = \sqrt{s^2}$) and Coefficient of Variation ($CV = \frac{s}{\bar{x}} \times 100\%$).
  * **Measures of Position (Relative Standing):**
    * Percentiles ($P_k$) & Empirical CDF (ECDF).
    * Quartiles ($Q_1, Q_2, Q_3$), Deciles ($D_1 \dots D_9$), and Quintiles.
    * Percentile Rank (relative standing of an arbitrary score: $\frac{\text{Count}(<x) + 0.5 \cdot \text{Count}(=x)}{n} \times 100\%$).
    * Standard $Z$-Score ($z = \frac{x - \bar{x}}{s}$) vs. **Modified $Z$-Score** ($M_i = \frac{0.6745(x_i - \tilde{x})}{\text{MAD}}$) to prevent outlier masking.
    * Cross-scale performance standardization.
  * **Measures of Shape & Distribution Geometry:**
    * The 4 Statistical Moments (Mean, Variance, Skewness, Kurtosis).
    * **Skewness:** Symmetrical vs. Right-Skewed ($\text{Mean} > \text{Median}$) vs. Left-Skewed ($\text{Mean} < \text{Median}$).
    * Pearson's median skewness ($Sk_2$), Fisher-Pearson 3rd moment ($g_1$), and Bowley's quartile skewness ($Sk_B$).
    * **Kurtosis:** Tail-heaviness and outlier propensity: Mesokurtic (Normal), Leptokurtic (fat tails / Black Swan risk), Platykurtic (thin tails / flat peak).
    * Full Kurtosis ($\beta_2$) vs. Excess Kurtosis ($\beta_2 - 3$).
    * **Data Transformations:** Logarithmic ($y = \log(x)$) and Box-Cox power transforms for normalizing right-skewed features.
  * **Outlier Detection:**
    * **Tukey's IQR Fences:** $[Q_1 - 1.5 \times IQR, \; Q_3 + 1.5 \times IQR]$.
    * **Z-Score Method:** Observations where $|Z| > 3.0$ standard deviations.
    * **Modified Z-Score Method:** Observations where $|M_i| > 3.5$ based on Median & MAD.

---

### 2. `02_data_population` — Synthetic Population Sampling & Mixture Models
* **Location:** [`Day7/02_data_population/02_data_population.ipynb`](02_data_population/02_data_population.ipynb)
* **Topics Covered:**
  * **Modern NumPy Generator API:** `rng = np.random.default_rng(seed=42)`.
  * **Multi-Distribution Sampling:** Normal, Continuous Uniform, Exponential, Poisson, and Binomial.
  * **Mixture Models (Multi-Modal Populations):**
    * Simulating heterogeneous customer populations (e.g. 70% budget shoppers $\mathcal{N}(35, 8)$ + 30% luxury buyers $\mathcal{N}(120, 20)$).
  * **Anomaly Injection:** Introducing controlled 1% cyber fraud chargebacks ($400 - $600).
  * **Diagnostic Assessment:** Visualizing bimodal shapes via Histograms and Normal Quantile-Quantile (Q-Q) plots.

---

### 3. `03_bivariate_relationship` — Covariance, Pearson vs. Spearman & Non-Linear Traps
* **Location:** [`Day7/03_bivariate_relationship/03_bivariate_relationship.ipynb`](03_bivariate_relationship/03_bivariate_relationship.ipynb)
* **Topics Covered:**
  * **Covariance ($Cov(X, Y)$):**
    $$Cov(X, Y) = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{n - 1}$$
    Measures joint directional linear variability (scale-dependent).
  * **Pearson Correlation Coefficient ($r$):**
    $$r = \frac{Cov(X, Y)}{s_X \cdot s_Y} \in [-1.0, +1.0]$$
    Scale-independent, standardized linear correlation.
  * **Spearman Rank Correlation ($\rho$):**
    Non-parametric correlation evaluated on ranks; captures monotonic non-linear relationships ($Y = e^X$).
  * **The Critical $r \approx 0$ Exam Trap:**
    * Zero correlation ($r = 0$) only indicates lack of **linear** association.
    * Variables can have a perfect deterministic quadratic relationship ($Y = X^2$ centered at 0) where $r \approx 0.0$!
  * **Bivariate OLS Linear Regression:**
    $$\text{Slope } \beta_1 = \frac{Cov(X, Y)}{Var(X)} = r \frac{s_Y}{s_X}, \quad \text{Intercept } \beta_0 = \bar{Y} - \beta_1 \bar{X}, \quad R^2 = r^2$$

---

## ⚡ Mathematical Reference Card

| Measure / Metric | Mathematical Expression | Key Interpretation / Use Case |
| :--- | :---: | :--- |
| **Winsorized Mean** | $\bar{x}_{w,\alpha} = \frac{1}{n} \left( k x_{(k+1)} + \sum x_{(i)} + k x_{(n-k)} \right)$ | Caps top/bottom $\alpha\%$ outliers; keeps full $N$. |
| **Coefficient of Variation** | $CV = \left(\frac{s}{\bar{x}}\right) \times 100\%$ | Unitless volatility comparison across different scales. |
| **Tukey Outlier Fences** | $[Q_1 - 1.5 \times IQR, \quad Q_3 + 1.5 \times IQR]$ | Robust outlier boundary regardless of distribution shape. |
| **Covariance** | $Cov(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n - 1}$ | Sign (+/-) indicates direction of joint association. |
| **Pearson Correlation ($r$)** | $r = \frac{Cov(X, Y)}{s_X s_Y}$ | Linear strength between $-1.0$ (inverse) and $+1.0$ (direct). |
| **Spearman Rank ($\rho$)** | $\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$ | Monotonic relationship (resistant to non-linear distortion). |
| **Standard $Z$-Score** | $z = \frac{x - \bar{x}}{s}$ | Distance from mean in units of standard deviation ($\mu=0, \sigma=1$). |
| **Modified $Z$-Score ($M_i$)** | $M_i = \frac{0.6745(x_i - \tilde{x})}{\text{MAD}}$ | Robust position indicator ($|M_i| > 3.5$ is outlier); immune to masking. |
| **Percentile Rank** | $PR(x) = \frac{\text{Count}(<x) + 0.5 \cdot \text{Count}(=x)}{n} \times 100\%$ | Inverse percentile: percentage of cohort scoring at or below $x$. |
| **Skewness ($g_1$)** | $g_1 = \frac{\frac{1}{n}\sum(x_i - \bar{x})^3}{s^3}$ | Asymmetry: $>0$ right-tail pull ($\bar{x} > \text{Med}$), $<0$ left-tail pull. |
| **Excess Kurtosis ($\gamma_2$)** | $\gamma_2 = \frac{\frac{1}{n}\sum(x_i - \bar{x})^4}{s^4} - 3$ | Tail weight: $>0$ Leptokurtic (fat tails / Black Swans), $<0$ Platykurtic (thin). |



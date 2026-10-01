# Day 7: Statistical Measures (Complete Suite)
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
│   ├── 04_measures_of_shape_and_distribution_geometry.ipynb # Skewness, Kurtosis (3 types), Moments, and Log/Power transformations
│   └── 01_statistical_measures.ipynb                   # Integrated end-to-end laboratory notebook
├── 02_statistical_measure/
│   ├── 01_measures_of_central_tendency_updated.ipynb   # Upstream harmonized central tendency notebook
│   ├── 02_measures_of_dispersion_variability.ipynb     # Upstream harmonized dispersion notebook
│   ├── 03_measures_of_position.ipynb                   # Upstream harmonized position notebook
│   ├── 04_measures_of_shape_and_distribution_geometry.ipynb # Upstream harmonized shape & kurtosis notebook
│   └── readme.md                                       # Comprehensive mathematical theory guide
├── 03_bivariate_relationships/
│   └── 01_covariance_and_pearson_correlation.ipynb     # Upstream initial covariance & Pearson correlation introduction
└── readme.md                                           # Day 7 Master Reference Guide
```

*(Note: Extended bivariate relationship modeling, Spearman rank correlation, and Data Population have been expanded into [`Day8/`](../Day8/readme.md).)*

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



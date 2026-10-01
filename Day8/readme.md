# Day 8: Data Population & Bivariate Relationships
> **Programme:** C-DAC PGCP-AI (Post Graduate Certificate Programme in AI)  
> **Course:** Data Analytics  
> **Author:** abs6187 (`23f2000876@ds.study.iitm.ac.in`)  
> **Date:** October 1, 2026  

---

## 📌 Day 8 Structure & Learning Modules

```
Day8/
├── 01_data_population/
│   └── 01_data_population.ipynb           # Synthetic population sampling, mixture models & anomaly injection
├── 03_bivariate_relationship/
│   └── 03_bivariate_relationship.ipynb     # Covariance, Pearson vs. Spearman, and the r≈0 non-linear trap
└── readme.md                               # Day 8 Master Reference Guide
```

---

## 📖 Module Overviews

### 1. `01_data_population` — Synthetic Population Sampling & Mixture Models
* **Location:** [`Day8/01_data_population/01_data_population.ipynb`](01_data_population/01_data_population.ipynb)
* **Topics Covered:**
  * **Modern NumPy Generator API:** `rng = np.random.default_rng(seed=42)`.
  * **Multi-Distribution Sampling:** Normal, Continuous Uniform, Exponential, Poisson, and Binomial.
  * **Mixture Models (Multi-Modal Populations):**
    * Simulating heterogeneous customer populations (e.g. 70% budget shoppers $\mathcal{N}(35, 8)$ + 30% luxury buyers $\mathcal{N}(120, 20)$).
  * **Anomaly Injection:** Introducing controlled 1% cyber fraud chargebacks ($400 - $600).
  * **Diagnostic Assessment:** Visualizing bimodal shapes via Histograms and Normal Quantile-Quantile (Q-Q) plots.

---

### 2. `03_bivariate_relationship` — Covariance, Pearson vs. Spearman & Non-Linear Traps
* **Location:** [`Day8/03_bivariate_relationship/03_bivariate_relationship.ipynb`](03_bivariate_relationship/03_bivariate_relationship.ipynb)
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
| **Covariance** | $Cov(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n - 1}$ | Sign (+/-) indicates direction of joint association; magnitude is scale-dependent. |
| **Pearson Correlation ($r$)** | $r = \frac{Cov(X, Y)}{s_X s_Y}$ | Linear strength between $-1.0$ (inverse) and $+1.0$ (direct). |
| **Spearman Rank ($\rho$)** | $\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$ | Monotonic relationship (resistant to non-linear distortion and extreme outliers). |
| **OLS Slope ($\beta_1$)** | $\beta_1 = \frac{Cov(X, Y)}{Var(X)} = r \frac{s_Y}{s_X}$ | Rate of change in $Y$ per unit increase in $X$. |
| **OLS Intercept ($\beta_0$)** | $\beta_0 = \bar{Y} - \beta_1 \bar{X}$ | Expected value of $Y$ when $X = 0$. |
| **Coefficient of Determination** | $R^2 = r^2 \in [0, 1]$ | Proportion of variance in $Y$ explained by linear relationship with $X$. |

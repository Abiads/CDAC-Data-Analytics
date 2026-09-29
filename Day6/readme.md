# Day 6: Continuous Probability Distributions — Master Reference & Taxonomy
> **Programme:** C-DAC PGCP-AI (Post Graduate Certificate Programme in AI)  
> **Course:** Data Analytics  
> **Session:** Continuous Random Variables & Probability Distributions

---

## 1. What is a Continuous Probability Distribution?

A **Continuous Random Variable** $X$ can assume any real value within an interval $(a, b) \subseteq \mathbb{R}$. Unlike discrete variables where probabilities are assigned to individual points ($P(X = x)$), for continuous variables:

1. **Point Probability is Zero:** $P(X = x_0) = 0$ for any specific single value $x_0$.
2. **Probability is Area Under the Curve:** The probability that $X$ falls within an interval $[a, b]$ is given by the integral of the **Probability Density Function (PDF)** $f(x)$:
   $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx$$
3. **Fundamental Properties of a Valid PDF:**
   - Non-negativity: $f(x) \ge 0 \quad \forall x \in \text{Support}$
   - Total Area Axiom: $\int_{-\infty}^{\infty} f(x) \, dx = 1$
4. **Cumulative Distribution Function (CDF):**
   $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(u) \, du, \quad \frac{d}{dx} F(x) = f(x)$$
5. **Percentile Point Function (PPF / Quantile / Inverse CDF):**
   $$x_q = F^{-1}(q) \quad \text{such that} \quad P(X \le x_q) = q \in [0, 1]$$

---

## 2. Master Taxonomy & Where Used in Industry / AI

| Family | Distribution | Key Parameters | Support Domain | Mean $\mathbb{E}[X]$ | Variance $\text{Var}(X)$ | 🏢 Where Used: Industry, Business & AI Applications |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Symmetric / Baseline** | **Normal (Gaussian)** | $\mu \in \mathbb{R}, \sigma > 0$ | $(-\infty, \infty)$ | $\mu$ | $\sigma^2$ | **Six Sigma Quality Control (GE, Motorola):** Parts tolerance monitoring ($<3.4$ defects per million at $6\sigma$). OLS regression residuals, Gaussian Naive Bayes classification. |
| | **Standard Normal $\mathcal{Z}$** | $\mu=0, \sigma=1$ | $(-\infty, \infty)$ | $0$ | $1$ | **`StandardScaler()` Feature Normalization:** Z-scores ($|Z| > 3$) for automated financial fraud detection and data cleaning. |
| | **Continuous Uniform** | $a < b$ | $[a, b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | **Hyperparameter Optimization (`RandomizedSearchCV`):** Baseline non-informative prior; random generation for Monte Carlo engines. |
| **Skewed / Lifetime** | **Exponential** | $\lambda > 0$ (rate) or $\beta = 1/\lambda$ | $[0, \infty)$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | **Cloud SRE & Systems Reliability (AWS, Google Cloud):** Modeling Mean Time Between Failures (MTBF); customer service call center queue wait times. |
| | **Gamma** | $k > 0$ (shape), $\theta > 0$ (scale) | $[0, \infty)$ | $k\theta$ | $k\theta^2$ | **Multi-stage Queuing & Insurance Claims:** Aggregate claim payouts; Bayesian conjugate prior for Poisson customer arrival rates. |
| | **Weibull** | $k > 0$ (shape), $\lambda > 0$ (scale) | $[0, \infty)$ | $\lambda \Gamma(1 + 1/k)$ | $\lambda^2 [\Gamma(1+2/k) - \Gamma^2(1+1/k)]$ | **Aerospace & Renewable Energy (Boeing, GE):** Jet engine turbine blade fatigue; bathtub curve failure forecasting (infant mortality $k<1$, aging wear-out $k>1$); wind turbine speeds. |
| | **Log-Normal** | $\mu \in \mathbb{R}, \sigma > 0$ | $(0, \infty)$ | $e^{\mu + \sigma^2/2}$ | $(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$ | **Quant Finance & Tech Platforms (Netflix, Spotify):** Black-Scholes stock options (prices cannot be negative); server response p95/p99 latency; household income distributions. |
| | **Pareto (Power-Law)** | $\alpha > 0$ (shape), $x_m > 0$ (scale) | $[x_m, \infty)$ | $\frac{\alpha x_m}{\alpha - 1}$ ($\alpha > 1$) | $\frac{\alpha x_m^2}{(\alpha-1)^2(\alpha-2)}$ ($\alpha > 2$) | **The 80/20 Rule in Retail (Amazon):** $80\%$ of sales driven by $20\%$ of products; DDoS attack packet traffic volumes; catastrophic natural disaster damage modeling. |
| **Inferential / Sampling** | **Student's t** | $\nu > 0$ (deg. of freedom) | $(-\infty, \infty)$ | $0$ ($\nu > 1$) | $\frac{\nu}{\nu - 2}$ ($\nu > 2$) | **A/B Testing with Small Samples ($n < 30$):** Heavy-tail risk modeling for hedge funds; **t-SNE** non-linear dimensionality reduction and cluster visualization. |
| | **Chi-Square ($\chi^2$)** | $k \in \mathbb{N}^+$ (deg. of freedom) | $[0, \infty)$ | $k$ | $2k$ | **Feature Selection in ML (`SelectKBest(chi2)`):** Testing independence between categorical input features and targets; survey independence contingency testing. |
| | **F-Distribution** | $d_1, d_2 > 0$ (d.o.f.) | $[0, \infty)$ | $\frac{d_2}{d_2 - 2}$ ($d_2 > 2$) | Complex ($d_2 > 4$) | **ANOVA & Linear Regression Diagnostics:** Comparing efficacy across $>2$ clinical drug treatment groups simultaneously; testing overall $R^2$ model significance. |
| **Bounded / Proportional** | **Beta** | $\alpha > 0, \beta > 0$ (shapes) | $[0, 1]$ | $\frac{\alpha}{\alpha + \beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | **AdTech & E-Commerce (Thompson Sampling):** Bounded support $[0, 1]$ for real-time click-through rate (CTR) optimization and Bayesian A/B testing. |
| | **Triangular** | $a < c \le b$ (min, mode, max) | $[a, b]$ | $\frac{a+b+c}{3}$ | $\frac{a^2+b^2+c^2-ab-ac-bc}{18}$ | **Project Risk Simulation (PERT / CPM):** Three-point estimation (Optimistic $a$, Mode $c$, Pessimistic $b$) for construction and defense contract timelines. |
| **Heavy-Tailed / Special** | **Laplace (Double Exp)** | $\mu \in \mathbb{R}, b > 0$ | $(-\infty, \infty)$ | $\mu$ | $2b^2$ | **L1 Lasso Regularization Prior:** Forces non-essential weights to zero. **Differential Privacy (Apple, Google):** Calibrated noise injection for user database privacy. |
| | **Cauchy (Lorentzian)** | $x_0 \in \mathbb{R}, \gamma > 0$ | $(-\infty, \infty)$ | **Undefined** | **Undefined (Infinite)** | **Algorithmic Stress-Testing:** Worst-case scenario testing with undefined variance; resonance absorption profiles in nuclear spectroscopy. |
| | **Logistic** | $\mu \in \mathbb{R}, s > 0$ | $(-\infty, \infty)$ | $\mu$ | $\frac{s^2 \pi^2}{3}$ | **Logistic Regression Link Function:** Sigmoid activation in neural networks; **Elo Rating System** in Chess, FIFA, and competitive esports. |

---

## 3. Implementation Cheat Sheet: NumPy Generator vs. SciPy Stats

| Distribution | Modern NumPy Draw (`rng = np.random.default_rng()`) | SciPy Distribution Object (`from scipy import stats`) |
| :--- | :--- | :--- |
| **Normal** | `rng.normal(loc=mu, scale=sigma, size=N)` | `stats.norm(loc=mu, scale=sigma)` |
| **Uniform** | `rng.uniform(low=a, high=b, size=N)` | `stats.uniform(loc=a, scale=b-a)` |
| **Exponential** | `rng.exponential(scale=1/lam, size=N)` | `stats.expon(scale=1/lam)` |
| **Gamma** | `rng.gamma(shape=k, scale=theta, size=N)` | `stats.gamma(a=k, scale=theta)` |
| **Weibull** | `rng.weibull(a=k, size=N) * lam` | `stats.weibull_min(c=k, scale=lam)` |
| **Log-Normal** | `rng.lognormal(mean=mu, sigma=sigma, size=N)` | `stats.lognorm(s=sigma, scale=np.exp(mu))` |
| **Pareto** | `(rng.pareto(a=alpha, size=N) + 1) * xm` | `stats.pareto(b=alpha, scale=xm)` |
| **Student's t** | `rng.standard_t(df=nu, size=N)` | `stats.t(df=nu)` |
| **Chi-Square** | `rng.chisquare(df=k, size=N)` | `stats.chi2(df=k)` |
| **F-Distribution**| `rng.f(dfnum=d1, dfden=d2, size=N)` | `stats.f(dfn=d1, dfd=d2)` |
| **Beta** | `rng.beta(a=alpha, b=beta, size=N)` | `stats.beta(a=alpha, b=beta)` |
| **Triangular** | `rng.triangular(left=a, mode=c, right=b, size=N)` | `stats.triang(c=(c-a)/(b-a), loc=a, scale=b-a)` |
| **Laplace** | `rng.laplace(loc=mu, scale=b, size=N)` | `stats.laplace(loc=mu, scale=b)` |
| **Cauchy** | `stats.cauchy.rvs(loc=x0, scale=gamma, size=N)` | `stats.cauchy(loc=x0, scale=gamma)` |
| **Logistic** | `rng.logistic(loc=mu, scale=s, size=N)` | `stats.logistic(loc=mu, scale=s)` |

---

## 4. Goodness-of-Fit & Model Selection Diagnostics

When working with empirical datasets in machine learning, selecting the correct continuous distribution requires formal statistical testing:

1. **Kolmogorov-Smirnov (K-S) Test (`scipy.stats.kstest`):**
   - Non-parametric test comparing empirical CDF against theoretical CDF:
     $$D = \sup_x |F_{\text{empirical}}(x) - F_{\text{theoretical}}(x)|$$
   - High $p$-value ($p > 0.05$) indicates no significant difference (distribution fits data well).
2. **Quantile-Quantile (Q-Q) Plot (`scipy.stats.probplot`):**
   - Plots empirical sample quantiles against theoretical quantiles.
   - Points falling along the $45^\circ$ reference diagonal confirm distributional alignment; curvature reveals skewness or tail heaviness.
3. **Information Criteria (AIC / BIC):**
   - Used to penalize over-parameterization when fitting candidate parametric distributions via Maximum Likelihood Estimation (MLE).

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
   - Non-negativity: $f(x) \ge 0 \quad orall x \in 	ext{Support}$
   - Total Area Axiom: $\int_{-\infty}^{\infty} f(x) \, dx = 1$
4. **Cumulative Distribution Function (CDF):**
   $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(u) \, du, \quad rac{d}{dx} F(x) = f(x)$$
5. **Percentile Point Function (PPF / Quantile / Inverse CDF):**
   $$x_q = F^{-1}(q) \quad 	ext{such that} \quad P(X \le x_q) = q \in [0, 1]$$

---

## 2. Master Taxonomy of Continuous Distributions

| Family | Distribution | Key Parameters | Support Domain | Mean $\mathbb{E}[X]$ | Variance $	ext{Var}(X)$ | Primary Data Science / AI Use Case |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Symmetric / Baseline** | **Normal (Gaussian)** | $\mu \in \mathbb{R}, \sigma > 0$ | $(-\infty, \infty)$ | $\mu$ | $\sigma^2$ | Central Limit Theorem, linear regression errors, Kalman filters. |
| | **Standard Normal** | $\mu=0, \sigma=1$ | $(-\infty, \infty)$ | $0$ | $1$ | Z-score standardization, hypothesis testing, weight initialization. |
| | **Continuous Uniform** | $a < b$ | $[a, b]$ | $rac{a+b}{2}$ | $rac{(b-a)^2}{12}$ | Randomized hyperparameter search, baseline non-informative prior. |
| **Skewed / Lifetime** | **Exponential** | $\lambda > 0$ (rate) or $eta = 1/\lambda$ | $[0, \infty)$ | $rac{1}{\lambda}$ | $rac{1}{\lambda^2}$ | Memoryless waiting times, server request intervals, time-to-failure. |
| | **Gamma** | $k > 0$ (shape), $	heta > 0$ (scale) | $[0, \infty)$ | $k	heta$ | $k	heta^2$ | Aggregated queuing delays, rainfall amounts, Bayesian Poisson prior. |
| | **Weibull** | $k > 0$ (shape), $\lambda > 0$ (scale) | $[0, \infty)$ | $\lambda \Gamma(1 + 1/k)$ | $\lambda^2 [\Gamma(1+2/k) - \Gamma^2(1+1/k)]$ | Industrial reliability, component fatigue, wind speed forecasting. |
| | **Log-Normal** | $\mu \in \mathbb{R}, \sigma > 0$ | $(0, \infty)$ | $e^{\mu + \sigma^2/2}$ | $(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$ | Asset prices (Black-Scholes), income distributions, file sizes. |
| | **Pareto (Power-Law)** | $lpha > 0$ (shape), $x_m > 0$ (scale) | $[x_m, \infty)$ | $rac{lpha x_m}{lpha - 1}$ ($lpha > 1$) | $rac{lpha x_m^2}{(lpha-1)^2(lpha-2)}$ ($lpha > 2$) | 80/20 power law, extreme wealth inequality, network packet bursts. |
| **Inferential / Sampling** | **Student's t** | $
u > 0$ (deg. of freedom) | $(-\infty, \infty)$ | $0$ ($
u > 1$) | $rac{
u}{
u - 2}$ ($
u > 2$) | Small-sample inference ($\sigma$ unknown), robust t-regression. |
| | **Chi-Square ($\chi^2$)** | $k \in \mathbb{N}^+$ (deg. of freedom) | $[0, \infty)$ | $k$ | $2k$ | Sample variance distribution, Goodness-of-fit tests, feature selection. |
| | **F-Distribution** | $d_1, d_2 > 0$ (d.o.f.) | $[0, \infty)$ | $rac{d_2}{d_2 - 2}$ ($d_2 > 2$) | Complex ($d_2 > 4$) | ANOVA (Analysis of Variance), Regression overall significance test. |
| **Bounded / Proportional** | **Beta** | $lpha > 0, eta > 0$ (shapes) | $[0, 1]$ | $rac{lpha}{lpha + eta}$ | $rac{lphaeta}{(lpha+eta)^2(lpha+eta+1)}$ | A/B testing conversion rates, CTR modeling, Bayesian Binomial prior. |
| | **Triangular** | $a < c \le b$ (min, mode, max) | $[a, b]$ | $rac{a+b+c}{3}$ | $rac{a^2+b^2+c^2-ab-ac-bc}{18}$ | Project risk estimation (PERT/CPM), simulation with sparse data. |
| **Heavy-Tailed / Special** | **Laplace (Double Exp)** | $\mu \in \mathbb{R}, b > 0$ | $(-\infty, \infty)$ | $\mu$ | $2b^2$ | L1 Regularization (Lasso prior), robust noise, differential privacy. |
| | **Cauchy (Lorentzian)** | $x_0 \in \mathbb{R}, \gamma > 0$ | $(-\infty, \infty)$ | **Undefined** | **Undefined (Infinite)** | Stress-testing algorithms, pathological heavy tails, resonance physics. |
| | **Logistic** | $\mu \in \mathbb{R}, s > 0$ | $(-\infty, \infty)$ | $\mu$ | $rac{s^2 \pi^2}{3}$ | Logistic regression link function, neural network sigmoid activation. |

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
     $$D = \sup_x |F_{	ext{empirical}}(x) - F_{	ext{theoretical}}(x)|$$
   - High $p$-value ($p > 0.05$) indicates no significant difference (distribution fits data well).
2. **Quantile-Quantile (Q-Q) Plot (`scipy.stats.probplot`):**
   - Plots empirical sample quantiles against theoretical quantiles.
   - Points falling along the $45^\circ$ reference diagonal confirm distributional alignment; curvature reveals skewness or tail heaviness.
3. **Information Criteria (AIC / BIC):**
   - Used to penalize over-parameterization when fitting candidate parametric distributions via Maximum Likelihood Estimation (MLE).

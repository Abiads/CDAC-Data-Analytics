"""
Concepts used in this example:
1. Descriptive Statistics: Computing Mean, Trimmed Mean, Median, Bessel-corrected Variance/Std, IQR, and Outlier detection via Tukey Fences.
2. Distribution Moments: Evaluating 3rd moment (Skewness) and 4th moment (Excess Kurtosis) using scipy.stats.
3. Probability Distributions: Continuous Z-score cumulative probabilities (norm.cdf) and discrete Binomial probabilities (binom.pmf).
4. Parametric Hypothesis Testing: Two-sample independent t-test (ttest_ind) and One-Way ANOVA (f_oneway).
5. Non-Parametric Independence Testing: Contingency tables and Pearson's Chi-Square Test (chi2_contingency).
6. Time Series Foundations: Rolling window smoothing using Simple Moving Average (SMA).
7. Statistical Data Visualization: Multi-panel plots illustrating distributions, hypothesis tests, and time series smoothing via Matplotlib & Seaborn.
8. Comprehensive Distribution Gallery: Visual graphs, PMF/PDF functions, and parameters for all 12 key distributions (Binomial, Poisson, Geometric, Bernoulli, Normal, Student's t, Exponential, Log-Normal, Uniform, Chi-Square, F-Distribution, and Central Limit Theorem).
"""

import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def print_section(title: str):
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


# -------------------------------------------------------------------------
# 1. Descriptive Statistics, Dispersion & Moments
# -------------------------------------------------------------------------
print_section("1. DESCRIPTIVE STATISTICS & MOMENT SHAPE ANALYSIS")

np.random.seed(42)  # To reproduce the same random numbers
spending = np.array([25.0, 32.5, 45.0, 28.0, 35.0, 110.0, 42.0, 38.5, 29.0, 52.0])

mean_val = np.mean(spending)
trimmed_mean = stats.trim_mean(spending, 0.1)  # Trim top & bottom 10%
median_val = np.median(spending)
# Bessel's Correction:
# Why ddof=1? Sample variance around sample mean (x̄) systematically underestimates
# the true population spread (around μ). Dividing by (N - 1) instead of N inflates
# the value back up to make it an UNBIASED estimator: E[s²] = σ².
std_pop = np.std(spending, ddof=0)    # Population formula (divide by N)
std_val = np.std(spending, ddof=1)    # Sample formula with Bessel's correction (divide by N - 1)
q1, q3 = np.percentile(spending, [25, 75])
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

skew_val = stats.skew(spending)
kurt_val = stats.kurtosis(spending)  # Fisher excess kurtosis (Gaussian = 0)

print(f"Sample Mean             : ${mean_val:.2f}")
print(f"Trimmed Mean (10%)      : ${trimmed_mean:.2f}")
print(f"Sample Median           : ${median_val:.2f}")
print(f"Population Std Dev (σ)  : ${std_pop:.2f} (Biased: divide by N={len(spending)})")
print(f"Sample Std Dev (s)      : ${std_val:.2f} (Bessel's correction: divide by N-1={len(spending)-1})")
print(f"Interquartile Range(IQR): ${iqr:.2f} (Q1: ${q1:.2f}, Q3: ${q3:.2f})")
print(f"Tukey Outlier Fences    : [${lower_fence:.2f}, ${upper_fence:.2f}]")
outliers = spending[(spending < lower_fence) | (spending > upper_fence)]
print(f"Identified Outliers     : {outliers}")
print(f"Skewness (3rd Moment)   : {skew_val:.3f} (Right-skewed, Mean > Median)")
print(f"Excess Kurtosis (4th)   : {kurt_val:.3f} (Leptokurtic / Heavy-tailed)")


# -------------------------------------------------------------------------
# 2. Probability Distributions & Standardization
# -------------------------------------------------------------------------
print_section("2. PROBABILITY DISTRIBUTIONS & Z-SCORES")

# Continuous Standard Normal Distribution
mu, sigma = 50.0, 10.0
raw_score = 65.0
z_score = (raw_score - mu) / sigma
prob_greater = 1.0 - stats.norm.cdf(z_score)
print(f"Population Mean = {mu}, Std Dev = {sigma}")
print(f"Raw Score = {raw_score} -> Standardized Z-Score = {z_score:.2f}")
print(f"Probability of scoring > {raw_score}: {prob_greater:.4f} ({prob_greater*100:.2f}%)")

# Discrete Binomial Distribution: 10 trials, conversion rate p = 0.20
# Probability of observing exactly 3 conversions: P(X = 3)
p_3_conversions = stats.binom.pmf(k=3, n=10, p=0.2)
print(f"\nBinomial P(X = 3 | n = 10, p = 0.20): {p_3_conversions:.4f} ({p_3_conversions*100:.2f}%)")


# -------------------------------------------------------------------------
# 3. Inferential Hypothesis Testing
# -------------------------------------------------------------------------
print_section("3. INFERENTIAL HYPOTHESIS TESTING (A/B, ANOVA, CHI-SQUARE)")

# A. Two-Sample Independent t-Test (A/B Test: Page A vs Page B)
page_a = np.array([12.5, 14.2, 11.8, 13.0, 12.9, 14.5, 13.2])
page_b = np.array([15.1, 16.5, 14.8, 17.2, 15.9, 16.0, 15.5])

t_stat, p_val_t = stats.ttest_ind(page_a, page_b)
print(f"Two-Sample t-Test : t-statistic = {t_stat:.3f}, p-value = {p_val_t:.5f}")
if p_val_t < 0.05:
    print("Decision: Reject H0 (p < 0.05)! Significant performance difference.")
else:
    print("Decision: Fail to reject H0.")

# B. One-Way ANOVA (Compare 3 Marketing Acquisition Channels)
channel_email = [22, 25, 24, 26, 23]
channel_social = [30, 28, 32, 29, 31]
channel_search = [18, 19, 21, 20, 17]

f_stat, p_val_anova = stats.f_oneway(channel_email, channel_social, channel_search)
print(f"\nOne-Way ANOVA     : F-statistic = {f_stat:.3f}, p-value = {p_val_anova:.5e}")
if p_val_anova < 0.05:
    print("Decision: Reject H0 (p < 0.05)! Group means differ across marketing channels.")

# C. Chi-Square Test of Independence (Gender vs. Subscription Tier)
contingency_table = np.array([
    [40, 60],  # Male: [Basic, Premium]
    [65, 35]   # Female: [Basic, Premium]
])
chi2, p_val_chi, dof, expected = stats.chi2_contingency(contingency_table)
print(f"\nChi-Square (χ²)   : chi2 = {chi2:.3f}, p-value = {p_val_chi:.5f}, dof = {dof}")
if p_val_chi < 0.05:
    print("Decision: Reject H0 (p < 0.05)! Subscription tier is dependent on gender.")


# -------------------------------------------------------------------------
# 4. Time Series Foundations: Rolling Window Moving Average
# -------------------------------------------------------------------------
print_section("4. TIME SERIES ANALYSIS: SIMPLE MOVING AVERAGE (SMA)")

daily_sales = pd.Series([100, 112, 105, 120, 135, 128, 140, 152, 148, 160])
sma_3 = daily_sales.rolling(window=3).mean()

ts_df = pd.DataFrame({'Sales': daily_sales, '3_Day_SMA': sma_3})
print(ts_df)
print("-" * 65)


# -------------------------------------------------------------------------
# 5. Statistical Data Visualization (Matplotlib & Seaborn)
# -------------------------------------------------------------------------
print_section("5. GENERATING STATISTICAL VISUALIZATIONS")

# Styling configurations
sns.set_theme(style="whitegrid", palette="muted")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Subplot 1: Boxplot & Outlier Detection with Mean & Trimmed Mean
ax1 = axes[0, 0]
sns.boxplot(x=spending, ax=ax1, color="#9ecae1", width=0.4, showmeans=False)
sns.stripplot(x=spending, ax=ax1, color="#08519c", size=8, jitter=0.1, alpha=0.8)

# Vertical annotation lines
ax1.axvline(mean_val, color="#de2d26", linestyle="--", linewidth=2, label=f"Mean: ${mean_val:.1f}")
ax1.axvline(trimmed_mean, color="#756bb1", linestyle=":", linewidth=2, label=f"Trimmed Mean (10%): ${trimmed_mean:.1f}")
ax1.axvline(median_val, color="#31a354", linestyle="-", linewidth=2, label=f"Median: ${median_val:.1f}")
ax1.axvline(upper_fence, color="#fd8d3c", linestyle="-.", linewidth=1.5, label=f"Upper Fence: ${upper_fence:.1f}")

ax1.set_title("1. Spending Distribution & Outlier Detection (Tukey)", fontsize=12, fontweight="bold")
ax1.set_xlabel("Spending Amount ($)", fontsize=11)
ax1.legend(loc="upper right", frameon=True)

# Subplot 2: Normal Distribution PDF with Z-Score Shading
ax2 = axes[0, 1]
x_axis = np.linspace(mu - 3.5 * sigma, mu + 3.5 * sigma, 500)
y_pdf = stats.norm.pdf(x_axis, mu, sigma)
ax2.plot(x_axis, y_pdf, color="#2b83ba", linewidth=2.5, label=r"Normal PDF ($\mu=50, \sigma=10$)")

# Shade tail area for raw_score >= 65 (Z >= 1.5)
x_tail = x_axis[x_axis >= raw_score]
y_tail = stats.norm.pdf(x_tail, mu, sigma)
ax2.fill_between(x_tail, y_tail, color="#d7191c", alpha=0.4, label=f"P(X ≥ 65) = {prob_greater*100:.2f}% (Z=1.5)")
ax2.axvline(raw_score, color="#d7191c", linestyle="--", linewidth=1.5)
ax2.set_title("2. Normal Distribution & Upper Tail Probability", fontsize=12, fontweight="bold")
ax2.set_xlabel("Score", fontsize=11)
ax2.set_ylabel("Probability Density", fontsize=11)
ax2.legend(loc="upper left", frameon=True)

# Subplot 3: Two-Sample t-Test (A/B Test Comparison)
ax3 = axes[1, 0]
ab_data = pd.DataFrame({
    'Conversion_Rate': np.concatenate([page_a, page_b]),
    'Variant': ['Page A (Control)'] * len(page_a) + ['Page B (Treatment)'] * len(page_b)
})
sns.boxplot(data=ab_data, x='Variant', y='Conversion_Rate', hue='Variant', ax=ax3, palette=["#a1d99b", "#41ab5d"], legend=False)
sns.stripplot(data=ab_data, x='Variant', y='Conversion_Rate', ax=ax3, color="black", size=6, jitter=0.1)
ax3.set_title(f"3. A/B Testing: Two-Sample t-Test (p = {p_val_t:.5f})", fontsize=12, fontweight="bold")
ax3.set_ylabel("Conversion Rate (%)", fontsize=11)
ax3.set_xlabel("")

# Subplot 4: Time Series 3-Day Moving Average Smoothing
ax4 = axes[1, 1]
days = np.arange(1, len(daily_sales) + 1)
ax4.plot(days, daily_sales, marker="o", color="#252525", linewidth=1.8, label="Actual Daily Sales")
ax4.plot(days, sma_3, marker="s", color="#e6550d", linewidth=2.5, linestyle="--", label="3-Day SMA Trend")
ax4.set_title("4. Time Series Trend: 3-Day Simple Moving Average", fontsize=12, fontweight="bold")
ax4.set_xlabel("Day Index", fontsize=11)
ax4.set_ylabel("Sales Units", fontsize=11)
ax4.set_xticks(days)
ax4.legend(loc="upper left", frameon=True)

plt.tight_layout()

# Save output diagram in Day3 directory
script_dir = os.path.dirname(os.path.abspath(__file__))
plot_filename = os.path.join(script_dir, "statistics_visualization.png")
plt.savefig(plot_filename, dpi=200)
print(f"Generated and saved statistical diagram to '{plot_filename}'.")
print("-" * 65)

# Uncomment to display interactively if running in GUI window:
# plt.show()


# -------------------------------------------------------------------------
# 6. Comprehensive Probability Distributions Gallery (All Key Examples)
# -------------------------------------------------------------------------
print_section("6. ALL PROBABILITY DISTRIBUTION GRAPHS & EXAMPLES")

dist_summary_data = [
    ("Binomial", "Discrete", "n (trials), p (success prob)", "P(X=k) = nCk * p^k * (1-p)^(n-k)", "E[X]=np, Var=np(1-p)", "A/B test conversions, quality defect rates"),
    ("Poisson", "Discrete", "lambda (average arrival rate)", "P(X=k) = (lambda^k * e^-lambda)/k!", "E[X]=lambda, Var=lambda", "Website traffic/hour, server requests, call arrivals"),
    ("Geometric", "Discrete", "p (success probability)", "P(X=k) = (1-p)^(k-1) * p", "E[X]=1/p, Var=(1-p)/p^2", "Sales calls until 1st deal, attempts until password cracked"),
    ("Bernoulli", "Discrete", "p (success probability)", "P(X=1)=p, P(X=0)=1-p", "E[X]=p, Var=p(1-p)", "Single coin toss, binary customer churn flag"),
    ("Normal (Gaussian)", "Continuous", "mu (mean), sigma (std dev)", "f(x) = 1/(sigma*sqrt(2pi)) * e^(-(x-mu)^2/(2sigma^2))", "E[X]=mu, Var=sigma^2", "Human heights, test scores, measurement noise"),
    ("Student's t", "Continuous", "df (degrees of freedom)", "Heavy-tailed bell curve -> Normal as df -> inf", "E[X]=0 (df>1), Var=df/(df-2)", "Hypothesis testing on small sample sizes (n < 30)"),
    ("Exponential", "Continuous", "lambda (rate parameter)", "f(x) = lambda * e^(-lambda*x)  [x >= 0]", "E[X]=1/lambda, Var=1/lambda^2", "Server response latency, equipment time-to-failure"),
    ("Uniform (Cont.)", "Continuous", "a (min), b (max)", "f(x) = 1/(b-a)  [a <= x <= b]", "E[X]=(a+b)/2, Var=(b-a)^2/12", "Randomized waiting time, Monte Carlo input draws"),
    ("Log-Normal", "Continuous", "mu, sigma of ln(X)", "f(x) = 1/(x*sigma*sqrt(2pi)) * e^...", "Right-skewed, strictly positive", "Income/wealth distribution, stock prices, asset returns"),
    ("Chi-Square (χ²)", "Continuous", "k (degrees of freedom)", "Sum of k independent squared standard normal variates", "E[X]=k, Var=2k", "Goodness-of-fit tests, categorical independence tests"),
    ("F-Distribution", "Continuous", "df1, df2 (degrees of freedom)", "Ratio of two scaled chi-square variates (variance ratio)", "E[X]=df2/(df2-2) (df2>2)", "One-Way ANOVA, regression overall significance test"),
    ("Sampling Dist (CLT)", "Continuous", "n (sample size), mu, sigma", "X_bar ~ N(mu, sigma/sqrt(n)) as n -> inf", "E[X_bar]=mu, SE=sigma/sqrt(n)", "Inferential statistics, confidence intervals, survey polls"),
]

df_dist_ref = pd.DataFrame(
    dist_summary_data,
    columns=["Distribution", "Type", "Parameters", "Formula (PMF / PDF)", "Moments (Mean & Var)", "Real-World Data Analytics Application"]
)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_dist_ref.to_string(index=False))
print("-" * 65)


def plot_all_distribution_graphs(save_path: str = None):
    """
    Renders and exports a 12-panel comprehensive visualization matrix
    of all essential probability distributions used in Data Analytics.
    """
    fig, axes = plt.subplots(4, 3, figsize=(18, 18))
    fig.suptitle("Comprehensive Probability Distributions Showcase (Discrete & Continuous)", 
                 fontsize=17, fontweight="bold", y=0.995)

    # 1. Binomial Distribution (Discrete)
    ax1 = axes[0, 0]
    n_trials = 20
    k_vals = np.arange(0, n_trials + 1)
    for p, col, lbl in [(0.2, "#2b83ba", "p=0.2 (Right-skewed)"), 
                        (0.5, "#41ab5d", "p=0.5 (Symmetric)"), 
                        (0.8, "#d7191c", "p=0.8 (Left-skewed)")]:
        pmf = stats.binom.pmf(k_vals, n=n_trials, p=p)
        ax1.plot(k_vals, pmf, marker='o', linestyle='-', color=col, label=lbl, alpha=0.85)
        ax1.vlines(k_vals, 0, pmf, color=col, alpha=0.25)
    ax1.set_title(r"1. Binomial: $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ ($n=20$)", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Number of Successes (k)")
    ax1.set_ylabel("Probability Mass P(X=k)")
    ax1.legend(frameon=True, fontsize=8.5)

    # 2. Poisson Distribution (Discrete)
    ax2 = axes[0, 1]
    k_pois = np.arange(0, 22)
    for lam, col in [(1.5, "#756bb1"), (5.0, "#e6550d"), (10.0, "#3182bd")]:
        pmf = stats.poisson.pmf(k_pois, mu=lam)
        ax2.plot(k_pois, pmf, marker='s', linestyle='-', color=col, label=rf"$\lambda={lam}$ ($E[X]={lam}, Var={lam}$)")
        ax2.vlines(k_pois, 0, pmf, color=col, alpha=0.25)
    ax2.set_title(r"2. Poisson: $P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}$", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Event Count (k)")
    ax2.set_ylabel("Probability Mass P(X=k)")
    ax2.legend(frameon=True, fontsize=8.5)

    # 3. Geometric Distribution (Discrete)
    ax3 = axes[0, 2]
    k_geom = np.arange(1, 15)
    for p, col in [(0.2, "#fdae61"), (0.4, "#2c7bb6"), (0.7, "#d7191c")]:
        pmf = stats.geom.pmf(k_geom, p=p)
        ax3.plot(k_geom, pmf, marker='^', linestyle='-', color=col, label=rf"$p={p}$ ($E[X]={1/p:.1f}$ trials)")
        ax3.vlines(k_geom, 0, pmf, color=col, alpha=0.25)
    ax3.set_title(r"3. Geometric: $P(X=k)=(1-p)^{k-1}p$", fontsize=11, fontweight="bold")
    ax3.set_xlabel("Trials until 1st Success (k)")
    ax3.set_ylabel("Probability Mass P(X=k)")
    ax3.legend(frameon=True, fontsize=8.5)

    # 4. Normal (Gaussian) Distribution (Continuous)
    ax4 = axes[1, 0]
    x_norm = np.linspace(-6, 6, 500)
    for s, col in [(0.5, "#d7191c"), (1.0, "#2c7bb6"), (2.0, "#41ab5d")]:
        pdf = stats.norm.pdf(x_norm, loc=0, scale=s)
        ax4.plot(x_norm, pdf, color=col, linewidth=2, label=rf"$\mu=0, \sigma={s}$")
    ax4.fill_between(x_norm[(x_norm >= -1) & (x_norm <= 1)], 
                    stats.norm.pdf(x_norm[(x_norm >= -1) & (x_norm <= 1)], 0, 1), 
                    color="#2c7bb6", alpha=0.2, label=r"68.3% within $\pm 1\sigma$")
    ax4.set_title(r"4. Normal: $f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$", fontsize=11, fontweight="bold")
    ax4.set_xlabel("x")
    ax4.set_ylabel("Probability Density f(x)")
    ax4.legend(frameon=True, fontsize=8.5)

    # 5. Student's t-Distribution (Continuous)
    ax5 = axes[1, 1]
    x_t = np.linspace(-4.5, 4.5, 500)
    ax5.plot(x_t, stats.norm.pdf(x_t), color="black", linestyle="--", linewidth=2, label=r"Standard Normal $\mathcal{N}(0,1)$")
    for df, col in [(1, "#e41a1c"), (3, "#377eb8"), (10, "#4daf4a"), (30, "#984ea3")]:
        pdf = stats.t.pdf(x_t, df=df)
        ax5.plot(x_t, pdf, color=col, linewidth=1.8, label=rf"$df={df}$ (Heavy tails)")
    ax5.set_title(r"5. Student's t: Converges to Normal as $df \to \infty$", fontsize=11, fontweight="bold")
    ax5.set_xlabel("t-statistic")
    ax5.set_ylabel("Probability Density")
    ax5.legend(frameon=True, fontsize=8.5)

    # 6. Exponential Distribution (Continuous)
    ax6 = axes[1, 2]
    x_exp = np.linspace(0, 6, 500)
    for lam, col in [(0.5, "#2b83ba"), (1.0, "#41ab5d"), (2.0, "#d7191c")]:
        pdf = stats.expon.pdf(x_exp, scale=1.0/lam)
        ax6.plot(x_exp, pdf, color=col, linewidth=2, label=rf"$\lambda={lam}$ (Rate), Mean={1/lam:.1f}")
        ax6.fill_between(x_exp, pdf, color=col, alpha=0.08)
    ax6.set_title(r"6. Exponential: $f(x)=\lambda e^{-\lambda x}$ ($x \geq 0$)", fontsize=11, fontweight="bold")
    ax6.set_xlabel("Time / Distance between arrivals (x)")
    ax6.set_ylabel("Probability Density f(x)")
    ax6.legend(frameon=True, fontsize=8.5)

    # 7. Log-Normal Distribution (Continuous)
    ax7 = axes[2, 0]
    x_log = np.linspace(0.01, 5, 500)
    for s, col in [(0.25, "#31a354"), (0.5, "#3182bd"), (1.0, "#de2d26")]:
        pdf = stats.lognorm.pdf(x_log, s=s, scale=np.exp(0))
        ax7.plot(x_log, pdf, color=col, linewidth=2, label=rf"$\mu=0, \sigma={s}$")
    ax7.set_title(r"7. Log-Normal: $\ln(X) \sim \mathcal{N}(\mu, \sigma^2)$ (Income/Wealth)", fontsize=11, fontweight="bold")
    ax7.set_xlabel("x (Strictly positive, right-skewed)")
    ax7.set_ylabel("Probability Density f(x)")
    ax7.legend(frameon=True, fontsize=8.5)

    # 8. Continuous Uniform Distribution (Continuous)
    ax8 = axes[2, 1]
    a, b = 2.0, 8.0
    x_uni = np.linspace(0, 10, 500)
    pdf_uni = stats.uniform.pdf(x_uni, loc=a, scale=b - a)
    ax8.plot(x_uni, pdf_uni, color="#756bb1", linewidth=2.5, label=rf"$\mathcal{{U}}(a={a}, b={b})$")
    ax8.fill_between(x_uni, pdf_uni, color="#bcbddc", alpha=0.35)
    ax8.axvline(a, color="#636363", linestyle=":")
    ax8.axvline(b, color="#636363", linestyle=":")
    ax8.text((a+b)/2, 1/(b-a)*0.5, rf"$f(x) = \frac{{1}}{{b-a}} = {1/(b-a):.2f}$" + "\n" + rf"Mean = {(a+b)/2:.1f}", 
            ha="center", fontsize=9.5, bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.8))
    ax8.set_title(r"8. Uniform (Continuous): $f(x)=\frac{1}{b-a}$ ($a \leq x \leq b$)", fontsize=11, fontweight="bold")
    ax8.set_xlabel("x")
    ax8.set_ylabel("Probability Density f(x)")
    ax8.set_ylim(0, 0.25)
    ax8.legend(frameon=True, fontsize=8.5)

    # 9. Chi-Square Distribution (Continuous)
    ax9 = axes[2, 2]
    x_chi = np.linspace(0.01, 20, 500)
    for df_val, col in [(2, "#e41a1c"), (4, "#ff7f00"), (7, "#377eb8"), (12, "#4daf4a")]:
        pdf = stats.chi2.pdf(x_chi, df=df_val)
        ax9.plot(x_chi, pdf, color=col, linewidth=2, label=rf"$k={df_val}$ (df)")
    ax9.set_title(r"9. Chi-Square ($\chi^2$): Sum of $k$ Squared Normals", fontsize=11, fontweight="bold")
    ax9.set_xlabel(r"$\chi^2$ statistic")
    ax9.set_ylabel("Probability Density f(x)")
    ax9.set_ylim(0, 0.55)
    ax9.legend(frameon=True, fontsize=8.5)

    # 10. F-Distribution (Continuous)
    ax10 = axes[3, 0]
    x_f = np.linspace(0.01, 4.5, 500)
    for dfn, dfd, col in [(2, 10, "#e41a1c"), (5, 10, "#377eb8"), (10, 20, "#4daf4a")]:
        pdf = stats.f.pdf(x_f, dfn=dfn, dfd=dfd)
        ax10.plot(x_f, pdf, color=col, linewidth=2, label=rf"$df_1={dfn}, df_2={dfd}$")
    ax10.set_title(r"10. F-Distribution: Ratio of Variances (ANOVA)", fontsize=11, fontweight="bold")
    ax10.set_xlabel("F-ratio")
    ax10.set_ylabel("Probability Density f(x)")
    ax10.set_ylim(0, 0.9)
    ax10.legend(frameon=True, fontsize=8.5)

    # 11. Bernoulli & Discrete Uniform (Discrete)
    ax11 = axes[3, 1]
    dice_outcomes = np.arange(1, 7)
    dice_probs = np.full(6, 1/6)
    ax11.bar(dice_outcomes, dice_probs, color="#80b1d3", edgecolor="#386cb0", width=0.45, label="Discrete Uniform (Fair Die: P=1/6)")
    # Bernoulli marker overlay
    coin_outcomes = np.array([0, 1])
    coin_probs = np.array([0.35, 0.65])
    ax11.step(coin_outcomes, coin_probs, where='mid', color="#e41a1c", linewidth=2.2, linestyle="--", label="Bernoulli Trial (p=0.65)")
    ax11.set_title(r"11. Discrete Uniform (Die) & Bernoulli ($p=0.65$)", fontsize=11, fontweight="bold")
    ax11.set_xlabel("Discrete Outcomes")
    ax11.set_ylabel("Probability P(X=x)")
    ax11.set_ylim(0, 0.75)
    ax11.legend(frameon=True, fontsize=8.5)

    # 12. Central Limit Theorem Convergence (Sampling Distribution)
    ax12 = axes[3, 2]
    np.random.seed(42)
    pop = stats.expon.rvs(scale=2.0, size=50000)  # Heavily skewed population
    for n, col in [(2, "#e41a1c"), (10, "#ff7f00"), (30, "#4daf4a"), (100, "#377eb8")]:
        sample_means = [np.mean(np.random.choice(pop, size=n)) for _ in range(2000)]
        sns.kdeplot(sample_means, ax=ax12, color=col, linewidth=2, label=rf"Sample size $n={n}$")
    ax12.set_title(r"12. CLT: Skewed Population $\to$ Normal $\bar{X}$", fontsize=11, fontweight="bold")
    ax12.set_xlabel(r"Sample Mean ($\bar{x}$)")
    ax12.set_ylabel("Density")
    ax12.legend(frameon=True, fontsize=8.5)

    plt.tight_layout(rect=[0, 0.01, 1, 0.98])
    
    if save_path:
        plt.savefig(save_path, dpi=200)
        print(f"Generated and saved all 12 distribution graphs to '{save_path}'.")
    
    # Uncomment to display interactively if running in GUI window:
    # plt.show()


# Generate and save the comprehensive 12-distribution visualizer
all_dist_filename = os.path.join(script_dir, "all_distribution_graphs.png")
plot_all_distribution_graphs(save_path=all_dist_filename)
print("=" * 65)


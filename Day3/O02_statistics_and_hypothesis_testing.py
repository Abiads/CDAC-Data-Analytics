"""
Concepts used in this example:
1. Descriptive Statistics: Computing Mean, Trimmed Mean, Median, Bessel-corrected Variance/Std, IQR, and Outlier detection via Tukey Fences.
2. Distribution Moments: Evaluating 3rd moment (Skewness) and 4th moment (Excess Kurtosis) using scipy.stats.
3. Probability Distributions: Continuous Z-score cumulative probabilities (norm.cdf) and discrete Binomial probabilities (binom.pmf).
4. Parametric Hypothesis Testing: Two-sample independent t-test (ttest_ind) and One-Way ANOVA (f_oneway).
5. Non-Parametric Independence Testing: Contingency tables and Pearson's Chi-Square Test (chi2_contingency).
6. Time Series Foundations: Rolling window smoothing using Simple Moving Average (SMA).
7. Statistical Data Visualization: Multi-panel plots illustrating distributions, hypothesis tests, and time series smoothing via Matplotlib & Seaborn.
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
std_val = np.std(spending, ddof=1)  # ddof=1 for sample standard deviation (n-1)
q1, q3 = np.percentile(spending, [25, 75])
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

skew_val = stats.skew(spending)
kurt_val = stats.kurtosis(spending)  # Fisher excess kurtosis (Gaussian = 0)

print(f"Sample Mean             : ${mean_val:.2f}")
print(f"Trimmed Mean (10%)      : ${trimmed_mean:.2f}")
print(f"Sample Median           : ${median_val:.2f}")
print(f"Sample Std Dev (s)      : ${std_val:.2f} (Bessel's correction n-1)")
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

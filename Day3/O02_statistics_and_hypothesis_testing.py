"""
Concepts used in this example:
1. Descriptive Statistics: Computing Mean, Median, Bessel-corrected Variance/Std, IQR, and Outlier detection via Tukey Fences.
2. Distribution Moments: Evaluating 3rd moment (Skewness) and 4th moment (Excess Kurtosis) using scipy.stats.
3. Probability Distributions: Continuous Z-score cumulative probabilities (norm.cdf) and discrete Binomial probabilities (binom.pmf).
4. Parametric Hypothesis Testing: Two-sample independent t-test (ttest_ind) and One-Way ANOVA (f_oneway).
5. Non-Parametric Independence Testing: Contingency tables and Pearson's Chi-Square Test (chi2_contingency).
6. Time Series Foundations: Rolling window smoothing using Simple Moving Average (SMA).
"""

import numpy as np
import pandas as pd
from scipy import stats


def print_section(title: str):
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


# -------------------------------------------------------------------------
# 1. Descriptive Statistics, Dispersion & Moments
# -------------------------------------------------------------------------
print_section("1. DESCRIPTIVE STATISTICS & MOMENT SHAPE ANALYSIS")

np.random.seed(42) # to reproduce the same random numbers
spending = np.array([25.0, 32.5, 45.0, 28.0, 35.0, 110.0, 42.0, 38.5, 29.0, 52.0])
# loc means
mean_val = np.mean(spending)
median_val = np.median(spending)
std_val = np.std(spending, ddof=1)  # ddof=1 for sample standard deviation (n-1)
q1, q3 = np.percentile(spending, [25, 75])
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

skew_val = stats.skew(spending)
kurt_val = stats.kurtosis(spending)  # Fisher excess kurtosis (Gaussian = 0)

print(f"Sample Mean             : ${mean_val:.2f}")
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

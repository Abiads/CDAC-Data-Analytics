# C-DAC PGCP-AI: Data Analytics Master Notes & Study Guide
> **Batch:** August 2026 | **Centre:** ACTS, Pune  
> **Course Duration:** 120 Hours (50 Theory + 50 Lab + 20 Self-Learning)  
> **Evaluation Scheme:** Theory Exam (40%) + Lab Exam (40%) + Internal Assessment (20%)

Welcome to the comprehensive, easy-to-understand **Data Analytics Nano Notes & Study System**. This repository contains deep-dive session notes, real-world intuitive analogies, runnable Python code labs, and batch-generated technical diagram infographics.

---

## 📚 Module Navigation & Syllabus Mapping

| Module | Title | Sessions Included | Hours | Key Topics | Study Link |
| :---: | :--- | :---: | :---: | :--- | :---: |
| ⚡ | **Exam Mnemonics & Rote-Learning** | All Sessions | — | Mnemonics (LINE, p-value, Skewness), Formula Recall Cards, Exam Traps | [Read Mnemonics Guide](00_rote_learning_and_mnemonics.md) |
| **01** | **Foundations & Exploratory Data Analysis** | Sessions 1 – 4 | 28 Hrs | Business Analytics Lifecycle, Nature of Data, Colab/Jupyter Setup, EDA, Seaborn Visuals | [Read Module 1](01_foundations_and_eda.md) |
| **02** | **Statistical Methods & Probability Foundations** | Sessions 5 – 12 | 40 Hrs | Central Tendency, Dispersion, Outliers (IQR/Z-Score), Bayes' Theorem, CLT, Distributions, Z-Test, Chi-Square | [Read Module 2](02_statistics_and_probability.md) |
| **03** | **Predictive & Prescriptive Analytics** | Sessions 13 – 20 | 32 Hrs | Predictive Modeling, Information Gain, Decision Trees, OLS Regression, Forecasting, Monte Carlo, Linear Optimization | [Read Module 3](03_predictive_and_prescriptive_analytics.md) |
| **04** | **Model Evaluation, Advanced Analytics & Power BI** | Sessions 21 – 25 | 20 Hrs | Overfitting, Stratified K-Fold, Confusion Matrix, ROC-AUC, PCA / Factor Analysis, Power BI Architecture & DAX | [Read Module 4](04_evaluation_advanced_analytics_powerbi.md) |

---

## 🖼️ Visual Infographics Gallery

All infographics have been generated in high resolution with modern visual design aesthetics:

| Infographic Concept | Preview / Reference | Description & Key Focus |
| :--- | :---: | :--- |
| **Exam Mnemonics & Tricks** | [Mnemonics Cheatsheet](images/mnemonics_exam_tricks.jpg) | "LINE" regression, "p is low, H0 must go", Skewness tail rule, Type I vs II |
| **Master Formulas Card** | [Formulas Memory Card](images/formulas_rote_card.jpg) | Variance (n-1), Tukey IQR Fences, Bayes' Theorem, CLT SE, Entropy, F1, R² |
| **Exam Traps & Hacks** | [Traps & Hacks Card](images/exam_traps_and_hacks.jpg) | r=0 non-linear trap, Accuracy trap in imbalance, Power BI Column vs Measure |
| **Data Analytics Life Cycle** | [Lifecycle Diagram](images/lifecycle_infographic.jpg) | 6-Stage workflow: Discovery ➔ Prep ➔ Model Plan ➔ Build ➔ QA ➔ Deployment |
| **Probability Distributions & CLT** | [Distributions Diagram](images/probability_distributions.jpg) | Comparison of Normal, Binomial, Poisson + Central Limit Theorem convergence |
| **Decision Trees & Segmentation** | [Decision Tree Diagram](images/decision_trees_segmentation.jpg) | 2D Space partitioning, Information Gain, Tree induction, and IF-THEN rules |
| **Classifier Evaluation Matrix** | [Evaluation Matrix](images/classifier_evaluation_matrix.jpg) | Confusion Matrix (TP, FP, TN, FN), Precision, Recall, F1, ROC-AUC curve |
| **Power BI Architecture & ETL** | [Power BI Pipeline](images/powerbi_pipeline_architecture.jpg) | Data Sources ➔ Power Query ETL ➔ Star Schema Modeling & DAX ➔ Reports |

---

## ⚡ Master "Nano" Cheat-Sheet (High-Yield Formulas)

### 1. Descriptive Statistics
- **Sample Variance:** $s^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}$
- **Coefficient of Variation:** $CV = \frac{s}{\bar{x}} \times 100\%$
- **Tukey Outlier Fences:** $[Q_1 - 1.5 \times \text{IQR}, \quad Q_3 + 1.5 \times \text{IQR}]$

### 2. Probability & Inference
- **Bayes' Theorem:** $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$
- **Central Limit Theorem Standard Error:** $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$
- **One-Sample Z-Statistic:** $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$
- **Chi-Square Statistic:** $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$

### 3. Machine Learning & Predictive Modeling
- **Entropy:** $H(S) = -\sum_{i=1}^c p_i \log_2(p_i)$
- **Gini Impurity:** $Gini(S) = 1 - \sum_{i=1}^c p_i^2$
- **Information Gain:** $IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$
- **Coefficient of Determination ($R^2$):** $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$

### 4. Classification Metrics
- **Accuracy:** $\frac{TP + TN}{TP + TN + FP + FN}$
- **Precision:** $\frac{TP}{TP + FP}$
- **Recall (Sensitivity):** $\frac{TP}{TP + FN}$
- **Specificity:** $\frac{TN}{TN + FP}$
- **F1-Score:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

---

## 🛠️ Recommended Lab Practical Workflow
When appearing for the C-DAC practical lab exam:
1. **Always start with dataset inspection:**
   ```python
   df.info()
   df.describe()
   df.isnull().sum()
   ```
2. **Clean before modeling:** Impute missing values with median/mode; handle outliers with IQR or log transformations.
3. **Partition properly:** Never train and test on the same data; always use `train_test_split(..., stratify=y)`.
4. **Select appropriate metric:** Use F1-Score or ROC-AUC for imbalanced data, not raw Accuracy.
5. **Interpret business impact:** Connect statistical results back to business decisions.

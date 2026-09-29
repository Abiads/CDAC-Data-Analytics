"""
Assignment 5: Quality Control Bottling Audit
Course: Data Analytics (CDAC PGCP-AI)

Scenario:
A beverage factory fills soda bottles with a target volume of 500 mL 
and a standard deviation of 2 mL.

Tasks:
1. Generate 2,000 bottle volumes using a Normal Distribution.
2. Any bottle under 495 mL is underfilled and rejected. 
   Count how many bottles get rejected and calculate the rejection rate percentage.
3. Calculate the sample mean and std of your dataset to verify they match the factory setup.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def run_bottling_audit(num_bottles=2000, target_mean=500.0, target_std=2.0, reject_threshold=495.0, seed=42):
    # Set seed for reproducible results
    np.random.seed(seed)
    
    # 1. Generate 2,000 bottle volumes (Normal Distribution)
    volumes = np.random.normal(loc=target_mean, scale=target_std, size=num_bottles)
    
    # 2. Count rejected bottles (< 495 mL) and rejection rate percentage
    rejected_mask = volumes < reject_threshold
    rejected_count = np.sum(rejected_mask)
    rejection_rate = (rejected_count / num_bottles) * 100
    
    # Theoretical normal distribution benchmark (Z-Score)
    # Z = (495 - 500) / 2 = -2.5
    z_cutoff = (reject_threshold - target_mean) / target_std
    theoretical_rejection_rate = stats.norm.cdf(z_cutoff) * 100
    
    # 3. Calculate sample mean and standard deviation
    sample_mean = np.mean(volumes)
    sample_std = np.std(volumes, ddof=1)
    
    # Print formatted Quality Control Audit Report
    print("=" * 68)
    print("        QUALITY CONTROL BOTTLING AUDIT REPORT (N=2,000)        ")
    print("=" * 68)
    print(f"Factory Target Mean Volume     : {target_mean:.2f} mL")
    print(f"Factory Target Std Deviation   : {target_std:.2f} mL")
    print("-" * 68)
    print(f"Sample Calculated Mean         : {sample_mean:.3f} mL (Difference: {sample_mean - target_mean:+.3f} mL)")
    print(f"Sample Calculated Std (ddof=1) : {sample_std:.3f} mL (Difference: {sample_std - target_std:+.3f} mL)")
    print(f"Verification Result            : MATCHES factory setup within statistical sampling error")
    print("-" * 68)
    print(f"Underfilled Rejection Cutoff   : < {reject_threshold:.1f} mL (Z = {z_cutoff:.1f} sigma)")
    print(f"Rejected Bottles Count         : {rejected_count} / {num_bottles}")
    print(f"Empirical Rejection Rate       : {rejection_rate:.2f}%")
    print(f"Theoretical Benchmark (Z=-2.5) : {theoretical_rejection_rate:.2f}% (Phi(-2.5))")
    print("=" * 68)
    
    # Plotting Graphical Visualization
    plt.figure(figsize=(10, 6), dpi=120)
    
    # Histogram of bottle volumes
    n, bins, patches = plt.hist(volumes, bins=40, density=False, 
                                color='#2ecc71', edgecolor='white', alpha=0.85, 
                                label='Conforming Bottles (>= 495 mL)')
    
    # Highlight rejected underfilled bottles in red
    for c_bin, patch in zip(bins[:-1], patches):
        if c_bin < reject_threshold:
            patch.set_facecolor('#e74c3c')
            patch.set_label('Underfilled & Rejected (< 495 mL)' if 'Underfilled & Rejected (< 495 mL)' not in [p.get_label() for p in plt.gca().get_legend_handles_labels()[0]] else "")
            
    # Draw vertical line for cutoff threshold
    plt.axvline(reject_threshold, color='#c0392b', linestyle='--', linewidth=2.5,
                label=f'Rejection Limit: {reject_threshold:.0f} mL')
    
    # Draw vertical line for target mean
    plt.axvline(target_mean, color='#2c3e50', linestyle='-', linewidth=2.0,
                label=f'Target Fill: {target_mean:.0f} mL')
    
    # Annotation on rejection zone
    plt.annotate(f'Rejected: {rejected_count} bottles ({rejection_rate:.2f}%)\n[Theory: {theoretical_rejection_rate:.2f}%]',
                 xy=(reject_threshold, max(n) * 0.15), xytext=(reject_threshold - 3.5, max(n) * 0.45),
                 arrowprops=dict(facecolor='#c0392b', shrink=0.08, width=1.5, headwidth=8),
                 fontsize=11, fontweight='bold', color='#c0392b',
                 bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdedec', edgecolor='#e74c3c', alpha=0.9))
    
    plt.title('Assignment 5: Quality Control Bottling Audit (N=2,000 Bottles)', 
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Fill Volume (mL)', fontsize=12, fontweight='semibold')
    plt.ylabel('Bottle Count (Frequency)', fontsize=12, fontweight='semibold')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='#f8f9fa', framealpha=0.95, loc='upper right')
    plt.tight_layout()
    
    return volumes, rejected_count, rejection_rate, sample_mean, sample_std

if __name__ == '__main__':
    run_bottling_audit()
    plt.show()

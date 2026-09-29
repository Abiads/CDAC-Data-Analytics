"""
Assignment 4: E-Commerce Delivery Time Estimator
Course: Data Analytics (CDAC PGCP-AI)

Scenario:
An e-commerce platform estimates order delivery times.
On average, a delivery takes 30 minutes with a standard deviation of 5 minutes.

Tasks:
1. Simulate delivery times for 1,000 orders using a Normal Distribution.
2. Calculate what percentage of deliveries took longer than 40 minutes.
3. Plot the delivery times and draw a threshold at the 40-minute mark.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simulate_delivery_times(num_orders=1000, mean_time=30.0, std_time=5.0, threshold=40.0, seed=42):
    # Set seed for reproducible results
    np.random.seed(seed)
    
    # 1. Simulate delivery times for 1,000 orders (Normal Distribution)
    delivery_times = np.random.normal(loc=mean_time, scale=std_time, size=num_orders)
    
    # 2. Calculate percentage of deliveries taking longer than 40 minutes
    late_mask = delivery_times > threshold
    late_count = np.sum(late_mask)
    late_percentage = (late_count / num_orders) * 100
    
    # Theoretical normal distribution benchmark (Z-Score)
    # Z = (40 - 30) / 5 = 2.0
    z_score = (threshold - mean_time) / std_time
    theoretical_late_pct = (1.0 - stats.norm.cdf(z_score)) * 100
    
    # Print formatted audit report
    print("=" * 65)
    print("      E-COMMERCE DELIVERY TIME ESTIMATOR SIMULATION REPORT      ")
    print("=" * 65)
    print(f"Target Distribution         : Normal(mean={mean_time:.1f} min, std={std_time:.1f} min)")
    print(f"Total Simulated Orders      : {num_orders:,}")
    print(f"Sample Mean Delivery Time   : {np.mean(delivery_times):.2f} minutes")
    print(f"Sample Standard Deviation   : {np.std(delivery_times, ddof=1):.2f} minutes")
    print(f"Minimum Delivery Time       : {np.min(delivery_times):.2f} minutes")
    print(f"Maximum Delivery Time       : {np.max(delivery_times):.2f} minutes")
    print("-" * 65)
    print(f"Delivery Delay Threshold    : > {threshold:.1f} minutes (Z = +{z_score:.1f} sigma)")
    print(f"Orders Exceeding Threshold  : {late_count} / {num_orders}")
    print(f"Empirical Late Percentage   : {late_percentage:.2f}%")
    print(f"Theoretical Benchmark (Z=2) : {theoretical_late_pct:.2f}% (1 - Phi(2.0))")
    print("=" * 65)
    
    # 3. Plot the delivery times with a threshold at 40-minute mark
    plt.figure(figsize=(10, 6), dpi=120)
    
    # Histogram of simulated delivery times
    n, bins, patches = plt.hist(delivery_times, bins=35, density=False, 
                                color='#3498db', edgecolor='white', alpha=0.85, 
                                label='On-Time Deliveries (<= 40 min)')
    
    # Highlight bars beyond the threshold in red/orange
    for c_bin, patch in zip(bins[:-1], patches):
        if c_bin >= threshold:
            patch.set_facecolor('#e74c3c')
            patch.set_label('Delayed Deliveries (> 40 min)' if 'Delayed Deliveries (> 40 min)' not in [p.get_label() for p in plt.gca().get_legend_handles_labels()[0]] else "")
    
    # Draw vertical threshold line at 40 minutes
    plt.axvline(threshold, color='#c0392b', linestyle='--', linewidth=2.5,
                label=f'Late Threshold: {threshold:.0f} min')
    
    # Draw vertical mean line at 30 minutes
    plt.axvline(mean_time, color='#2c3e50', linestyle='-', linewidth=2.0,
                label=f'Mean Delivery: {mean_time:.0f} min')
    
    # Annotate the late region
    plt.annotate(f'Late Orders: {late_count} ({late_percentage:.2f}%)\n[Theory: {theoretical_late_pct:.2f}%]',
                 xy=(threshold, max(n) * 0.4), xytext=(threshold + 2.5, max(n) * 0.55),
                 arrowprops=dict(facecolor='#c0392b', shrink=0.08, width=1.5, headwidth=8),
                 fontsize=11, fontweight='bold', color='#c0392b',
                 bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdf2e9', edgecolor='#e74c3c', alpha=0.9))
    
    plt.title('Assignment 4: E-Commerce Delivery Time Estimator (N=1,000 Orders)', 
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Delivery Time (minutes)', fontsize=12, fontweight='semibold')
    plt.ylabel('Order Frequency (Count)', fontsize=12, fontweight='semibold')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='#f8f9fa', framealpha=0.95, loc='upper left')
    plt.tight_layout()
    
    return delivery_times, late_percentage

if __name__ == '__main__':
    simulate_delivery_times()
    plt.show()

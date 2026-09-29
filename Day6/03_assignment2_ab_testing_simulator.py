# ==============================================================================
# ASSIGNMENT 2: E-COMMERCE WEB ANALYTICS A/B TESTING SIMULATOR
# Course: Data Analytics (CDAC PGCP-AI)
#
# Task:
# 1. Simulate 1000 incoming website visitors.
# 2. Assign a random float between 0.0 and 1.0 (and 0.0 to 1.9).
# 3. If value < 0.5: Assign to Design A, Otherwise: Assign to Design B.
# 4. Print the percentage of visitors assigned to each design.
# ==============================================================================

import numpy as np

def run_ab_test_simulation(n_visitors=1000, high_bound=1.0, threshold=0.5, seed=42):
    """
    Simulates A/B testing visitor allocation.
    """
    np.random.seed(seed)
    
    # 1. Generate random floats for each visitor
    random_values = np.random.uniform(low=0.0, high=high_bound, size=n_visitors)
    
    # 2. Assign to Design A if < threshold, otherwise Design B
    design_a_mask = random_values < threshold
    count_a = np.sum(design_a_mask)
    count_b = n_visitors - count_a
    
    # 3. Calculate percentages
    pct_a = (count_a / n_visitors) * 100
    pct_b = (count_b / n_visitors) * 100
    
    return {
        'n_visitors': n_visitors,
        'high_bound': high_bound,
        'threshold': threshold,
        'count_a': count_a,
        'count_b': count_b,
        'pct_a': pct_a,
        'pct_b': pct_b,
        'values': random_values,
        'design_a_mask': design_a_mask
    }

def print_results(res):
    print("=" * 65)
    print(f"   A/B TESTING SIMULATION RESULTS (Random Range: [0.0, {res['high_bound']}])")
    print("=" * 65)
    print(f"Total Incoming Visitors Simulated : {res['n_visitors']}")
    print(f"Assignment Rule                   : If random_val < {res['threshold']} -> Design A, else Design B")
    print("-" * 65)
    print(f"Design A (Control) Visitors       : {res['count_a']} ({res['pct_a']:.2f}%)")
    print(f"Design B (Variant) Visitors       : {res['count_b']} ({res['pct_b']:.2f}%)")
    print("=" * 65)
    
    # Expected Theoretical Probabilities
    expected_p_a = (min(res['threshold'], res['high_bound']) / res['high_bound']) * 100
    expected_p_b = 100.0 - expected_p_a
    print(f"Theoretical Expected Split        : Design A: {expected_p_a:.2f}% | Design B: {expected_p_b:.2f}%")
    print()

if __name__ == '__main__':
    # Case 1: Standard 50/50 A/B Test split (Random float between 0.0 and 1.0)
    print("--- CASE 1: STANDARD 50/50 A/B TEST (Range: 0.0 to 1.0) ---")
    results_std = run_ab_test_simulation(n_visitors=1000, high_bound=1.0, threshold=0.5, seed=42)
    print_results(results_std)

    # Case 2: Exact range as typed in prompt (Random float between 0.0 and 1.9)
    print("--- CASE 2: PROMPT TYPED RANGE (Range: 0.0 to 1.9) ---")
    results_prompt = run_ab_test_simulation(n_visitors=1000, high_bound=1.9, threshold=0.5, seed=42)
    print_results(results_prompt)

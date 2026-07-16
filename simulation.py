import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])

T = 5000
N_RUNS = 30
np.random.seed(42)

alpha_min = 0.01
theta = 0.20          # Slightly adjusted
delta = 0.09
alpha_init = 0.10

def run_simulation(use_adaptive=True, fixed_alpha=None):
    p_true = np.zeros(T)
    p_hat = np.zeros(T)
    alpha = np.zeros(T)
    tracking_error = np.zeros(T)

    p_true[0] = p_hat[0] = 0.5
    alpha[0] = alpha_init if use_adaptive else fixed_alpha

    high_plasticity_steps = 0
    smoothed_error = 0

    for t in range(1, T):
        drift = np.random.normal(0, 0.004)
        if np.random.rand() < 0.045:
            drift += np.random.choice([-0.40, 0.40])
        p_true[t] = np.clip(p_true[t-1] + drift, 0.03, 0.97)

    for t in range(T-1):
        o_t = np.random.binomial(1, p_true[t])
        error = np.abs(p_hat[t] - o_t)
        eta = np.random.normal(0, 0.007)
        current_alpha = alpha[t] if use_adaptive else fixed_alpha

        p_hat[t+1] = (1 - current_alpha) * p_hat[t] + current_alpha * o_t + eta
        p_hat[t+1] = np.clip(p_hat[t+1], 0.0, 1.0)

        tracking_error[t] = np.abs(p_true[t] - p_hat[t])

        if use_adaptive:
            smoothed_error = 0.9 * smoothed_error + 0.1 * error

            if smoothed_error > theta:
                scale = 1 + delta * (smoothed_error / theta)
                alpha[t+1] = min(1.0, alpha[t] * scale)
            else:
                alpha[t+1] = max(alpha_min, alpha[t] * (1 - delta * 0.4))

            if alpha[t] > 0.25:
                high_plasticity_steps += 1
        else:
            alpha[t+1] = fixed_alpha

    return np.mean(tracking_error), high_plasticity_steps / T

# Run simulations
results = {}
results['Adaptive'] = [run_simulation(use_adaptive=True) for _ in range(N_RUNS)]

for fa in [0.05, 0.10, 0.20]:
    results[f'Fixed {fa}'] = [run_simulation(use_adaptive=False, fixed_alpha=fa) for _ in range(N_RUNS)]

print("=== Final Comparison ===")
for name, res in results.items():
    errors = [r[0] for r in res]
    print(f"{name:12}: {np.mean(errors):.4f} ± {np.std(errors):.4f}")

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))
labels = list(results.keys())
data = [[r[0] for r in results[name]] for name in labels]

axs[0].boxplot(data, tick_labels=labels)
axs[0].set_title('Tracking Error Comparison')
axs[0].set_ylabel('Mean Tracking Error')
axs[0].tick_params(axis='x', rotation=15)
axs[0].grid(True, alpha=0.3)

plasticity = [r[1] for r in results['Adaptive']]
axs[1].hist(plasticity, bins=12, color='#2ca02c', alpha=0.75, edgecolor='black')
axs[1].set_title('Time in High-Plasticity Regime (Adaptive)')

plt.tight_layout()
plt.savefig('ras_toy_comparison.pdf', bbox_inches='tight')
plt.savefig('ras_toy_comparison.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: ras_toy_comparison.pdf")

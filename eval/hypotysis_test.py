from scipy.stats import binom_test

# Number of times prompt engineering is better
successes = 20
# Total number of samples
n = 25
# Perform binomial test (two-sided)
p_value = binom_test(successes, n, p=0.5, alternative='greater')

print(f"P-value: {p_value}")


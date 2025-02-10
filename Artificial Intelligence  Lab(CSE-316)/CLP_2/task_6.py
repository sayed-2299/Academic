import numpy as np

random_values = np.random.random(100)
normalized_values = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))

print("normalized_value",normalized_values)
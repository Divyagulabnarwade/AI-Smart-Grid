import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

voltage = np.random.normal(230, 5, rows)
frequency = np.random.normal(50, 0.2, rows)
current = np.random.normal(10, 2, rows)
power_factor = np.random.uniform(0.8, 1.0, rows)

# Introduce anomalies
voltage[:20] = np.random.normal(180, 10, 20)
frequency[:20] = np.random.normal(48, 0.5, 20)

df = pd.DataFrame({
    "Voltage": voltage,
    "Frequency": frequency,
    "Current": current,
    "PowerFactor": power_factor
})

df.to_csv("data/grid_data.csv", index=False)

print("Grid sensor dataset created successfully!")
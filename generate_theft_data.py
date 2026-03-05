import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = {
    "AvgConsumption": np.random.uniform(100, 500, rows),
    "PeakOffPeakRatio": np.random.uniform(0.5, 2.0, rows),
    "MonthlyVariance": np.random.uniform(10, 100, rows),
}

df = pd.DataFrame(data)

# Create theft label
df["Theft"] = (
    (df["PeakOffPeakRatio"] > 1.7) |
    (df["MonthlyVariance"] < 20)
).astype(int)

df.to_csv("data/theft_data.csv", index=False)

print("Theft dataset created successfully!")
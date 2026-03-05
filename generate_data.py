import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = {
    "GHI": np.random.uniform(200, 1000, rows),
    "Temperature": np.random.uniform(20, 45, rows),
    "WindSpeed": np.random.uniform(1, 10, rows),
    "Humidity": np.random.uniform(20, 90, rows)
}

df = pd.DataFrame(data)

df["SolarOutput"] = (
    0.005 * df["GHI"]
    - 0.01 * df["Temperature"]
    + 0.02 * df["WindSpeed"]
    - 0.002 * df["Humidity"]
    + np.random.normal(0, 0.2, rows)
)

df.to_csv("data/solar_data.csv", index=False)

print("Dataset created successfully!")
import pandas as pd
import numpy as np

np.random.seed(42)

hours = 24 * 60  # 60 days of hourly data
date_range = pd.date_range(start="2025-01-01", periods=hours, freq="H")

base_load = 500

load = (
    base_load
    + 100 * np.sin(np.linspace(0, 20*np.pi, hours))   # daily pattern
    + 50 * np.random.randn(hours)                    # randomness
)

df = pd.DataFrame({
    "Datetime": date_range,
    "Load": load
})

df.to_csv("data/load_data.csv", index=False)

print("Load dataset created successfully!")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/solar_data.csv")

# Features and Target
X = df[["GHI", "Temperature", "WindSpeed", "Humidity"]]
y = df["SolarOutput"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/solar_model.pkl")

print("Model trained and saved successfully!")
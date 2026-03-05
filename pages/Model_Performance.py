import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()
import pandas as pd
import joblib
from sklearn.metrics import r2_score, accuracy_score

st.set_page_config(page_title="Model Performance", layout="wide")

st.title("📊 AI Model Performance Dashboard")

st.divider()

# =========================
# ☀ SOLAR MODEL PERFORMANCE
# =========================

st.subheader("☀ Solar Forecast Model")

solar_df = pd.read_csv("data/solar_data.csv")
solar_model = joblib.load("models/solar_model.pkl")

X_solar = solar_df[["GHI", "Temperature", "WindSpeed", "Humidity"]]
y_solar = solar_df["SolarOutput"]

solar_predictions = solar_model.predict(X_solar)

r2 = r2_score(y_solar, solar_predictions)

st.write(f"Solar Model Accuracy (R² Score): {round(r2, 2)}")

if r2 > 0.8:
    st.success("Solar prediction model performance is excellent.")
elif r2 > 0.5:
    st.warning("Solar prediction model performance is moderate.")
else:
    st.error("Solar prediction model needs improvement.")

st.divider()

# =========================
# 🔍 THEFT MODEL PERFORMANCE
# =========================

st.subheader("🔍 Theft Detection Model")

theft_df = pd.read_csv("data/theft_data.csv")
theft_model = joblib.load("models/theft_model.pkl")

X_theft = theft_df[["AvgConsumption", "PeakOffPeakRatio", "MonthlyVariance"]]
y_theft = theft_df["Theft"]

theft_predictions = theft_model.predict(X_theft)

accuracy = accuracy_score(y_theft, theft_predictions)

st.write(f"Theft Detection Accuracy: {round(accuracy, 2)}")

if accuracy > 0.85:
    st.success("Theft detection model is highly accurate.")
elif accuracy > 0.6:
    st.warning("Theft detection model is moderately accurate.")
else:
    st.error("Theft detection model needs improvement.")
import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Load Forecasting", layout="wide")

st.title("⚡ Load Forecasting")
st.markdown("### Time-Series Load Prediction (Hyderabad Grid Simulation)")

st.divider()

# Load dataset
import os
df = pd.read_csv(os.path.join("data", "load_data.csv"))
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Show time-series graph
st.subheader("📈 Historical Load Data")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["Datetime"],
    y=df["Load"],
    mode='lines',
    name="Load (MW)"
))
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
fig.update_layout(template="plotly_dark", height=400)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Simple Forecast Model
st.subheader("🔮 Next 24 Hour Forecast")

# Create time index feature
df["HourIndex"] = np.arange(len(df))

X = df[["HourIndex"]]
y = df["Load"]

model = LinearRegression()
model.fit(X, y)

# Predict next 24 hours
# Automatically forecast next 48 hours
forecast_hours = 48

last_date = df["Datetime"].iloc[-1]

future_dates = pd.date_range(
    start=last_date + pd.Timedelta(hours=1),
    periods=forecast_hours,
    freq="H"
)

future_hours = np.arange(len(df), len(df) + forecast_hours).reshape(-1, 1)

future_predictions = model.predict(future_hours)
forecast_df = pd.DataFrame({
    "Datetime": future_dates,
    "PredictedLoad": future_predictions
})

# Plot forecast
# ---------------- COMBINED HISTORICAL + FORECAST GRAPH ----------------

# ---------------- CLEAR HISTORICAL + FORECAST GRAPH ----------------

forecast_fig = go.Figure()

# Last 48 hours historical data
last_48 = df.tail(48)

forecast_fig.add_trace(go.Scatter(
    x=last_48["Datetime"],
    y=last_48["Load"],
    mode='lines',
    name="Historical Load (Last 48 Hours)",
    line=dict(width=3)
))

# Future 24 hour prediction
forecast_fig.add_trace(go.Scatter(
    x=forecast_df["Datetime"],
    y=forecast_df["PredictedLoad"],
    mode='lines+markers',
    name="Next 24 Hours Forecast",
    line=dict(dash='dash', width=3)
))

forecast_fig.update_layout(
    title="Load Forecast (Last 48 Hours + Next 24 Hours)",
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=450,
    xaxis_title="Date & Time",
    yaxis_title="Load (MW)"
)

st.plotly_chart(forecast_fig, use_container_width=True)

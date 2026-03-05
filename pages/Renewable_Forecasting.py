import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()

import joblib
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import requests

API_KEY = "e1b42557f5ae19411fa25a4ced32c891"
CITY = "Hyderabad"   # you can change city

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return temperature, humidity, wind_speed
st.set_page_config(page_title="Renewable Forecasting", layout="wide")

st.title("☀ Renewable Energy Forecasting")
st.markdown("### AI-Based Solar Output Prediction (Hyderabad Case Study)")

st.divider()

# Load model
model = joblib.load("models/solar_model.pkl")

# Input Section
st.subheader("🌤 Real-Time Weather Inputs (Hyderabad)")

col1, col2 = st.columns(2)

with col1:
    ghi = st.slider("Global Horizontal Irradiance (W/m²)", 200, 1000, 600)

with col2:
    if st.button("🌤 Get Live Weather"):
        temperature, humidity, windspeed = get_weather()
        st.session_state.temperature = temperature
        st.session_state.humidity = humidity
        st.session_state.windspeed = windspeed

# If weather already loaded, show it
if "temperature" in st.session_state:
    temperature = st.session_state.temperature
    humidity = st.session_state.humidity
    windspeed = st.session_state.windspeed

    st.success("Live Weather Loaded ✅")
    st.write("🌡 Temperature:", temperature, "°C")
    st.write("💨 Wind Speed:", windspeed, "m/s")
    st.write("💧 Humidity:", humidity, "%")
st.divider()

# Predict
if st.button("🚀 Predict Solar Output") and "temperature" in st.session_state:

    temperature = st.session_state.temperature
    humidity = st.session_state.humidity
    windspeed = st.session_state.windspeed

    input_data = np.array([[ghi, temperature, windspeed, humidity]])
    prediction = model.predict(input_data)[0]

    st.success(f"🌞 Predicted Solar Output: {round(prediction, 2)} MW")
    # 📊 Input Summary
    # 📊 Input Summary
    st.subheader("📊 Input Summary")

    st.markdown(f"""
<div style="background-color:#1e293b;padding:20px;border-radius:12px">
<table style="width:100%;color:white;border-collapse:collapse">
<tr style="background-color:#0f172a">
<th style="padding:10px;text-align:left">Feature</th>
<th style="padding:10px;text-align:left">Value</th>
</tr>
<tr><td style="padding:8px">GHI</td><td>{ghi}</td></tr>
<tr><td style="padding:8px">Temperature</td><td>{temperature}</td></tr>
<tr><td style="padding:8px">Wind Speed</td><td>{windspeed}</td></tr>
<tr><td style="padding:8px">Humidity</td><td>{humidity}</td></tr>
</table>
</div>
""", unsafe_allow_html=True)
    # 📈 Prediction Visualization
    st.subheader("📈 Prediction Visualization")

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Solar Output (MW)"],
        y=[prediction],
        text=[round(prediction, 2)],
        textposition="auto"
    ))

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # 🧠 Feature Importance
    st.subheader("🧠 Feature Importance (Model Coefficients)")

    importance = model.coef_

    importance_fig = go.Figure()

    importance_fig.add_trace(go.Bar(
        x=["GHI", "Temperature", "Wind Speed", "Humidity"],
        y=importance
    ))

    importance_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=400
    )

    st.plotly_chart(importance_fig, use_container_width=True)
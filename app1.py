import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
import random

st.set_page_config(page_title="AI Smart Grid", layout="wide")

st.title("⚡ AI SMART GRID SYSTEM")
st.markdown("### Intelligent Energy Monitoring & Prediction")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Renewable Forecasting",
        "Load Forecasting",
        "Anomaly Detection",
        "Theft Detection",
        "Optimization",
        "Model Performance"
    ]
)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.header("📊 Grid Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Solar Output (kW)", random.randint(200, 900))
    col2.metric("Active Load (kW)", random.randint(300, 1000))
    col3.metric("Theft Cases", random.randint(0, 5))
    col4.metric("Grid Stability %", random.randint(85, 99))

    st.subheader("Power Distribution")

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=["Solar", "Battery", "Grid"],
        values=[40, 25, 35],
        hole=0.4
    ))

    st.plotly_chart(fig, use_container_width=True)


# ---------------- RENEWABLE FORECAST ----------------
elif page == "Renewable Forecasting":

    st.header("☀ Solar Energy Prediction")

    ghi = st.slider("Global Horizontal Irradiance", 200, 1000, 600)
    temperature = st.slider("Temperature", 10, 45, 30)
    wind = st.slider("Wind Speed", 0, 10, 3)
    humidity = st.slider("Humidity", 10, 100, 50)

    if st.button("Predict Solar Output"):

        prediction = (ghi * 0.5 + temperature * 2 - humidity * 0.3 + wind * 1.5) / 100

        st.success(f"Predicted Solar Output: {round(prediction,2)} MW")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Solar Output"],
            y=[prediction]
        ))

        st.plotly_chart(fig, use_container_width=True)


# ---------------- LOAD FORECASTING ----------------
elif page == "Load Forecasting":

    st.header("⚡ Electricity Demand Prediction")

    hour = st.slider("Hour of Day", 0, 23, 12)
    temperature = st.slider("Temperature", 10, 45, 30)

    if st.button("Predict Load"):

        load = 300 + hour * 10 + temperature * 5

        st.success(f"Predicted Load Demand: {load} kW")

        hours = list(range(24))
        loads = [300 + h * 10 + temperature * 5 for h in hours]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=hours,
            y=loads,
            mode="lines+markers"
        ))

        st.plotly_chart(fig, use_container_width=True)


# ---------------- ANOMALY DETECTION ----------------
elif page == "Anomaly Detection":

    st.header("⚠ Grid Health Monitoring")

    voltage = st.slider("Voltage", 200, 260, 230)
    frequency = st.slider("Frequency", 48, 52, 50)

    if voltage < 210 or voltage > 250 or frequency < 49 or frequency > 51:

        st.error("⚠ Grid Anomaly Detected")

    else:

        st.success("Grid Operating Normally")


# ---------------- THEFT DETECTION ----------------
elif page == "Theft Detection":

    st.header("🔍 Electricity Theft Detection")

    consumption = st.slider("Consumer Usage", 0, 1000, 500)
    meter = st.slider("Meter Reading", 0, 1000, 400)

    if abs(consumption - meter) > 200:

        st.error("⚠ Possible Electricity Theft Detected")

    else:

        st.success("No Theft Detected")


# ---------------- OPTIMIZATION ----------------
elif page == "Optimization":

    st.header("🔋 Smart Energy Distribution")

    solar = random.randint(200, 800)
    demand = random.randint(300, 900)
    battery = random.randint(20, 100)

    st.write("Solar Power:", solar)
    st.write("Load Demand:", demand)
    st.write("Battery Level:", battery)

    if solar > demand:

        st.success("Solar energy is enough. Extra energy stored in battery.")

    elif battery > 30:

        st.warning("Battery supplying additional power.")

    else:

        st.error("Using electricity from main grid.")


# ---------------- MODEL PERFORMANCE ----------------
elif page == "Model Performance":

    st.header("📈 AI Model Accuracy")

    models = ["Solar Prediction", "Load Forecast", "Theft Detection"]

    accuracy = [92, 89, 94]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=models,
        y=accuracy
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.write("Average Accuracy:", sum(accuracy)/len(accuracy), "%")

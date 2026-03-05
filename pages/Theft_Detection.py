import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()
import pandas as pd
import joblib
import plotly.graph_objects as go

st.title("🔍 Electricity Theft Detection")

# ---------------- LOAD DATA ----------------
import os
df = pd.read_csv(os.path.join("data", "theft_data.csv"))

# ---------------- LOAD MODEL ----------------
model = joblib.load("models/theft_model.pkl")

st.subheader("Enter Consumer Details")

monthly_usage = st.number_input("Monthly Usage (kWh)", 0, 2000, 500)
peak_usage = st.number_input("Peak Usage (kWh)", 0, 500, 100)
bill_change = st.slider("Bill Change Percentage (%)", -100, 100, 10)

# ---------------- PREDICTION ----------------
if st.button("Check Theft"):

    input_data = [[monthly_usage, peak_usage, bill_change]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ Suspicious Usage Detected (Possible Theft)")
    else:
        st.success("✅ Normal Electricity Usage")

# ---------------- GRAPH SECTION ----------------
st.subheader("Theft Overview from Dataset")

normal_count = len(df[df["Theft"] == 0])
theft_count = len(df[df["Theft"] == 1])

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Normal Usage", "Suspicious Usage"],
    y=[normal_count, theft_count],
    text=[normal_count, theft_count],
    textposition="outside"
))

# 🔥 ONLY CHANGE: Dark Theme
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig, use_container_width=True)

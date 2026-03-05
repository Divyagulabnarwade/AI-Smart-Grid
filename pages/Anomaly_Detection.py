import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()
import pandas as pd
from sklearn.cluster import KMeans

st.set_page_config(page_title="Grid Health", layout="wide")

st.title("⚡ Electricity Grid Health Check")

st.divider()

# Load data
import os
path = os.path.join("data", "grid_data.csv")
df = pd.read_csv(path)

# AI check (hidden logic)
features = df[["Voltage", "Frequency", "Current", "PowerFactor"]]
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(features)

cluster_counts = df["Cluster"].value_counts()
problem_count = cluster_counts.min()

# Simple Output for User
st.subheader("📢 Current Grid Condition")

if problem_count < 10:
    st.success("🟢 Everything is working normally.")
elif problem_count < 30:
    st.warning("🟡 Small issue detected. Monitoring required.")
else:
    st.error("🔴 Serious grid problem detected! Immediate action needed.")

st.write(f"Number of unusual readings detected: {problem_count}")

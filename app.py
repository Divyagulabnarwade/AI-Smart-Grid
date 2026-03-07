import streamlit as st
import random
from datetime import datetime
st.set_page_config(
    page_title="GridMind",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ FULL DARK PROFESSIONAL STYLE ------------------
st.markdown("""
<style>

header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background-color: #0f172a;
}

h1, h2, h3, h4, h5, h6, p, div, span {
    color: white !important;
}

section[data-testid="stSidebar"] {
    min-width: 280px !important;
    max-width: 280px !important;
    background-color: #111827 !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.main-title {
    text-align: center;
    font-size: 56px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1 !important;
    margin-bottom: 40px;
}

.kpi-card {
    background-color: #1e293b;
    padding: 30px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<div class='main-title'>⚡GridMind</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI Smart Grid Intelligence Platform</div>", unsafe_allow_html=True)
now = datetime.now()
st.write("📅", now.strftime("%d %B %Y"))
st.write("⏰", now.strftime("%H:%M:%S"))

st.divider()

# ------------------ AI LOGIC ------------------
solar_output = random.randint(600, 1000)
load = random.randint(500, 900)
theft = random.randint(0, 30)
stability = random.randint(80, 100)

if solar_output > load:
    solar_status = "Solar energy is sufficient for current demand"
else:
    solar_status = "Solar production is lower than demand"

if load > solar_output:
    load_status = "Grid demand is currently high"
else:
    load_status = "Load demand is balanced"

if theft > 10:
    theft_status = "Possible electricity theft detected"
else:
    theft_status = "No major theft activity"

if stability > 90:
    stability_status = "Grid operating in stable condition"
else:
    stability_status = "Grid stability needs monitoring"

# ------------------ SYSTEM OVERVIEW ------------------
st.markdown("## 📊 System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='kpi-card'>
        <h3>☀ Solar Output</h3>
        <p>{solar_status}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='kpi-card'>
        <h3>⚡ Active Load</h3>
        <p>{load_status}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='kpi-card'>
        <h3>🔍 Theft Cases</h3>
        <p>{theft_status}</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='kpi-card'>
        <h3>🧠 Grid Stability</h3>
        <p>{stability_status}</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


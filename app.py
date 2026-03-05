import streamlit as st

st.set_page_config(
    page_title="GridMind",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ FULL DARK PROFESSIONAL STYLE ------------------
st.markdown("""
<style>

/* Remove white header + menu + footer */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Main background */
.stApp {
    background-color: #0f172a;
}

/* Force all text white */
h1, h2, h3, h4, h5, h6, p, div, span {
    color: white !important;
}

/* Sidebar width and color */
section[data-testid="stSidebar"] {
    min-width: 280px !important;
    max-width: 280px !important;
    background-color: #111827 !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Title styling */
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

/* KPI Cards */
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

st.divider()

# ------------------ SYSTEM OVERVIEW ------------------
st.markdown("## 📊 System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='kpi-card'>
        <h3>☀ Solar Output</h3>
        <h2>850 kW</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='kpi-card'>
        <h3>⚡ Active Load</h3>
        <h2>720 kW</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='kpi-card'>
        <h3>🔍 Theft Cases</h3>
        <h2>23</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='kpi-card'>
        <h3>🧠 Grid Stability</h3>
        <h2>98%</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()


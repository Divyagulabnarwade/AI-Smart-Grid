import streamlit as st

def apply_dark_theme():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    h1, h2, h3, h4, h5, h6, p, div, label {
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827 !important;
        min-width: 280px !important;
        max-width: 280px !important;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
    }

    .kpi-card {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0,255,255,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
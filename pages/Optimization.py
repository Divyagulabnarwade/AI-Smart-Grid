import streamlit as st
from utils.style import apply_dark_theme
apply_dark_theme()

st.set_page_config(page_title="Energy Optimization", layout="wide")

st.title("🔋 Smart Energy Management")
st.markdown("### Automatic Energy Distribution")
st.divider()

st.subheader("Enter Current Energy Values")

col1, col2 = st.columns(2)

with col1:
    solar_power = st.slider("Current Solar Power (kW)", 0, 1000, 500)

with col2:
    load_demand = st.slider("Current Electricity Demand (kW)", 0, 1000, 600)

battery_level = st.slider("Battery Level (%)", 0, 100, 50)

st.divider()

st.subheader("⚡ System Decision")

battery_capacity = 300   # max battery support in kW
battery_available = (battery_level / 100) * battery_capacity

if solar_power >= load_demand:
    extra = solar_power - load_demand
    st.success(f"☀ Solar power fully supplies the load.")
    st.info(f"Extra {extra} kW energy is stored in the battery.")

else:
    deficit = load_demand - solar_power

    if battery_available >= deficit:
        st.warning(f"Solar is insufficient.")
        st.info(f"🔋 Battery supplies {deficit} kW to meet the demand.")
        st.success("No grid power needed.")

    else:
        grid_needed = deficit - battery_available
        st.error("Solar and battery are insufficient.")
        st.info(f"🌐 Grid supplies {grid_needed:.1f} kW to meet demand.")
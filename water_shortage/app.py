import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("water_model.pkl")

st.set_page_config(page_title="Water Availability Predictor", layout="centered")

st.title("💧 Water Availability Prediction System")
st.markdown("Predict water availability based on environmental and demographic factors.")

# ---- USER INPUT ---- #
st.sidebar.header("Enter Input Values")

temperature = st.sidebar.slider("Temperature (°C)", 10.0, 50.0, 30.0)
population = st.sidebar.slider("Population", 10000, 1000000, 500000)
reservoir_level = st.sidebar.slider("Reservoir Level (%)", 0.0, 100.0, 50.0)
rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 500.0, 100.0)

# ---- CREATE INPUT DATAFRAME ---- #
input_data = pd.DataFrame({
    "temperature": [temperature],
    "population": [population],
    "reservoir_level": [reservoir_level],
    "rainfall": [rainfall]   # new feature added
})

st.subheader("📊 Input Data")
st.write(input_data)

# ---- HANDLE MODEL INPUT ---- #
try:
    prediction = model.predict(input_data)
except:
    # fallback if rainfall was not used in training
    input_data = input_data.drop(columns=["rainfall"])
    prediction = model.predict(input_data)

# ---- OUTPUT ---- #
st.subheader("🔍 Prediction Result")

st.success(f"Predicted Water Availability: {prediction[0]:.2f}")

# ---- INTERPRETATION ---- #
if prediction[0] > 50:
    st.info("✅ Good Water Availability")
elif prediction[0] > 20:
    st.warning("⚠️ Moderate Water Availability")
else:
    st.error("❌ High Risk of Water Shortage")

# ---- VISUALIZATION ---- #
st.subheader("📈 Feature Impact Visualization")

chart_data = pd.DataFrame({
    "Feature": ["Temperature", "Population", "Reservoir", "Rainfall"],
    "Values": [temperature, population, reservoir_level, rainfall]
})

st.bar_chart(chart_data.set_index("Feature"))

# ---- FOOTER ---- #
st.markdown("---")
st.caption("AI-based Water Resource Management System 💡")
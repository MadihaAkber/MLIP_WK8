import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 California House Price Predictor")
st.write("Predict median housing values using machine learning.")

model = joblib.load(MODEL_PATH)

st.sidebar.header("Enter Housing Information")

MedInc = st.sidebar.slider("Median Income (10k USD)", 0.5, 15.0, 5.0)
HouseAge = st.sidebar.slider("House Age", 1, 50, 20)
AveRooms = st.sidebar.slider("Average Rooms", 1.0, 10.0, 5.0)
AveBedrms = st.sidebar.slider("Average Bedrooms", 0.5, 5.0, 1.0)
Population = st.sidebar.slider("Population", 100, 5000, 800)
AveOccup = st.sidebar.slider("Average Occupants", 1.0, 10.0, 3.0)
Latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 36.5)
Longitude = st.sidebar.slider("Longitude", -124.0, -114.0, -119.0)

if st.button("Predict House Price"):

    input_data = pd.DataFrame([{
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Predicted Median Housing Value")
    st.metric("Estimated Value", f"${prediction * 100000:,.2f}")
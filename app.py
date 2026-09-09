import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("Car Price Prediction")
st.write("Enter the car details to predict its selling price.")

# User inputs
year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2015
)

present_price = st.number_input(
    "Present Price",
    min_value=0.0,
    value=5.0
)

owner = st.selectbox(
    "Owner",
    [0, 1, 2]
)

car_age = 2026 - year

st.write(f"Car Age: {car_age} years")

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

selling_type = st.selectbox(
    "Selling Type",
    ["Dealer", "Individual"]
)

# Create input data with EXACT same columns as training data
input_data = pd.DataFrame({
    "Year": [year],
    "Present_Price": [present_price],
    "Owner": [owner],
    "Car_Age": [car_age],
    "Fuel_Type_Diesel": [1 if fuel_type == "Diesel" else 0],
    "Fuel_Type_Petrol": [1 if fuel_type == "Petrol" else 0],
    "Transmission_Manual": [1 if transmission == "Manual" else 0],
    "Selling_type_Individual": [1 if selling_type == "Individual" else 0]
})

# Prediction
if st.button("Predict Selling Price"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Owner": [owner],
        "Fuel_Type_Diesel": [1 if fuel_type == "Diesel" else 0],
        "Fuel_Type_Petrol": [1 if fuel_type == "Petrol" else 0],
        "Transmission_Manual": [1 if transmission == "Manual" else 0],
        "Selling_type_Individual": [1 if selling_type == "Individual" else 0],
        "Car_Age": [car_age]
    })

    # Match the exact order used during training
    input_data = input_data[scaler.feature_names_in_]

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Selling Price: ₹{prediction[0]:.2f} Lakhs")

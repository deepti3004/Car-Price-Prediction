import streamlit as st
import pandas as pd
import joblib
import base64

# Page config
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

# Helper to load images as base64
def get_base64_img(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

car_silhouette_b64 = get_base64_img("car.png")

# Custom Dark Glassmorphism CSS
st.markdown(f"""
<style>
    /* Dark background */
    .stApp {{
        background: radial-gradient(circle at top right, #1c2230 0%, #0d1117 60%, #06090e 100%);
        color: #e2e8f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    /* Main container card styling */
    div[data-testid="stVerticalBlock"] > div:has(div.card-anchor) {{
        background: rgba(26, 32, 46, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 32px 36px 36px 36px;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.45);
    }}

    /* Title section */
    .header-box {{
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 24px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        padding-bottom: 16px;
    }}
    .header-icon {{
        width: 44px;
        height: 44px;
        filter: invert(85%) sepia(10%) saturate(300%) hue-rotate(180deg);
    }}
    .header-title {{
        font-size: 1.9rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
        letter-spacing: -0.5px;
    }}
    .header-subtitle {{
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-top: 3px;
        text-transform: uppercase;
        letter-spacing: 0.7px;
    }}

    /* Car Age badge */
    .age-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(30, 80, 160, 0.25);
        border: 1px solid rgba(75, 140, 255, 0.4);
        box-shadow: 0 0 12px rgba(45, 125, 255, 0.2);
        color: #70b0ff;
        padding: 8px 16px;
        border-radius: 10px;
        font-weight: 500;
        font-size: 0.92rem;
        margin-top: 27px;
    }}

    /* Input labels & widgets */
    label p {{
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        color: #cbd5e1 !important;
    }}
    div[data-baseweb="input"], div[data-baseweb="select"] > div {{
        background-color: rgba(18, 23, 34, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 10px !important;
        color: #f1f5f9 !important;
    }}

    /* Prediction button */
    .stButton > button {{
        width: 100%;
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.8px;
        box-shadow: 0 4px 18px rgba(2, 132, 199, 0.35);
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 6px 22px rgba(2, 132, 199, 0.55);
    }}

    /* Decorative bottom illustration */
    .corner-car-img {{
        width: 100%;
        max-width: 155px;
        display: block;
        margin-left: auto;
        opacity: 0.85;
        filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.5));
    }}
</style>
""", unsafe_allow_html=True)


# Header with car icon
st.markdown(f"""
<div class="header-box">
    {'<img src="data:image/png;base64,' + car_silhouette_b64 + '" class="header-icon"/>' if car_silhouette_b64 else '🚗'}
    <div>
        <div class="header-title">Car Price <b>Prediction</b></div>
        <div class="header-subtitle">Enter the car details below to get your valuation</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Form grid (2 columns)
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    year = st.number_input("Year", min_value=1990, max_value=2026, value=2024, step=1)
    present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, value=8.0, step=0.25)
    owner = st.selectbox(
    "Owner",
    [0, 1, 2],
    format_func=lambda x: {
        0: "First Hand",
        1: "Second Hand",
        2: "Third Hand or More"
    }[x])
    selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"])

with col2:
    car_age = 2026 - year
    st.markdown(f"""
        <div class="age-badge">
            <span>⏱</span> Car Age: {car_age} {'year' if car_age == 1 else 'years'}
        </div>
    """, unsafe_allow_html=True)

    fuel_type = st.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG"])
    transmission = st.selectbox("Transmission", ["Automatic", "Manual"])


st.write("")

# Submit section
if st.button("PREDICT SELLING PRICE"):
    try:
        model = joblib.load("car_price_model.pkl")
        scaler = joblib.load("scaler.pkl")

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

        input_data = input_data[scaler.feature_names_in_]
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        st.success(f"Estimated Valuation: ₹{prediction[0]:.2f} Lakhs")
    except Exception as e:
        st.error(f"Error predicting price: {e}")
        

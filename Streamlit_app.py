import streamlit as st 
import pickle
import numpy as np

# Load model and encoders
with open('models/trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Commented out label encoder loading and usage due to missing file
# with open('label_encoders.pkl', 'rb') as f:
#     label_encoders = pickle.load(f)
#     le_fuel, le_seller, le_transmission = label_encoders

st.title("Used Car Price Predictor 🚗")

# Input fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, value=5.0)
kms_driven = st.number_input("KMs Driven", min_value=0, value=50000)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
# Temporarily replace categorical inputs with fixed values or remove them
fuel_type = "Petrol"
seller_type = "Dealer"
transmission = "Manual"

# Predict button
if st.button("Predict Price"):
    # Commented out encoding due to missing label encoders
    # fuel_encoded = le_fuel.transform([fuel_type])[0]
    # seller_encoded = le_seller.transform([seller_type])[0]
    # transmission_encoded = le_transmission.transform([transmission])[0]
    
    # Calculate car age
    age = 2025 - year

    # Construct feature array (ensure it matches training order)
    # Using placeholder encoded values 0 for categorical features
    features = np.array([[present_price, kms_driven, owner, age,
                          0, 0, 0]])
    
    # Predict
    prediction = model.predict(features)[0]
    st.success(f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs")

import streamlit as st
import pandas as pd
import pickle

# Load model from local .pkl (must be in the same folder)
with open("decision_tree_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Airline Satisfaction Prediction")
st.write("Enter passenger details to predict Satisfaction:")

# --- User Inputs ---
gender = st.selectbox("Gender", ["Male", "Female"])
customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
travel_type = st.selectbox("Type of Travel", ["Business", "Personal"])
travel_class = st.selectbox("Class", ["Eco", "Eco Plus", "Business"])
flight_distance = st.number_input("Flight Distance", min_value=0)
departure_delay = st.number_input("Departure Delay", min_value=0)
arrival_delay = st.number_input("Arrival Delay", min_value=0)

# --- Prepare input for model ---
# Manual encoding of categorical variables
input_data = pd.DataFrame({
    "Gender": [0 if gender == "Male" else 1],
    "Customer type": [0 if customer_type == "Loyal Customer" else 1],
    "Type of travel": [0 if travel_type == "Business" else 1],
    "Class": [0 if travel_class == "Eco" else 1 if travel_class == "Eco Plus" else 2],
    "Flight distance": [flight_distance],
    "Departure delay": [departure_delay],
    "Arrival delay": [arrival_delay]
})

# --- Prediction ---
if st.button("Predict Satisfaction"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Satisfaction: {prediction}")

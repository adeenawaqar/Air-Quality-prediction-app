# app.py
import streamlit as st
import pandas as pd
import pickle

# Load the trained model (must be in the same folder)
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
onboard_service = st.number_input("Onboard Service", min_value=0)
seat_comfort = st.number_input("Seat Comfort", min_value=0)
leg_room_service = st.number_input("Leg Room Service", min_value=0)
cleanliness = st.number_input("Cleanliness", min_value=0)
food_drink = st.number_input("Food and Drink", min_value=0)
inflight_service = st.number_input("In-Flight Service", min_value=0)
inflight_wifi = st.number_input("In-Flight Wifi Service", min_value=0)
inflight_entertainment = st.number_input("In-Flight Entertainment", min_value=0)
baggage_handling = st.number_input("Baggage Handling", min_value=0)

# --- Prepare input for model ---
input_data = pd.DataFrame({
    "Gender": [gender],
    "Customer type": [customer_type],
    "Type of travel": [travel_type],
    "Class": [travel_class],
    "Flight distance": [flight_distance],
    "Departure delay": [departure_delay],
    "Arrival delay": [arrival_delay],
    "On-board service": [onboard_service],
    "Seat comfort": [seat_comfort],
    "Leg room service": [leg_room_service],
    "Cleanliness": [cleanliness],
    "Food and drink": [food_drink],
    "In-flight Service": [inflight_service],
    "In-flight Wifi Service": [inflight_wifi],
    "In-flight Entertainment": [inflight_entertainment],
    "Baggage Handling": [baggage_handling]
})

# --- Encode categorical features manually ---
for col in ["Gender", "Customer type", "Type of travel", "Class"]:
    input_data[col] = input_data[col].astype("category").cat.codes

# --- Predict ---
if st.button("Predict Satisfaction"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Satisfaction: {prediction}")


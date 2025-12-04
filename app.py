import streamlit as st

st.title("Airline Satisfaction Prediction (No scikit-learn)")

st.write("Enter passenger details:")

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
inflight_service = st.number_input("In-flight Service", min_value=0)
inflight_wifi = st.number_input("In-flight Wifi Service", min_value=0)
inflight_entertainment = st.number_input("In-flight Entertainment", min_value=0)
baggage_handling = st.number_input("Baggage Handling", min_value=0)

# --- Simple Prediction Logic ---
# This is a dummy rule-based system
score = (
    onboard_service + seat_comfort + leg_room_service + cleanliness + 
    food_drink + inflight_service + inflight_wifi + inflight_entertainment + baggage_handling
)

# Example simple logic
if score >= 30:
    prediction = "Satisfied"
else:
    prediction = "Not Satisfied"

# --- Display Prediction ---
if st.button("Predict Satisfaction"):
    st.success(f"Predicted Satisfaction: {prediction}")


import streamlit as st
import pandas as pd

st.title("Airline Satisfaction Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
travel_type = st.selectbox("Type of Travel", ["Business", "Personal"])
travel_class = st.selectbox("Class", ["Eco", "Eco Plus", "Business"])

flight_distance = st.number_input("Flight Distance (km)", min_value=0, max_value=20000, value=500)
departure_delay = st.number_input("Departure Delay (minutes)", min_value=0, max_value=500, value=0)
arrival_delay = st.number_input("Arrival Delay (minutes)", min_value=0, max_value=500, value=0)

onboard_service = st.number_input("Onboard Service (0-5)", min_value=0, max_value=5, value=3)
departure_arrival_convenience = st.number_input("Departure & Arrival Time Convenience (0-5)", min_value=0, max_value=5, value=3)
seat_comfort = st.number_input("Seat Comfort (0-5)", min_value=0, max_value=5, value=3)
leg_room_service = st.number_input("Leg Room Service (0-5)", min_value=0, max_value=5, value=3)
cleanliness = st.number_input("Cleanliness (0-5)", min_value=0, max_value=5, value=3)
food_drink = st.number_input("Food and Drink (0-5)", min_value=0, max_value=5, value=3)
inflight_service = st.number_input("In-Flight Service (0-5)", min_value=0, max_value=5, value=3)
inflight_wifi = st.number_input("In-Flight Wifi Service (0-5)", min_value=0, max_value=5, value=3)
inflight_entertainment = st.number_input("In-Flight Entertainment (0-5)", min_value=0, max_value=5, value=3)
baggage_handling = st.number_input("Baggage Handling (0-5)", min_value=0, max_value=5, value=3)

input_data = pd.DataFrame({
    "Gender": [0 if gender == "Male" else 1],
    "Customer type": [0 if customer_type == "Loyal Customer" else 1],
    "Type of travel": [0 if travel_type == "Business" else 1],
    "Class": [0 if travel_class == "Eco" else 1 if travel_class == "Eco Plus" else 2],
    "Flight distance": [flight_distance],
    "Departure delay": [departure_delay],
    "Arrival delay": [arrival_delay],
    "On-board service": [onboard_service],
    "Departure & Arrival Time Convenience": [departure_arrival_convenience],
    "Seat comfort": [seat_comfort],
    "Leg room service": [leg_room_service],
    "Cleanliness": [cleanliness],
    "Food and drink": [food_drink],
    "In-flight Service": [inflight_service],
    "In-flight Wifi Service": [inflight_wifi],
    "In-flight Entertainment": [inflight_entertainment],
    "Baggage Handling": [baggage_handling]
})

if st.button("Show Data"):
    st.write(input_data)

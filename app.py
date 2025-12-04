import streamlit as st
import pandas as pd

st.title("Airline Satisfaction Prediction")

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

input_data = pd.DataFrame({
    "Gender": [0 if gender == "Male" else 1],
    "Customer type": [0 if customer_type == "Loyal Customer" else 1],
    "Type of travel": [0 if travel_type == "Business" else 1],
    "Class": [0 if travel_class == "Eco" else 1 if travel_class == "Eco Plus" else 2],
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

if st.button("Show Data"):
    st.write(input_data)


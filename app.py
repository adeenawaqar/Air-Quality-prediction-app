import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("Airline Satisfaction Prediction (All Features, No File Handling)")
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
departure_arrival_convenience = st.number_input("Departure & Arrival Time Convenience", min_value=0)
seat_comfort = st.number_input("Seat Comfort", min_value=0)
leg_room_service = st.number_input("Leg Room Service", min_value=0)
cleanliness = st.number_input("Cleanliness", min_value=0)
food_drink = st.number_input("Food and Drink", min_value=0)
inflight_service = st.number_input("In-flight Service", min_value=0)
inflight_wifi = st.number_input("In-flight Wifi Service", min_value=0)
inflight_entertainment = st.number_input("In-flight Entertainment", min_value=0)
baggage_handling = st.number_input("Baggage Handling", min_value=0)

# --- Encode categorical inputs manually ---
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

# --- Train a Decision Tree inside the app ---
# Dummy dataset for demonstration (replace with more realistic data if needed)
X_train = pd.DataFrame({
    "Gender": [0, 1, 0, 1],
    "Customer type": [0, 1, 0, 1],
    "Type of travel": [0, 1, 0, 1],
    "Class": [0, 1, 0, 2],
    "Flight distance": [500, 1000, 700, 1200],
    "Departure delay": [10, 30, 0, 5],
    "Arrival delay": [5, 25, 0, 10],
    "On-board service": [3, 4, 2, 5],
    "Departure & Arrival Time Convenience": [3, 5, 2, 4],
    "Seat comfort": [3, 4, 2, 5],
    "Leg room service": [3, 4, 2, 5],
    "Cleanliness": [3, 4, 2, 5],
    "Food and drink": [3, 4, 2, 5],
    "In-flight Service": [3, 4, 2, 5],
    "In-flight Wifi Service": [3, 2, 1, 4],
    "In-flight Entertainment": [3, 4, 2, 5],
    "Baggage Handling": [3, 4, 2, 5]
})
y_train = [1, 0, 1, 0]  # 1 = Satisfied, 0 = Not satisfied

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# --- Predict ---
if st.button("Predict Satisfaction"):
    prediction = model.predict(input_data)[0]
    result = "Satisfied" if prediction == 1 else "Not Satisfied"
    st.success(f"Predicted Satisfaction: {result}")

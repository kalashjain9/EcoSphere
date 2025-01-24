import streamlit as st
import pandas as pd
import joblib

# Import custom modules
from carbon_calculator import calculate_carbon_footprint
from carbon_credits import get_carbon_credits_marketplace
from rewards_system import RewardsSystem

class SustainabilityPlatform:
    def __init__(self):
        st.set_page_config(page_title="Sustainable Future Platform", page_icon="🌍")
        self.load_crop_prediction_model()
        self.initialize_session_state()

    def load_crop_prediction_model(self):
        """Load pre-trained machine learning model"""
        try:
            self.crop_model = joblib.load('model_storage/crop_random_forest.joblib')
            st.sidebar.success("Crop Prediction Model Loaded!")
        except FileNotFoundError:
            st.sidebar.error("Crop Prediction Model not found.")
            self.crop_model = None

    def initialize_session_state(self):
        """Initialize session state variables"""
        session_vars = {
            'logged_in': False,
            'username': '',
            'total_carbon_footprint': 0,
            'carbon_tax': 0,
            'supercoins': 0,
            'offset_history': []
        }
        
        for var, default_value in session_vars.items():
            if var not in st.session_state:
                st.session_state[var] = default_value

    def login_page(self):
        """Login page for the platform"""
        st.title("Sustainable Future Platform Login")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username == 'user' and password == 'user':
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Credentials")

    def main_dashboard(self):
        """Main dashboard with different sections"""
        menu = [
            "Carbon Footprint Calculator", 
            "Carbon Credits Marketplace", 
            "Crop Prediction",
            "User Profile"
        ]
        
        choice = st.sidebar.radio("Navigation", menu)
        
        if choice == "Carbon Footprint Calculator":
            self.carbon_footprint_calculator()
        elif choice == "Carbon Credits Marketplace":
            self.carbon_credits_marketplace()
        elif choice == "Crop Prediction":
            self.crop_prediction()
        elif choice == "User Profile":
            self.user_profile()

    def carbon_footprint_calculator(self):
        """Calculate carbon footprint"""
        st.title("Carbon Footprint Calculator")
        
        house_energy = st.number_input("House Energy Consumption (kWh)", min_value=0.0)
        household_fuel = st.number_input("Household Fuel Consumption (Liters)", min_value=0.0)
        transport_fuel = st.number_input("Transport Fuel Consumption (Liters)", min_value=0.0)
        
        if st.button("Calculate"):
            carbon_footprint = calculate_carbon_footprint(
                house_energy, household_fuel, transport_fuel
            )
            st.success(f"Your Carbon Footprint: {carbon_footprint:.2f} kg CO2")

    def carbon_credits_marketplace(self):
        """Display carbon credits marketplace"""
        st.title("Carbon Credits Marketplace")
        
        marketplace = get_carbon_credits_marketplace()
        
        for credit in marketplace:
            st.subheader(credit['name'])
            st.write(f"Credits: {credit['credits']} kg CO2")
            st.write(f"Description: {credit['description']}")
            st.write(f"Cost per Credit: ${credit['cost_per_credit']}")
            st.button(f"Buy {credit['name']} Credits")

    def crop_prediction(self):
        """Crop prediction section"""
        st.title("Crop Prediction")
        
        if self.crop_model is None:
            st.error("Crop prediction model not loaded.")
            return
        
        nitrogen = st.number_input("Nitrogen Content", min_value=0.0)
        phosphorus = st.number_input("Phosphorus Content", min_value=0.0)
        potassium = st.number_input("Potassium Content", min_value=0.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
        
        if st.button("Predict Crop"):
            features = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
            prediction = self.crop_model.predict([features])
            st.success(f"Recommended Crop: {prediction[0]}")

    def user_profile(self):
        """User profile section"""
        st.title("User Profile")
        st.write(f"Welcome, {st.session_state.username}!")
        st.metric("SuperCoins", st.session_state.supercoins)

    def main(self):
        """Main application workflow"""
        if not st.session_state.logged_in:
            self.login_page()
        else:
            if st.sidebar.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
            self.main_dashboard()

def main():
    platform = SustainabilityPlatform()
    platform.main()

if __name__ == "__main__":
    main()
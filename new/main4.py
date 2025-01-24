import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import random
from datetime import datetime, timedelta

class ComprehensiveSustainabilityPlatform:
    def __init__(self):
        """Initialize Comprehensive Sustainability Platform"""
        st.set_page_config(page_title="EcoSphere: Global Sustainability Platform", page_icon="🌍", layout="wide")
        
        # Initialize session state variables
        self._initialize_session_state()
        
        # Load crop recommendation model
        self.load_crop_model()
        
        # Global Environmental Data
        self.global_environmental_data = {
            'annual_co2_emissions': 36.44,  # billion tons globally
            'trees_destroyed_per_year': 15000000000,  # 15 billion trees
            'forest_loss_rate': 10000000,  # hectares per year
            'global_carbon_budget': {
                'industrial': 65,
                'transportation': 20,
                'agriculture': 10,
                'buildings': 5
            }
        }
        
        # Carbon Credits Marketplace
        self.carbon_credits_marketplace = {
            'Tree Plantation': {'offset_value': 50, 'price': 500, 'description': 'Plant trees to offset carbon'},
            'Solar Panel Donation': {'offset_value': 100, 'price': 1000, 'description': 'Support solar energy initiatives'},
            'Wind Mill Project': {'offset_value': 75, 'price': 750, 'description': 'Invest in wind energy infrastructure'},
            'Reforestation Program': {'offset_value': 60, 'price': 600, 'description': 'Support large-scale forest restoration'}
        }
    
    def _initialize_session_state(self):
        """Initialize all session state variables"""
        default_states = {
            'logged_in': False,
            'username': '',
            'wallet_balance': 0,
            'supercoins': 0,
            'carbon_tax': 0,
            'total_personal_emissions': 0,
            'carbon_offset_history': [],
            'environmental_impact_score': 0
        }
        
        for key, value in default_states.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    def load_crop_model(self):
        """Load pre-trained machine learning model for crop recommendation"""
        try:
            self.crop_model = joblib.load('model_storage/crop_random_forest.joblib')
            st.sidebar.success("Crop Recommendation Model loaded successfully!")
        except FileNotFoundError:
            st.sidebar.error("Crop Recommendation Model file not found.")
            self.crop_model = None
    
    def login_page(self):
        """User Login Page"""
        st.title("🌍 EcoSphere: Sustainability Platform")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                if username == 'user' and password == 'user':
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid Credentials")
        
        with col2:
            st.header("Welcome to EcoSphere")
            st.write("""
            🌿 Join our mission to combat climate change
            🌍 Track your carbon footprint
            🌱 Earn rewards for sustainable actions
            💡 Make a difference, one step at a time
            """)
    
    def global_impact_dashboard(self):
        """Create a comprehensive global environmental impact dashboard"""
        st.header("🌐 Global Environmental Impact Dashboard")
        
        # CO2 Emissions Breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Global CO2 Emissions by Sector")
            sector_fig = px.pie(
                names=list(self.global_environmental_data['global_carbon_budget'].keys()),
                values=list(self.global_environmental_data['global_carbon_budget'].values()),
                title="CO2 Emissions Distribution"
            )
            st.plotly_chart(sector_fig)
        
        with col2:
            st.subheader("Deforestation Impact")
            trees_fig = go.Figure(go.Indicator(
                mode = "number+delta",
                value = self.global_environmental_data['trees_destroyed_per_year'],
                number = {'prefix': "🌳 "},
                title = {"text": "Trees Destroyed Annually"},
                delta = {'position': "top", 'reference': 10000000000}
            ))
            st.plotly_chart(trees_fig)
        
        # Personal vs Global Emissions Comparison
        st.subheader("Your Contribution to Global Emissions")
        personal_emissions = st.session_state.total_personal_emissions
        global_emissions = self.global_environmental_data['annual_co2_emissions'] * 1000000000  # Convert to tons
        
        comparison_fig = go.Figure(data=[
            go.Bar(name='Personal Emissions', x=['Your Emissions'], y=[personal_emissions]),
            go.Bar(name='Global Annual Emissions', x=['Global Emissions'], y=[global_emissions])
        ])
        comparison_fig.update_layout(barmode='group', title='Personal vs Global CO2 Emissions')
        st.plotly_chart(comparison_fig)
        
        # Environmental Advice Section
        st.header("🌿 Personalized Environmental Recommendations")
        self._generate_environmental_advice(personal_emissions)
    
    def _generate_environmental_advice(self, personal_emissions):
        """Generate personalized environmental advice based on emissions"""
        advice_categories = {
            'low': [
                "Great job! Your emissions are relatively low.",
                "Continue your eco-friendly practices.",
                "Consider sharing your sustainable lifestyle tips."
            ],
            'medium': [
                "You can improve your carbon footprint.",
                "Consider switching to energy-efficient appliances.",
                "Explore public transportation or carpooling options."
            ],
            'high': [
                "Your carbon footprint is significant. Time for major changes!",
                "Prioritize renewable energy sources.",
                "Consider major lifestyle adjustments to reduce emissions."
            ]
        }
        
        # Categorize emissions
        if personal_emissions < 2000:
            category = 'low'
        elif personal_emissions < 5000:
            category = 'medium'
        else:
            category = 'high'
        
        # Display advice
        for advice in advice_categories[category]:
            st.info(advice)
        
        # Tree Planting Recommendation
        trees_to_plant = max(1, int(personal_emissions / 500))
        st.warning(f"Recommendation: Plant {trees_to_plant} trees to offset your emissions")
    
    def carbon_footprint_calculator(self):
        """Carbon Footprint Calculation Module"""
        st.header("🌿 Carbon Footprint Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            energy_sources = {
                'Electricity': st.number_input("Monthly Electricity (kWh)", min_value=0.0),
                'Natural Gas': st.number_input("Natural Gas Consumption (therms)", min_value=0.0),
                'Renewable Energy %': st.slider("Percentage of Renewable Energy", 0, 100, 0)
            }
        
        with col2:
            transport_details = {
                'Personal Car': st.number_input("Monthly Car Miles", min_value=0.0),
                'Public Transit': st.number_input("Public Transit Miles", min_value=0.0),
                'Flight Miles': st.number_input("Annual Flight Miles", min_value=0.0)
            }
        
        if st.button("Calculate Carbon Footprint"):
            # Emission Calculation Logic
            total_emissions = (
                energy_sources['Electricity'] * 0.5 +  # CO2 per kWh
                energy_sources['Natural Gas'] * 5.3 +  # CO2 per therm
                transport_details['Personal Car'] * 0.404 +  # CO2 per mile
                transport_details['Public Transit'] * 0.2 +  # CO2 per mile
                transport_details['Flight Miles'] * 0.25  # CO2 per mile
            ) * (1 - energy_sources['Renewable Energy %']/100)
            
            st.session_state.total_personal_emissions = total_emissions
            
            # Advanced Visualization
            emission_breakdown = pd.DataFrame({
                'Source': ['Electricity', 'Natural Gas', 'Personal Car', 'Public Transit', 'Flights'],
                'Emissions': [
                    energy_sources['Electricity'] * 0.5,
                    energy_sources['Natural Gas'] * 5.3,
                    transport_details['Personal Car'] * 0.404,
                    transport_details['Public Transit'] * 0.2,
                    transport_details['Flight Miles'] * 0.25
                ]
            })
            
            fig = px.bar(
                emission_breakdown, 
                x='Source', 
                y='Emissions', 
                title='Carbon Emissions by Source'
            )
            st.plotly_chart(fig)
            
            st.success(f"Total Carbon Footprint: {total_emissions:.2f} kg CO2")
    
    def crop_recommendation(self):
        """Crop Recommendation for Carbon Offset"""
        st.header("🌾 Crop Recommendation for Carbon Offset")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nitrogen = st.number_input("Nitrogen (N) Content", min_value=0.0, step=1.0)
            phosphorus = st.number_input("Phosphorus (P) Content", min_value=0.0, step=1.0)
            potassium = st.number_input("Potassium (K) Content", min_value=0.0, step=1.0)
        
        with col2:
            temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
        
        ph_value = st.slider("Soil pH Value", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0)
        
        if st.button("Recommend Crop"):
            features = [nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]
            
            if self.crop_model:
                crop = self.crop_model.predict([features])[0]
                st.success(f"Recommended Crop for Carbon Offset: {crop}")
                
                # Additional Crop Information
                crop_carbon_offset = {
                    'Rice': 4.5,
                    'Wheat': 3.8,
                    'Corn': 5.2,
                    'Soybean': 4.0,
                    'Potato': 3.5
                }
                
                if crop in crop_carbon_offset:
                    st.info(f"This crop can help offset approximately {crop_carbon_offset.get(crop, 0):.2f} kg of CO2")
            else:
                st.error("Crop Recommendation Model not available")
    
    def carbon_credits_market(self):
        """Carbon Credits Marketplace"""
        st.header("🌍 Carbon Credits Marketplace")
        
        st.write(f"Current Carbon Tax to Offset: ₹{st.session_state.carbon_tax}")
        st.write(f"Wallet Balance: ₹{st.session_state.wallet_balance}")
        
        for credit_type, details in self.carbon_credits_marketplace.items():
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(credit_type)
                st.write(f"Carbon Offset: {details['offset_value']} kg CO2")
                st.write(f"Price: ₹{details['price']}")
                st.write(details['description'])
            
            with col2:
                if st.button(f"Buy {credit_type}"):
                    if st.session_state.wallet_balance >= details['price']:
                        st.session_state.wallet_balance -= details['price']
                        st.session_state.carbon_tax -= details['offset_value']
                        
                        # Track carbon offset history
                        st.session_state.carbon_offset_history.append({
                            'date': datetime.now(),
                            'offset_amount': details['offset_value'],
                            'credit_type': credit_type
                        })
                        
                        if st.session_state.carbon_tax <= 0:
                            # Award supercoins when carbon tax is fully offset
                            supercoins_earned = int(details['price'] / 10)
                            st.session_state.supercoins += supercoins_earned
                            st.success(f"Carbon Tax Fully Offset! Earned {supercoins_earned} SuperCoins")
                            st.session_state.carbon_tax = 0
                        else:
                            st.success(f"Purchased {credit_type}. Remaining Carbon Tax: ₹{st.session_state.carbon_tax}")
                    else:
                        st.error("Insufficient Wallet Balance")
    
    def wallet_management(self):
        """Wallet Management and Top-up"""
        st.header("💰 Wallet Management")
        
        # Default Card Details
        default_card = {
            'number': '1234567812345678',
            'expiry_month': '01',
            'expiry_year': '2026',
            'name': 'User'
        }
        
        st.subheader("Current Wallet Balance")
        st.write(f"₹{st.session_state.wallet_balance}")
        
        st.subheader("Add Money to Wallet")
        
        # Card Details Input
        col1, col2 = st.columns(2)
        
        with col1:
            card_number = st.text_input("Card Number", value=default_card['number'])
            expiry_month = st.text_input("Expiry Month", value=default_card['expiry_month'])
        
        with col2:
            expiry_year = st.text_input("Expiry Year", value=default_card['expiry_year'])
            cardholder_name = st.text_input("Cardholder Name", value=default_card['name'])
        
        amount_to_add = st.number_input("Amount to Add (₹)", min_value=0, step=100)
        
        if st.button("Add Money"):
            st.session_state.wallet_balance += amount_to_add
            st.success(f"Added ₹{amount_to_add} to Wallet")
    
    def rewards_section(self):
        """Rewards and Supercoin Redemption"""
        st.header("🏆 Rewards Section")
        
        st.write(f"Total SuperCoins: {st.session_state.supercoins}")
        
        # Redeem SuperCoins (1% of total)
        redeemable_amount = st.session_state.supercoins * 0.01
        
        # Rewards Visualization
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("SuperCoin Earning History")
            if hasattr(st.session_state, 'carbon_offset_history'):
                rewards_df = pd.DataFrame([
                    {'Date': entry['date'], 'SuperCoins': int(entry['offset_amount'] / 10)} 
                    for entry in st.session_state.carbon_offset_history
                ])
                
                if not rewards_df.empty:
                    rewards_fig = px.line(
                        rewards_df, 
                        x='Date', 
                        y='SuperCoins', 
                        title='SuperCoin Earnings Over Time'
                    )
                    st.plotly_chart(rewards_fig)
                else:
                    st.write("No rewards earned yet")
        
        with col2:
            st.subheader("Redemption Options")
            redemption_options = {
                "Plant a Tree": 500,
                "Carbon Credit Donation": 1000,
                "Renewable Energy Support": 1500
            }
            
            selected_redemption = st.selectbox(
                "Redeem SuperCoins for:", 
                list(redemption_options.keys())
            )
            
            if st.button("Redeem"):
                required_coins = redemption_options[selected_redemption]
                if st.session_state.supercoins >= required_coins:
                    st.session_state.supercoins -= required_coins
                    st.success(f"Redeemed {selected_redemption}!")
                    
                    # Additional reward tracking
                    if 'redemption_history' not in st.session_state:
                        st.session_state.redemption_history = []
                    
                    st.session_state.redemption_history.append({
                        'date': datetime.now(),
                        'redemption': selected_redemption,
                        'coins_spent': required_coins
                    })
                else:
                    st.error("Insufficient SuperCoins")
        
        if st.button("Redeem as Wallet Balance"):
            if st.session_state.supercoins > 0:
                st.session_state.wallet_balance += redeemable_amount
                st.session_state.supercoins = 0
                st.success(f"Redeemed ₹{redeemable_amount}. SuperCoins Reset to 0.")
            else:
                st.warning("No SuperCoins available for redemption")
    
    def environmental_contribution_tracker(self):
        """Track and visualize user's environmental contributions"""
        st.header("🌍 Environmental Contribution Tracker")
        
        # Carbon Offset History
        if st.session_state.carbon_offset_history:
            offset_df = pd.DataFrame(st.session_state.carbon_offset_history)
            
            # Visualize Offset History
            offset_fig = px.line(
                offset_df, 
                x='date', 
                y='offset_amount', 
                color='credit_type',
                title='Carbon Offset Progress'
            )
            st.plotly_chart(offset_fig)
        
        # Impact Metrics
        col1, col2 = st.columns(2)
        
        with col1:
            total_offset = sum(entry['offset_amount'] for entry in st.session_state.carbon_offset_history)
            st.metric("Total CO2 Offset", f"{total_offset:.2f} kg")
        
        with col2:
            equivalent_trees = total_offset / 22
            st.metric("Equivalent Trees Saved", f"{equivalent_trees:.2f}")
        
        # Detailed Contribution Breakdown
        st.subheader("Contribution Breakdown")
        if st.session_state.carbon_offset_history:
            contribution_breakdown = pd.DataFrame(st.session_state.carbon_offset_history)
            contribution_summary = contribution_breakdown.groupby('credit_type')['offset_amount'].sum()
            
            contribution_fig = px.pie(
                values=contribution_summary.values, 
                names=contribution_summary.index, 
                title='Carbon Offset by Initiative'
            )
            st.plotly_chart(contribution_fig)
    
    def profile_section(self):
        """User Profile and Analytics"""
        st.header("👤 User Profile")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Personal Stats")
            st.write(f"Username: {st.session_state.username}")
            st.write(f"Total Carbon Emissions: {st.session_state.total_personal_emissions:.2f} kg CO2")
            st.write(f"Total Carbon Tax Offset: ₹{st.session_state.carbon_tax}")
        
        with col2:
            st.subheader("Financial Overview")
            st.write(f"Wallet Balance: ₹{st.session_state.wallet_balance}")
            st.write(f"Total SuperCoins: {st.session_state.supercoins}")
        
        # Environmental Impact Score
        st.subheader("Environmental Impact Score")
        impact_score = self._calculate_impact_score()
        st.progress(impact_score / 100)
        st.write(f"Your Impact Score: {impact_score}/100")
    
    def _calculate_impact_score(self):
        """Calculate user's environmental impact score"""
        # Base calculation considering various factors
        base_score = 50  # Start with a median score
        
        # Adjust score based on emissions
        if st.session_state.total_personal_emissions < 2000:
            base_score += 20
        elif st.session_state.total_personal_emissions > 5000:
            base_score -= 20
        
        # Adjust for carbon offsets
        total_offset = sum(entry['offset_amount'] for entry in st.session_state.carbon_offset_history)
        base_score += min(total_offset / 100, 30)
        
        # Adjust for SuperCoins (indicating engagement)
        base_score += min(st.session_state.supercoins / 100, 10)
        
        return min(max(base_score, 0), 100)
    
    def run(self):
        """Main Application Workflow"""
        if not st.session_state.logged_in:
            self.login_page()
        else:
            st.sidebar.title(f"Welcome, {st.session_state.username}")
            
            # Sidebar Navigation
            menu_options = [
                "Global Impact Dashboard",
                "Carbon Footprint Calculator", 
                "Crop Recommendation", 
                "Carbon Credits Market", 
                "Environmental Contribution",
                "Wallet Management", 
                "Rewards", 
                "Profile"
            ]
            
            choice = st.sidebar.radio("Navigation", menu_options)
            
            if st.sidebar.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
            
            # Main Content Area
            if choice == "Global Impact Dashboard":
                self.global_impact_dashboard()
            elif choice == "Carbon Footprint Calculator":
                self.carbon_footprint_calculator()
            elif choice == "Crop Recommendation":
                self.crop_recommendation()
            elif choice == "Carbon Credits Market":
                self.carbon_credits_market()
            elif choice == "Environmental Contribution":
                self.environmental_contribution_tracker()
            elif choice == "Wallet Management":
                self.wallet_management()
            elif choice == "Rewards":
                self.rewards_section()
            elif choice == "Profile":
                self.profile_section()

def main():
    platform = ComprehensiveSustainabilityPlatform()
    platform.run()

if __name__ == "__main__":
    main()
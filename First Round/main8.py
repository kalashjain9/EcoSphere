import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime, timedelta
import random

class ComprehensiveSustainabilityPlatform:
    def __init__(self):
        """Initialize Comprehensive Sustainability Platform"""
        st.set_page_config(page_title="EcoSphere: Global Sustainability Platform", page_icon="🌍", layout="wide")
        
        # Initialize session state variables
        self._initialize_session_state()
        
        # Load crop recommendation model
        self.load_crop_model()
        
        # Global Environmental Data with Real-time Insights
        self.global_environmental_data = {
            'annual_co2_emissions': 36.44,  # billion tons globally
            'trees_destroyed_per_year': 15000000000,  # 15 billion trees
            'forest_loss_rate': 10000000,  # hectares per year
            'global_carbon_budget': {
                'Industrial Sector': 65,
                'Transportation': 20,
                'Agriculture': 10,
                'Buildings': 5
            }
        }

        # Enhanced Carbon Credits Marketplace with Precise Rupee Pricing
        self.carbon_credits_marketplace = {
            '🌳 Tree Plantation': {
                'offset_value': 100,
                'price': 100,  # Precise pricing
                'description': 'Plant native trees to offset carbon emissions',
                'co2_absorption_rate': 22,  # kg CO2 per tree per year
                'eco_bonus': '🍃 Biodiversity Boost'
            },
            '☀️ Solar Panel Donation': {
                'offset_value': 500,
                'price': 500,  # Precise pricing
                'description': 'Support renewable solar energy initiatives',
                'co2_reduction_rate': 0.5,  # tons CO2 per solar panel per year
                'eco_bonus': '💡 Energy Independence'
            },
            '💨 Wind Mill Project': {
                'offset_value': 500,
                'price': 500,  # Precise pricing
                'description': 'Invest in community wind energy infrastructure',
                'co2_reduction_rate': 0.9,  # tons CO2 per windmill per year
                'eco_bonus': '🌬️ Rural Empowerment'
            },
            '🌲 Reforestation Program': {
                'offset_value': 250,
                'price': 250,  # Precise pricing
                'description': 'Support large-scale forest restoration efforts',
                'co2_absorption_rate': 25,  # kg CO2 per tree per year
                'eco_bonus': '🐾 Wildlife Corridor'
            }
        }
    
    def _initialize_session_state(self):
        """Initialize all session state variables with zero values"""
        default_states = {
            'logged_in': False,
            'username': '',
            'wallet_balance': 0,  # Start with zero balance
            'supercoins': 0,
            'carbon_tax': 0,
            'total_personal_emissions': 0,
            'carbon_offset_history': [],
            'environmental_impact_score': 0,
            'eco_challenges_completed': [],
            'green_innovations': [],
            'daily_green_challenge': ''
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
        """Enhanced User Login Page with Innovative Green Theme"""
        st.title("🌍 EcoSphere: Sustainability Platform")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                if username == 'user' and password == 'user':
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    # Innovative Feature: Random Green Challenge on Login
                    green_challenges = [
                        "🚲 Bike to Work This Week",
                        "🥤 Zero Plastic Day Challenge",
                        "💡 Energy-saving Marathon",
                        "🌱 Plant a Seed Campaign"
                    ]
                    st.session_state.daily_green_challenge = random.choice(green_challenges)
                    st.rerun()
                else:
                    st.error("Invalid Credentials. Default: username='user', password='user'")
        
        with col2:
            st.header("Green Innovation Hub")
            st.markdown("""
            🌿 Innovative Sustainability Features:
            - Dynamic Carbon Challenges
            - Personal Eco-Impact Tracking
            - Gamified Sustainability Rewards
            - Real-time Global Impact Visualization
            """)
    
    def carbon_footprint_calculator(self):
        """Advanced Carbon Footprint Calculation with Innovative Visualization"""
        st.header("🌿 Carbon Footprint Calculator")
        
        col1, col2 = st.columns(2)
        
        # Initialize all inputs to zero
        energy_sources = {
            'Electricity': 0.0,
            'Natural Gas': 0.0,
            #'Renewable Energy %': 0
        }
        
        transport_details = {
            'Personal Car': 0.0,
            'Public Transit': 0.0,
            'Flight Miles': 0.0
        }
        
        with col1:
            energy_sources['Electricity'] = st.number_input("Monthly Electricity (kWh)", min_value=0.0, value=0.0)
            energy_sources['Natural Gas'] = st.number_input("Natural Gas Consumption (kg)", min_value=0.0, value=0.0)
        
        with col2:
            transport_details['Personal Car'] = st.number_input("Monthly Car Journey in kms", min_value=0.0, value=0.0)
            transport_details['Public Transit'] = st.number_input("Public Transit in kms", min_value=0.0, value=0.0)
            transport_details['Flight Miles'] = st.number_input("Annual Flight Journey in kms", min_value=0.0, value=0.0)
        
        if st.button("Calculate Carbon Footprint"):
            # Enhanced Emission Calculation
            total_emissions = (
                energy_sources['Electricity'] * 0.475 +  # CO2 per kWh
                energy_sources['Natural Gas'] * 2.75 +  # CO2 per therm
                transport_details['Personal Car'] * 0.25 +  # CO2 per mile
                transport_details['Public Transit'] * 0.100 +  # CO2 per mile
                transport_details['Flight Miles'] * 0.15  # CO2 per mile
            ) #* (1 - energy_sources['Renewable Energy %']/100)
            
            # Convert emissions to Carbon Tax
            carbon_tax = total_emissions * 5  # ₹10 per ton of CO2
            
            st.session_state.total_personal_emissions = total_emissions
            st.session_state.carbon_tax = carbon_tax
            
            # Detailed Emissions Visualization
            emission_breakdown = pd.DataFrame({
                'Source': ['Electricity', 'Natural Gas', 'Personal Car', 'Public Transit', 'Flights'],
                'Emissions': [
                    energy_sources['Electricity'] * 0.475,
                    energy_sources['Natural Gas'] * 2.75,
                    transport_details['Personal Car'] * 0.25,
                    transport_details['Public Transit'] * 0.100,
                    transport_details['Flight Miles'] * 0.15
                ]
            })
            
            # Emissions Comparison with Global Emissions
            global_emissions = self.global_environmental_data['annual_co2_emissions'] * 1000000000  # Convert to kg
            
            comparison_fig = go.Figure(data=[
                go.Bar(name='Your Emissions', x=['Personal'], y=[total_emissions], marker_color='green'),
                go.Bar(name='Global Annual Emissions', x=['Global'], y=[global_emissions], marker_color='red')
            ])
            comparison_fig.update_layout(
                title='Your Emissions vs Global Annual Emissions',
                yaxis_title='CO2 Emissions (kg)',
                barmode='group'
            )
            
            #st.plotly_chart(comparison_fig)            
            # Innovative Feature: Carbon Emission Personality
            emission_personality = self._get_carbon_personality(total_emissions)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.bar(
                    emission_breakdown, 
                    x='Source', 
                    y='Emissions', 
                    title='Your Carbon Emission Sources'
                )
                st.plotly_chart(fig)
            
            with col2:
                st.success(f"Total Carbon Footprint: {total_emissions:.2f} kg CO2")
                st.warning(f"Calculated Carbon Tax: ₹{carbon_tax:.2f}")
                st.info(f"Carbon Personality: {emission_personality}")
    
    def _get_carbon_personality(self, emissions):
        """Assign a fun carbon emission personality"""
        personalities = [
            "🌱 Earth Whisperer (Low Emission)",
            "🍃 Green Guardian",
            "🌍 Climate Conscious Citizen",
            "🏭 Industrial Impact Maker",
            "🔥 Carbon Volcano (High Emission)"
        ]
        
        if emissions < 50:
            return personalities[0]
        elif emissions < 100:
            return personalities[1]
        elif emissions < 200:
            return personalities[2]
        elif emissions < 500:
            return personalities[3]
        else:
            return personalities[4]
    
    def carbon_credits_market(self):
        """Enhanced Carbon Credits Marketplace"""
        st.header("🌍 Carbon Credits Marketplace")
        
        st.write(f"Current Carbon Tax to Offset: ₹{st.session_state.carbon_tax:.2f}")
        st.write(f"Wallet Balance: ₹{st.session_state.wallet_balance:.2f}")
        
        # Display Daily Green Challenge if available
        if st.session_state.daily_green_challenge:
            st.info(f"Today's Green Challenge: {st.session_state.daily_green_challenge}")
        
        for credit_type, details in self.carbon_credits_marketplace.items():
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(credit_type)
                st.write(f"Carbon Offset: {details['offset_value']} kg CO2")
                st.write(f"Price: ₹{details['price']}")
                st.write(details['description'])
                st.write(f"Eco Bonus: {details['eco_bonus']}")
            
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
                            st.success(f"Purchased {credit_type}. Remaining Carbon Tax: ₹{st.session_state.carbon_tax:.2f}")
                    else:
                        st.error("Insufficient Wallet Balance")
    
    def wallet_management(self):
        """Enhanced Wallet Management with Card Validation"""
        st.header("💰 Wallet Management")
    
    # Default Card Details (to be used for validation)
        default_card = {
        'number': '1234567812345678',
        'expiry_month': '01',
        'expiry_year': '2026',
        'name': 'User'
        }
    
        st.subheader("Current Wallet Balance")
        st.write(f"₹{st.session_state.wallet_balance:.2f}")
    
        st.subheader("Add Money to Wallet")
    
    # Card Details Input with Empty Initial Values
        col1, col2 = st.columns(2)
    
        with col1:
            card_number = st.text_input("Card Number", value="")
            expiry_month = st.text_input("Expiry Month", value="")
    
        with col2:
            expiry_year = st.text_input("Expiry Year", value="")
            cardholder_name = st.text_input("Cardholder Name", value="")
        
        amount_to_add = st.number_input("Amount to Add (₹)", min_value=0, step=100)
        
        if st.button("Add Money"):
            # Validate card details against default credentials
            if (card_number == default_card['number'] and
                expiry_month == default_card['expiry_month'] and
                expiry_year == default_card['expiry_year'] and
                cardholder_name == default_card['name']):
                
                st.session_state.wallet_balance += amount_to_add
                st.success(f"Added ₹{amount_to_add} to Wallet")
            else:
                st.error("Invalid Card Details. Please use the correct credentials.")

    def rewards_section(self):
        """Enhanced Rewards and Supercoin Redemption"""
        st.header("🏆 Rewards Section")
        
        st.write(f"Total SuperCoins: {st.session_state.supercoins}")
        
        # Redeem SuperCoins (1% of total)
        redeemable_amount = st.session_state.supercoins * 0.1
        
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
                "🌳 Plant a Tree": 100,
                "💡 Carbon Credit Donation": 500,
                "🌞 Renewable Energy Support": 500
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
                st.success(f"Redeemed ₹{redeemable_amount:.2f}. SuperCoins Reset to 0.")
            else:
                st.warning("No SuperCoins available for redemption")
    
    # [Previous methods remain the same: login_page, carbon_footprint_calculator, etc.]
    
    def global_impact_dashboard(self):
        """Create a comprehensive global environmental impact dashboard with dynamic visualizations"""
        st.header("🌐 Global Environmental Impact Dashboard")
        
        # Historical CO2 Emissions Data (simulated with some real-world inspired values)
        historical_emissions = {
            'Global': [
                {'year': 2010, 'emissions': 33.0},
                {'year': 2012, 'emissions': 34.5},
                {'year': 2014, 'emissions': 35.6},
                {'year': 2016, 'emissions': 36.2},
                {'year': 2018, 'emissions': 37.1},
                {'year': 2020, 'emissions': 34.7},  # COVID-19 impact
                {'year': 2022, 'emissions': 36.4}
            ],
            'Personal': []
        }
        
        # User Consumption Data Input Section
        st.subheader("Additional Environmental Data")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            water_consumption = st.number_input("Monthly Water Consumption (m³)", min_value=0.0, value=0.0)
        
        with col2:
            electricity_consumption = st.number_input("Monthly Electricity (kWh)", min_value=0.0, value=0.0)
        
        with col3:
            waste_generation = st.number_input("Monthly Waste Generation (kg)", min_value=0.0, value=0.0)
        
        # Prepare Personal Emissions Data
        if st.button("Add to Dashboard"):
            # Add user's data point to personal emissions
            current_year = datetime.now().year
            personal_emissions_value = st.session_state.total_personal_emissions
            
            historical_emissions['Personal'].append({
                'year': current_year,
                'emissions': personal_emissions_value,
                'water_consumption': water_consumption,
                'electricity_consumption': electricity_consumption,
                'waste_generation': waste_generation
            })
        
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
        
        # Dynamic Emissions Comparison
        st.subheader("Emissions Trend Comparison")
        
        if historical_emissions['Personal']:
            # Prepare DataFrame for visualization
            global_df = pd.DataFrame(historical_emissions['Global'])
            personal_df = pd.DataFrame(historical_emissions['Personal'])
            
            # Emissions Trend Line Chart
            trend_fig = go.Figure()
            
            # Global Emissions Line
            trend_fig.add_trace(go.Scatter(
                x=global_df['year'], 
                y=global_df['emissions'], 
                mode='lines+markers', 
                name='Global Emissions'
            ))
            
            # Personal Emissions Line
            if not personal_df.empty:
                trend_fig.add_trace(go.Scatter(
                    x=personal_df['year'], 
                    y=personal_df['emissions'], 
                    mode='lines+markers', 
                    name='Personal Emissions'
                ))
            
            trend_fig.update_layout(
                title='CO2 Emissions Trend: Global vs Personal',
                xaxis_title='Year',
                yaxis_title='CO2 Emissions (billion tons)'
            )
            st.plotly_chart(trend_fig)
        
        # Additional Resource Consumption Visualization
        if historical_emissions['Personal']:
            st.subheader("Resource Consumption Analysis")
            
            # Prepare resource consumption data
            resource_df = pd.DataFrame(historical_emissions['Personal'])
            
            # Create subplots
            fig = go.Figure()
            
            # Water Consumption
            fig.add_trace(go.Bar(
                x=resource_df['year'], 
                y=resource_df['water_consumption'], 
                name='Water Consumption'
            ))
            
            # Electricity Consumption
            fig.add_trace(go.Bar(
                x=resource_df['year'], 
                y=resource_df['electricity_consumption'], 
                name='Electricity Consumption'
            ))
            
            # Waste Generation
            fig.add_trace(go.Bar(
                x=resource_df['year'], 
                y=resource_df['waste_generation'], 
                name='Waste Generation'
            ))
            
            fig.update_layout(
                title='Personal Resource Consumption',
                xaxis_title='Year',
                yaxis_title='Consumption',
                barmode='group'
            )
            
            st.plotly_chart(fig)
        
        # Environmental Impact Insights
        st.subheader("Environmental Impact Insights")
        
        if historical_emissions['Personal']:
            latest_personal_data = historical_emissions['Personal'][-1]
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Water Consumption", f"{latest_personal_data['water_consumption']:.2f} m³")
            
            with col2:
                st.metric("Electricity Consumption", f"{latest_personal_data['electricity_consumption']:.2f} kWh")
            
            with col3:
                st.metric("Waste Generation", f"{latest_personal_data['waste_generation']:.2f} kg")
    
    # Remaining methods from the previous implementation remain the same
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
            st.write(f"Total Carbon Tax: ₹{st.session_state.carbon_tax:.2f}")
        
        with col2:
            st.subheader("Financial Overview")
            st.write(f"Wallet Balance: ₹{st.session_state.wallet_balance:.2f}")
            st.write(f"Total SuperCoins: {st.session_state.supercoins}")
        
        # Environmental Impact Score
        st.subheader("Environmental Impact Score")
        impact_score = self._calculate_impact_score()
        st.progress(impact_score / 100)
        st.write(f"Your Impact Score: {impact_score}/100")
    
    def _calculate_impact_score(self):
        """Calculate user's environmental impact score"""
        base_score = 0  # Start with a median score
        
        # Adjust score based on emissions
        if st.session_state.total_personal_emissions < 2000:
            base_score += 100
        elif st.session_state.total_personal_emissions > 5000:
            base_score -= 100
        
        # Adjust for carbon offsets
        total_offset = sum(entry['offset_amount'] for entry in st.session_state.carbon_offset_history)
        base_score += min(total_offset / 100, 30)
        
        # Adjust for SuperCoins (indicating engagement)
        base_score += min(st.session_state.supercoins / 100, 10)
        
        return min(max(base_score, 0), 100)
    
    def crop_recommendation(self):
        """Advanced Crop Recommendation for Carbon Offset"""
        st.header("🌾 Crop Recommendation System")
        
        # Machine Learning Based Crop Recommendation
        st.subheader("ML-Powered Crop Recommendation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Soil Nutrient Inputs
            nitrogen = st.number_input("Nitrogen (N) Content", min_value=0.0, step=1.0, value=0.0)
            phosphorus = st.number_input("Phosphorus (P) Content", min_value=0.0, step=1.0, value=0.0)
            potassium = st.number_input("Potassium (K) Content", min_value=0.0, step=1.0, value=0.0)
        
        with col2:
            # Environmental Conditions
            temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1, value=0.0)
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)
        
        # Additional Inputs
        ph_value = st.slider("Soil pH Value", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0, value=0.0)
        
        # Carbon Offset Recommendation Section
        st.subheader("Carbon Offset Potential")
        
        # User's total emissions for context
        emissions = st.session_state.total_personal_emissions
        st.write(f"Your Total Carbon Emissions: {emissions:.2f} kg CO2")
        
        # Prediction Button
        if st.button("Predict Crop and Carbon Offset Potential"):
            # Prepare features for ML model
            features = [nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]
            
            # Check if model is loaded
            if self.crop_model:
                # Predict Crop
                crop = self.crop_model.predict([features])[0]
                
                # Crop-specific carbon absorption rates
                crop_carbon_rates = {
                    'Rice': 0.5, 
                    'Wheat': 0.4, 
                    'Corn': 0.6, 
                    'Soybean': 0.3,
                    'Potato': 0.2,
                    'Tomato': 0.15,
                    'Cotton': 0.35
                }
                
                # Calculate potential carbon offset
                absorption_rate = crop_carbon_rates.get(crop, 0.25)  # Default rate if crop not found
                potential_offset = absorption_rate * 100  # Assuming 100 plants
                
                # Display Results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.success(f"Recommended Crop: {crop}")
                    st.write("Input Features:")
                    input_df = pd.DataFrame([features], 
                        columns=['Nitrogen', 'Phosphorus', 'Potassium', 
                                 'Temperature', 'Humidity', 'pH Value', 'Rainfall'])
                    st.dataframe(input_df)
                
                with col2:
                    st.metric("Potential CO2 Offset", f"{potential_offset:.2f} kg")
                    st.info(f"By planting {crop}, you can offset approximately {potential_offset:.2f} kg of CO2")
                    
                    # Compare with user's emissions
                    offset_percentage = (potential_offset / emissions) * 100 if emissions > 0 else 0
                    st.warning(f"This crop can offset {offset_percentage:.2f}% of your carbon emissions")
            else:
                st.error("Crop Recommendation Model not available. Please load the model.")
        
        # Additional Guidance
        st.markdown("### 🌱 Crop Selection Tips")
        st.write("""
        - Input accurate soil and environmental data
        - Consider local climate conditions
        - Consult local agricultural experts
        - Rotate crops to maintain soil health
        """)

    def run(self):
        """Main Application Workflow"""
        if not st.session_state.logged_in:
            self.login_page()
        else:
            st.sidebar.title(f"Welcome, {st.session_state.username}")
            
            # Sidebar Navigation with Emojis
            menu_options = [
                "💨 Carbon Footprint Calculator", 
                "🌍 Carbon Credits Market", 
                "💰 Wallet Management", 
                "🏆 Rewards", 
                "🌐 Global Impact Dashboard",
                "🌱 Environmental Contribution",
                "🌾 Crop Recommendation",
                "👤 Profile"
            ]
            
            choice = st.sidebar.radio("Navigation", menu_options)
            
            if st.sidebar.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
            
            # Main Content Area
            if choice == "💨 Carbon Footprint Calculator":
                self.carbon_footprint_calculator()
            elif choice == "🌍 Carbon Credits Market":
                self.carbon_credits_market()
            elif choice == "💰 Wallet Management":
                self.wallet_management()
            elif choice == "🏆 Rewards":
                self.rewards_section()
            elif choice == "🌐 Global Impact Dashboard":
                self.global_impact_dashboard()
            elif choice == "🌱 Environmental Contribution":
                self.environmental_contribution_tracker()
            elif choice == "🌾 Crop Recommendation":
                self.crop_recommendation()
            elif choice == "👤 Profile":
                self.profile_section()

def main():
    platform = ComprehensiveSustainabilityPlatform()
    platform.run()

if __name__ == "__main__":
    main()
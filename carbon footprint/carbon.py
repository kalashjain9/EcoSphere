import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

# Carbon Emission Factors (example values)
EMISSION_FACTORS = {
    'electricity': 0.5,  # kg CO2 per kWh
    'natural_gas': 0.2,  # kg CO2 per cubic meter
    'diesel': 2.68,      # kg CO2 per liter
    'petrol': 2.31,      # kg CO2 per liter
}

# Carbon Credits for Plants
CARBON_CREDITS = {
    'Tree Types': {
        'Pine': 22,       # kg CO2 per year
        'Oak': 20,        # kg CO2 per year
        'Maple': 18,      # kg CO2 per year
        'Eucalyptus': 25, # kg CO2 per year
    },
    'Crop Types': {
        'Bamboo': 15,     # kg CO2 per year
        'Miscanthus': 12, # kg CO2 per year
        'Hemp': 10,       # kg CO2 per year
    }
}

class CarbonFootprintCalculator:
    def __init__(self):
        self.carbon_tax_rate = 50  # $ per ton of CO2

    def calculate_household_emissions(self, electricity_consumption, gas_consumption):
        electricity_emissions = electricity_consumption * EMISSION_FACTORS['electricity']
        gas_emissions = gas_consumption * EMISSION_FACTORS['natural_gas']
        return electricity_emissions + gas_emissions

    def calculate_transport_emissions(self, diesel_consumption, petrol_consumption):
        diesel_emissions = diesel_consumption * EMISSION_FACTORS['diesel']
        petrol_emissions = petrol_consumption * EMISSION_FACTORS['petrol']
        return diesel_emissions + petrol_emissions

    def calculate_carbon_tax(self, total_emissions):
        return total_emissions * (self.carbon_tax_rate / 1000)  # Convert to $/kg

    def suggest_carbon_offset_plants(self, carbon_tax):
        carbon_to_offset = carbon_tax / (self.carbon_tax_rate / 1000)
        
        # Prioritize plants based on carbon sequestration
        sorted_credits = sorted(
            [(plant, credits) for category in CARBON_CREDITS.values() for plant, credits in category.items()], 
            key=lambda x: x[1], 
            reverse=True
        )
        
        recommended_plants = []
        total_offset = 0
        
        for plant, credits in sorted_credits:
            if total_offset < carbon_to_offset:
                recommended_plants.append(plant)
                total_offset += credits
        
        return recommended_plants

def main():
    st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍")
    
    # Initialize calculator
    calculator = CarbonFootprintCalculator()
    
    # Sidebar Navigation
    st.sidebar.title("Carbon Footprint Dashboard")
    menu = st.sidebar.radio("Navigation", 
        ["Home", "Emissions Calculator", "Carbon Market", "Offset Strategies", "Impact Visualization"]
    )
    
    if menu == "Home":
        st.title("Sustainable Carbon Footprint Platform")
        st.write("""
        ## Understand, Calculate, and Offset Your Carbon Emissions
        
        Our platform helps you:
        - Track your household and transportation carbon footprint
        - Calculate your carbon tax
        - Find personalized carbon offset strategies
        - Explore sustainable plant options
        """)
        
        # Quick stats
        col1, col2, col3 = st.columns(3)
        col1.metric("Global Avg Emissions", "4.5 tons/person/year")
        col2.metric("Carbon Tax Rate", "$50/ton CO2")
        col3.metric("Global Goal", "Net Zero by 2050")
    
    elif menu == "Emissions Calculator":
        st.header("Carbon Emissions Calculator")
        
        # Household Emissions
        st.subheader("Household Emissions")
        col1, col2 = st.columns(2)
        with col1:
            electricity = st.number_input("Monthly Electricity Consumption (kWh)", min_value=0.0, value=300.0)
        with col2:
            gas = st.number_input("Monthly Gas Consumption (m³)", min_value=0.0, value=50.0)
        
        # Transport Emissions
        st.subheader("Transportation Emissions")
        col1, col2 = st.columns(2)
        with col1:
            diesel = st.number_input("Monthly Diesel Consumption (Liters)", min_value=0.0, value=20.0)
        with col2:
            petrol = st.number_input("Monthly Petrol Consumption (Liters)", min_value=0.0, value=30.0)
        
        # Calculate Emissions
        if st.button("Calculate Carbon Footprint"):
            household_emissions = calculator.calculate_household_emissions(electricity, gas)
            transport_emissions = calculator.calculate_transport_emissions(diesel, petrol)
            total_emissions = household_emissions + transport_emissions
            carbon_tax = calculator.calculate_carbon_tax(total_emissions)
            offset_plants = calculator.suggest_carbon_offset_plants(carbon_tax)
            
            st.subheader("Emissions Results")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Emissions", f"{total_emissions:.2f} kg CO2")
            col2.metric("Carbon Tax", f"${carbon_tax:.2f}")
            col3.metric("Offset Plants", f"{len(offset_plants)} suggested")
            
            st.write("Recommended Offset Plants:", ", ".join(offset_plants))
    
    elif menu == "Carbon Market":
        st.header("Carbon Credits Marketplace")
        
        # Display Carbon Credits
        st.subheader("Available Carbon Credits")
        market_data = []
        for category, plants in CARBON_CREDITS.items():
            for plant, credits in plants.items():
                market_data.append({
                    'Category': category, 
                    'Plant': plant, 
                    'Carbon Credits (kg/year)': credits,
                    'Price': f"${credits * 0.5:.2f}"
                })
        
        df = pd.DataFrame(market_data)
        st.dataframe(df)
        
        # Visualization
        fig = px.bar(df, x='Plant', y='Carbon Credits (kg/year)', 
                     color='Category', title='Carbon Sequestration by Plant')
        st.plotly_chart(fig)
    
    elif menu == "Offset Strategies":
        st.header("Carbon Offset Strategies")
        
        strategies = [
            {"name": "Tree Planting", "impact": "High", "cost": "Medium", "difficulty": "Easy"},
            {"name": "Urban Gardening", "impact": "Medium", "cost": "Low", "difficulty": "Easy"},
            {"name": "Solar Panel Installation", "impact": "Very High", "cost": "High", "difficulty": "Complex"}
        ]
        
        st.table(pd.DataFrame(strategies))
    
    elif menu == "Impact Visualization":
        st.header("Global Carbon Impact Visualization")
        
        # Sample data for visualization
        emissions_data = pd.DataFrame({
            'Country': ['USA', 'China', 'India', 'Russia', 'Japan'],
            'Annual Emissions (Million Tons)': [5000, 10000, 2500, 1800, 1200]
        })
        
        fig = px.pie(emissions_data, values='Annual Emissions (Million Tons)', names='Country', 
                     title='Global Carbon Emissions Distribution')
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
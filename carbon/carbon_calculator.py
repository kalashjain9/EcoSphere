def calculate_carbon_footprint(house_energy, household_fuel, transport_fuel):
    """
    Calculate carbon footprint based on energy and fuel consumption
    """
    # Carbon emission factors
    house_emission = house_energy * 0.5  # kg CO2 per kWh
    household_fuel_emission = household_fuel * 2.5  # kg CO2 per liter
    transport_emission = transport_fuel * 2.3  # kg CO2 per liter
    
    # Total carbon footprint
    total_carbon_footprint = (
        house_emission + 
        household_fuel_emission + 
        transport_emission
    )
    
    return total_carbon_footprint
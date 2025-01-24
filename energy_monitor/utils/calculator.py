def calculate_carbon_footprint(electricity, gas, water):
    electricity_factor = 0.92  # kg CO2/kWh
    gas_factor = 2.3          # kg CO2/liter
    water_factor = 0.36       # kg CO2/liter
    
    total = (electricity * electricity_factor +
             gas * gas_factor +
             water * water_factor)
    return round(total, 2)

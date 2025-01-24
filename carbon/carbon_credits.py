def get_carbon_credits_marketplace():
    """
    Generate a marketplace of carbon offset options
    """
    carbon_credits = [
        {
            'name': 'Tree Planting',
            'credits': 50,
            'description': 'Native forest tree planting',
            'cost_per_credit': 5
        },
        {
            'name': 'Bamboo Grove',
            'credits': 30,
            'description': 'Fast-growing bamboo plantation',
            'cost_per_credit': 3
        },
        {
            'name': 'Mangrove Restoration',
            'credits': 75,
            'description': 'Coastal mangrove ecosystem restoration',
            'cost_per_credit': 7
        }
    ]
    
    return carbon_credits
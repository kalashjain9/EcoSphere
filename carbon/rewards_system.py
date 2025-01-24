import pandas as pd

class RewardsSystem:
    """
    Manage user rewards and supercoin tracking
    """
    def __init__(self, initial_supercoins=0):
        self.supercoins = initial_supercoins
        self.redemption_history = []
    
    def earn_supercoins(self, carbon_offset):
        """
        Calculate supercoins earned based on carbon offset
        """
        supercoins_earned = int(carbon_offset / 10)
        self.supercoins += supercoins_earned
        return supercoins_earned
    
    def redeem_supercoins(self, amount):
        """
        Redeem supercoins for monetary value
        """
        if amount <= self.supercoins:
            money_value = amount * 0.01  # 1% conversion
            self.supercoins -= amount
            
            redemption_record = {
                'amount': amount,
                'money_value': money_value,
                'timestamp': pd.Timestamp.now()
            }
            self.redemption_history.append(redemption_record)
            
            return money_value
        else:
            raise ValueError("Insufficient SuperCoins")
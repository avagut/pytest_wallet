"""Create a wallet app for learning about pytest."""


class InsufficientAmount(Exception):
    pass
    
class Wallet(object):
    """Wallet object to handle add cash and spend cash."""
    def __init__(self,initialamount=0):
        """Set up the initial amount in the wallet"""
        self.balance = initialamount
    def add_cash(self, cash_amount):
        """Add the passed amount to the current balance"""
        self.balance += cash_amount
        
    def spend_cash(self, cash_amount):
        """Add the passed amount to the current balance"""
        if cash_amount > self.balance:
            raise InsufficientAmount('Available Balance not enough to spend Ksh. {}'.format(cash_amount))
        self.balance -= cash_amount

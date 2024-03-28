from interfaces.flow import IFlow
from classes.account import Account


# Dummy data
import json

with open("data/account.json", 'r') as f:
    data = json.load(f)
# Create an Account object
acc = Account(data['id'], data['amount'])


class BalanceCheckFlow(IFlow):
    """This class represents the balance checking flow."""

    def execute(self, input, session_id):
        # Implement the logic for balance checking
        print("Please provide your account details")
        # Get account details from the database

        
        # Get the account ID from obtained account details
        account_id = acc.get_id()

        # Get the balance of the account
        

        # Return the balance
        return "Your balance is $100."
    



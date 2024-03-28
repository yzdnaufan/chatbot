from interfaces.flow import IFlow

class BalanceCheckFlow(IFlow):
    """This class represents the balance checking flow."""

    def execute(self, input, session_id):
        # Implement the logic for balance checking
        return "Your balance is $100."


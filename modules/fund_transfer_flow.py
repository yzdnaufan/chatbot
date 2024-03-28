from classes.context_manager import ContextManager
from interfaces.flow import IFlow

class FundTransferFlow(IFlow):
    """
    This class represents the flow for handling fund transfers in the chatbot.
    """

    def execute(self, input, session_id):
        # Implement the logic for each step in the fund transfer flow
        
        if "confirm" in input.lower():
            return "Fund transfer confirmed."
        else:
            return "Please confirm the fund transfer."

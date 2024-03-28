from interfaces.bot import IBotService
from services.banking import BankingService
from services.flow import FlowManager

class BankingChatbot(IBotService):
    """
    A chatbot class that manages the flow of conversation for a banking service. It uses a FlowManager to process queries and a BankingService for banking operations.
    """

    def __init__(self, banking_service: BankingService, flow_manager: FlowManager) -> None:
        """
        Initializes a new instance of the BankingChatbot class.

        Args:
            banking_service (BankingService): The banking service to use for banking operations.
            flow_manager (FlowManager): The flow manager to use for processing queries.
        """
        self.banking_service = banking_service
        self.flow_manager = flow_manager

    def respond_to_query(self, query, session_id):
        """
        Responds to a query by processing it through the flow manager and returning the response.

        Args:
            query (str): The query to respond to.
            session_id (str): The session id for the current chat session.

        Returns:
            str: The response from the flow manager.
        """
        # Delegate the flow management to the flow manager service
        flow_response = self.flow_manager.process_query(query, session_id)

        # The chatbot can further process the flow response or directly return it
        return flow_response
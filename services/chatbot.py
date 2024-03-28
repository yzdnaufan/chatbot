from interfaces.bot import IBotService
from services.banking import BankingService
from services.flow import FlowManager

from random import randint
import json

# Dummy session data
with open("data/session.json", 'r') as f:
    data = (json.load(f))


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
        self.session_id = None
        self.session = None 

    def initiate(self, session_id= None) :
        print("Initiating session")
        print(f"session_id: {session_id}")
        if session_id :
            self.session_id = session_id
            try:
                self.session = data[self.session_id]
            except KeyError:
                self.session = {
                    'data': {
                        "message":[],
                        "active": True
                    }
                }
        
        while self.session_id == None or self.session_id not in data:
            self.session_id = str(randint(10000, 99999))
            self.session = {
                'data': {
                    "message":[],
                    "active": True
                }
            }
        print(data[self.session_id])

        if self.session_id not in data:
            print("Creating new session")
            with open("data/session.json", 'w') as f:
                data[self.session_id] = self.session
                json.dump(data, f)

        print("Hi, I'm a chat bot, how can I help you?")
        return None
    




    def respond_to_query(self, query):
        """
        Responds to a query by processing it through the flow manager and returning the response.

        Args:
            query (str): The query to respond to.
            session_id (str): The session id for the current chat session.

        Returns:
            str: The response from the flow manager.
        """
        # Delegate the flow management to the flow manager service
        flow_response = self.flow_manager.process_query(query, self.session_id)

        # The chatbot can further process the flow response or directly return it
        return flow_response
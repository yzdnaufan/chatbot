from services.flow import FlowManager
from services.banking import BankingService
from services.chatbot import BankingChatbot

# Initialize services
banking_service = BankingService()
flow_manager = FlowManager()
chatbot = BankingChatbot(banking_service, flow_manager)

# database_client = DatabaseClient()

# Simulate conversation
def bubble(q, current_chatbot: BankingChatbot):
    print(f"user : {q}")
    print(f"bot : {current_chatbot.respond_to_query(q)}")

session_id = "12345"

chatbot.initiate(session_id)
q = "I want to know my balance"
bubble(q, chatbot)
q = "123456 is my account"
bubble(q, chatbot)

def query(message: str, session_id: str):
    chatbot.initiate(session_id)
    response = chatbot.respond_to_query(message)

    # DatabaseClient(session_id).append_context(message, response)
    

    print(f"user : {message}")
    print(f"bot : {response}")


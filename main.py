from services.flow import FlowManager
from services.banking import BankingService
from services.chatbot import BankingChatbot

# Initialize services
banking_service = BankingService()
flow_manager = FlowManager()
chatbot = BankingChatbot(banking_service, flow_manager)

# Simulate conversation
session_id = "user123"
print(chatbot.respond_to_query("I want to know my balance", session_id))
print(chatbot.respond_to_query("123456 is my account", session_id))
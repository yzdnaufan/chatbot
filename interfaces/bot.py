from abc import ABC, abstractmethod

# Interface for chatbot services
class IBotService(ABC):
    @abstractmethod
    def respond_to_query(self, query):
        pass

    # @abstractmethod
    # def get_response(self, query):
    #     pass

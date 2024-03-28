from abc import ABC, abstractmethod

class IFlow(ABC):
    @abstractmethod
    def execute(self, user_id, context_manager, message):
        pass
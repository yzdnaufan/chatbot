from abc import ABC, abstractmethod

# Interface for banking services
class IBankingService(ABC):
    @abstractmethod
    def transfer_funds(self, from_account, to_account, amount):
        pass

    @abstractmethod
    def check_balance(self, account):
        pass

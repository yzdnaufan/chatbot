from classes.transaction import Transaction
from classes.account import Account

from interfaces.banking import IBankingService

# Implementation of banking services
class BankingService(IBankingService):
    """
    A class that provides banking services such as transferring funds and checking balance.
    """

    def transfer_funds(self, transaction: Transaction, amount: float):
        """
        Transfers funds from one account to another.

        Args:
            transaction (Transaction): The transaction details.
            amount (float): The amount to be transferred.

        Returns:
            str: A message indicating the success or failure of the transfer.
        """
        if transaction.from_account.balance >= amount:
            transaction.from_account.balance -= amount
            transaction.to_account.balance += amount
            return f"Transferred {amount} from {transaction.from_account.id} to {transaction.to_account.id} with method {transaction.method}"
        return "Insufficient funds"

    def check_balance(self, account: Account):
        """
        Checks the balance of an account.

        Args:
            account (Account): The account to check the balance for.

        Returns:
            str: A message displaying the account balance.
        """
        return f"Account balance for {account.id}: {account.balance}"

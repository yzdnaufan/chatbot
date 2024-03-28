from classes.account import Account

class Transaction:
    """
    Represents a transaction between two accounts.

    Attributes:
        from_account (Account): The account from which the transaction is made.
        to_account (Account): The account to which the transaction is made.
        amount (int): The amount of money involved in the transaction.
        method (str): The method used for the transaction.
    """

    def __init__(self, from_account: Account, to_account: Account, amount: int, method: str) -> None:
        self.to = to_account
        self.from_account = from_account
        self.amount = amount
        self.method = method
    

    
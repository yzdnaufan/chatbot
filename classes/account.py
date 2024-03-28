class Account:
    """
    Represents a bank account.

    Attributes:
        id (str): The unique identifier of the account.
        balance (float): The current balance of the account.
    """

    def __init__(self, id : str, balance : int) -> None:
        self.id = id
        self.balance = balance

    def __str__(self) -> str:
        return f"Account ID: {self.id}, Balance: {self.balance}"
    
    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance
    
    def get_id(self):
        """
        Get the unique identifier of the account.

        Returns:
            int: The unique identifier of the account.
        """
        return self.id
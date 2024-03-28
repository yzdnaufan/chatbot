class Account :
    def __init__(self, id, balance) -> None:
        self.id = id
        self.balance = balance

    def __str__(self) -> str:
        return f"Account ID: {self.id}, Balance: {self.balance}"
    
    def get_balance(self):
        return self.balance
    
    def get_id(self):
        return self.id
from client import Client
class Account:
    client = Client('', '')
    def __init__(self, accountNumber, balance = 0):
        self.accountNumber = accountNumber
        self.balance = balance



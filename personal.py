from datetime import datetime

from bank import Amount

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transaction = []
    def deposit(self, amount: float):
        if amount <=0:
            raise ValueError("Deposit amount should be positive.")
        transaction = Amount(amount, datetime.now)
        self.transaction.append(transaction)
        self.balance += amount
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise ValueError("You have not enough balance")
        transaction = Amount(amount,datetime.now(), "Withdrawal")
        self.transaction.append(transaction)
        self.balance -= amount
    def print_transaction_history(self):
        if not self.transaction:
            print("No transaction")
        else:
            for transaction in self.transaction:
                print(transaction)


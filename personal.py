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
        transaction = Amount(amount, "WITHDRAWAL")
        self.transaction.append(transaction)
        self.balance -= amount
    def print_transaction_history(self):
        if not self.transaction:
            print("No transaction")
        else:
            for transaction in self.transaction:
                print(transaction)
    def get_balance(self):
        return self.balance
    def get_account_number(self):
        return self.account_number
    def set_account_number(self, account_number: int):
        self.account_number = account_number
    def get_account_holder(self):
        return self.account_holder
    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder
    def __str__(self):
        return f'Account number{self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance: .2f}'
    def __add__(self, amount: float):
        self.deposit(amount)
        return self
    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self
from bank import Amount
from personal import PersonalAccount

if __name__ == "__main__":
    account = PersonalAccount(123456, "Aaa Bbb")
    account.deposit(231)
    account.withdraw(63)
    print(f"Current Balance: ${account.get_balance():.2f}")
    print("\nTransaction History:")
    account.print_transaction_history()
    print(f"\nUpdated Balance: ${account.get_balance():.2f}")
    print("\nUpdated Transaction History:")
    account.print_transaction_history()
    print(account)
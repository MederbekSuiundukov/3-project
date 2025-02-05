from bank import Amount
from personal import PersonalAccount

if __name__ == "__main__":
    account = PersonalAccount(123456, "Aaa Bbb")
    deposit = Amount(231, "DEPOSIT")
    withdrawal = Amount(63, "WITHDRAWAL")
    print(f"Current Balance: ${account.get_balance():.2f}")
    print("\nTransaction History:")
    account.print_transaction_history()
    account += 500.00
    account -= 100.00
    print(f"\nUpdated Balance: ${account.get_balance():.2f}")
    print("\nUpdated Transaction History:")
    account.print_transaction_history()
class BankAccount_kwap:
    def __init__(self_kwap, balance_kwap):
        self_kwap.__balance = balance_kwap

    def deposit_kwap(self_kwap, amount_kwap):
        self_kwap.__balance += amount_kwap

    def withdraw_kwap(self_kwap, amount_kwap):
        if amount_kwap <= self_kwap.__balance:
            self_kwap.__balance -= amount_kwap
        else:
            print("Insufficient funds")

    def get_balance_kwap(self_kwap):
        return self_kwap.__balance


account_kwap = BankAccount_kwap(5000)
account_kwap.deposit_kwap(1000)
account_kwap.withdraw_kwap(2000)
print("Balance_kwap:", account_kwap.get_balance_kwap())

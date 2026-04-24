class BankAccount_kwap:
    def __init__(self_kwap, account_name_kwap, balance_kwap):
        self_kwap.account_name_kwap = account_name_kwap
        self_kwap.balance_kwap = balance_kwap
    
    def deposit_kwap(self_kwap, amount_kwap):
        self_kwap.balance_kwap += amount_kwap
        print("Deposit successful")
    
    def withdraw_kwap(self_kwap, amount_kwap):
        if amount_kwap <= self_kwap.balance_kwap:
            self_kwap.balance_kwap -= amount_kwap
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_kwap(self_kwap):
        print("Balance:", self_kwap.balance_kwap)


account_kwap = BankAccount_kwap("Juan", 5000)
account_kwap.deposit_kwap(1000)
account_kwap.withdraw_kwap(2000)
account_kwap.display_balance_kwap()

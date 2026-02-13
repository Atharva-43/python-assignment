class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Account Number:", self.account_no)
        print("Current Balance:", self.balance)
# ---- Example usage ----
acc1 = BankAccount(12345, 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.check_balance()

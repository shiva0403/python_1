class MinimumBalanceError(Exception):
    pass

class Account:
    AccNumber = 1001
    def __init__(self, name, balance=1000):
        if(balance < 1000):
            raise MinimumBalanceError("Minimum balance should be 1000")
        self.name = name
        self.balance = balance
        self.account_number = Account.AccNumber
        Account.AccNumber += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError("Amount cannot be withdrawn, minimum balance should be 1000")
        self.balance -= amount

    def show_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

a1 = Account("John", 2000)
a1.show_details()
a1.deposit(1000)
a1.show_details()
a1.withdraw(500)
a1.show_details()
a2 = Account("Jane", 5000)
a2.show_details()
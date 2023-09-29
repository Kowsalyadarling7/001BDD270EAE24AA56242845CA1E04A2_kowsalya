class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

# Create instances of BankAccount
account1 = BankAccount("John Doe")
account2 = BankAccount("Jane Smith", 1000)

# Test deposit and withdrawal functionality
print(account1.deposit(500))
print(account2.withdraw(200))
print(account1.withdraw(1000))

class BankAccount:
    def __init__(self, user, balance, months):
        self.user = user
        self.balance = balance
        self.months = months

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def interest(self):
        earn = self.balance * 0.04 * (self.months / 12)
        self.balance += earn
        return earn


user1 = SavingsAccount("John", 100, 2)

print(f'''
Account Holder: {user1.user}
Initial Balance: {user1.balance}
Interest ({user1.months} month period): {user1.interest():.2f}
Interest + Balance: {user1.balance:.2f}
Deposit 50: {user1.deposit(50):.2f}
Withdraw 34: {user1.withdraw(34):.2f}''')

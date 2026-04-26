class BankAccount:
    accounts_made = 0

    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

        BankAccount.accounts_made += 1

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}php deposited")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdraw amount more than balance")
            return
        self.__balance -= amount
        print(f"{amount}php withdrawn")

    def get_balance(self):
        return f"Balance: {self.__balance}php"

    def transfer(self, receiver, amount):
        if amount > self.__balance:
            print("Insufficient funds, transfer failed")
            return

        self.__balance -= amount
        receiver._BankAccount__balance += amount

        print(f"Transferred {amount}php to {receiver.__holder_name}")


user1 = BankAccount("12345", "Clifford", 69420)
user2 = BankAccount("67898", "Adrian", 67)

user1.deposit(420)
user1.deposit(800135)
user1.withdraw(124)
user1.withdraw(1000000000)
user1.transfer(user2, 5)

user2.deposit(5138008)
user2.deposit(1)
user2.withdraw(124)
user2.withdraw(1000000000)



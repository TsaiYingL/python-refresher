class Bankaccount:
    def __init__(self, name, acc_num=0, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def withdraw(self, num):
        self.balance -= num
        print(f"{self.name} has ${self.balance} in account.")

    def deposit(self, num):
        self.balance += num
        print(f"{self.name} has ${self.balance} in account.")

    def current_balance(self):
        print(f"{self.name} has ${self.balance} in account.")

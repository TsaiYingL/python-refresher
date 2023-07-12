class Bankaccount:
    def __init__(self, name, acc_num, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def withdraw(self, num):
        if self.balance - num >= 0:
            self.balance -= num
            return f"{self.name} has ${self.balance} in account."
        else:
            return "Invalid withdraw"

    def deposit(self, num):
        self.balance += num
        return f"{self.name} has ${self.balance} in account."

    def current_balance(self):
        return f"{self.name} has ${self.balance} in account."


if __name__ == "__main__":
    account = Bankaccount("Tsai", 1234567)
    account.deposit(100)

# Debug:
# what if adding/taking out negative num
# __init__: entering numbers instead of letters for name (or the other way around)
# comments and documentation
# the f"..." is a formatting string
# testing****
# when importing packets, it allows you to use the classes in the packet
# if __name__ == "__main__":

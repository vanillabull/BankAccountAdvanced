amount = 0

class BankAccount:
    def __init__(self, owner, balance=0, ):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self):
        while True:
            try:
                deposit_amount = int(input("Deposit desired amount: "))
                self.balance += deposit_amount
                self.history.append(f"Deposited: {deposit_amount}")
                break
            except ValueError:
                print("Please enter in form of numbers")
    def withdraw(self):
        while True:
            try:
                withdraw_amount = int(input("Withdraw desired amount: "))
                if self.balance < withdraw_amount:
                    print("You have insufficient funds.")
                else:
                    print("Amount withdrawn.")
                    self.balance -= withdraw_amount
                    self.history.append(f"Withdrew: {withdraw_amount}")
                    break
            except ValueError:
                print("Please enter a number")
    def show_summary(self):
        print(f"---- {self.owner}'s Account ----")
        print("Current Balance:", self.balance)
        for item in self.history:
            print("-", item)
        
acc = BankAccount("Alex", 100)
acc.deposit()
acc.withdraw()
acc.show_summary()
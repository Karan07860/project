class BankAccount():
    def __init__(self, account_number, account_holder_name,balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance+=amount
        print(f"deposit initiated. Balance is now ${self.balance}")
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f" withdraw initiated. balance is now ${self.balance}")
        
    def check_balance(self):
        print(f"balance is now${self.balance}")
account_1 = BankAccount(567, "Amit", 70)
account_1.deposit(30)
account_1.withdraw(10)
account_1.check_balance()
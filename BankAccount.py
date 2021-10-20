class BankAccount: 
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
    
    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def add_interest(self):
        pass

    def print_statement(self):
        pass
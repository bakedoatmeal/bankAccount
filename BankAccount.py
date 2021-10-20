class BankAccount: 
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance: 
            print("Insufficient funds")
            new_balance = self.balance - amount
            self.balance = new_balance
            return 
            
        new_balance = self.balance - amount
        self.balance = new_balance
        print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self):
        print(f"The current account balance is ${self.balance}")
        return self.balance

    def add_interest(self):
        pass

    def print_statement(self):
        pass

mitchell_account = BankAccount("Mitchell", 3141592, 0)
mitchell_account.deposit(400000)

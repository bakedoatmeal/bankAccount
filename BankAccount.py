class BankAccount: 
    def __init__(self, full_name, account_number, balance, account_type):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        bank.append(self)

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        print(f"Amount deposited: ${amount} new balance: ${self.format_print_balance()}")

    def withdraw(self, amount):
        if amount > self.balance: 
            print("Insufficient funds.")
            new_balance = self.balance - 10
            self.balance = new_balance
            print(f"You have been charged an overdraft fee of $10.00. New balance: ${self.format_print_balance()}")
            return 
            
        new_balance = self.balance - amount
        self.balance = new_balance
        print(f"Amount withdrawn: ${amount} new balance: ${self.format_print_balance()}")

    def get_balance(self):
        print(f"The current account balance is ${self.balance}")
        return self.balance

    def add_interest(self):
        if self.account_type == "checking":
            interest_rate = 0.00083
        else:
            interest_rate = 0.0001
        new_balance = self.balance * 1 - self.balance * interest_rate
        self.balance = new_balance
        print(f"Interest has been charged! New balance: {self.format_print_balance()}")

    def print_statement(self):
        print(self.full_name)
        account_string = str(self.account_number)
        print(f"Account No.: ****{account_string[-4: len(account_string)]}")
        print(f"Balance: ${self.format_print_balance()}")

    def format_print_balance(self):
        balance_string = self.balance
        balance_string = "{:.2f}".format(balance_string)
        return balance_string

bank = []

mitchell_account = BankAccount("Mitchell", 3141592, 0, "savings")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

jane_account = BankAccount("Jane", 3141593, 2000, "checking")
ara_account = BankAccount("Ara", 3141594, 2000, "savings")
ara_account.add_interest()
jane_account.add_interest()
jane_account.print_statement()
ara_account.print_statement()

for account in bank: 
    account.add_interest()
    account.print_statement()


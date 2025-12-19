# 1. Bank Account Simulation**

# Problem:

# Design a `BankAccount` class with attributes like:

# - Account Number
# - Account Holder Name
# - Balance

# Add methods to:

# 1. Deposit money.
# 2. Withdraw money (ensure sufficient balance).
# 3. Display account details.

# **Hint:**  implement appropriate validations.

class Bank:
    def __init__(self,account_name,account_num,account_balance):
        self.account_number = account_num
        self.holder_name = account_name
        self.balance = account_balance

    def deposit_money(self, deposit_amount):
        self.balance += deposit_amount
        print("Account balance = $",self.balance)

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("You don't have sufficient balance.")
            print("Account balance = $",self.balance)
        else:
            self.balance -= withdraw_amount
            print("Account balance = $",self.balance)
    
    def account_details(self):
        print(f"""
    -----------------------------------------------
        Account Holder Name: {self.holder_name}
        Account Number: {self.account_number}
        Account Balance: $ {self.balance}
    -----------------------------------------------
        """)

account_1 = Bank("Om Joshi", 243823463, 500)

account_1.deposit_money(300)
account_1.withdraw_money(400)
account_1.withdraw_money(500)
account_1.account_details()
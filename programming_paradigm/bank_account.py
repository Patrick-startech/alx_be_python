class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional starting balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

 

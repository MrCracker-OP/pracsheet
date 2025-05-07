class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

# Example usage
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount("1234567890", "John Doe", 1000.00)

    # Print account info
    print(account.get_account_info())

    # Deposit money
    account.deposit(500.00)

    # Withdraw money
    account.withdraw(200.00)

    # Attempt to withdraw more than the balance
    account.withdraw(2000.00)

    # Print the final balance
    print(f"Final balance: ${account.get_balance():.2f}")

def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit_money(balance):
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} has been deposited to your account.")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw_money(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount:.2f} has been withdrawn from your account.")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

def atm_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Ask user to enter their initial balance
balance = float(input("Enter your initial balance: $"))

while True:
    atm_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        check_balance(balance)
    elif choice == '2':
        balance = deposit_money(balance)
        check_balance(balance)
    elif choice == '3':
        balance = withdraw_money(balance)
        check_balance(balance)
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please try again.")
def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 0.50
    elif units <= 200:
        bill = (100 * 0.50) + ((units - 100) * 0.75)
    elif units <= 300:
        bill = (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.20)
    else:
        bill = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)
    return bill

# Ask user to input the number of units consumed
units = int(input("Enter the number of units consumed: "))

# Calculate and print the total bill amount
total_bill = calculate_electricity_bill(units)
print(f"The total electricity bill for {units} units is: ${total_bill:.2f}")

# Define the recursive function to calculate the sum of the digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Take an integer input from the user
number = int(input("Enter an integer: "))

# Display the sum of the digits
print(f"The sum of the digits of {number} is: {sum_of_digits(number)}")

# Define the recursive function to find the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take an integer input from the user representing the number of terms
terms = int(input("Enter the number of terms: "))

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

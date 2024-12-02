# Define the recursive function to find GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
1
# Take two integer inputs from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the GCD of the two numbers
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

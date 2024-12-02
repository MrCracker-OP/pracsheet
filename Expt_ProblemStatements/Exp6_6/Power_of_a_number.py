# Define the recursive function to calculate power
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Take two integer inputs from the user: the base and the exponent
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

# Display the result of the power calculation
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")

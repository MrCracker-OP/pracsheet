# Define the recursive function to reverse the string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Take a string input from the user
user_string = input("Enter a string: ")

# Display the reversed string
print(f"The reversed string is: {reverse_string(user_string)}")

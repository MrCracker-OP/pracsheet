# Define the recursive function to check if the string is a palindrome
def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    elif s[0] == s[-1]:
        # Recursively check the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Take a string input from the user
user_string = input("Enter a string: ")

# Display whether the string is a palindrome
if is_palindrome(user_string):
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")

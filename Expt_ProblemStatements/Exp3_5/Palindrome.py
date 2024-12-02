# Input string
input_string = "A man a plan a canal Panama"

# Remove spaces and convert to lowercase
cleaned_string = ''.join(input_string.split()).lower()

# Check if the cleaned string is equal to its reverse
is_palindrome = cleaned_string == cleaned_string[::-1]

# Print the result
if is_palindrome:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

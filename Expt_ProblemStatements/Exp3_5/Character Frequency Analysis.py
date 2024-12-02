# Take input from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to hold character frequencies
freq_dict = {}

# Convert the string to lowercase to make the count case-insensitive
input_string = input_string.lower()

# Iterate through each character in the string
for char in input_string:
    # Check if the character is alphabetic
    if char.isalpha():
        # If the character is already in the dictionary, increment its count
        if char in freq_dict:
            freq_dict[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            freq_dict[char] = 1

# Print the resulting frequency dictionary
print(freq_dict)

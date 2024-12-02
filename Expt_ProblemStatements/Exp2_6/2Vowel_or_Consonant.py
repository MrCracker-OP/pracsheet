def check_vowel_or_consonant(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return "vowel"
    else:
        return "consonant"

# Ask user to input a single character
char = input("Enter a single alphabetic character: ")

# Check if the input is valid
if len(char) == 1 and char.isalpha():
    result = check_vowel_or_consonant(char)
    print(f"The character '{char}' is a {result}.")
else:
    print("Please enter a single alphabetic character.")

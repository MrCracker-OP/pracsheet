import string

# Input string
input_string = "Hello, world! This is a test string with several different lengths of words."

# Remove punctuation using str.translate
translator = str.maketrans('', '', string.punctuation)
cleaned_string = input_string.translate(translator)

# Split the cleaned string into words
words = cleaned_string.split()

# Find the longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Print the longest word
print("The longest word is:", longest_word)

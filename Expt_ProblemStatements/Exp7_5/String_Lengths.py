# Define a list of strings
strings = ["apple", "banana", "cherry", "date"]

# Calculate the length of each string using map() and lambda
lengths = list(map(lambda s: len(s), strings))

# Display the resulting list of lengths
print(lengths)

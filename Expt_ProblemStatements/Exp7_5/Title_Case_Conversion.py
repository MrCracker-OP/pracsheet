# Define a list of strings
strings = ["hello world", "python programming", "map and lambda"]

# Convert each string to title case using map() and lambda
title_cased_strings = list(map(lambda s: s.title(), strings))

# Display the resulting list of title-cased strings
print(title_cased_strings)

# Define two lists of equal length
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Combine the lists element-wise into a list of tuples using map() and lambda
combined_list = list(map(lambda x, y: (x, y), list1, list2))

# Display the resulting list of tuples
print(combined_list)

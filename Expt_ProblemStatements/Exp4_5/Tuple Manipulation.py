# Input tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

# Concatenate the two tuples
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}")

# Find the common elements between the two tuples
common_elements = tuple(set(tuple1) & set(tuple2))
print(f"Common elements: {common_elements}")

# Create a new tuple by repeating the elements of the first tuple three times
repeated_tuple = tuple1 * 3
print(f"Repeated tuple: {repeated_tuple}")

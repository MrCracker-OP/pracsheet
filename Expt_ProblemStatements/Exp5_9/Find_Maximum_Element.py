import numpy as np

# Create a 2D array (matrix) using NumPy
matrix = np.array([
    [10, 22, 35],
    [44, 55, 66],
    [77, 88, 99]
])

# Find the maximum element in the array
max_element = np.max(matrix)

# Find the position (row and column index) of the maximum element
max_position = np.unravel_index(np.argmax(matrix), matrix.shape)

# Display the maximum element and its position
print("Original 2D Array:")
print(matrix)

print("\nMaximum Element:")
print(max_element)

print("\nPosition of Maximum Element (row, column):")
print(max_position)

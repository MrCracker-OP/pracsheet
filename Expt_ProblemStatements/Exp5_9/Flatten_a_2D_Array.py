import numpy as np

# Create a 2D array using NumPy
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Flatten the 2D array into a 1D array
flattened_array = matrix.flatten()

# Alternatively, you can use the .ravel() method
# flattened_array = matrix.ravel()

# Display the original 2D array and the resulting 1D array
print("Original 2D Array:")
print(matrix)

print("\nFlattened 1D Array:")
print(flattened_array)

import numpy as np

# Create a 1D array with 12 elements
array_1d = np.arange(12)

# Define the number of rows and columns for the 2D array
rows, cols = 3, 4

# Reshape the 1D array into a 2D array with the specified number of rows and columns
array_2d = array_1d.reshape((rows, cols))

# Display the original 1D array and the reshaped 2D array
print("Original 1D Array:")
print(array_1d)
print("\nReshaped 2D Array:")
print(array_2d)

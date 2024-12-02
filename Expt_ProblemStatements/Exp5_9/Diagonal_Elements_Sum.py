import numpy as np

# Create a square 2D array (matrix) using NumPy
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate the sum of the elements on the main diagonal
diagonal_sum = np.trace(matrix)

# Display the sum of the diagonal elements
print("Matrix:")
print(matrix)

print("\nSum of the diagonal elements:")
print(diagonal_sum)

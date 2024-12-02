import numpy as np

# Create a 2D array (matrix) using NumPy
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate the transpose of the matrix
transpose = np.transpose(matrix)

# Alternatively, you can use the .T attribute
# transpose = matrix.T

# Display the original and transposed matrices
print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix:")
print(transpose)

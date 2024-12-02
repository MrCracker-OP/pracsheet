import numpy as np

# Define the size of the matrices
rows, cols = 3, 3

# Create two 2D arrays (matrices) of the same size with random integers
matrix1 = np.random.randint(0, 10, (rows, cols))
matrix2 = np.random.randint(0, 10, (rows, cols))

# Perform element-wise addition of the two matrices
result_matrix = np.add(matrix1, matrix2)

# Display the matrices and the result
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResulting Matrix after Addition:")
print(result_matrix)

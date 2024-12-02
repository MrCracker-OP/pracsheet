import numpy as np

# Create two 2D arrays (matrices) using NumPy
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix_b = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Perform matrix multiplication
result = np.matmul(matrix_a, matrix_b)

# Display the resulting matrix
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nResulting Matrix (Matrix A multiplied by Matrix B):")
print(result)
import numpy as np

# Create a 2D array (matrix) using NumPy
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Calculate the average of each row
row_averages = np.mean(matrix, axis=1)

# Calculate the average of each column
column_averages = np.mean(matrix, axis=0)

# Display the original 2D array
print("Original 2D Array:")
print(matrix)

# Display the row averages
print("\nAverage of each row:")
print(row_averages)

# Display the column averages
print("\nAverage of each column:")
print(column_averages)

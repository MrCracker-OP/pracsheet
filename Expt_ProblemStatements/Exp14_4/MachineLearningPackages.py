import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data using NumPy
np.random.seed(0)
data = np.random.randn(100, 3)  # 100 rows and 3 columns of random data

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3'])

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Calculate some basic statistics using Pandas
print("\nBasic statistics:")
print(df.describe())

# Plot the data using Matplotlib
plt.figure(figsize=(10, 6))

# Plot Feature1 and Feature2
plt.subplot(2, 1, 1)
plt.plot(df['Feature1'], label='Feature1')
plt.plot(df['Feature2'], label='Feature2')
plt.legend()
plt.title('Feature1 and Feature2')

# Plot Feature3
plt.subplot(2, 1, 2)
plt.plot(df['Feature3'], label='Feature3', color='r')
plt.legend()
plt.title('Feature3')

# Display the plots
plt.tight_layout()
plt.show()

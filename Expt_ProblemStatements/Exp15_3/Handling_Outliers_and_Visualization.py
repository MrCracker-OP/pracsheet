import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file into a pandas DataFrame
df = pd.read_csv('temperature.csv')

# 2. Identify and remove outliers in the Temperature column
# Calculate the Interquartile Range (IQR)
Q1 = df['Temperature'].quantile(0.25)
Q3 = df['Temperature'].quantile(0.75)
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
df_cleaned = df[(df['Temperature'] >= lower_bound) & (df['Temperature'] <= upper_bound)]

# 3. Plot a line chart of Temperature over time before and after removing outliers

plt.figure(figsize=(14, 7))

# Line chart before removing outliers
plt.subplot(1, 2, 1)
plt.plot(df['Date'], df['Temperature'], color='blue', marker='o')
plt.title('Temperature Over Time (Before Removing Outliers)')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.xticks(rotation=45)

# Line chart after removing outliers
plt.subplot(1, 2, 2)
plt.plot(df_cleaned['Date'], df_cleaned['Temperature'], color='green', marker='o')
plt.title('Temperature Over Time (After Removing Outliers)')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

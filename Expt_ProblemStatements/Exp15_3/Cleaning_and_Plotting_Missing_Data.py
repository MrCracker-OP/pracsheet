import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file into a pandas DataFrame
df = pd.read_csv('employees.csv')

# 2. Identify and print the number of missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# 3. Fill missing values in the Salary column with the mean salary
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)

# 4. Fill missing values in the Joining_Date column with the most frequent date
most_frequent_date = df['Start Date'].mode()[0]
df['Start Date'].fillna(most_frequent_date, inplace=True)

# 5. Plot a histogram of the Salary distribution before and after filling missing values

# Reload the original data to compare before filling
df_original = pd.read_csv('employees.csv')

# Histogram before filling missing values
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df_original['Salary'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Salary Distribution Before Filling Missing Values')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Histogram after filling missing values
plt.subplot(1, 2, 2)
plt.hist(df['Salary'], bins=20, color='green', edgecolor='black')
plt.title('Salary Distribution After Filling Missing Values')
plt.xlabel('Salary')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

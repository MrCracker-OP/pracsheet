import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 1. Load the CSV file into a pandas DataFrame
df = pd.read_csv('student_scores.csv')

# 2. Normalize the Score column (scaling between 0 and 1)
scaler = MinMaxScaler()
df['Normalized_Score'] = scaler.fit_transform(df[['Score']])

# 3. Create a scatter plot of Score for each Subject with different colors for each subject

# Define colors for each subject
colors = {'Digital Electronics': 'blue', 'Data Mining': 'green', 'Python Labs': 'red', 'Economics': 'purple', 'Statistics Labs': 'Magenta'}

# Plotting
plt.figure(figsize=(10, 6))
for subject in df['Subject'].unique():
    subset = df[df['Subject'] == subject]
    plt.scatter(subset['Student_ID'], subset['Normalized_Score'],
                color=colors.get(subject, 'black'), label=subject)

plt.title('Normalized Scores by Subject')
plt.xlabel('Student ID')
plt.ylabel('Normalized Score (0 to 1)')
plt.legend(title='Subject')
plt.show()

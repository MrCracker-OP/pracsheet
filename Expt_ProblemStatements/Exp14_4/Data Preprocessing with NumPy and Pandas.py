import numpy as np
import pandas as pd

# 1. Create a NumPy array with student scores
scores = np.array([[85, 90, 88], [78, 85, 92], [90, 95, 85]])

# 2. Calculate the mean score for each subject
mean_scores = np.mean(scores, axis=0)
print("Mean scores for each subject:", mean_scores)

# 3. Standardize the scores by subtracting the mean and dividing by the standard deviation for each subject
std_scores = np.std(scores, axis=0)
standardized_scores = (scores - mean_scores) / std_scores

# 4. Convert the standardized scores into a pandas DataFrame and add column names for the subjects
subject_names = ['Math', 'Science', 'English']
df = pd.DataFrame(standardized_scores, columns=subject_names)

print("Standardized Scores DataFrame:")
print(df)


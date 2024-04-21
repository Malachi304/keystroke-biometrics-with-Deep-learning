# Various Stats on preprocessed, and processed data to assist in data optimization (Features only) 

import pandas as pd
import seaborn as sns
import numpy as np

df_new = pd.read_csv('Data/newData.csv')
df_original = pd.read_csv('Data/Data.csv')

# Combined, and Preprocessed data
df_processed = pd.read_csv('Data/ProcessedData.csv')

df_processed.drop(columns=['subject', 'target'], inplace=True)
# Heatmap of processed data 
sns.heatmap(df_processed.corr())
#plt.show()



df_new.drop(columns=['subject','sessionIndex', 'rep'], inplace=True)
df_original.drop(columns=[ 'subject', 'sessionIndex', 'rep'], inplace=True)
#print(df_new.info())
#print(df_original.info())


correlation_matrix = df_new.corrwith(df_original)

# Print correlation matrix
#print(correlation_matrix)






# THE CODE BELOW NEEDS to be edited to look at outliers within specific feature columns, read DataStats/Stat-information.txt

# Calculate z-scores for each column
z_scores_original = (df_original - df_original.mean()) / df_original.std()
z_scores_new = (df_new - df_new.mean()) / df_new.std()
z_scores_p = (df_processed - df_processed.mean()) / df_processed.std()

# Define threshold for outlier detection (z-score greater than 3 or less than -3)
threshold = 3

# Identify outliers in personal dataset
outliers_new = np.abs(z_scores_new) > threshold

print("Outliers New:")
print(len(df_new[outliers_new.any(axis=1)]))


df_outliers_new = df_new[outliers_new.any(axis=1)]

#df_outliers_new.to_csv("Ouiers_new.csv")



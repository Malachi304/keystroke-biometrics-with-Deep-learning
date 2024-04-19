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

# Assuming df_original is your DataFrame
# Calculate z-scores for each column
z_scores_original = (df_original - df_original.mean()) / df_original.std()
z_scores_new = (df_new - df_new.mean()) / df_new.std()

# Define threshold for outlier detection (z-score greater than 3 or less than -3)
threshold = 3

# Identify outliers
outliers_original = np.abs(z_scores_original) > threshold
outliers_new = np.abs(z_scores_new) > threshold


# Print rows corresponding to outliers
print("Outliers Original:")
print(len(df_original[outliers_original.any(axis=1)]))
# Print rows corresponding to outliers
print("Outliers New:")
print(len(df_new[outliers_new.any(axis=1)]))

tdf0 = df_original[outliers_original.any(axis=1)]
tdf1 = df_new[outliers_new.any(axis=1)]

tdf0.to_csv("Ouliers_og.csv")
tdf1.to_csv("Ouiers_new.csv")



# Various Stats on preprocessed, and processed data to assist in data optimization (Features only) 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df_new = pd.read_csv('Data/newData.csv')
df_origional = pd.read_csv('Data/Data.csv')

# Combined, and Preprocessed data
df_processed = pd.read_csv('Data/ProcessedData.csv')

df_processed.drop(columns=['subject', 'target'], inplace=True)
# Heatmap of processed data 
sns.heatmap(df_processed.corr())
plt.show()



df_new.drop(columns=['subject','sessionIndex', 'rep'], inplace=True)
df_origional.drop(columns=['subject', 'sessionIndex', 'rep'], inplace=True)

correlation_matrix = df_new.corrwith(df_origional)

# Print correlation matrix
print(correlation_matrix)

# Assuming df_original is your DataFrame
# Calculate z-scores for each column
# z_scores = (df_origional - df_origional.mean()) / df_origional.std()

# Define threshold for outlier detection (e.g., z-score greater than 3 or less than -3)
#threshold = 3

# Identify outliers
#outliers = np.abs(z_scores) > threshold

# Print rows corresponding to outliers
#print("Outliers:")
#print(df_original[outliers.any(axis=1)])

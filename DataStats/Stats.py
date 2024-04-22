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





# Define threshold for outlier detection (z-score greater than 3 or less than -3)
threshold = 3
outliers_flags = pd.DataFrame(index=df_new.index, columns=df_new.columns)
# Loop over each column
for column in df_new.columns:
    # Calculate z-scores for the current column
    z_scores = (df_new[column] - df_new[column].mean()) / df_new[column].std()
    # Identify outliers using the threshold for the current column
    outliers_flags[column] = np.abs(z_scores) > threshold

# Count outliers for each column
outliers_counts = outliers_flags.sum()

# Print number of outliers for each column
print("Number of outliers for each column in the new dataset:")
print(outliers_counts)


#df_outliers_new.to_csv("Ouiers_new.csv")



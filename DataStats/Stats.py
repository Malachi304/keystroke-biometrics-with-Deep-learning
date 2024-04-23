# Various Stats on preprocessed, and processed data to assist in data optimization (Features only) 

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 


df_new = pd.read_csv('Data/newData.csv')
df_original = pd.read_csv('Data/Data.csv')
df_keyboards = pd.read_csv('Data/Keyboards.csv')
df_clean = pd.read_csv("C:\VScode\keystrokeTracker\Data\cleaned_dataset_2.5TreashHold.csv")

# Combined, and Preprocessed data
df_processed = pd.read_csv('Data/ProcessedData.csv')
df_processed.drop(columns=['subject', 'target'], inplace=True)

# Heatmap of processed data 
sns.heatmap(df_processed.corr())
#plt.show()



df_new.drop(columns=['subject','sessionIndex', 'rep'], inplace=True)
df_original.drop(columns=[ 'subject', 'sessionIndex', 'rep'], inplace=True)
df_keyboards.drop(columns=['subject', 'sessionIndex', 'rep'], inplace=True)


correlation_matrix = df_clean.corrwith(df_original)

# Print correlation matrix
#print(correlation_matrix)

df_new_sum = df_new.describe()
print('-=-=-=-=-=-=-=-=')
df_origional_sum =df_original.describe()
# Compare specific statistics, for example, mean values for each column
mean_comparison = df_new_sum.loc['mean'] - df_origional_sum.loc['mean']
print("\nDifference in mean values between datasets:")
print(mean_comparison)

# Define threshold for outlier detection (z-score greater than 3 or less than -3)
threshold = 2.5
outliers_flags = pd.DataFrame(index=df_new.index, columns=df_new.columns)
# Loop over each column
for column in df_new.columns:
    # Calculate z-scores for the current column
    z_scores = (df_new[column] - df_new[column].mean()) / df_new[column].std()
    # Identify outliers using the threshold for the current column
    outliers_flags[column] = np.abs(z_scores) > threshold

# Identify rows containing outliers in any column
outliers_row_flags = outliers_flags.any(axis=1)

# Remove rows containing outliers
df_new_cleaned = df_new[~outliers_row_flags]

# Save the cleaned DataFrame to a new CSV file
#df_new_cleaned.to_csv('Data/cleaned_dataset_2.5TreashHold.csv', index=False)


# Count outliers for each column
#outliers_counts = outliers_flags.sum()

# Print number of outliers for each column
#print("Number of outliers for each column in the new dataset:")
#print(outliers_counts)

# Save outliers only to file
#df_outliers_new.to_csv("Ouiers_new.csv")



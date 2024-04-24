# Various Stats on preprocessed, and processed data to assist in data optimization (Features only) 
# Anything commeted out can be used to print or show graphs 
# All parameters contaianing datasets can be interchanged to run various stats 

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

# Read all data we want to run stats on
df_new = pd.read_csv('Data/newData.csv')
df_original = pd.read_csv('Data/Data.csv')
df_keyboards = pd.read_csv('Data/Keyboards.csv')
df_clean = pd.read_csv("C:\VScode\keystrokeTracker\Data\cleaned_dataset_2.5TreashHold.csv")
df_processed = pd.read_csv('Data/ProcessedData.csv')

# Random subject from main dataset we wish to compare to newData(i.e persional data)
df_filtered_original = df_original[df_original['subject'] == 's020']

# If you wanted to save subjects to csv


target_subject = 's020'
df_test = df_original
df_test['target'] = (df_test['subject'] == target_subject).astype(int)
df_test.drop(columns=['sessionIndex', 'rep'], inplace=True)
df_test.to_csv("Data/Subject_so20.csv", index=False)
#filtered_df_original.to_csv("Subject_so20.csv", index=False)

# Remove non-resourcful features
df_filtered_original.drop(columns=['subject', 'sessionIndex', 'rep'], inplace=True)
df_processed.drop(columns=['subject', 'target'], inplace=True)
df_new.drop(columns=['subject','sessionIndex', 'rep'], inplace=True)
df_original.drop(columns=[ 'subject', 'sessionIndex', 'rep'], inplace=True)
df_keyboards.drop(columns=['subject', 'sessionIndex', 'rep'], inplace=True)

# Heatmap of processed data 
sns.heatmap(df_processed.corr())
#plt.show()

# Correlation matrix between two datasets
correlation_matrix = df_new.corrwith(df_filtered_original)
#print(correlation_matrix)

# Save data set stat descriptions to varible
df_new_summery = df_new.describe()
df_original_summery =df_original.describe()
df_filtered_summery = df_filtered_original.describe()

# Compare specific statistics, for example, mean values for each column
mean_comparison_percentage = abs((df_new_summery.loc['mean'] - df_filtered_summery.loc['mean']) / df_filtered_summery.loc['mean']) * 100
# Calculate mean percentage difference between sets
mean_comparison_raw = abs(df_new_summery.loc['mean'] - df_original_summery.loc['mean']) 

#print("\nDifference in mean values between datasets Percentages:")
#print(mean_comparison_percentage)
#print("\nDifference in mean values between datasets Raw:")
#print(mean_comparison_raw)
#Print("Stat breakdown of outlier removed data")
#print(df_new_summery)
#print(df_original_summery)

# Collect all mean values
mean_values_new = df_new_summery.loc['mean']
mean_values_original = df_original_summery.loc['mean']
mean_values_filterd = df_filtered_summery.loc['mean']


# Collect all standard deviation values
std_values_original = df_original_summery.loc['std']
std_values_new = df_new_summery.loc['std']
std_values_filtered = df_filtered_summery.loc['std']


# Plot bar plot for comparison of std
plt.figure(figsize=(10, 6))
plt.bar(std_values_filtered.index, std_values_filtered, color='skyblue', label='Subject s020', alpha=0.7)
plt.bar(std_values_new.index, std_values_new, color='orange', label='New Dataset', alpha=0.7)

plt.title('Comparison of Standard Deviations between Datasets')
plt.xlabel('Features')
plt.ylabel('Standard Deviation')
plt.xticks(rotation=90)  
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
#plt.show()

# Create a density plot of mean values 
plt.figure(figsize=(10, 6))
sns.kdeplot(mean_values_new, color='skyblue', fill=True)
sns.kdeplot(mean_values_original, color='orange', label='Original Dataset', fill=True)
plt.title('Mean Values of Features in the New Data vs Origional Data')
plt.xlabel('Mean')
plt.ylabel('Density')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
#plt.show()


# Section Below is for outlier detection which we don't utalize with the model
#============================================================================================

# Define threshold for outlier detection (z-score greater than 3 or less than -3)
threshold = 3
outliers_flags = pd.DataFrame(index=df_new.index, columns=df_new.columns)
# Loop over each column
for column in df_filtered_original.columns:
    # Calculate z-scores for the current column
    z_scores = (df_new[column] - df_new[column].mean()) / df_new[column].std()
    # Identify outliers using the threshold for the current column
    outliers_flags[column] = np.abs(z_scores) > threshold

# Identify rows containing outliers in any column
outliers_row_flags = outliers_flags.any(axis=1)

# Remove rows containing outliers
df_new_cleaned = df_new[~outliers_row_flags]

# Save the cleaned DataFrame to a new CSV file
#df_new_cleaned.to_csv('Data/cleaned_filtered_dataset_3ThreashHold.csv', index=False)


# Count outliers for each column
outliers_counts = outliers_flags.sum()

# Print number of outliers for each column
#print("Number of outliers for each column in the new dataset:")
#print(outliers_counts)

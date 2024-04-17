# Processes new data, contained in 'newData', to match origional data set 'Data'
# Saves processed data to 'processedData' which will be combined with origional data in 'ModelData'

import pandas as pd


# Load the new dataset captured from KeyCapture sessions
df = pd.read_csv('newData.csv')

# Remove rows where any element equals zero
# Happens on occasion (Unkown issue, possibly latency), data does not need to be replaced until after all sessions are complete
#df_processed = df[(df != 0).all(axis=1)]

# Save the filtered dataset
#df_processed.to_csv('ProcessedData.csv', index=False)



#==================================================
# This next section is for testing if data from random columns 
# in new and origional dataset are significantly different (mean)
# based on 0.05 significance level
#==================================================

# Load the origional dataset
df1 = pd.read_csv('Data.csv')
# Specify the column for which you want to calculate the mean
column_name = 'DD.t.i'

# Calculate the mean of the specified column
column_mean = df[column_name].mean()
column_mean1 = df1[column_name].mean()


print(f"The mean of '{column_name}' column is: {column_mean} for newData")
print(f"The mean of '{column_name}' column is: {column_mean1} for Data")

from scipy.stats import ttest_ind
# Perform independent samples t-test
# Assume equal variances by default
t_statistic, p_value = ttest_ind([column_mean], [column_mean1])

# Set significance level
alpha = 0.05

# Print the results
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

import scipy

p_value = scipy.stats.norm.sf(abs(column_mean)) 
print('p value is : ' + str(p_value)) 

# Compare p-value to significance level
if p_value < alpha:
    print("Reject the null hypothesis: Means are statistically different")
else:
 print("Fail to reject the null hypothesis: Means are not statistically different")
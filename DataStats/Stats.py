# Various Stats on data collected and model results

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#==================================================
# Testing correlations between data
#==================================================

df = pd.read_csv('Data/newData.csv')
df1 = pd.read_csv('Data/Data.csv')
# Combine Data
combined_df = pd.concat([df1, df], axis=0)

heat_map_data = combined_df
heat_map_data = heat_map_data.drop(['subject'], axis=1) 
# Heatmap of combined data set
sns.heatmap(heat_map_data.corr())
plt.show()


df_test = df.drop(['subject'], axis=1)
df1_test = df1.drop(['subject'], axis=1)

correlation_matrix = df_test.corrwith(df1_test)

# Print correlation matrix
print(correlation_matrix)

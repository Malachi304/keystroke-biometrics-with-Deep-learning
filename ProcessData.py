# Processes new data, contained in 'newData', to match origional data set 'Data'
# Saves processed data to 'processedData' which will be combined with origional data in 'ModelData'

import pandas as pd


# Load the new dataset captured from KeyCapture sessions
df = pd.read_csv('data/newData.csv')
#round decimal place
df = df.round(4)

df1 = pd.read_csv('data/Data.csv')

# Concatinate origional data, and new data
combined_df = pd.concat([df1, df], axis=0)
combined_df.drop(columns=['sessionIndex', 'rep'], inplace=True)

target_subject = 's060'

combined_df['target'] = (combined_df['subject'] == target_subject).astype(int)
df_combined = df[(df != 0).all(axis=1)]

combined_df.to_csv('Data/ProcessedData.csv', index=False)
print("done")

# Remove rows where any element equals zero
# Happens on occasion (Unkown issue, possibly latency), data does not need to be replaced until after all sessions are complete
# REMOVED FEATURE because some of the origional data has negative values
# df_processed = df[(df != 0).all(axis=1)]

# Save the filtered dataset
#df_processed.to_csv('ProcessedData.csv', index=False)

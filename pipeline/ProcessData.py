# Processes new data, contained in 'newData', to match origional data set 'Data'
# Saves processed data to 'processedData' which will be combined with origional data in 'ModelData'
#==============================================================================

import pandas as pd

# Load the new dataset captured from KeyCapture sessions
df = pd.read_csv('data/newData.csv')
df1 = pd.read_csv('data/Data.csv')

# Round decimal place
df= df.round(4)

# Tried to make data cleaner to look at by adding trailing zeros 
#Combined_df = df.applymap(lambda x: "{:.4f}".format(x))

# Concatinate origional data, and new data
combined_df = pd.concat([df1, df], axis=0)
combined_df.drop(columns=['sessionIndex', 'rep'], inplace=True)


t2 = 's057'
# Label encoding subject, 1 for newData, 0 for origional data
target_subject = 's060'
combined_df['target'] = (combined_df['subject'] == target_subject).astype(int)
#combined_df['target'] = (combined_df['subject'] == t2).astype(int)

combined_df.to_csv('Data/ProcessedDataV2.csv', index=False)
print(combined_df.info())
print(combined_df.tail())


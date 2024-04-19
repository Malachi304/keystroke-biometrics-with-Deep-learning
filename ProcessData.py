# Processes new data, contained in 'newData', to match origional data set 'Data'
# Saves processed data to 'processedData' which will be combined with origional data in 'ModelData'
#==============================================================================

import pandas as pd
from DataStats.Stats import Outliers_new, Outliers_original

# Load the new dataset captured from KeyCapture sessions
df = pd.read_csv('data/newData.csv')
df1 = pd.read_csv('data/Data.csv')
print(len(Outliers_new))
print(len(Outliers_original))
# Round decimal place
#df= df.round(4)
# Combined_df = df.applymap(lambda x: "{:.4f}".format(x))

# Concatinate origional data, and new data
#combined_df = pd.concat([df1, df], axis=0)
#combined_df.drop(columns=['sessionIndex', 'rep'], inplace=True)

# Label encoding subject, 1 for newData, 0 for origional data
#target_subject = 's060'
#combined_df['target'] = (combined_df['subject'] == target_subject).astype(int)
#combined_df.to_csv('Data/ProcessedData.csv', index=False)


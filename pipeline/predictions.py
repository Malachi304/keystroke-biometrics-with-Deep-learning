import keras
import pandas as pd 
import joblib

model = keras.models.load_model('Saved_Models/Pre-Outlier-processing.h5')
sc = joblib.load('Saved_Models/scaler.pkl')

#origional_data = pd.read_csv("Data/ProcessedData.csv")
#prediction_data = origional_data.drop(columns=["subject", "target"]).iloc[1000]

#new_data = pd.read_csv('data/newData.csv')
#new_data.drop(columns=['subject', 'sessionIndex', 'rep'])

keyboards = pd.read_csv("Data/Keyboards.csv")


FalseAcceptance_count = 0
Acceptance_count = 0
n = 0

# Specify the target value for the 'subject' column
target_value = 's000-KEYBOARD_USED'

# Filter the DataFrame to select rows where 'subject' equals the target value
filtered_rows = keyboards[keyboards['subject'] == target_value]
filtered_rows.drop(columns=['subject', 'rep', 'sessionIndex'], inplace=True)

for index, row in filtered_rows.iterrows():

    prediction_data_reshaped = row.values.reshape(1, -1)
    normalized_data = sc.transform(prediction_data_reshaped)
    
    prediction = model.predict(normalized_data)

    print(prediction)
    if prediction[0][0] < 0.5:
        #print("Access Denied")
        FalseAcceptance_count = FalseAcceptance_count + 1
    else:
        Acceptance_count = Acceptance_count + 1
        
    n = n + 1

print(f'False Acceptance rate {target_value}: {FalseAcceptance_count/n}')
print(f'Acceptance rate {target_value}: {Acceptance_count/n}')
print(f'Data Quantity: {n}')
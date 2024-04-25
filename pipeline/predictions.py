import keras
import pandas as pd 
import joblib

# Load Model
model = keras.models.load_model('Saved_Models/s060.h5')
# Load scaler used to train
sc = joblib.load('Saved_Models/scaler.pkl')
# Load dataset with all keystroke data from subject s060
keyboards = pd.read_csv("Data/Keyboards.csv")


FalseAcceptance_count = 0
Acceptance_count = 0
# Number of data each keyboard has in dataset
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

# Calculations 
print(f'False Acceptance rate {target_value}: {FalseAcceptance_count/n}')
print(f'Acceptance rate {target_value}: {Acceptance_count/n}')
print(f'Data Quantity: {n}')
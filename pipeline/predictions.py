import keras
import pandas as pd 
import joblib

model = keras.models.load_model('Saved_Models/Pre-Outlier-Processing-dropout.h5')
sc = joblib.load('Saved_Models/scaler.pkl')

origional_data = pd.read_csv("Data/ProcessedData.csv")
#prediction_data = origional_data.drop(columns=["subject", "target"]).iloc[1000]

new_data = pd.read_csv('data/newData.csv')
new_data.drop(columns=['subject', 'sessionIndex', 'rep'])

keyboards = pd.read_csv("Data/Keyboards.csv")


FalseAcceptance_count = 0
Acceptance_count = 0
n = 50
i=0

while i < n:

    prediction_data = keyboards.drop(columns=['subject', 'rep', 'sessionIndex']).iloc[i+1]

    prediction_data_reshaped = prediction_data.values.reshape(1, -1)
    normalized_data = sc.transform(prediction_data_reshaped)
   
    prediction = model.predict(normalized_data)

    print(prediction)
    if prediction[0][0] < 0.5:
        #print("Access Denied")
        FalseAcceptance_count = FalseAcceptance_count + 1
    else:
        Acceptance_count = Acceptance_count + 1
    
    i = i + 1

print(f'False Acceptance rate (50 Lenovo keystrokes): {FalseAcceptance_count/n}')
print(f'Acceptance rate (50 Lenovo keystrokes): {Acceptance_count/n}')
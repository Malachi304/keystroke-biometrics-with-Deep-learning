import keras
import pandas as pd 
import joblib

model = keras.models.load_model('Saved_Models/Pre-Outlier-Processing-dropout.h5')
sc = joblib.load('Saved_Models/scaler.pkl')

origional_data = pd.read_csv("Data/ProcessedData.csv")
#prediction_data = origional_data.drop(columns=["subject", "target"]).iloc[1000]

keyboards = pd.read_csv("Data/Keyboards.csv")
prediction_data = keyboards.drop(columns=['subject', 'rep', 'sessionIndex']).iloc[4]

prediction_data_reshaped = prediction_data.values.reshape(1, -1)

normalized_data = sc.transform(prediction_data_reshaped)
prediction = model.predict(normalized_data)

print(prediction)
if prediction[0][0] < 0.5:
    print("Access Denied")
else:
    print("Access Granted")
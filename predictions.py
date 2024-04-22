import keras
import pandas as pd 
import joblib
import numpy as np

model = keras.models.load_model('Allmodels/Pre-Outlier-processing.h5')
sc = joblib.load('scaler.pkl')

data = pd.read_csv("Data/ProcessedData.csv")
prediction_data = data.drop(columns=["subject", "target"]).iloc[33]

prediction_data_reshaped = prediction_data.values.reshape(1, -1)

#print(prediciton_data)
normalized_data = sc.transform(prediction_data_reshaped)
prediction = model.predict(normalized_data)

if prediction[0][0] < 0.5:
    print("Access Denied")
else:
    print("Access Granted")
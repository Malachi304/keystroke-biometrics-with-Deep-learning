import tensorflow as tf
import keras 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder



data = pd.read_csv('Data.csv')
#print("Unique values in the 'subject' column before filtering:")
#print(data['subject'].unique())

#data = data[data['subject'].str.isnumeric()]

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'subject' column
data['subject'] = label_encoder.fit_transform(data['subject'])

#data['subject'] = data['subject'].str.replace('^s0+', '', regex=True)
#data.replace({'s': 0}, inplace=True)
#print(data.head())

x = data.drop(columns=['subject'])
y = data['subject']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Unique values in y_train:", y_train.unique())
print("Unique values in y_test:", y_test.unique())


# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(len(y.unique()), activation='softmax')  # Output layer with softmax activation for multi-class classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

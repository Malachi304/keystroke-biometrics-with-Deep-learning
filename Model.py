import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense




data = pd.read_csv('data/ProcessedData.csv')


x = data.drop(columns=['subject', 'target'])
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the model architecture
model = Sequential([
    Dense(32, activation='relu', input_shape=(31,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  
])

# Compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.1)
model.save('AllModels/Pre-Outlier-processing.h5')

# Evaluate the model
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

df = data
df = df.drop(columns=['subject', 'target'])
df = df.loc[3]

#Process data``
prediction = model.predict(df)
print(prediction)
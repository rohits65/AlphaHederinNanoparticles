import numpy as np
from keras.layers import Dense, Activation
from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
from joblib import dump
# Importing the dataset
data = pd.read_csv("../../data/DrugData - main.csv").dropna(subset=['xlogP', 'EE', 'TPSA', 'MW', 'LToG', 'RRPercent', 'MPS', 'CX'])

# Get the columns associated with x, y
x_values = data[['xlogP', 'EE', 'TPSA', 'MW', 'LToG', 'CX', 'MPS']].to_numpy().reshape(-1, 7)#[0:40]  # Change last num_params
y_values = np.ravel(data[['RRPercent']].to_numpy())#[0:40] # .reshape(-1, 1)
# y_values = [val/100 for val in y_values]

X = x_values#dataset[:, :-1]
y = y_values#dataset[:, -1]

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialising the ANN
model = Sequential()

# Adding the input layer and the first hidden layer
model.add(Dense(32, activation = 'relu', input_dim = 7))

# Adding the second hidden layer
model.add(Dense(units = 32, activation = 'relu'))

# Adding the third hidden layer
model.add(Dense(units = 32, activation = 'relu'))

# Adding the output layer

model.add(Dense(units = 1, activation='relu'))

#model.add(Dense(1))
# Compiling the ANN
model.compile(optimizer = 'adagrad', loss = 'mean_absolute_error')

# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size = 80, epochs = 500, validation_data=(X_test, y_test))
model.save("../savedStates/releaseRatePercentage_model.savedstate")

model = load_model("../savedStates/releaseRatePercentage_model.savedstate")
dump(sc, "../savedStates/releaseRatePercentage_scaler.savedstate")

y_pred = model.predict(X_test)

plt.plot(y_test, color = 'blue', label = 'Real data')
plt.plot(y_pred, color = 'red', label = 'Predicted data')
plt.title('Prediction')
plt.legend()
plt.show()
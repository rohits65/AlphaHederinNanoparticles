import pandas as pd
import numpy as np

def cleanData():
    data = pd.read_csv("data/DrugData - Sheet1.csv").dropna(subset=['BE'])
    BEData = data[['TPSA', 'CX', 'MPS', 'BE']]
    xVals = BEData[['TPSA', 'CX', 'MPS']].to_numpy()

    yVals = BEData[['BE']].to_numpy()
    return (xVals, yVals)

x,y = cleanData()


from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Ridge # LinearRegression, etc...
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, max_error
import numpy as np

# Create a neural network

# @param hidden_layer_sizes: (a, b); a = A little higher than (or double of) b; b = number of parameters
regr = MLPRegressor(solver='lbfgs', alpha=0.2, hidden_layer_sizes=(9,5), random_state=0)

# Data processing function
def processData(x, y):
    rawxdata = x.reshape(-1,3)
    rawydata = y.reshape(-1, 1)

    # Automatically randomizes the data
    X_train, X_test, y_train, y_test = train_test_split(rawxdata, rawydata, random_state=0)
    return (X_train, y_train, X_test, y_test)

X_train, y_train, X_test, y_test = processData(x,y)

# Fit the rgxline
regr.fit(X_train, y_train)

print(X_test, ":\n", regr.predict(X_test))

# Accuracy
print(explained_variance_score(y_test, regr.predict(X_test)))
print(max_error(y_test, regr.predict(X_test)))
print(max_error(y_train, regr.predict(X_train)))

# Anatomy
print(regr.n_layers_)
print(regr.hidden_layer_sizes)

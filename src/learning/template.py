
# Data processing/manipulation dependencies
import pandas as pd
import numpy as np

# ML dependencies
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Ridge # LinearRegression, etc...
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, max_error


# Create a function to pull the data from the csv file, and output x, y
def cleanData():
    # Read csv and remove rows w/o data points in the column 'BE'
    data = pd.read_csv("data/DrugData - Sheet1.csv").dropna(subset=['BE'])

    # Get the columns associated with x, y
    xVals = data[['TPSA', 'CX', 'MPS']].to_numpy().reshape(-1, 3) # Change last number to # of params
    yVals = data[['BE']].to_numpy().reshape(-1, 1)

    return (xVals, yVals)

x, y = cleanData()
# Create a neural network

'''
@param solver: 'lbfgs' (small, easy datasets) or 'adam' (large, complex datasets)
@param alpha (>=0): 0 means you trust all of your data; Inf means you dont trust any of your data
@param hidden_layer_sizes: Really random tuple. Start off with (# of params ^ 2, # of params * 2) 
    and modify from there.
@param random_state: Don't touch. 
'''
regr = MLPRegressor(solver='lbfgs', alpha=0.2, hidden_layer_sizes=(9,5), random_state=0)

# Data processing function
'''
@param x: numpy arary 
@param y: numpy array
'''
def processData(x, y):
    rawxdata = x
    rawydata = y

    # Automatically randomizes and splits the data
    X_train, X_test, y_train, y_test = train_test_split(rawxdata, rawydata, random_state=0)
    return (X_train, y_train, X_test, y_test)

X_train, y_train, X_test, y_test = processData(x,y)

# Fit the regression 
regr.fit(X_train, y_train)

# For manual evaluation
print(X_test, ":\n", regr.predict(X_test))

# Accuracy
# The below value should be as close to 1 as possible; play with the params in MLPRegressor
print(explained_variance_score(y_test, regr.predict(X_test)))

# Maximum amount of error in the test/train sets
print(max_error(y_test, regr.predict(X_test)))
print(max_error(y_train, regr.predict(X_train)))

# Anatomy of the model
print(regr.n_layers_)
print(regr.hidden_layer_sizes)

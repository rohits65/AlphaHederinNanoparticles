# Data processing/manipulation dependencies
import numpy as np
import pandas as pd

# ML dependencies
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor


# Create a function to pull the data from the csv file, and output x, y
def clean_data() -> tuple:
    # Read csv and remove rows w/o data points in the column 'BE'
    data = pd.read_csv("../../data/DrugData - main.csv").dropna(subset=['BE'])

    # Get the columns associated with x, y
    x_values = data[['TPSA', 'CX', 'MPS', 'MW', 'LToG', 'xlogP']].to_numpy().reshape(-1, 6)  # Change last num_params
    y_values = data[['BE']].to_numpy()  # .reshape(-1, 1)

    return x_values, y_values


x, y = clean_data()

# Create a neural network

'''
@param solver: 'lbfgs' (small, easy datasets) or 'adam' (large, complex datasets)
@param alpha (>=0): 0 means you trust all of your data; Inf means you dont trust any of your data
@param hidden_layer_sizes: Really random tuple. Start off with (# of params ^ 2, # of params * 2) 
    and modify from there.
@param random_state: Don't touch. 
'''
regr = MLPRegressor(solver='lbfgs', alpha=0.36, hidden_layer_sizes=(3, 5), random_state=9, max_iter=1000)

# Data processing function
'''
@param x: numpy arary 
@param y: numpy array
'''


def processData(raw_x_data, raw_y_data) -> tuple:
    # Automatically randomizes and splits the data
    x_train, x_test, y_train, y_test = train_test_split(raw_x_data, raw_y_data, random_state=0, test_size=0.2)
    return x_train, y_train, x_test, y_test


X_train, y_train, X_test, y_test = processData(x, y)

# Fit the regression
regr.fit(X_train, y_train)

# For manual evaluation
print(X_test, ":\n", regr.predict(X_test))

# Accuracy
# The below value should be as close to 1 as possible; play with the params in MLPRegressor
print(explained_variance_score(y_test, regr.predict(X_test)))
print(explained_variance_score(np.vstack([y_test, y_train]), regr.predict(np.vstack([X_test, X_train]))))

# Maximum amount of error in the test/train sets
# print(max_error(y_test, regr.predict(X_test)))
# print(max_error(y_train, regr.predict(X_train)))
#
# # Anatomy of the model
# print(regr.n_layers_)
# print(regr.hidden_layer_sizes)

print(regr.predict([[129, 383, 135.0, 243.22, 1 ,-2.1]]))


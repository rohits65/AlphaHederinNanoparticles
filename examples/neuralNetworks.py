'''
Linear Regressions work, but as our model becomes more complicated (added layers), one
needs to look to more complex models to deal with the large number of inputs.
'''

from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Ridge # LinearRegression, etc...
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, max_error
import numpy as np

# Create a neural network

# @param hidden_layer_sizes: (a, b); a = A little higher than (or double of) b; b = number of parameters
regr = MLPRegressor(solver='lbfgs', alpha=0, hidden_layer_sizes=(4, 2), random_state=0)

# Data processing function
def processData():
    rawxdata = np.array([[1, 1], [10, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]).reshape(-1,2)
    rawydata = np.array([2, 12, 4, 5, 6, 7, 8, 9, 10, 11])

    # Automatically randomizes the data
    X_train, X_test, y_train, y_test = train_test_split(rawxdata, rawydata, random_state=0)
    return (X_train, y_train, X_test, y_test)

X_train, y_train, X_test, y_test = processData()

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

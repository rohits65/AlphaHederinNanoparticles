# Import models and dependecies 
from sklearn.linear_model import Ridge # LinearRegression, etc...
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Create a pipeline
pipe = make_pipeline(
    # @param alpha: 0 --> I trust my data; ()->Inf --> There a lot of outliers
    Ridge(alpha=0, fit_intercept=True, normalize=True)   
)

# Data processing function
def processData():
    rawxdata = np.array([[1, 1], [10, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]).reshape(-1,2)
    rawydata = np.array([2, 12, 4, 5, 6, 7, 8, 9, 10, 11]).reshape(-1,1) 

    # Automatically randomizes the data
    X_train, X_test, y_train, y_test = train_test_split(rawxdata, rawydata, random_state=0)
    return (X_train, y_train, X_test, y_test)

# Get the data
X_train, y_train, X_test, y_test = processData()

# Fit the pipeline
pipe.fit(X_train, y_train)

# Print accuracy
print(X_test, ":\n", pipe.predict(X_test))
print(pipe.predict([[1,109]]))
print(pipe.predict([[100,109]]))


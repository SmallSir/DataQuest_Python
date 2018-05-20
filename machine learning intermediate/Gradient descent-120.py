## 2. Linear model ##

from sklearn.linear_model import LinearRegression
import numpy as np

# We can add a dimension to an array by using np.newaxis
print("Shape of the series:", pga['distance'].shape)
print("Shape with newaxis:", pga['distance'][:, np.newaxis].shape)

# The X variable in LinearRegression.fit() must have 2 dimensions\
lm = LinearRegression()
lm.fit(pga['distance'][:,np.newaxis],pga['accuracy'])
theta1 = lm.coef_[0]
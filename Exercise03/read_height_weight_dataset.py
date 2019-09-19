# read men/women height weight data..

import matplotlib.pyplot as plt
import numpy as np

# Load data
data = np.loadtxt('height_weight.csv', delimiter=';', skiprows=1)
X = data[:,1:3]
y = data[:,0]


#%% 2D data

# weight
plt.plot(X[:,0], y, 'r.', markersize=1)

# height
plt.plot(X[:,1], y, 'r.', markersize=1)


    

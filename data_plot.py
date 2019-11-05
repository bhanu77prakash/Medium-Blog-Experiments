import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import argparse 


parser = argparse.ArgumentParser(description='Help')
parser.add_argument("-F", '--file', type=str, default= "nofile",
                    help='File containing the dataset to be plotted')

args = parser.parse_args()

dataset = pd.read_csv(args.file) 

# The following code is same for all the datasets. Only the line plotting part changes. 
X = dataset.iloc[:,:2].values
y = dataset.iloc[:,2:3].values
set1x = []
set1y = []

set2x = []
set2y = []

print(y.shape)

limit = 0

for i in range(y.shape[0]):
	if(y[i][0] == 0):
		set1x.append(X[i][0])
		limit = max(limit, X[i][0])
		set1y.append(X[i][1])
		limit = max(limit, X[i][1])
	elif(y[i][0] == 1):
		set2x.append(X[i][0])
		limit = max(limit, X[i][0])
		set2y.append(X[i][1])
		limit = max(limit, X[i][1])

plt.scatter([x for x in set1x], [x for x in set1y], s=1, label="Class 0")
plt.scatter([x for x in set2x], [x for x in set2y], s=1, label="Class 1")

# Plotting the lines
limit = int(limit+3)
axes = plt.gca()
axes.set_xlim([0,limit])
axes.set_ylim([0,limit])
x_vals = np.array([0,limit])

# The code below repeats three times for the three lines. If you are plotting fewer lines please comment out the parts accordingly. The code itself is self-explanatory.

# You have to get the slope and the intercept from the weights of the model. 
# The lines plotted here are in the form y = mx+c. So please convert the ax+by+c=0 format to this slope-intercept format.

# Line 1
slope = -2.2646914/2.2443554
intercept = 26.653484/2.2443554
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, 'r-')

# Line 2
slope = -7.6048846/7.664243
intercept = 17.568861/7.664243
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, 'b-')

# Line 3
slope = -7.3501625/7.3648877
intercept = 16.354841/7.3648877
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, 'g-')


plt.title('Dataset in 2D plane')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(loc='upper right')
plt.show()
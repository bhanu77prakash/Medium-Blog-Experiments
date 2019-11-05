# This file contains the code used for generating the datasets. 

import numpy as np
import csv

X1 = np.random.uniform(0,3, 1000)
Y1 = np.random.uniform(0,3, 1000)

set1 = []
for i in range(len(X1)):
	if(X1[i]+Y1[i] < 2.5):
		set1.append((X1[i], Y1[i]))

X1 = np.random.uniform(0,10, 1000)
Y1 = np.random.uniform(0,10, 1000)
for i in range(len(X1)):
	if(X1[i]+Y1[i] > 7 and X1[i]+Y1[i] < 10.5):
		set1.append((X1[i], Y1[i]))
print(len(set1))

X1 = np.random.uniform(0,7, 1000)
Y1 = np.random.uniform(0,7, 1000)
set2 = []

for i in range(len(X1)):
	if(X1[i]+Y1[i] > 3 and X1[i]+Y1[i] < 6.5):
		set2.append((X1[i], Y1[i]))

X1 = np.random.uniform(0,15, 1000)
Y1 = np.random.uniform(0,15, 1000)

for i in range(len(X1)):
	if(X1[i]+Y1[i] > 11 ):
		set2.append((X1[i], Y1[i]))

print(len(set1))

import matplotlib.pyplot as plt

plt.scatter([x[0] for x in set1], [x[1] for x in set1])
plt.scatter([x[0] for x in set2], [x[1] for x in set2])

plt.show()

save = True
if save:
	data = [["X", "Y", "Label"]]
	for x in set1:
		data.append([x[0], x[1], 0])
	for x in set2:
		data.append([x[0], x[1], 1])

	with open('data_blog_3.csv', 'w') as writeFile:
	    writer = csv.writer(writeFile)
	    writer.writerows(data)
	writeFile.close()

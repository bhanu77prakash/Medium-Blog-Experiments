import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense 
from matplotlib import pyplot as plt
import argparse 


parser = argparse.ArgumentParser(description='Help')
parser.add_argument("-F", '--file', type=str, default= "nofile",
                    help='File containing the dataset to be trained on')
parser.add_argument("-M", '--model', type=int, default= 1,
                    help='Model number to run')
parser.add_argument("-E", '--epochs', type=int, default= 100,
                    help='Number of epochs')


args = parser.parse_args()

dataset = pd.read_csv(args.file) 
# print(dataset.head(10))
X = dataset.iloc[:,:2].values
y = dataset.iloc[:,2:3].values

if(args.model == 1):
	input_nodes = 1
	layer_nodes = [] 
elif(args.model == 2):
	input_nodes = 2
	layer_nodes = [1]
elif(args.model == 3):
	input_nodes = 2
	layer_nodes = [1]
elif(args.model == 4):
	input_nodes = 3
	layer_nodes = [1]
elif(args.model == 5):
	input_nodes = 3
	layer_nodes = [10, 10, 1]

model = Sequential()
model.add(Dense(input_nodes, input_dim=2, activation='sigmoid'))
for nodes in layer_nodes:
	model.add(Dense(nodes, activation='sigmoid'))
# model.add(Dense(5, activation='sigmoid'))
# model.add(Dense(2, activation='sigmoid'))
# model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
history = model.fit(X, y, epochs=args.epochs, batch_size=1, verbose=True)

i = 0
for layer in model.layers:
	weights = layer.get_weights()[0]
	biases = layer.get_weights()[1]
	print("Layer %d weights: "%i)
	print("Weights: "+str(weights))
	print("Biases: "+str(biases))
	i+=1

example = True
if example:
	print("Predictions for the points [-15, -15] and [15, 15]")
	out = model.predict(np.array([[-15, -15 ], [15, 15]]))
	print(out)

# print(history.__dict__)
plt.plot(history.history['accuracy'])
# # plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()
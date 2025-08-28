import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

from ucimlrepo import fetch_ucirepo 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

"""
This file creates an artifical neural network to classify the data from the link below. It has one hidden layer. The number of epochs and batch_size can be tuned for different performance. The classes are encoded using scikits labelencoder. The file prints the accuracy of the ANN at the end of the file.

Data:
    - https://archive.ics.uci.edu/dataset/53/iris

LabelEncoder documentation:
    - https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html

Source followed to create ANN:
    - https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
"""

# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

# metadata 
# print(iris.metadata) 
  
# variable information 
print(iris.variables) 

# change to desired scikit shape (1D series)
y = y["class"]

#  encode the iris types
le = LabelEncoder()
y = le.fit_transform(y)

# initialize sequential model with layers
model = Sequential()
model.add(Dense(12, input_shape=(4,), activation="relu"))
# use softmax since there are 3 classes
model.add(Dense(3, activation="softmax"))

# compile keras model
model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=["accuracy"])

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fit model to dataset
model.fit(X_train , y_train, epochs=75, batch_size=20)

_, accuracy = model.evaluate(X_test, y_test)

# print results
print("Accuracy: ", accuracy)
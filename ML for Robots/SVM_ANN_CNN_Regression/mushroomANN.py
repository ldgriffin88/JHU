import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

from ucimlrepo import fetch_ucirepo 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

"""
This file creates an artifical neural network to classify the data from the link below. It has one hidden layer. The number of epochs and batch_size can be tuned for different performance. The classes are encoded using scikits labelencoder and the features are encoded using OneHotEncoder. The file prints the accuracy of the ANN at the end of the file.

Data:
    - https://archive.ics.uci.edu/dataset/73/mushroom

LabelEncoder documentation:
    - https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html

OneHotEncoder Documentation:
    - https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

Source followed to create ANN:
    - https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

"""

# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
X = mushroom.data.features 
y = mushroom.data.targets 
  
# metadata 
# print(mushroom.metadata) 
  
# variable information 
print(mushroom.variables) 

# change to desired scikit shape (1D series)
y = y["poisonous"]

# to encode data
enc = OneHotEncoder(handle_unknown="ignore")

# for hot encoder to determine categories of each feature
enc.fit(X)

# transform features
X = enc.transform(X)

print(X)

# encode targets
le = LabelEncoder()
y = le.fit_transform(y) 

# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize sequential model with layers
model = Sequential()
model.add(Dense(12, input_shape=(117,), activation="relu"))
model.add(Dense(1, activation="sigmoid"))

# compile keras model
model.compile(loss='binary_crossentropy', optimizer="adam", metrics=["accuracy"])

# fit model to dataset
model.fit(X_train , y_train, epochs=5, batch_size=5)

_, accuracy = model.evaluate(X_test, y_test)

# print results
print("Accuracy: ", accuracy)
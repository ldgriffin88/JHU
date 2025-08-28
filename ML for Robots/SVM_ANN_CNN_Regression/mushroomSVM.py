import pandas
from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder

"""
This file takes mushroom data from the URL below and uses the scikit SVM to classify mushrooms. Since the data is not numerical, it is encoded using scikits OneHotEncoder. The SVM uses a linear kernel and outputs the classification report to show precision, recall, and f1-score

Data: https://archive.ics.uci.edu/dataset/73/mushroom

OneHotEncoder Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

Other Sources:
- https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
- https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python
  
"""
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73)
  
# data (as pandas dataframes) 
X = mushroom.data.features
y = mushroom.data.targets
  
# # metadata 
# print(mushroom.metadata)

# variable information 
# print(mushroom.variables)

# change to desired scikit shape (1D series)
y = y['poisonous']

# to encode data
enc = OneHotEncoder(handle_unknown="ignore")

# fot hot encoder to determine categories of each feature
enc.fit(X)

# transform features
X = enc.transform(X)
# print("Transformed X")
# print(X)

# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, stratify=y)

#Create a svm Classifier
clf = svm.SVC(kernel='linear') 

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# output report
print(classification_report(y_test,y_pred))

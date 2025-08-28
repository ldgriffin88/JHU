import pandas
from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import  classification_report

"""
This file takes iris data from the URL below and uses the scikit SVM to classify it. 

Data: https://archive.ics.uci.edu/dataset/53/iris

Other Sources:
- https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
- https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python
  
"""

# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# # metadata 
# print(iris.metadata) 

# variable information 
# print(iris.variables)

# change to desired scikit shape (1D series)
y = y['class']

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

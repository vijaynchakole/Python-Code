import pandas as pd
import numpy as np
import matplotlib
import scipy as sp
import sklearn
import sys
import os
from IPython.display import display
import IPython
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import mglearn

import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")



[9]
#The iris object that is returned by load_iris is a Bunch object,
# which is very similar to a dictionary. It contains keys and values:
iris_dataset = load_iris()

[10]
#print(f"Keys of iris_dataset : {iris_dataset.keys()}")
#The value of the key DESCR is a short description of the dataset.
[11]
#print(iris_dataset['DESCR'][:193] + "\n...")

[12]
#The value of the key target_names is an array of strings,
# containing the species of flower that we want to predict:
#print(iris_dataset['target_names'])

[13]
#The value of feature_names is a list of strings, giving the description of each feature
#print(f"Features names : \n {iris_dataset['feature_names']}")

[14]
#The data itself is contained in the target and data fields.
# data contains the numeric measurements of sepal length, sepal width, petal length, and petal width in a NumPy array
#print(f"type of data : {type(iris_dataset['data'])}")

[15]
#print(f"shape of data : {iris_dataset['data'].shape}")

[16]
#print(f"First Five rows of data : \n {iris_dataset['data'][:5]}")
#From this data, we can see that all of the first five flowers have a petal width of 0.2 cm
# and that the first flower has the longest sepal, at 5.1 cm.

[17]
#The target array contains the species of each of the flowers that were measured, also as a NumPy array:
#print(f"Type of target : {type(iris_dataset['target'])}")
#target is a one-dimensional array, with one entry per flower

[18]
#print(f"shape of target : {iris_dataset['target'].shape}")
#The species are encoded as integers from 0 to 2:

[19]
#print(f"Target : \n {iris_dataset['target']}")
#The meanings of the numbers are given by the iris['target_names'] array: 0 means setosa,
# 1 means versicolor, and 2 means virginica.
#print(iris_dataset)

[20]
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

#The output of the train_test_split function is X_train, X_test, y_train, and y_test,
# which are all NumPy arrays. X_train contains 75% of the rows of the dataset, and X_test contains the remaining 25%:

[21]
#print(f"iris data shape : {iris_dataset['data'].shape}")
#print(f"iris target : { iris_dataset['target'].shape}")
#print(f"X_train shape : {X_train.shape}")
#print(f"y_train shape : {y_train.shape}")

[22]
#print(f"X_test shape : {X_test.shape}")
#print(f"y_test shape : {y_test.shape}")

[23]
#create dataframe from data in X_train
#label the columns using the strings in iris_dataset.feature_names

iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
#print(iris_dataframe)

#create a scatter matrix from the dataframe, color byn y_train
#pd.plotting.scatter_matrix(iris_dataframe,c=y_train, figsize = (15,15), marker ='o', hist_kwds = {'bins' : 20}, s = 60,alpha =.8, cmap = mglearn.cm3 )
#plt.show()
[24]
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

#To build the model on the training set, we call the fit method of the knn object
[25]
knn.fit(X_train,y_train)

#print(knn.fit(X_train,y_train))
#Making prediction
[26]
X_new = np.array([[5,2.9,1,0.2]])
#print(f"X_new shape : {X_new.shape}")
#i = 10
#print(i)
[27]
prediction = knn.predict(X_new)
print(f"Prediction : {prediction}")
print(f"predicted target name : {iris_dataset['target_names'][prediction]}")
# Our model predicts that this new iris belongs to the class 0, meaning its species is setosa
[28]
y_pred = knn.predict(X_test)
print(f"Test Set Predictions:\n {y_pred}")

[29]
print(f"test set score : {np.mean(y_pred == y_test):.2f}")

#We can also use the score method of the knn object, which will compute the test set accuracy for us
[30]
print(f"Test set score: {knn.score(X_test,y_test):.2f}")


#Here is a summary of the code needed for the whole training and evaluation procedure:
#KNN Algorithm
[31]
X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
print(f"Test set score : {knn.score(X_test,y_test):.2f}")


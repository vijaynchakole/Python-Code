# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:55:30 2020

@author: hp
"""

from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target
X
y


# Training and Test Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30,
                                                    random_state = 42)

scaler = preprocessing.StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


knn = neighbors.KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)
pred_y = knn.predict(X_test)
accuracy_score(y_test, pred_y)

###############################################################################
# Encoding Categorical Features
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()
y = encode.fit_transform(y)

###############################################################################

# Imputing  Missing Values
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = 0, strategy = "mean")
imp.fit_transform(X_train)

###############################################################################

# Generating Polynomial Features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(5)
poly.fit_transform(X)

###############################################################################

# Preprocessing The Data

# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
standardized_X = scaler.fit_transform(X_train)
standardized_X_test = scaler.fit_transform(X_test)


###############################################################################

# Normalization
from sklearn.preprocessing import Normalizer
scaler = Normalizer()
normalized_X_train = scaler.fit_transform(X_train)
normalized_X_test = scaler.fit_transform(X_test)


###############################################################################

# Binarization
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold = 0.0)
binary_X = binarizer.fit_transform(X)

###############################################################################

# Create Your Model
# Supervised Learning Estimators

# Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize = True)

# Support Vector Machine
from sklearn.svm import SVC
svc = SVC(kernel = 'linear')

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

# KNN
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors = 5)


###############################################################################

# Unsupervised Learning Estimator

#Principal Component Analysis (PCA)
from sklearn.decomposition import PCA
pca = PCA(n_components = 0.95)

# KMeans
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters = 3, random_state = 42)

###############################################################################

# Model fitting

# Supervised learning 
lr.fit(X_train, y_train)
svc.fit(X_train, y_train)
knn.fit(X_train, y_train)

# Unsupervised learning
k_means.fit(X_train)
pca_model = pca.fit_transform(X_train)

###############################################################################
# Prediction
# SUpervised Estimators
pred_y = svc.predict(X_test)
pred_y = lr.predict(X_test)
pred_y = knn.predict(X_test)

# Unsupervised Estimators
pred_y = k_means.predict(X_test)

###############################################################################

# Evaluate Your Model performance

# Classification matrics

# Accuracy Score
knn.score(X_test, y_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred_y)


# Classification report
from sklearn.metrics import  classification_report
classification_report(y_test, pred_y)


# Cunfusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, pred_y)

###############################################################################

# Regression matrix

# Mean Absolute Error
from sklearn.metrics import mean_absolute_error
y_true = [3,-0.5, 2]
mean_absolute_error(y_true, pred_y)


# Mean Square Error
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, pred_y)


# R Square
from sklearn.metrics import r2_score
r2_score(y_true, pred_y)

###############################################################################

# Clustering Metrics

# Adjusted Rand Index
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(y_true, pred_y)

# Homogeneity
from sklearn.metrics import homogeneity_score
homogeneity_score(y_true, pred_y)

# V-measure
from sklearn.metrics import v_measure_score
v_measure_score(y_true, pred_y)


###############################################################################

# Cross-Validation
from sklearn.model_selection import cross_val_score
cross_val_score(knn, X_train, cv = 4)
cross_val_score(lr, X_train, cv = 2)
cross_val_score(lr, X, y, cv = 2)


###############################################################################

# Tune Your Model
import numpy as np
# Grid Search
from sklearn.model_selection import GridSearchCV

params = {"n_neighbors" : np.arange(1, 3), "metrics" : ["euclidean", "cityblock"]}

grid = GridSearchCV(estimator = knn, param_grid = params )
grid.fit(X_train, y_train)
grid.best_score_
grid.best_estimator_.n_neighbors

###############################################################################

from sklearn.model_selection import RandomizedSearchCV

params = {"n_neighbors" : range(1, 5),
          "weight" : ["uniform", "distance"]}


research = RandomizedSearchCV(estimator = knn, param_distributions = params, cv = 4,
                              n_iter = 8, random_state = 42)


research.fit(X_train, y_train)
research.best_score_

###############################################################################




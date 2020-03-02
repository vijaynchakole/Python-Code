# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 04:09:24 2020

@author: hp
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,Normalizer
from sklearn.decomposition import PCA

nutrient = pd.read_csv(r"C:/Users/hp/PycharmProjects/college/nutrient.csv")
nutrient

nutrient.columns
type(nutrient)
nutrient = nutrient.drop('Food_Item', axis = 1)

""" 

1) StandardScaler() : The StandardScaler in scikit-learn ensures
 that for each feature the mean is 0 and the variance is 1,
 bringing all features to the same magnitude.

2) MinMaxScaler() :  The MinMaxScaler, on the other hand,
 shifts the data such that all features are exactly between 0 and 1. 

3) RobustScaler() : the RobustScaler uses the median and quartiles,1 instead of mean and variance.
 This makes the RobustScaler ignore data points that are very different from the rest (like measurement errors). 
These odd data points are also called outliers,



4) Normalizer() : the Normalizer does a very different kind of rescaling. 
It scales each data point such that the feature vector has a Euclidean length of 1

"""


#scaler = StandardScaler() #first two PC = 66%
#scaler = MinMaxScaler()  # first two PC = 73%
#scaler = RobustScaler()   #first two PC = 90%
scaler = Normalizer()     # first two PC = 99.33%  ..........first PC = 97%

scaler.fit(nutrient)

nutrient_scaled = scaler.fit_transform(nutrient)

pca = PCA(svd_solver = 'auto')

principalComponents = pca.fit_transform(nutrient_scaled)
principalComponents.shape

df_plot = pd.DataFrame(principalComponents,columns=['PC1','PC2','PC3','PC4','PC5'],index = nutrient.index)
df_plot

#Variance Explained

import matplotlib.pyplot as plt

y = pca.explained_variance_ratio_ * 100
x = np.arange(1,6)
plt.plot(x,y)
plt.show()


print((pca.explained_variance_ratio_*100))


#Cumulative Variation Explained

import matplotlib.pyplot as plt

y = np.cumsum(pca.explained_variance_ratio_ * 100)
x = np.arange(1,6)
plt.plot(x,y)
plt.show()


print(np.cumsum(pca.explained_variance_ratio_ * 100))

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 03:21:47 2020

@author: hp
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,Normalizer
from sklearn.decomposition import PCA

protein = pd.read_csv(r"C:/Users/hp/PycharmProjects/college/Protein.csv")
protein

protein.columns
type(protein)
protein = protein.drop('Country', axis = 1)

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

#best scaler is Normalizer first 2 components gives you 80 percentage of information of data



#scaler = StandardScaler()   # first two PC = 62%
#scaler = MinMaxScaler()     # first two PC = 63%
#scaler = RobustScaler()     # first two PC = 64%
scaler = Normalizer()    # first two PC = 81% with third PC = 90% with forth PC = 96%

scaler.fit(protein)

protein_scaled = scaler.fit_transform(protein)

pca = PCA(svd_solver = 'auto')

principalComponents = pca.fit_transform(protein_scaled)
principalComponents.shape

df_plot = pd.DataFrame(principalComponents,columns=['PC1','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9'],index = protein.index)
df_plot

#Variance Explained

import matplotlib.pyplot as plt

y = pca.explained_variance_ratio_ * 100
x = np.arange(1,10)
plt.plot(x,y)
plt.show()


print(pca.explained_variance_ratio_ * 100)


#Cumulative Variation Explained

import matplotlib.pyplot as plt

y = np.cumsum(pca.explained_variance_ratio_ * 100)
x = np.arange(1,10)
plt.plot(x,y)
plt.show()


print(np.cumsum(pca.explained_variance_ratio_ * 100))



# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 04:26:20 2020

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 04:09:24 2020

@author: hp
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,Normalizer
from sklearn.decomposition import PCA

Bankrupt = pd.read_csv(r"C:/Users/hp/PycharmProjects/college/Bankruptcy.csv")
Bankrupt

Bankrupt.columns
type(Bankrupt)
Bankrupt = Bankrupt.drop(['NO','D'], axis = 1)
Bankrupt.columns

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


#scaler = StandardScaler() #first two PC = 48%
#scaler = MinMaxScaler()  # first two PC = 46%
#scaler = RobustScaler()   #first two PC = 47%
scaler = Normalizer()     # first two PC = 96.53%  .first PC = 67% , first three PC = 98.54%

scaler.fit(Bankrupt)

Bankrupt_scaled = scaler.fit_transform(Bankrupt)

pca = PCA(svd_solver = 'auto')

principalComponents = pca.fit_transform(Bankrupt_scaled)
principalComponents.shape

df_plot = pd.DataFrame(principalComponents,columns=['YR', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10',
       'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20',
       'R21', 'R22', 'R23', 'R24'],index = Bankrupt.index)
df_plot

#Variance Explained

import matplotlib.pyplot as plt

y = pca.explained_variance_ratio_ * 100
x = np.arange(1,26)
plt.plot(x,y)
plt.show()


print((pca.explained_variance_ratio_*100))


#Cumulative Variation Explained

import matplotlib.pyplot as plt

y = np.cumsum(pca.explained_variance_ratio_ * 100)
x = np.arange(1,26)
plt.plot(x,y)
plt.show()


print(np.cumsum(pca.explained_variance_ratio_ * 100))



###################################################################################

### From: https://github.com/teddyroland/python-biplot/blob/master/biplot.py
import seaborn as sns
 
# Scatter plot based and assigne color based on 'label - y'
sns.lmplot('YR', 'R1', data=df_plot, fit_reg = False, size = 15, scatter_kws={"s": 100})
 
# set the maximum variance of the first two PCs
# this will be the end point of the arrow of each **original features**
xvector = pca.components_[0]
yvector = pca.components_[1]
 
# value of the first two PCs, set the x, y axis boundary
xs = df_plot['YR']
ys = df_plot['R1']
 
## visualize projections
 
## Note: scale values for arrows and text are a bit inelegant as of now,
##       so feel free to play around with them
for i in range(len(xvector)):
    # arrows project features (ie columns from csv) as vectors onto PC axes
    # we can adjust length and the size of the arrow
    plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
              color='r', width=0.005, head_width=0.05)
    plt.text(xvector[i]*max(xs)*1.1, yvector[i]*max(ys)*1.1,
             list(Bankrupt.columns.values)[i], color='r')
 
for i in range(len(xs)):
    plt.text(xs[i]*1.08, ys[i]*1.08, list(Bankrupt.index)[i], color='b') # index number of each observations
plt.title('PCA Plot of first PCs')
plt.show()

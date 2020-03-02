import numpy as np
import pandas as pd
milk = pd.read_csv("F:/Python Material/Python Course/Datasets/milk.csv",index_col=0)
milk.head()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)

from sklearn.decomposition import PCA
pca = PCA()
principalComponents = pca.fit_transform(milkscaled)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_) 
print(pca.explained_variance_ratio_ * 100) 
 

import matplotlib.pyplot as plt
y = pca.explained_variance_ratio_ * 100
x = np.arange(1,6)
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
y = np.cumsum(pca.explained_variance_ratio_ * 100)
x = np.arange(1,6)
plt.plot(x,y)
plt.show()

# principalComponents are PCA scores

df_plot = pd.DataFrame(principalComponents,
                 columns = ['PC1', 'PC2','PC3','PC4','PC5'],
                 index = milk.index)

pca_loadings = pd.DataFrame(pca.components_.T, index=milk.columns, columns=['V1', 'V2','V3','V4','V5'] )
pca_loadings

#### Calculating Scores alternatively using numpy
from numpy.linalg import eig
milkscaled = pd.DataFrame(milkscaled)
values, vectors = eig(milkscaled.corr())
print(values)
print(vectors)
PCA_Score = np.matmul(milkscaled,vectors)

# OR Using SVD using scipy
from scipy.linalg import svd
U, s, VT = svd(milkscaled)
PCA_Score2 = np.matmul(milkscaled,VT.T)


##########################################################
milkscaled = pd.DataFrame(milkscaled,columns=milk.columns, index=milk.index)
##########################################################
### From: https://github.com/teddyroland/python-biplot/blob/master/biplot.py
import seaborn as sns
 
# Scatter plot based and assigne color based on 'label - y'
sns.lmplot('PC1', 'PC2', data=df_plot, fit_reg = False, size = 15, scatter_kws={"s": 100})
 
# set the maximum variance of the first two PCs
# this will be the end point of the arrow of each **original features**
xvector = pca.components_[0]
yvector = pca.components_[1]
 
# value of the first two PCs, set the x, y axis boundary
xs = df_plot['PC1']
ys = df_plot['PC2']
 
## visualize projections
 
## Note: scale values for arrows and text are a bit inelegant as of now,
##       so feel free to play around with them
for i in range(len(xvector)):
    # arrows project features (ie columns from csv) as vectors onto PC axes
    # we can adjust length and the size of the arrow
    plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
              color='r', width=0.005, head_width=0.05)
    plt.text(xvector[i]*max(xs)*1.1, yvector[i]*max(ys)*1.1,
             list(milk.columns.values)[i], color='r')
 
for i in range(len(xs)):
    plt.text(xs[i]*1.08, ys[i]*1.08, list(milk.index)[i], color='b') # index number of each observations
plt.title('PCA Plot of first PCs')
plt.show()
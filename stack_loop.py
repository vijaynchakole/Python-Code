# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 00:20:56 2020

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier


bankrupt = pd.read_csv(r"C:/Users/hp/PycharmProjects/college/Bankruptcy.csv")

bankrupt
bankrupt.columns

bankrupt = bankrupt.drop('NO',axis = 1)
bankrupt

#y = bankrupt[['D']]
#y.shape
#y

#type(y)
y = bankrupt[['D']]
y
type(y)

X = bankrupt.iloc[:,1:26]
X.columns
type(X)



X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state=42)

X_train.shape
X_test.shape
y_train.shape
y_test.shape


#Logistic Regression
logreg = LogisticRegression(random_state = 42)
logreg.fit(X_train,y_train)
logreg_pred_y = logreg.predict(X_train)
logreg_pred_y.shape


#Gaussian naive bayes
Gaussian = GaussianNB()
Gaussian.fit(X_train,y_train)
Gaussian_pred_y = Gaussian.predict(X_train)
Gaussian_pred_y.shape


#DecisionTreeClassifier
DTC = DecisionTreeClassifier(random_state = 42, max_depth = 4)
DTC.fit(X_train,y_train)
DTC_pred_y = DTC.predict(X_train)
DTC_pred_y.shape

#support vector classifier
svc = SVC(probability = True)
svc.fit(X_train,y_train)
svc_pred_y = svc.predict(X_train)


# support vector Linear classifier
svcl =SVC(probability = True, kernel = 'linear')
svcl.fit(X_train,y_train)
svcl_pred_y = svcl.predict(X_train)
svcl_pred_y.shape

"""

svcl = SVC(probability = True,kernel = 'linear')
svcl.fit(X_train,y_train)
svcl_pred_y = svc.predict(X_train)
svcl_pred_y.shape
"""

#combining all predicted Y of train set

combine_X_train = np.column_stack((logreg_pred_y,Gaussian_pred_y,DTC_pred_y,svc_pred_y))

combine_X_train.shape

type(combine_X_train)

combine_X_train = pd.DataFrame(combine_X_train, columns = ["logreg_pred_y", "Gaussian_pred_y", "DTC_pred_y","svc_pred_y"])
combine_X_train.shape



from xgboost import XGBClassifier
xgb = XGBClassifier(random_state=2019)
fit_xgb = xgb.fit(combine_X_train,y_train)

#Test operation######################

logreg_pred_y= logreg.predict(X_test)
Gaussian_pred_y = Gaussian.predict(X_test)
DTC_pred_y = DTC.predict(X_test) 
svc_pred_y = svc.predict(X_test)


combine_X_test = np.column_stack((logreg_pred_y,Gaussian_pred_y,DTC_pred_y,svc_pred_y))


combine_X_test.shape
logreg_pred_y.shape
Gaussian_pred_y.shape
DTC_pred_y.shape
svc_pred_y.shape
combine_X_test = pd.DataFrame(combine_X_test, columns = ["logreg_pred_y","Gaussian_pred_y","DTC_pred_y","svc_pred_y"])
combine_X_test.shape


#final Y################################

from xgboost import XGBClassifier
xgb = XGBClassifier(random_state = 42)
xgb.fit(combine_X_train,y_train)
combine_X_train.shape
y_train.shape
pred_y_test = xgb.predict(combine_X_test)
combine_X_test.shape

pred_y_test.shape

roc_auc_score(y_test,pred_y_test)

# whole dataset with combine values


combine_X_train.set_index(X_train.index,inplace=True)
combine_X_original = pd.concat([X_train,combine_X_train],axis = 1)

combine_X_original.shape



from xgboost import XGBClassifier
xgb = XGBClassifier(random_state = 42)
xgb.fit(combine_X_original,y_train)





combine_X_test.set_index(X_test.index,inplace=True)
X_test.shape

combine_X_test_original = pd.concat([X_test,combine_X_test],axis = 1)
combine_X_test_original.shape

xgb = XGBClassifier(random_state = 42)
xgb.fit(combine_X_original,y_train)
combine_X_test_original.shape
pred_y = xgb.predict(combine_X_test_original)
pred_y.shape


roc_auc_score(y_test,pred_y)

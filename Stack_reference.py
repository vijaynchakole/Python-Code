# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:55:01 2020

@author: hp
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:/Users/hp/PycharmProjects/college/Bankruptcy.csv")

df.columns

X = df.iloc[:,2:27]
y = df.iloc[:,1]

from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score


# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state=2019)


from sklearn.linear_model import LogisticRegression
glm = LogisticRegression()
glm.fit(X_train,y_train)
y_glm = glm.predict_proba(X_train)[:,1]
y_glm.shape

from sklearn.naive_bayes import GaussianNB
gaussian = GaussianNB()
gaussian.fit(X_train, y_train)
y_gauss = gaussian.predict_proba(X_train)[:,1]
y_gauss.shape

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(random_state=2019,max_depth=4)
dtc.fit(X_train,y_train)
y_dtc = dtc.predict_proba(X_train)[:,1]
y_dtc.shape

from sklearn.svm import SVC
svc = SVC(probability = True)
svc.fit(X_train, y_train)
y_svc = svc.predict_proba(X_train)[:,1]
y_svc.shape


from sklearn.svm import SVC
svcl = SVC(probability = True,kernel='linear')
svcl.fit(X_train, y_train)
y_svcl = svcl.predict_proba(X_train)[:,1]
y_svcl.shape

comb_X = np.column_stack((y_glm,y_gauss,y_svc,y_svcl))
comb_X.shape
y_glm.shape
y_gauss.shape
y_svc.shape
y_svcl.shape
comb_X.shape
## Convert to pandas frame
comb_X = pd.DataFrame(comb_X,columns=['y_glm','y_gauss','y_svc','y_svcl'])
comb_X.shape
from xgboost import XGBClassifier
xgb = XGBClassifier(random_state=2019)
fit_xgb = xgb.fit(comb_X,y_train)

####### test operations ############

y_glm = glm.predict_proba(X_test)[:,1]
y_gauss = gaussian.predict_proba(X_test)[:,1]
y_dtc = dtc.predict_proba(X_test)[:,1]
y_svc = svc.predict_proba(X_test)[:,1]
y_svcl = svcl.predict_proba(X_test)[:,1]

comb_X_test = np.column_stack((y_glm,y_gauss,y_svc,y_svcl))

comb_X_test.shape
y_glm.shape
y_gauss.shape
y_svc.shape
y_svcl.shape
## Convert to pandas frame
comb_X_test = pd.DataFrame(comb_X_test,columns=['y_glm','y_gauss','y_svc','y_svcl'])
comb_X_test.shape
y_glm.shape
########## Y final ############
xgb = XGBClassifier(random_state=2019)
fit_xgb = xgb.fit(comb_X,y_train)
y_pred_prob = xgb.predict_proba(comb_X_test)[:,1]

y_train.shape
comb_X.shape

from sklearn.metrics import roc_auc_score
roc_auc_score(y_test, y_pred_prob)




############# operations on original data sets  ###############

comb_X.set_index(X_train.index,inplace=True)
comb_X_original = pd.concat([X_train,comb_X],axis='columns')

from xgboost import XGBClassifier
xgb = XGBClassifier(random_state=2019)
fit_xgb = xgb.fit(comb_X_original,y_train)


comb_X_test.set_index(X_test.index,inplace=True)
comb_X_test_original = pd.concat([X_test,comb_X_test],axis='columns')

xgb = XGBClassifier(random_state=2019)
fit_xgb = xgb.fit(comb_X_original,y_train)
y_pred_prob = xgb.predict_proba(comb_X_test_original)[:,1]

from sklearn.metrics import roc_auc_score
roc_auc_score(y_test, y_pred_prob)


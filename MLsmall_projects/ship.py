# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:24:52 2019

@author: aarus
"""

import pandas as pd


dataset=pd.read_csv('train.csv')


# feature matrix [4,5,6,7] 4 is string
X=dataset.iloc[:,[4,5,6,7]].values
#vector of prediction [1]
y=dataset.iloc[:,1].values


from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
X[:,0]=lab.fit_transform(X[:,0])


from sklearn.impute import SimpleImputer
SI=SimpleImputer()
X[:,[1]]=SI.fit_transform(X[:,[1]])


test_dataset=pd.read_csv('test.csv')

X_test=test_dataset.iloc[:,[3,4,5,6]].values

X_test[:,0]=lab.fit_transform(X_test[:,0])
X_test[:,[1]]=SI.fit_transform(X_test[:,[1]])





test_y_dataset=pd.read_csv('ship_pred.csv')

y_test=test_y_dataset.iloc[:,1].values



from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(X,y)

y_pred=dtc.predict(X_test)


dtc.score(X_test,y_test)




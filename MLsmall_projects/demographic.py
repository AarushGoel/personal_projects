# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:16:46 2019

@author: aarus
"""

import pandas as pd


dataset=pd.read_csv('data2.csv')


X=dataset.iloc[:,1:4].values
y=dataset.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
X[:,0]=lab.fit_transform(X[:,0])
y=lab.fit_transform(y)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
knn=LogisticRegression()
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)


knn.score(X_train,y_train)

knn.score(X_test,y_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)








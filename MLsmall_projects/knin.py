# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:03:23 2019

@author: aarus
"""

import pandas as pd
from sklearn.datasets import load_iris

dataset=load_iris() 


X=dataset.data
y=dataset.target


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)


from sklearn.neighbors import KNeighborsClassifier
km=KNeighborsClassifier(n_neighbors=5)
km.fit(X_train,y_train)

y_pred=km.predict(X_test)
km.score(X_test,y_test)
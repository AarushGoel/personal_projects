# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:43:03 2019

@author: aarus
"""

import pandas as pd


dataset=pd.read_csv('housing.csv')

X=dataset.iloc[:,[0,1,2,3,4,5,6,7,9]].values
y=dataset.iloc[:,-2].values



from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()

X[:,8]=lab.fit_transform(X[:,8])



from sklearn.impute import SimpleImputer
si=SimpleImputer()
X=si.fit_transform(X)

'''
from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(categorical_features=[8])
X=oh.fit_transform(X)
X=X.toarray()
'''

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2,include_bias=False)

X_train_poly=poly.fit_transform(X_train)


X_test_poly=poly.fit_transform(X_test)


from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()


lin_reg.fit(X_train_poly,y_train)


lin_reg.score(X_test_poly,y_test)
lin_reg.score(X_train_poly,y_train)

y_predict=lin_reg.predict(X_test_poly)

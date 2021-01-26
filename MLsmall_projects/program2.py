# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:11:17 2019

@author: aarus
"""

import pandas as pd


dataset=pd.read_csv('data1.csv')

X=dataset.iloc[:,0:3].values
z=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
X[:,2]=lab.fit_transform(X[:,2])
lab.classes_
lab2=LabelEncoder()

z=lab2.fit_transform(z)
lab2.classes_

from sklearn.impute import SimpleImputer
sim=SimpleImputer()
X[:,0:2]=sim.fit_transform(X[:,0:2])


from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(categorical_features=[2])
X=oh.fit_transform(X)
X=X.toarray()




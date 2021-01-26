# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:28:05 2019

@author: aarus
"""


import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv('data1.csv')


X=dataset.iloc[:,0:3].values
z=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
X[:,2]=lab.fit_transform(X[:,2])


lab2=LabelEncoder()
z=lab2.fit_transform(z)

plt.scatter(X[:0],X[:1])
plt.xlabel('Age')
plt.ylabel('')
plt.show()

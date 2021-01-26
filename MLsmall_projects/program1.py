# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:14:28 2019

@author: aarus
"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder


dataset=pd.read_csv('data2.csv')

X=dataset.iloc[:,2:4].values
z=dataset.iloc[:,4].values

lab=LabelEncoder()
z=lab.fit_transform(z)
lab.classes_

plt.scatter(X[z==0,0],X[z==0,1],c='red',label='High Income')
plt.scatter(X[z==1,0],X[z==1,1],c='blue',label='Low Income')
plt.scatter(X[z==2,0],X[z==2,1],c='green',label='lower Middle Income')
plt.scatter(X[z==3,0],X[z==3,1],c='black',label='Upper Middle Income')

plt.title('Analysis on Internet Users')
plt.xlabel('Birth Rate')
plt.ylabel('Internet Users')
plt.legend()

plt.show()








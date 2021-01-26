# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:34:23 2019

@author: aarus
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset =pd.read_csv('data2.csv')

X=dataset.iloc[:,2].values
X=X.reshape(-1,1)
y=dataset.iloc[:,3].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)




plt.scatter(X,y)
plt.show()

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)


plt.plot(X_train,lin_reg.predict(X_train))
plt.show()

lin_reg.score(X_test,y_test)
lin_reg.score(X_train,y_train)



lin_reg.predict([[11.044]])

lin_reg.coef_
lin_reg.intercept_

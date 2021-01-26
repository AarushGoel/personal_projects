# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:21:28 2019

@author: aarus
"""


import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv('data2.csv')

X=dataset.iloc[:,2].values
X=X.reshape(-1,1)
y=dataset.iloc[:,3].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)

X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)




plt.scatter(X_train,y_train)
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2,include_bias=False)
X_poly=poly.fit_transform(X_train)


from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X_poly,y_train)


X_poly_test=poly.fit_transform(X_test)

plt.scatter(X_train,y_train)
plt.plot(X_test,lin_reg.predict(X_poly_test))
plt.show()

y_pred=lin_reg.predict(X_poly_test)


lin_reg.score(X_poly,y_train)

lin_reg.score(X_poly_test,y_test)





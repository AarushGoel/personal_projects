# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:17:25 2019

@author: aarus
"""

import numpy as np
import matplotlib.pyplot as plt



m=100

X=10* np.random.randn(m,1) -3

y=5*(X**2)+2*X +2 +np.random.randn(m,1)



plt.scatter(X,y)
plt.axis([-8,8,0,450])
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2,include_bias=False)
X_poly=poly.fit_transform(X)

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X_poly,y)

#lin_reg.score(X_poly,y)

X_new=np.linspace(-8,8,100).reshape(-1,1)

X_new_poly=poly.fit_transform(X_new)

y_new=lin_reg.predict(X_new_poly)

plt.scatter(X,y)
plt.plot(X_new,y_new,c='r')
plt.show()


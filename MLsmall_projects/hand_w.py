# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:00:09 2019

@author: aarus
"""

import pandas as pd
import matplotlib.pyplot as plt


from sklearn.datasets import load_digits
dataset=load_digits()

X=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X,y)

y[125]
some_digit=X[125]
some_digit_image=some_digit.reshape(8,8)
plt.imshow(some_digit_image)
plt.show()
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(max_depth=15)
dtc.fit(X_train,y_train)
dtc.score(X_test,y_test)

dtc.predict(X[[125],0:64])




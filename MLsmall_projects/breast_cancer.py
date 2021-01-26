# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:43:43 2019

@author: aarus
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



from sklearn.datasets import load_breast_cancer
dataset=load_breast_cancer()


X=dataset.data
y=dataset.target


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)



from sklearn.linear_model import LogisticRegression
log_reg=LogisticRegression()
log_reg.fit(X,y)


y_pred=log_reg.predict(X_test)


log_reg.score(X_train,y_train)

log_reg.score(X_test,y_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)




from sklearn.metrics import precision_score,recall_score,f1_score
precision_score(y_test,y_pred)
recall_score(y_test,y_pred)
f1_score(y_test,y_pred)





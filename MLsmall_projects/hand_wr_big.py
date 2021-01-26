# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:40:11 2019

@author: aarus
"""

import matplotlib.pyplot as plt

from sklearn.datasets import fetch_mldata
dataset=fetch_mldata('MNIST original')

X=dataset.data
y=dataset.target

s_d=X[500] #y[500]
s_d_i=s_d.reshape(28,28)

plt.imshow(s_d_i)
plt.show()


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(max_depth=13)
dtc.fit(X_train,y_train)






dtc.score(X_test,y_test)
y[12000]
y_pred=dtc.predict(X[[12000],0:784])








from sklearn.tree import export_graphviz
export_graphviz(dtc,out_file='tree.dot')


import graphviz

with open('tree.dot') as f:
    dot_graph=f.read()
    graphviz.Source(dot_graph)
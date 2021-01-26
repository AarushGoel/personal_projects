# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:42:54 2019

@author: aarus
"""

import pandas as pd


dataset=pd.read_csv('data3.csv',names=['age',
                                       'workclass',                                    
                                       'fnlwgt',
                                       'education',
                                       'education-num',
                                       'marital-status',
                                       'occupation',
                                       'relationship',
                                       'race',
                                       'gender',
                                       'capital-gain',
                                       'capital-loss',
                                       'hours-per-week',
                                       'native-country',
                                       'salary'],na_values=' ?')



dataset=dataset.drop(columns=['education'])

X=dataset.iloc[:,0:13].values
y=dataset.iloc[:,-1].values


#integer values[0,2,9,10,11]
#String values[1,4,5,6,7,8,12]
#[3] is already label encode

from sklearn.impute import SimpleImputer
SI=SimpleImputer()
X[:,[0,2,9,10,11]]=SI.fit_transform(X[:,[0,2,9,10,11]])


temp=pd.DataFrame(X[:,[1,4,5,6,7,8,12]])

for i in range(7):
    temp[i]=temp[i].fillna((temp[i].value_counts()).idxmax())
    
X[:,[1,4,5,6,7,8,12]]=temp

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()


for i in [1,4,5,6,7,8,12]:
    X[:,i]=lab.fit_transform(X[:,i])
    
    
from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(categorical_features=[[1,3,4,5,6,7,8,12]])

X=oh.fit_transform(X)
X=X.toarray()


y=lab.fit_transform(y)
lab.classes_

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)


from sklearn.linear_model import LogisticRegression
log_reg=LogisticRegression()
log_reg.fit(X_train,y_train)


log_reg.score(X_test,y_test)

y_pred=log_reg.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)



from sklearn.metrics import precision_score,recall_score,f1_score
precision_score(y_test,y_pred)
recall_score(y_test,y_pred)
f1_score(y_test,y_pred)

















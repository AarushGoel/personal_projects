# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:18:09 2019

@author: aarus
"""



import pandas as pd

dataset=pd.read_csv('bank.csv',na_values='unknown')


dataset=dataset.drop(columns=['poutcome'])

X=dataset.iloc[:,0:15].values
y=dataset.iloc[:,-1].values

#integer col index [0,5,9,11,12,13,14]
#strings col index [1,2,3,4,6,7,8,10,15]


from sklearn.impute import SimpleImputer
si=SimpleImputer()
X[:,[0,5,9,11,12,13,14]]=si.fit_transform(X[:,[0,5,9,11,12,13,14]])

temp=pd.DataFrame(X[:,[1,2,3,4,6,7,8,10]])

temp[0].value_counts() # Management     969
temp[1].value_counts() # married        2797
temp[2].value_counts() # secondary      2306
temp[3].value_counts() # no             4445
temp[4].value_counts() # yes            2559
temp[5].value_counts() # no             3830
temp[6].value_counts() # cellular       2896
temp[7].value_counts() # may            1398
#temp[8].value_counts() # failure        490***********




temp[0]=temp[0].fillna('management') # now 1007
temp[1]=temp[1].fillna('married') # now 2797
temp[2]=temp[2].fillna('secondary') # now 2493
temp[3]=temp[3].fillna('no') # now 4445
temp[4]=temp[4].fillna('yes') # now 2559
temp[5]=temp[5].fillna('no') # now 3830
temp[6]=temp[6].fillna('cellular') # now 4220
temp[7]=temp[7].fillna('may') # now 1398
#temp[8]=temp[8].fillna('failure') # now 4195 ***********


X[:,[1,2,3,4,6,7,8,10]]=temp
del(temp)



from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()#[1,2,3,4,6,7,8,10,15]
X[:,1]=lab.fit_transform(X[:,1])
X[:,2]=lab.fit_transform(X[:,2])
X[:,3]=lab.fit_transform(X[:,3])
X[:,4]=lab.fit_transform(X[:,4])
X[:,6]=lab.fit_transform(X[:,6])
X[:,7]=lab.fit_transform(X[:,7])
X[:,8]=lab.fit_transform(X[:,8])
X[:,10]=lab.fit_transform(X[:,10])



y=lab.fit_transform(y)
lab.classes_




from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(categorical_features=[1,2,3,4,6,7,8,10])
X=oh.fit_transform(X)
X=X.toarray()



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)






from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)

knn.score(X_test,y_test)

y_pred=knn.predict(X_test)




from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)



from sklearn.metrics import precision_score,recall_score,f1_score
precision_score(y_test,y_pred)
recall_score(y_test,y_pred)
f1_score(y_test,y_pred)



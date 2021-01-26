

import pandas as pd


dataset=pd.read_csv('add1.csv')

X=dataset.iloc[:,1:8].values
#X=X.reshape(1,-1)
y=dataset.iloc[:,-1].values



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)


from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)

lin_reg.score(X_test,y_test)

y_predict=lin_reg.predict(X_test)



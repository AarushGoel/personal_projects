
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




dataset=pd.read_csv('blood.csv')

X=dataset.iloc[2:,0].values
X=X.reshape(-1,1)
y=dataset.iloc[2:,-1].values


plt.title('Linear Regression')
plt.scatter(X,y)

plt.xlabel('Age')
plt.ylabel('BP')




from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)



from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)

#plt.scatter(X,y)
plt.plot(X_test,lin_reg.predict(X_test))

temp=lin_reg.predict(X_test)

lin_reg.score(X_train,y_train)


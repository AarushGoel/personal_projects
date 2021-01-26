# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:08:36 2019

@author: aarus
"""

import pandas as pd

import nltk

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

import re


from sklearn.externals import joblib



dataset=pd.read_csv('tweet.csv')


pro_tweet=[]

for i in range(31962):
    tweet=re.sub('@[\w]*',' ',dataset['tweet'][i])
    tweet=re.sub('[^a-zA-z#]',' ',tweet)
    tweet=tweet.lower()
    tweet=tweet.split()
    
    tweet=[ps.stem(token) for token in tweet if not token in stopwords.words('english')]
    tweet=' '.join(tweet)
    pro_tweet.append(tweet)



from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=3000)
X=cv.fit_transform(pro_tweet)
X=X.toarray()

joblib.dump(cv,'words_data')

cv=joblib.load('words_data')

cv.get_feature_names()

cv_test = CountVectorizer(vocabulary=cv.get_feature_names())


X1=cv_test.fit_transform(pro_tweet)
X1=X1.toarray()




y=dataset['label'].values


from sklearn.naive_bayes import GaussianNB
n_b=GaussianNB()
n_b.fit(X,y)


n_b.score(X,y)

joblib.dump(n_b,'tweet_naive')

n_b=joblib.load('tweet_naive')

y_pred=n_b.predict(X1)
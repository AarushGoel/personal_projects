# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:32:15 2019

@author: aarus
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()




dataset= pd.read_csv()


import re

pro_tweet=[]


for i in range():
        
    tweet=re.sub('@[\w]*',' ',dataset['tweet'][i])
    tweet=re.sub('[^a-zA-Z#]',' ',tweet)
    tweet=tweet.lower()
    tweet=tweet.split()
    tweet=[ps.stem(token) for token in tweet if not token in stopwords.words('english')]
    pro_tweet.append(tweet)
    
    
    
    
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=3000)
X=cv.fit_transform(pro_tweet)
X=X.toarray()

    
y=dataset['label']
    
from sklearn.naive_bayes import GaussianNB
n_b=GaussianNB()
n_b.fit(X,y)

n_b.score(X,y)






    







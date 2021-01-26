# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:02:24 2020

@author: aarus
"""

import pandas as pd

import numpy

df1=pd.read_csv("train_submissions.csv")

df2=pd.read_csv("user_data.csv")
df3=pd.read_csv("problem_data.csv")

X=pd.Series()

y=df1.iloc[:,2]

dffinal=pd.DataFrame(columns=['user_id','submission_count','problem_solved','contribution',
                              'country','follower_count','last_online_time_seconds',
                              'max_rating','rating','rank','registration_time_seconds',
                              'problem_id','level_type','points','tags','attempts_range'])

for i in range(len(df1)):
    user_id=df1['user_id'][0]
    prob_id=df1['problem_id'][0]
    user_data=df2.loc[df2.user_id==user_id]
    problem_data=df3.loc[df3.problem_id==prob_id]
    
    s1=user_data.iloc[0]
    s2=problem_data.iloc[0]
    s=s1.append(s2)
    
    s=s.values.reshape(1,-1)
    
    dffinal=dffinal.append(pd.DataFrame(s,columns=['user_id','submission_count','problem_solved','contribution',
                              'country','follower_count','last_online_time_seconds',
                              'max_rating','rating','rank','registration_time_seconds',
                              'problem_id','level_type','points','tags']))
    
    
    
    
    
X=dffinal

y=y[0:8340]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y)
    









from sklearn.
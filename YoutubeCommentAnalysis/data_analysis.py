# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:39:16 2020

@author: aarus
"""

import pandas as pd

import seaborn as sns

import numpy

from matplotlib import pyplot as plt



    
dataframe=pd.read_excel("video_details.xlsx")

X=dataframe.iloc[:,[6,7]]

plt.barh(X['chName'],X['chSubs'])
plt.show()
plt.savefig("fig1.png")

tips=sns.load_dataset(X)


sns.barplot(X['chSubs'],X['chName'])

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:21:53 2019

@author: aarus
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



X=np.random.randn(100)
y= 4+7*X +np.random.randn(100)


plt.scatter(X,y)
plt.show()

X=np.c_[X,np.ones(100)]


theta=np.linalg.inv((X.T@X))  @ (X.T @y)


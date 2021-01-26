# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 01:19:41 2019

@author: aarus
"""




from webscrap import getpagesource
import pandas as pd
import re


    

def processComments(soup,title):
    
    comments=soup.find(id="comments")
    
    comments=comments.find_all(id="content-text")
    
    
    dataframe=pd.DataFrame(columns=['S.No','Comments'])
    
    i=0
    
    for item in comments:
        
        try:
            
            comment=item.contents[0]
        
            dataframe.loc[i,'S.No']=i
        
            dataframe.loc[i,'Comments']=comment
    
            i+=1
        
        except:
            continue
        
        
    dataframe.to_excel(f'{title}.xlsx')
    
   
    



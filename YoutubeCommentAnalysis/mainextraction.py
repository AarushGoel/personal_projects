# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 01:34:12 2019

@author: aarus
"""


import trendurl

from mainvideo import processVideoWork


def extration():
    
    list_urls=trendurl.getVideoLinks()
    
    
    processVideoWork(list_urls)    
    
    return True

if __name__=="__main__":
    
    if extration():
        print("Successfully Extract......")
        
    else:
        print("Failed")
        
        
        
        
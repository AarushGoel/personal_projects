# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:34:54 2019

@author: aarus
"""


from webscrap import getpagesource
import pandas as pd
import re

import ytcomments

import videodetails

import io

from selenium import webdriver

def processVideoWork(urls):
    
    
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path=r"D:/major project/chromedriver.exe",options=options)
    
    
    
    for url in urls:
        
        soup=getpagesource(driver,'https://www.youtube.com/'+url)
    
        
        
        
        title,val=videodetails.processVideoDetails(soup)
            
        if val:
            text=soup.prettify()
    
    
    
            with io.open(f"{title}.text","w",encoding="utf-8") as file:
                file.write(text)
                file.close()
            print(url+"Success")
    
    
    
    driver.close()
    
    return True    
    
    
        
        
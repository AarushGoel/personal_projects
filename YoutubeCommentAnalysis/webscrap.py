# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:14:52 2019

@author: aarus
"""


from bs4 import BeautifulSoup   

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import io
import time


def getpagesource(driver,url):
     
    
    driver.get(url)


    elm=driver.find_element_by_tag_name('html')
    
    time_end=time.time()+5
    

    elm.send_keys(Keys.SPACE)
    while time.time()<time_end:
        
        elm.send_keys(Keys.PAGE_DOWN)
        
    text=driver.page_source
    
    
    soup=BeautifulSoup(text,'html5lib')
    
    
    
    

    return soup







    
    

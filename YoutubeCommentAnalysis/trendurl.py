# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 01:03:56 2019

@author: aarus
"""


from bs4 import BeautifulSoup   

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import io
import time




from selenium.webdriver.chrome.options import Options
    

def getVideoLinks():
    
    url="https://www.youtube.com/feed/trending"
    options = Options()
    options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path=r"D:/major project/chromedriver.exe",options=options)
    driver.get(url)


    elm=driver.find_element_by_tag_name('html')
    t=10
    time_end=time.time()+t
    
    
    while time.time()<time_end:
        
        elm.send_keys(Keys.PAGE_DOWN)
        
    text=driver.page_source
    
    driver.close()
    
    soup=BeautifulSoup(text,'html5lib')
    
    details=soup.find(id="grid-container")
    
    list_video_links=[]
    
    
    for a in details.find_all(id='video-title',href=True):
        list_video_links.append(a['href'])
        
    return list_video_links
    
    
    
    
    
    
    
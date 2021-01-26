# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:29:27 2019

@author: aarus
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url="https://www.gartner.com/reviews/review/view/822709"

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')

containers=page_soup.findAll("div",{"class":"col-sm-6"})
print(len(containers))
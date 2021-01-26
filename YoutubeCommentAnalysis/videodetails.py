# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:32:58 2019

@author: aarus
"""


import datetime


from webscrap import getpagesource
import pandas as pd
import re



def convertMK(var):
    if 'M' in var:
        var=float(re.sub('M','',var))*1000000
    elif 'K' in var:
        var=float(re.sub('K','',var))*1000
    return float(var)


def processVideoDetails(soup):
    
    details=soup.find(id="info-contents")
    
    
    
    channel_info=soup.find(id="meta-contents")


    var=channel_info.find(id="upload-info")
    
    
    #Channel name
    try:
        
        chn=var.find(id="channel-name")
    
        chn=chn.find("yt-formatted-string")
    
        for i in chn:
            channel_name=i.contents[0]
            break

    except:
        channel_name="None"    
        
    

    #number of Subscriber
    try:
        
        chs=var.find(id="owner-sub-count")
        subscribers=chs.contents[0]
    except:
        subscribers="None"
        
        
    #find number of comments
    
    try:
        
        var=soup.find(id="comments")
        var=var.find(id="count")
        comments=var.find("yt-formatted-string").contents[0]
    except:
        comments="None"      #comments are turned off 
    
    #no. of views
    count_views=details.find("yt-view-count-renderer")
    
    
    for i in count_views:
        views=i.contents[0]
        break
        
    
    #details of video like,dislike,views and so on 
    d=details.find_all("yt-formatted-string")
    
    
    list_details=[]
    
    for i in d:
        try:
            list_details.append(i.contents[0].contents[0])
        
        except:
            try:
                
                list_details.append(i.contents[0])
            except:
                list_details.append(None)
    
    list_details.append(views)
    list_details.remove('Share')
    list_details.remove('Save')
    
    
    list_details.append(channel_name)
    list_details.append(subscribers)
    list_details.append(comments)
    
    
    
    def title_cleaning(title):
            
        word=""
        for i in title:
            if i !='|':
                
                word+=i
            else:
                word=word[:-1]
                break
            
        return re.sub('[^a-zA-z0-9 ]','',word)
    
    import datetime
    
    def clean_date(d):
        
        
        
        if "Streamed live on " in d:
            d=d.replace("Streamed live on ",'')
            return datetime.datetime.strptime(re.sub(',','',d),'%b %d %Y').date()
        
        elif "ago" in d:
            if "hours" in d:
                
                d=int(re.findall('\d+',d)[0])
            
                if int(datetime.datetime.now().strftime("%H"))-d<0:
                    return datetime.date.today() -datetime.timedelta(days=1)
            
                else:
                    return datetime.date.today()
            elif "minutes" in d:
                return datetime.date.today()
                
        elif "Premiered " in d:
            d=d.replace("Premiered ",'')
            return datetime.datetime.strptime(re.sub(',','',d),'%b %d %Y').date()
        
                   
        else:
            return datetime.datetime.strptime(re.sub(',','',d),'%b %d %Y').date()
        
        
    #converting list into dictionery
    dict_video_details={}
    
    dict_video_details['trend']=re.sub('[#A-Za-z, ]','',list_details[0])
    
    
    dict_video_details['date']=clean_date(list_details[2])
    
    dict_video_details['title']=title_cleaning(list_details[1])
    
    dict_video_details['views']=re.sub('[A-Za-z, ]','',list_details[5])
    
    
    dict_video_details['likes']=convertMK(list_details[3])
    
    dict_video_details['dislikes']=convertMK(list_details[4])
    
    dict_video_details['chName']=list_details[6]
    
    
    dict_video_details['chSubs']=convertMK(re.sub(' \w+','',list_details[7]))
    
    
    dict_video_details['comments']=re.sub('[Comments\, ]','',list_details[8])
    
    
    try:
        dataframe=pd.read_excel('video_details.xlsx')
        
    except:
        
        dataframe=pd.DataFrame(columns=list(dict_video_details.keys()))
        
    df2 = pd.DataFrame([list(dict_video_details.values())],columns=list(dict_video_details.keys()))
        
    dataframe=dataframe.append(df2,ignore_index = True)
    
    
    dataframe.to_excel('video_details.xlsx',index=False)    
    
        
    
    if len(dict_video_details)==9:
        return dict_video_details['title'],True
    else:
        return False





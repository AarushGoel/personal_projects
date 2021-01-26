# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:52:25 2019

@author: aarus
"""
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)


youtube.videos().rate(rating='like', id='jWh0FaRRZC4').execute()
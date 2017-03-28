# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:06:48 2017
sendtofb and log 寄到Fb的function & log
@author: vicharm
"""
import os
import sys
import requests
def sendtofb(data): #send json to facebook
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)
        
def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

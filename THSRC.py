# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:14:41 2023

@author: USER
"""

import requests

import json

url = 'https://www.thsrc.com.tw/TimeTable/Search'

header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': 'TaiZhong',
    'EndStation': 'ZuoYing',
    'OutWardSearchDate': '2023/10/27',
    'OutWardSearchTime': '21:00',
    'ReturnSearchDate': '2023/10/27',
    'ReturnSearchTime': '21:00',
    }

data = requests.post(url,data=param,headers=header).text

thsrc = json.loads(data)

items = thsrc['data']['DepartureTable']['TrainItem']

for row in items:
    print(row['TrainNumber'])
    print(row['DepartureTime'])
    print(row['DestinationTime'])
    print(row['Duration'])
    print()
    print()
    
    
    
    




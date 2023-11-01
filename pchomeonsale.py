# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:29:35 2023

@author: USER
"""

import requests

import json

header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

url = 'https://ecapi-cdn.pchome.com.tw/fsapi/cms/onsale'

data = requests.get(url,headers=header).text

goods = json.loads(data)
  
allitems = goods['data']

for item in allitems:
    time = item['time']
    print(time)
    
    row = item['products']
    
    for r in row:
        name = r['name']
        img = r['image']
        
        origin = r['price']['origin']
        onsale = r['price']['onsale']
        
        print(name)
        print(img)
        print(origin)
        print(onsale)
        print()
        
    print('-' *40)


    
        
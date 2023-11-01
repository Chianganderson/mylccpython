# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:37:28 2023

@author: USER
"""

import requests

import json

header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

url = 'https://ecshweb.pchome.com.tw/search/v4.3/all/results'

for i in range(1,5):

    param = {
    'q': '小米',
    'page': i,
    'sort': 'rnk/dc'
    }
    
    data = requests.get(url,params=param,headers=header).text
    
    pchome = json.loads(data)
    
    goods = pchome['Prods']
    
    for item in goods:
        title = item['Name']
        photo = 'https://cs-a.ecimg.tw'+item['PicB']
        price = item['Price']
        info = item['Describe']
        print(title)
        print(photo)
        print(price)
        print(info)
        print()
        print()
    
    
    

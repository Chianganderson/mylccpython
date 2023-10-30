# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:10:08 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup

url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'

header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
    '_csrf':'8bec14a3-3908-4c48-8564-8ad93d343277',
         'rideDate':'2023/10/27',
         'station':'3310-五權'
         }

data = requests.post(url,data=param,headers=header).text

soup = BeautifulSoup(data,'html.parser')

go = soup.find(id='tab1')

items = go.find_all('tr')[1:]

for row in items:
    
    car = row.find('a').text
    
    tds = row.find_all('td')
    
    sp = row.find_all('span')
    
    print('順行車次:',car)
    print('起訖站點:',sp[2].text,sp[3].text,sp[4].text)
    print('出發時間:',tds[1].text)
    print('終點站:',tds[2].text)
    print()
    print()

go = soup.find(id='tab2')

items = go.find_all('tr')[1:]

for row in items:
    
    car = row.find('a').text
    
    tds = row.find_all('td')
    
    sp = row.find_all('span')
    
    print('逆行車次:',car)
    print('起訖站點:',sp[2].text,sp[3].text,sp[4].text)
    print('出發時間:',tds[1].text)
    print('終點站:',tds[2].text)
    print()
    print()





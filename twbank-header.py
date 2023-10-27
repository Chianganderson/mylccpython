# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:07:04 2023

@author: USER
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    } #瀏覽器版本#
    
data = requests.get(url,headers=header).text
#print(data)

soup = BeautifulSoup(data,'html.parser')

rate = soup.find('table')

#print(rate)

tbody = rate.find('tbody')

trs = tbody.find_all('tr')

for row in trs:
    #print(row)
    #print()
    #print()
    tds =row.find_all('td')
    
    currency = tds[0].text.strip()
    currency = currency.split() #切割以空白的方式進行切割#
    print(currency[0])
    
    print(tds[1].text.strip()) #.strip()去除前後空白#
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print(tds[4].text.strip())
    print()
    print()
    
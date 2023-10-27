# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:05:15 2023

@author: USER
"""


from bs4 import BeautifulSoup
import requests

url = 'https://news.tvbs.com.tw/realtime'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    } 
    
data = requests.get(url,headers=header).text


soup = BeautifulSoup(data,'html.parser')

news = soup.find('div',{'class':'news_list'})

news = news.find('div',{'class':'list'})

allli = news.find_all('li')

for row in allli:
    a = row.find('a')
    if a != None: #如果a不等於#
        link = 'https://news.tvbs.com.tw/realtime' + a.get('href')
        title = a.find('h2').text.strip()
        photo = a.find('img').get('data-original')
        print(link)
        print(title)
        print(photo)
        print()
        print()
    
    
                 
    
    
    
    
   
                
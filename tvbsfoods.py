# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:16:29 2023

@author: USER
"""

from bs4 import BeautifulSoup
import requests

url = 'https://supertaste.tvbs.com.tw/food'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    } 
    
data = requests.get(url,headers=header).text


soup = BeautifulSoup(data,'html.parser')

#food = soup.find('div',class_='article__content')

food = soup.find('div',{'class':'article__content'}) #用字典方式呈現#


a = food.find_all('a')

for row in a:
    img = row.find('img').get('data-original')
    title = row.find('h3').text.strip()
    postdate = row.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw' + row.get('href')
    
    print('圖片:',img)
    print('標題:',title)
    print('時間:',postdate)
    print('連結:',link)
    print()
    print()
    



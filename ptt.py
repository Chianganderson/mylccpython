# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.ptt.cc/bbs/Beauty/index.html'

g = 1

for i in range(1):
    
    header = {'cookie':'over18=1'}
    
    data = requests.get(url,headers=header).text
    
    soup = BeautifulSoup(data,'html.parser')
    
    area = soup.find_all('div',class_='r-ent')
    
    url = 'https://www.ptt.cc' + soup.find_all('a',class_='btn wide')[1].get('href')
    
    for item in area:
        if item.find('a') != None:
            date = item.find('div',class_='date').text
            link = 'https://www.ptt.cc' + item.find('a').get('href')
            title = item.find('a').text
            print('標題：',title)
            print('連結：',link)
            print('日期：',date)
            print()
            
            time.sleep(1)
            #進入內頁
            data = requests.get(link ,headers=header).text
            
            soup = BeautifulSoup(data,'html.parser')
            img = soup.find(id='main-content')
            imgs = img.find_all('a')
            for im in imgs:
                photo = im.get('href')
                if 'jp' in photo:
                    
                    w = requests.get(photo)
                    file = str(g) + '.jpg'
                    with open(file,'wb') as fObj:
                        fObj.write(w.content)
                    g+=1    
                
            print('-'*30)    
            time.sleep(1)
            
            
        
        
        
        
        
        
        
        
        
        
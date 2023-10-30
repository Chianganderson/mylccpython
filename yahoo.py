# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

from bs4 import BeautifulSoup

url ='https://tw.buy.yahoo.com/search/product?'

header={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

#param = {'p':'ps5'} 

param = {} #利用字典的方式進行資料查詢#

p = input('請輸入欲查詢的商品名稱:')

param['p'] = p #param參數#

data = requests.get(url,params=param,headers=header).text #參數帶法#

soup = BeautifulSoup(data,'html.parser')

goods = soup.find('div',{'class':'ResultList_resultList_IpWJt'})

items = goods.find_all('a')

for row in items:
    
    link = row.get('href')
        
    title = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 sc-1drl28c-5 czfCFU fUBIAU biZSHp')
    
    if title != None: # !=不等於 #
        
        title = title.text        
           
        price = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 eLSRyH eEsfHX').text
        
        price = price.replace('$','') #replace置換 用空白取代'$' 用空白置換',' #   
        
        price = price.replace(',','')
        
        print('商品:',title)

        print('價格:',price)
        
        print('連結:',link) 
        
        print()
       
     
        
    












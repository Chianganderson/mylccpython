# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

####
#爬蟲==>
#1.已整理的資料(json,xml,csv)
#2.未整理資料(網頁,login,look==>看不到,ajax)
#分析==>統計==>預測

#####

import requests #pip install requests要自己裝#
import json
url="https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/json?size=100"
data = requests.get(url).text #轉換成文字#

bike=json.loads(data) #轉換成串列#

area = dict()

for row in bike:
    if area.get(row['sarea']) == None:
        data = list()
        data.append(row['sna'])
        data.append(row['sbi'])
        data.append(row['bemp'])
        
        temp = []
        temp.append(data)
        area[row['sarea']] = temp
        
    else:
        areabike = area[row['sarea']]
        data = list()
        data.append(row['sna'])
        data.append(row['sbi'])
        data.append(row['bemp'])
        areabike.append(data)
        area[row['sarea']] = areabike

#print(area)

while True:
    keys = list(area.keys())
    print(keys)
    a = input('請輸入區域,Q離開:')
    if a == 'Q':
        break
    if area.get(a) == None:
        print('無此區域')
    else:
        bike = area[a]
        for row in bike:
            print(row[0])
            print(row[1])
            print(row[2])
        print('-'*30)
    
    
        





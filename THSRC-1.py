# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:14:41 2023

@author: USER
"""

import requests
import json
import csv

url = 'https://www.thsrc.com.tw/TimeTable/Search'
header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
thrsinfo = {'南港':'NanGang','台北':'TaiPei','板橋':'BanQiao','桃園':'TaoYuan','新竹':'XinZhu',
            '苗栗':'MiaoLi','台中':'TaiZhong','彰化':'ZhangHua','雲林':'YunLin',
            '嘉義':'JiaYi','台南':'TaiNan','左營':'ZuoYing'}
print('車站:',thrsinfo.keys())
gostation = input('出發站:')
endstation = input('抵達站:')
gotime = input('出發時間:')
go = thrsinfo.get(gostation,'NanGang') #預設值#
end = thrsinfo.get(endstation,'ZuoYing')


param = {
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': go,
    'EndStation': end,
    'OutWardSearchDate': '2023/11/01',
    'OutWardSearchTime': '21:00',
    'ReturnSearchDate': '2023/11/01',
    'ReturnSearchTime': '21:00',
    }

data = requests.post(url,data=param,headers=header).text
thsrc = json.loads(data)
items = thsrc['data']['DepartureTable']['TrainItem']

fileName = 'thrsc.csv'
fObj = open(fileName,'w',newline='')
csvWrite = csv.writer(fObj)
csvWrite.writerow(['車次','出發時間','抵達時間','旅行時間','停靠站'])
 

for row in items:
    if row['DepartureTime'] >= gotime:
        print(row['TrainNumber'])
        print(row['DepartureTime'])
        print(row['DestinationTime'])
        print(row['Duration']) 
        msg = ""
        station = row['StationInfo']    
        print('停靠站:',end='')
        
        for s in station: #迴圈表示方式#
            if s['Show'] == True:
                print(s['StationName'],end=',')
                msg += s['StationName'] + ","
                        
        print()
        
        csvWrite.writerow([row['TrainNumber'],row['DepartureTime'],row['DestinationTime'],row['Duration'],msg])
                       
        print()
        
fObj.close()
    
    
    
    




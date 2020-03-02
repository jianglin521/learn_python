#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import pickle

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
res = requests.get('https://www.toutiao.com/api/pc/hot_gallery/?widen=1',headers = header)
res.encoding = 'utf-8'
res = json.loads(res.text)
data = res['data']
print(data, 'data')

pickle_file = open('data.txt', 'wb')
pickle.dump(data, pickle_file) # 把数据放进去
pickle_file.close() # 关闭

    


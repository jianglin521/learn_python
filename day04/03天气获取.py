# 天气获取(接口问题)
import urllib.request
import json
import pickle

pickle_file = open('city_data.pkl', 'rb')
city = pickle.load(pickle_file)
city_name = input('请输入城市：')
city_password = city[city_name]
File1 = urllib.request.urlopen('http://m.weather.com.cn/data/' + city_password)
watherHTML = File1.read().decode('utf-8') # 读入打开url
watherJSON = json.JSONDecoder().decode(watherHTML) # 创建json
watherInfo = watherJSON['weatherinfo']

# 打印信息
print('城市', watherInfo['city'])
print('时间', watherInfo['date_y'])
print('24小时天气')
print('温度', watherInfo['temp1'])
print('天气', watherInfo['weather1'])
# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import re
from datetime import datetime

class TiantianSpider():
    def __init__(self):
      self.url = 'https://api.doctorxiong.club/v1/fund?code={}'
      self.headers = {
          'Host': 'api.doctorxiong.club',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
      }

      self.code = '160222,501057,161005,005827,001938,003096,161725'
      self.num = [1100.17,875.39,837.94,785.61,821.23,111.82,0]

    def get_content(self):
        url = self.url.format(self.code)
        response = requests.get(url=url,headers=self.headers)
        # print(response)
        data = json.loads(response.text)['data']
        # with open('test.json',"w",encoding='utf-8') as f:
        #     f.write(str(data))
        codeList = self.code.split(',')
        sum = 0
        #  遍历结果
        for index, item in enumerate(data):
            todayEarnings = round((float(item['expectWorth']) - float(item['netWorth'])) * self.num[index], 2)
            print("基金: {},涨跌幅: {}%, 今日收益: {}, 时间: {}".format(item['name'], item['expectGrowth'], todayEarnings, item['expectWorthDate']))
            sum += todayEarnings
        print('今日总收益：{} 时间：{}'.format(round(sum, 2), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) 
   
    def run(self):
        while True:
            data = self.get_content()
            # self.save_items(data, url_list.index(url) + 1)
            time_sleep = random.randint(300, 350)
            # print('暂停{}秒'.format(time_sleep))
            time.sleep(time_sleep)

if __name__ == '__main__':
    spider = TiantianSpider()
    spider.run()

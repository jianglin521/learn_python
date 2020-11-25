# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import os
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql

class ZhiHuSpider():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.base_url = 'https://www.zhihu.com/'
        self.url = 'https://www.zhihu.com/'
        self.headers = {
            'X-INFINITESCROLL': 'true',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'Cookie': '_zap=4400c78d-bb5e-408b-83ee-6eb260144c55; _xsrf=ABjvYnUA45tIdXPNr0rspzFxARUNCrCe; ISSW=1; d_c0="ALCV3hECNRKPTrM5VJbKVqrDe5g04e9t4Y0=|1605574957"; l_n_c=1; r_cap_id="YzI5NzA2MTZmMWFiNGM0NTk5ZjU3ZjQ1N2E4Y2U3NjE=|1605574960|40f9ee1cbbbea409eed0395d4ccb3b7c43222920"; cap_id="ZDljOGY2MzQ2MTQzNGVlODg2YTYyNTgzZGFlY2M2YTM=|1605574960|3011facc9db4ac39e54f0e239c04a480540fdeff"; l_cap_id="OTQ2MTY3NjRiNzVmNDg5NmI3MDZmMTI1M2MxMmJhYWY=|1605574960|c61ca7f5eabc09b50ecaf16380708fb258a4a6d1"; n_c=1; tst=r; q_c1=7f8a0db8573b4b4284759857f1972566|1605575021000|1605575021000; capsion_ticket="2|1:0|10:1605575158|14:capsion_ticket|44:M2ExOTMxY2U3NzZiNDk2M2EzMGVjZGI0YzJlYjAzNmE=|268ea10e95a2fb0f7a3b4c90901cb9be9a1d3c525acef0fcc2fbfccfb269056b"; z_c0=Mi4xc1lLUUF3QUFBQUFBc0pYZUVRSTFFaGNBQUFCaEFsVk5KbkNnWUFDY0FvVDhsaGRXbUo1SlJFUEdRTUdEc0lqX1ln|1605575206|f8c8fbbea9649bc69c57767703269d26d3bde90c; SESSIONID=MskEQWYXFqkhC0h28yAS2OoeesmxxoHN0j4g8WYPYCw; JOID=W1EUA0pUankJ6TvXbF0SINaU8lN1GRETTbBshjUaGxpgqwO_VjTqyl_hM95sONSJx6rv_GEFWmDsIZc26Ze9cOc=; osd=UVAVCkJea3gA4THWbVQaKteV-1t_GBAaRbpthzwSERthogu1VzXjwlXgMtdkMtWIzqLl_WAMUmrtIJ4-45a8ee8=; KLBRSID=d017ffedd50a8c265f0e648afe355952|1605601692|1605599177'
        }
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/driver/chromedriver.exe')
        self.db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='py_test',charset='utf8mb4')
        # 开启mysql的游标功能，创建一个游标对象；                           
        self.cursor = self.db.cursor()

	# 获取首页
    def get_url_list(self):
        url_list = []
        for i in range(0,1):
            html = requests.get(url = self.url,headers=self.headers) 
            html.encoding = 'utf-8'   # 网站可能使用gbk或utf-8编码，
            # print(html.text)
            # with open('{}.html'.format(i), 'w', encoding='utf-8') as f:
            #     f.write(html.text)
            html = etree.HTML(html.text)
            data = html.xpath("//div[@class='Card TopstoryItem TopstoryItem--old TopstoryItem-isRecommend']/div/div")  # 使用#xpath的链接

            for li in data:
                title = li.xpath("./h2/div/a/text()")
                url = li.xpath("./h2/div/a/@href")
                if len(title) > 0:
                    url_list.append('https:' + url[0])
            # 首页暂停
            time_sleep = random.randint(1, 5)
            print('暂停{}秒'.format(time_sleep))
            time.sleep(time_sleep)       
        return url_list

    def get_content(self, url, index):
        self.driver.get(url)
        time.sleep(1)
        html = self.driver.page_source
        # html = requests.get(url=url,headers=self.headers)
        # print(html.status_code, 'status_code')
        # # print(html.text)
        # with open('{0}.html'.format(index), 'w', encoding='utf-8') as f:
        #     f.write(html)
        html = etree.HTML(html)
        title = html.xpath("//h1/text()")[0]
        list_item = html.xpath("//div[@class='List-item']")
        content = ''
        for item in list_item:
            # index = list_item.index(item)
            name = str(item.xpath("./div/div[@class='ContentItem-meta']//a/text()"))
            content = content + name + '------------\n\n'
            article = item.xpath("./div//p/text()")
            # print(article)
            for p in article:
                print(p)
                content = content + p + '\n\n'
        self.save_items(url, title, content) # 保存数据库
        # article = html.xpath("//div//p/text()")
        if (not os.path.exists('./知乎')):
            os.makedirs('./知乎') 
        title = title.replace('?', '') # 删除标题特殊字符    
        with open('./知乎/{0}{1}.txt'.format(index,title), 'w', encoding='utf-8') as f:
            f.write(title + '\n\n' + content) 

    def save_items(self, url, title, content):
        sql = 'insert into test_spider(title,content,url) values(%s,%s,%s)'
        try:
            self.cursor.execute('select id from test_spider where url=%s', url)
            exist = self.cursor.fetchone()
            print(exist)
            if (not exist):
                self.cursor.execute(sql,(title, content, url))
                self.db.commit()
                print("插入成功")
        except Exception as e:
            print(e, "插入失败")
            self.db.rollback()

    def run(self):
        # 获取u列表数据
        url_list = self.get_url_list()
        # url = input('请输入链接:')
        # url_list = [url]
        print(url_list)
        for url in url_list:
            data = self.get_content(url, url_list.index(url) + 1)
            # self.save_items(data, url_list.index(url) + 1)
            time_sleep = random.randint(4, 8)
            print('暂停{}秒'.format(time_sleep))
            time.sleep(time_sleep)
        self.driver.close() # 关闭连接
        self.db.close() # 关闭连接      

if __name__ == '__main__':
    spider = ZhiHuSpider()
    spider.run()

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
            'Cookie': '_zap=24eb86d7-3a80-4f4e-aea8-2e9a9bf04887; d_c0="AAAbcLPDiRGPTo5ABej3BkuCDiznrsxFGSE=|1594082992"; _ga=GA1.2.749585512.1594082993; ISSW=1; _xsrf=SitTm4E7Lwc3FfD9cnDAeRPECt92fDQM; z_c0=Mi4xc1lLUUF3QUFBQUFBQUJ0d3M4T0pFUmNBQUFCaEFsVk5VeUR4WHdBRHIxM25HUVZRbkhlbWpZMzJGRWRTenNmUnN3|1594085971|4b0544a7cea327e1e4d287553bd2aac7823072c9; tst=r; q_c1=808350fd5e0947259bec2e3172c6592f|1598409488000|1594089089000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1598409485,1598433995,1599119067,1599126228; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1599126228; unlock_ticket="AGDA9j9lrgoXAAAAYQJVTdzBUF9peXe05f0Hk4ETqLxCN7WUUl9efQ=="; SESSIONID=gVePKNj34jjW1yxrS22h2QVheM2dLuOqRznfzqjFXN6; KLBRSID=e42bab774ac0012482937540873c03cf|1599126229|1599126226; JOID=VFgQCkibruNlyFr_TpTdsbqzlXBc-v2KP4YSkHGqwow-8yaBOU0dtTXLWfZIJNx-x3q3reUGbgJpghMnInRESFc=; osd=VV0RC0yaq-JkzFv6T5XZsL-ylHRd__yLO4cXkXCuw4k_8iKAPEwcsTTOWPdMJdl_xn62qOQHagNsgxIjI3FFSVM='
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
            print(html.text)
            with open('{}.html'.format(i), 'w', encoding='utf-8') as f:
                f.write(html.text)
            html = etree.HTML(html.text)
            data = html.xpath("//div[@class='Card TopstoryItem TopstoryItem-isRecommend']/div/div")   # 使用#xpath的链接
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
        # 获取url列表数据
        url_list = self.get_url_list()
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

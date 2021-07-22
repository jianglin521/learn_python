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
        # chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.base_url = 'https://www.zhihu.com/'
        self.url = 'https://www.zhihu.com/'
        self.headers = {
            'X-INFINITESCROLL': 'true',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'Cookie': '_zap=889d8154-5c73-42b3-8203-d1dad6005324; d_c0="AAAeG2uA_xKPTucYJ7fGb4shlCY-uFgmkG0=|1619164069"; ISSW=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1620781623,1620781688; _xsrf=dVjumsJjhljsYQEjU8iDWL08hs6T6843; captcha_session_v2="2|1:0|10:1626925611|18:captcha_session_v2|88:WkdBODVBaTBkaVJldlB3d1N0MEZ2RVNxcWFZUnBoYmlFMFFia0ZDbGI3b1hkdnNtRCtEc1hhZnVseXB2ZDU5Ug==|8db611e796fa324ddf584b4a61ad0be3bb54fdfc03f0c4aa33342ce846f82917"; SESSIONID=JSPbc9svjaXLEd48krCsoZX1rJVeS1kfyL76ky8qMAI; __snaker__id=0lf0zWmg9kyvDnVV; JOID=VVoVBU4iVrr8DEIELyPhIAxkw_w6bQfsnW1-dV9KMuC2SiQ1FQm4R50LRQAqnoZgHVXSYmiZuM49JRBx4XDWmYI=; osd=WloRC08tVr7yDU0EKy3gLwxgzf01bQPinGJ-cVFLPeCyRCU6FQ22RpILQQ4rkYZkE1TdYmyXucE9IR5w7nDSl4M=; gdxidpyhxdE=ZitK%5CumzXD9CsmCuKeDVNix4LQiW4qTIBGuUPXI%2FcVmwDXqklIazQnhCdS8XVyrIK6t%2FhPk%5C0iLduZJoLmj%5CnYigsNSVsPndMy1QRZJW7%2FwUUlRxcWEHpKWnET5I5%2B%5CgsyiA%2BS7WrSG1ingUEdzOo6yPWx1jjsfzkRvkIPuo4wgsZxMv%3A1626926514114; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=2n2i8RBlCCqSJXMgK4zAlUV%2FZ59oSLtCru47XkHFu8dpZCpz7EmIVFRS33qto7xFEnj6w9H%2BSl8z3z0xH5ZJ6%2FA7d2PqG28O%2F%2B6AGATV5dvRYVA7bV09aui4FQF%2BTV6DekI%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed4f15d8cb68f96aa7afceb8ba7c14a968f9e84f872899da585fb72a59ba08fcc2af0fea7c3b92af2b2fe8abb5a82b48da4f4598a888388ca40ba9fa4b6d5259aebf790d248b89dbe96b73d9cb588a7f834a8b096a4f372f59ba3aad54e928dfdd4f480ade9b8a7c866aaeab9dacb2191b4f89bb272f4a888d6d942f6f18fd8e73a94af89d3bb45edf5faa2c64b988afb85f55a9b8a8fd8e15ef4e7af96ec40868f8accd75ef69cab8ccc37e2a3; YD00517437729195%3AWM_TID=sxh8SUd%2FG%2B1FRAVVQRc7jKDgY0jlAOnI; l_n_c=1; r_cap_id="OGVlZmZmODU4OTEzNDkyZTgwMjVmYzI2MDg5ZDU5ZmU=|1626925624|82acffac2df5592c2e991ff46c3074a8cf1db995"; cap_id="N2MzZDRhNjQ4OGJlNGY1YmIwMzQ0YzU5MWU4Y2M1YmM=|1626925624|d9ce3ffac7e308ec26600fd710c05090e181a3e9"; l_cap_id="Njg3MjM5YjVjYjBjNDk0Mjk4MzM1ZDM5MjcwZjZiNjE=|1626925624|e7bad6d8355fd101e4997b5214f20cb93aa903b9"; n_c=1; z_c0=Mi4xc1lLUUF3QUFBQUFBQUI0YmE0RF9FaGNBQUFCaEFsVk5SemptWVFDZHhRcU9zeDJDNEZJaGZEakU2d21GdTdMLXRB|1626925639|f5ad4d2f71ea6ab4d299031e74ec0331a3c5ad30; tst=r; KLBRSID=57358d62405ef24305120316801fd92a|1626925873|1626925611'
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

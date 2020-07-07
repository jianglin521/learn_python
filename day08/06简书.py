# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import os
from lxml import etree

class JianShuSpider():
    def __init__(self):
        self.base_url = 'https://www.jianshu.com'
        self.url = 'https://www.jianshu.com/'
        self.headers = {
            'X-INFINITESCROLL': 'true',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'Cookie': '__yadk_uid=H4y0h2EAqQrtASfsSw5tCOOVhivLlglP; _ga=GA1.2.501903876.1593673082; _gid=GA1.2.1287963103.1593673082; _m7e_session_core=287332e2a1c8b6d8cfbde480d473b286; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221730e2d6369250-020c3967c3c108-594d2a16-2073600-1730e2d636a3b8%22%2C%22%24device_id%22%3A%221730e2d6369250-020c3967c3c108-594d2a16-2073600-1730e2d636a3b8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%7D%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1593678405,1593739650,1593745619,1593747778; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1593747778'
        }

	# 获取首页
    def get_url_list(self):
        url_list = []
        for i in range(1,3):
            url = 'https://www.jianshu.com/?seen_snote_ids%5B%5D=69969975&seen_snote_ids%5B%5D=71247447&seen_snote_ids%5B%5D=70039617&seen_snote_ids%5B%5D=69889687&seen_snote_ids%5B%5D=69111749&seen_snote_ids%5B%5D=69321133&seen_snote_ids%5B%5D=71032091&page={}'.format(i)
            html = requests.get(url=url,headers=self.headers) 
            # with open('{}.html'.format(i), 'w', encoding='utf-8') as f:
            #     f.write(html.text)
            html = etree.HTML(html.text)
            # data = html.xpath("//div[@id='list-container']/ul/li")   # 使用xpath的链接
            data = html.xpath("//li")   # 使用xpath的链接
            for li in data:
                url = li.xpath("./div[@class='content']/a/@href")[0]
                title = li.xpath("./div[@class='content']/a/text()")[0]
                print(title)
                url_list.append(self.base_url + url)
            # 首页暂停
            time_sleep = random.randint(1, 5)
            print('暂停{}秒'.format(time_sleep))
            time.sleep(time_sleep)       
        return url_list

    def get_content(self, url, index):
        html = requests.get(url=url,headers=self.headers)
        print(html.status_code, 'status_code')
        # print(html.text)
        # with open('{0}.html'.format(index), 'w', encoding='utf-8') as f:
        #     f.write(html.text)
        html = etree.HTML(html.text)
        title = html.xpath("//section/h1/text()")[0] 
        article = html.xpath('//section/article/p/text()')
        print(title, article)
        if (not os.path.exists('./简书')):
            os.makedirs('./简书') 
        title = title.replace('|', '') # 删除标题特殊字符    
        with open('./简书/{0}{1}.txt'.format(index,title), 'w', encoding='utf-8') as f:
            content = title + '\n\n'
            for p in article:
                content = content + p + '\n\n'
            f.write(content) 
    # def save_items(self, data, index):
    #     for item in data:
    #         print(item, 'item')
    #         print(item['id'], item['name'], 'item00')
    #         sql = 'insert into crm_spider(id,name,subsidiaryname,cardid) values(%s,%s,%s,%s)'
    #         try:
    #             self.cursor.execute('select id from crm_spider where id={}'.format(item['id']))
    #             exist = self.cursor.fetchone()
    #             print(exist)
    #             if (not exist):
    #                 self.cursor.execute(sql,(item['id'],item['name'],item['subsidiaryName'],item['cardId']))
    #                 self.db.commit()
    #                 print("插入成功")
    #         except:
    #             print("插入失败")
    #             self.db.rollback()

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

if __name__ == '__main__':
    spider = JianShuSpider()
    spider.run()

# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import os
from lxml import etree

class ZhiHuSpider():
    def __init__(self):
        self.base_url = 'https://www.zhihu.com/'
        self.url = 'https://www.zhihu.com/'
        self.headers = {
            'X-INFINITESCROLL': 'true',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'Cookie': '_zap=24eb86d7-3a80-4f4e-aea8-2e9a9bf04887; d_c0="AAAbcLPDiRGPTo5ABej3BkuCDiznrsxFGSE=|1594082992"; _ga=GA1.2.749585512.1594082993; _gid=GA1.2.743102147.1594082993; ISSW=1; _xsrf=SitTm4E7Lwc3FfD9cnDAeRPECt92fDQM; l_n_c=1; r_cap_id="MDhhMTU3ZDRmMTM4NDBmNTkzMDliNWVhMjgxZDFjODU=|1594085860|b46e6981832089f73a981fde1a887f51cfb15e17"; cap_id="M2YwZWQwY2Q3MTI1NDg2YmFjODE0NzBlZWVmZTY2MTI=|1594085859|8086d8e6552010c149bfdf0b392c765740f7a04b"; l_cap_id="NzQ3NGY1Y2IzYjA2NGU1MGEwM2U5YmM1NmViMzZhOTI=|1594085860|effe42116b39b93d5fa817fc39606dc5dcda6e41"; n_c=1; atoken_expired_in=7200; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594082993,1594085836,1594085890,1594085914; SESSIONID=6dymYJHSifEwQ0zXxC2pazfR666iUbjkEzu1tARL1ko; JOID=VlkUA09Hoa5DYi64CkOkPPa-5DQedMXWKjth8Fguwus1Nx7HUllyqBhnK7kPjXi0IvMslK4UnFdPgakG-BzHID4=; osd=UV0UBUJApa5Fbym8CkWpO_K-4jkZcMXQJzxl8F4jxe81MRPAVll0pR9jK78Ciny0JP4rkK4SkVBLga8L_xjHJjM=; auth_type=d2VjaGF0|1594085933|6ee1983400e4865939000b9a557cc2e8c76c3f2a; atoken=35_hpenPXDo2vC6O9vlEeFY8vDLwI7SymLZSX41p9wi2UIbtL_rGH7rCFSh_xMBqu51JWUSah5p9zd7zJKbz2WSLX15BkSPUwX9mqeIte7JQuY; token="MzVfaHBlblBYRG8ydkM2Tzl2bEVlRlk4dkRMd0k3U3ltTFpTWDQxcDl3aTJVSWJ0TF9yR0g3ckNGU2hfeE1CcXU1MUpXVVNhaDVwOXpkN3pKS2J6MldTTFgxNUJrU1BVd1g5bXFlSXRlN0pRdVk=|1594085933|44aa2c0604cb92c2e5cc27f0c4c1ecd6d53b54d0"; client_id="bzNwMi1qc0dCNGZCM20xTW1IaXhxRjRpenVoSQ==|1594085933|ac472a3a5990ba7557b14788715e3d7953ef1a77"; capsion_ticket="2|1:0|10:1594085933|14:capsion_ticket|44:ZTdmMWY1OTI4MWEyNGUwNThhOTRmNDRiNTE0MzgxNmY=|19732c2b83834edaf31b293efd58bf7d392e2305c5c97fdf99512d28e8284488"; z_c0=Mi4xc1lLUUF3QUFBQUFBQUJ0d3M4T0pFUmNBQUFCaEFsVk5VeUR4WHdBRHIxM25HUVZRbkhlbWpZMzJGRWRTenNmUnN3|1594085971|4b0544a7cea327e1e4d287553bd2aac7823072c9; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1594085973; unlock_ticket="AGDA9j9lrgoXAAAAYQJVTV3ZA19iTvzcMaJQG4CZ4KhnmMvihJfHbg=="; KLBRSID=af132c66e9ed2b57686ff5c489976b91|1594086051|1594085835'
        }

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
        html = requests.get(url=url,headers=self.headers)
        print(html.status_code, 'status_code')
        # print(html.text)
        # with open('{0}.html'.format(index), 'w', encoding='utf-8') as f:
        #     f.write(html.text)
        html = etree.HTML(html.text)
        title = html.xpath("//h1/text()")[0] 
        article = html.xpath("//div//p/text()")
        print(title, article)
        if (not os.path.exists('./知乎')):
            os.makedirs('./知乎') 
        title = title.replace('?', '') # 删除标题特殊字符    
        with open('./知乎/{0}{1}.txt'.format(index,title), 'w', encoding='utf-8') as f:
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
    spider = ZhiHuSpider()
    spider.run()

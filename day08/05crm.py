# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import pymysql

class CrmSpider():
    def __init__(self):
      self.base_url = 'http://localhost:8080'
      self.url = '{}/api/v1/employees/search?q=&page={}'
      self.headers = {
          'Referer': self.base_url,
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
          'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjEsImVpZCI6MSwiYXV0IjpbeyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfTUVNQkVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfTUVNQkVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfTUVNQkVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFU0VSVkFUSU9OIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFU0VSVkFUSU9OX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1NQT1RfQ0hFQ0tfSU4ifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9NRU1CRVJfVUkifSx7ImF1dGhvcml0eSI6IkFVVEhfRVhQT1JUX0NIRUNLSU5fQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfQ09VUlNFX09QUCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9FWFBPUlRfQ0hFQ0tJTl9PUFAifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9DVVNUT01FUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX01ZX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUFVCTElDX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NIRUNLX0NPTkZMSUNUX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1VQREFURV9DVVNUT01FUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NVU1RPTUVSX1VJIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX09SSUdJTkFMX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQ1VTVE9NRVJfREVMSVZFUllfQUxMIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX0NVU1RPTUVSX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUEFUVEVSTl9BTEwifSx7ImF1dGhvcml0eSI6IkFVVEhfVFJBTlNGRVJfQ1VTVE9NRVJfQUNISUVWRU1FTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfREVMX0NVU1RPTUVSX1NUVURFTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9PUkRFUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9PUkRFUl9VSSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfT1JERVJfSU5fU1VCU0lESUFSWSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX09SREVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1FVSUNLX09SREVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfT1JERVJfSU5fTVkifSx7ImF1dGhvcml0eSI6IkFVVEhfQVVESVRfT1JERVIifSx7ImF1dGhvcml0eSI6IkFVVEhfQVVESVRfT1BQX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1VQREFURV9BVURJVEVEX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX09SREVSX1NXSVRDSF9SRVNFUlZTRVJWSUNFIn0seyJhdXRob3JpdHkiOiJBVVRIX09SREVSX1NXSVRDSF9DSEVDS0lOU0VSVklDRSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1BBWU1FTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfT1JERVJfUEFZTUVOVF9BU1NPQ0lBVEUifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9TRVRUTEVNRU5UIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfUEVSRk9STUFOQ0UifSx7ImF1dGhvcml0eSI6IkFVVEhfQVVESVRfUEVSRk9STUFOQ0UifSx7ImF1dGhvcml0eSI6IkFVVEhfT1JERVJfVVBMT0FEIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfRU1QTE9ZRUUifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9FTVBMT1lFRSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX0FDQ09VTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9BQ0NPVU5UIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfUk9MRSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX1JPTEUifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9ERVBUIn0seyJhdXRob3JpdHkiOiJBVVRIX0FERF9ERVBUIn0seyJhdXRob3JpdHkiOiJBVVRIX1VQREFURV9ERVBUIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfRU1QTE9ZRUVfVUkifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9TWVNURU1fTk9USUNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfRU1QTE9ZRUVfQUdSRUVNRU5UIn0seyJhdXRob3JpdHkiOiJBVVRIX1VQREFURV9FTVBMT1lFRV9OQU1FIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfREVWSUNFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX1RFQUNIRVJfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NPVVJTRV9PUFBfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NPVVJTRV9TVEFUSVNUSUNTIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUkVWRU5VRV9UT1RBTF9TVEFUSVNUSUNTIn1dLCJzdWIiOiJqY2FkbWluMSIsInByb3AiOnsidXR5cCI6MSwiaW5pZCI6MTAwLCJzbmFtIjoi5oC76YOoIiwiaW5zdHlwZSI6MSwiYXBwaWQiOiIxNDBmZTFkYTllZDk1NGI3ZmI5IiwibW9iaWxlIjpbXSwicGF0dGVybiI6MSwidWlpZCI6MTA2MSwibmFtIjoi6JOd5paMIiwic3VpZCI6MTIzMjgwLCJzcGF0dGVybiI6W3siaWQiOjEsIm5hbWUiOiLogIHmnb_lupMifSx7ImlkIjoyLCJuYW1lIjoi5Lya5ZGY5Y2h5bqTIn1dLCJzdHlwIjoxfSwiZXhwIjoxNTkzNzU5ODk1LCJpYXQiOjE1OTM3NTYyOTUsImp0aSI6IjFUOFJuRmN0eEZPUTk4bmsiLCJzaWQiOjIwMDF9.kC8AcK8vjRyZErYvNL-Ei6At_1mRAk_NWP3UBge6m2WaGKcNBuUKtZVfI32L4MJiY1wDRoz_MxPH-Nr2XH864A'
      }
      self.db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='py_test',charset='utf8mb4')
      # 开启mysql的游标功能，创建一个游标对象；                           
      self.cursor = self.db.cursor()

    def get_url_list(self):
      url_list = []
      for i in range(150,200):
          url = self.url.format(self.base_url, i)
          url_list.append(url)
      return url_list

    def get_content(self, url):
        response = requests.get(url=url,headers=self.headers)
        response = json.loads(response.text)
        if (response['code'] == 1020000):
            return response['content']['content']
        else:
            print(response)
            return [] 

    def save_items(self, data, index):
        for item in data:
            print(item, 'item')
            print(item['id'], item['name'], 'item00')
            sql = 'insert into crm_spider(id,name,subsidiaryname,cardid) values(%s,%s,%s,%s)'
            try:
                self.cursor.execute('select id from crm_spider where id={}'.format(item['id']))
                exist = self.cursor.fetchone()
                print(exist)
                if (not exist):
                    self.cursor.execute(sql,(item['id'],item['name'],item['subsidiaryName'],item['cardId']))
                    self.db.commit()
                    print("插入成功")
            except:
                print("插入失败")
                self.db.rollback()

    def run(self):
        # 获取url列表数据
        url_list = self.get_url_list()
        for url in url_list:
            data = self.get_content(url)
            self.save_items(data, url_list.index(url) + 1)
            time_sleep = random.randint(4, 8)
            print('暂停{}秒'.format(time_sleep))
            time.sleep(time_sleep)
        self.db.close() # 关闭连接      

if __name__ == '__main__':
    spider = CrmSpider()
    spider.run()

# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import pymysql

class CrmSpider():
    def __init__(self):
    #   self.base_url = 'http://localhost:8080'
      self.base_url = 'http://jccrm.icfo.cn/crmapi'
      self.url = '{}/api/v1/employees/search?q=&page={}'
      self.headers = {
          'Referer': self.base_url,
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
          'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjEsImVpZCI6MSwiYXV0IjpbeyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfTUVNQkVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfTUVNQkVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfTUVNQkVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFU0VSVkFUSU9OIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFU0VSVkFUSU9OX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX1NQT1RfQ0hFQ0tfSU4ifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9NRU1CRVJfVUkifSx7ImF1dGhvcml0eSI6IkFVVEhfRVhQT1JUX0NIRUNLSU5fQ09VUlNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfQ09VUlNFX09QUCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9ERUxfQ09VUlNFX09QUF9JTl9TVUJTSURJQVJZIn0seyJhdXRob3JpdHkiOiJBVVRIX0VYUE9SVF9DSEVDS0lOX09QUCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX0NPVVJTRV9NRU1CRVIifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVTRVJWQVRJT05fUFVCTElDX0NPVVJTRV9TUEVDSUFMIn0seyJhdXRob3JpdHkiOiJBVVRIX0NIRUNLSU5fUFVCTElDIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQ09VUlNFX01FTUJFUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0lORk9STUFUSU9OX1NIQVJJTkcifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9DVVNUT01FUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX01ZX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUFVCTElDX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NIRUNLX0NPTkZMSUNUX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1VQREFURV9DVVNUT01FUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NVU1RPTUVSX1VJIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX09SSUdJTkFMX0NVU1RPTUVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQ1VTVE9NRVJfREVMSVZFUllfQUxMIn0seyJhdXRob3JpdHkiOiJBVVRIX1RSQU5TRkVSX0NVU1RPTUVSX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUEFUVEVSTl9BTEwifSx7ImF1dGhvcml0eSI6IkFVVEhfVFJBTlNGRVJfQ1VTVE9NRVJfQUNISUVWRU1FTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfREVMX0NVU1RPTUVSX1NUVURFTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfVFJBTlNGRVJfQ1VTVE9NRVJfVE9fUFVCTElDIn0seyJhdXRob3JpdHkiOiJBVVRIX09SREVSX1VJIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfT1JERVIifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9PUkRFUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX09SREVSX0lOX1NVQlNJRElBUlkifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9PUkRFUl9JTl9NWSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9RVUlDS19PUkRFUl9JTl9NWSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX09SREVSX0lOX01ZIn0seyJhdXRob3JpdHkiOiJBVVRIX0FVRElUX09SREVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0FVRElUX09QUF9PUkRFUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9VUERBVEVfQVVESVRFRF9PUkRFUiJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9PUkRFUl9TV0lUQ0hfUkVTRVJWU0VSVklDRSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9PUkRFUl9TV0lUQ0hfQ0hFQ0tJTlNFUlZJQ0UifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9QQVlNRU5UIn0seyJhdXRob3JpdHkiOiJBVVRIX09SREVSX1BBWU1FTlRfQVNTT0NJQVRFIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfU0VUVExFTUVOVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1BFUkZPUk1BTkNFIn0seyJhdXRob3JpdHkiOiJBVVRIX0FVRElUX1BFUkZPUk1BTkNFIn0seyJhdXRob3JpdHkiOiJBVVRIX09SREVSX1VQTE9BRCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX0VNUExPWUVFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfRU1QTE9ZRUUifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9BQ0NPVU5UIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfQUNDT1VOVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1JPTEUifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9ST0xFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfREVQVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9BRERfREVQVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9VUERBVEVfREVQVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9ERUxfREVQVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9ERVBUX1VJIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfVEVBQ0hFUl9VSSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1RFQUNIRVIifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9URUFDSEVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0FERF9TVUJTSURJQVJZIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfUExBVEZPUk1fRElWSURFIn0seyJhdXRob3JpdHkiOiJBVVRIX01PVkVfRU1QTE9ZRUUifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9FTVBMT1lFRV9VSSJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1RFQUNIRVJfQUNDT1VOVCJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9DVVJEX1NZU1RFTV9OT1RJQ0UifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9QUklOVEVSIn0seyJhdXRob3JpdHkiOiJBVVRIX0NVUkRfUFJPTU9URV9BVURJVF9BTEwifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9FTVBMT1lFRV9BR1JFRU1FTlQifSx7ImF1dGhvcml0eSI6IkFVVEhfVVBEQVRFX0VNUExPWUVFX05BTUUifSx7ImF1dGhvcml0eSI6IkFVVEhfQ1VSRF9ERVZJQ0UifSx7ImF1dGhvcml0eSI6IkFVVEhfVUlfREVWSUNFIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX1RFQUNIRVJfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NPVVJTRV9PUFBfU1RBVElTVElDUyJ9LHsiYXV0aG9yaXR5IjoiQVVUSF9SRUFEX0NPVVJTRV9TVEFUSVNUSUNTIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUkVWRU5VRV9UT1RBTF9TVEFUSVNUSUNTIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfUkVWRU5VRV9TVUJTSURJQVJZX1NUQVRJU1RJQ1MifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9SRVZFTlVFX0FHRU5UX1NUQVRJU1RJQ1MifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9XT1JLTE9BRF9TVEFUSVNUSUNTIn0seyJhdXRob3JpdHkiOiJBVVRIX1JFQURfWFVFU0hFX1NUQVRJU1RJQ1MifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9URUFDSEVSX0NVU1RPTUVSX1NUQVRJU1RJQ1MifSx7ImF1dGhvcml0eSI6IkFVVEhfUkVBRF9URUFDSEVSX1JFVkVOVUVfU1RBVElTVElDUyJ9XSwic3ViIjoiamNhZG1pbjEiLCJwcm9wIjp7InV0eXAiOjEsImluaWQiOjEwMCwic25hbSI6IuaAu-mDqCIsImluc3R5cGUiOjEsImFwcGlkIjoiMTQwZmUxZGE5ZWQ5NTRiN2ZiOSIsIm1vYmlsZSI6WyIxNzcxODMwODk1MSJdLCJwYXR0ZXJuIjoxLCJ1aWlkIjoxMDYxLCJuYW0iOiLok53mlowiLCJzdWlkIjpbMTIzMjgwXSwic3BhdHRlcm4iOlt7ImlkIjoxLCJuYW1lIjoi6ICB5p2_5bqTIn0seyJpZCI6MiwibmFtZSI6IuS8muWRmOWNoeW6kyJ9XSwic3R5cCI6MX0sImV4cCI6MTU5NTE1MDEyNCwiaWF0IjoxNTk1MTQ2NTI0LCJqdGkiOiJKajc5ODh3b0NIUDFFQ0hRIiwic2lkIjoyMDAxfQ.Kq765Uv8QrnrHyY4nLCldnTRMW_XfZnaL1b0NoS4GFqCH7zV9Q4D_uFnqT7O7X6Dp_Im7oKmuEx7Ycl5RD5hOw'
      }
      self.db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='py_test',charset='utf8mb4')
      # 开启mysql的游标功能，创建一个游标对象；                           
      self.cursor = self.db.cursor()

    def get_url_list(self):
      url_list = []
      for i in range(400,500):
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

import requests
from lxml import etree
import os
import pymysql

# 使用pymysql连接上mysql数据库服务器，创建了一个数据库对象；
db = pymysql.connect(
  host='localhost',
  user='root',
  password='123456',
  port=3306,
  db='python_test',
  charset='utf8mb4'
)

# 开启mysql的游标功能，创建一个游标对象；              
cursor = db.cursor()

# 爬取地址
url = 'https://www.dytt8.net/html/tv/hytv/20200113/59603.html'
#url = 'https://www.dytt8.net/html/gndy/dyzz/20200305/59784.html'

# path
path = './文件/'
# title
title = '爱情公寓5'
# 代理ip
proxies = {
  'http': '222.89.32.179:9999',
  'http': '118.78.196.81:8118',
  'http': '222.89.32.179:9999',
  'http': '118.78.196.81:8118',
  'http': '112.85.150.50:9999'
 }


class Spider:
    def start_request(self, url):
        """   请求获得主页的美女图片   """
        html = requests.get(url=url)    # 请求美女主页
        html.encoding = 'gbk'   # 网站可能使用gbk或utf-8编码，
        # print(html.text)
        html = etree.HTML(html.text)    # 使用Xpath前要用etree对网站进行处理
        url_list = html.xpath("//td[@style='WORD-WRAP: break-word']/a/@href")   # 使用xpath的链接
        #print(title,'url_list')
        print(type(url_list))   
        # 判断图片文件夹是否存在
        if not os.path.exists(path):
            os.makedirs(path)
        data = []
        print(url_list)
        for item in url_list:
            item = (item,)
            data.append(item)
        #保存链接
        #print(data)
        #self.finally_sql(data)  # 执行下一步：进入美女页

    def finally_sql(self, url_list):
        # 本地链接保存
        sql = 'insert into test(link) values(%s)'
        try:
            cursor.executemany(sql,url_list)
            db.commit()
            print("插入成功")
        except:
            print("插入失败")
            db.rollback()
        db.close()

    # 保存链接
    # def finally_link(self, url_list):
    #     # 本地链接保存
    #     with open(path + title + '.txt' , 'w', encoding='utf-8')as f:
    #         for url in url_list:
    #             #s = str(url_list[index]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    #             s = url.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
    #             f.write(s) 
    #         f.close()
    #         print('保存成功')

    # 保存图片
    # def finally_file(self, imgUrl, title, index):    
    #     #print(now_page, imgUrl)
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    #     img = requests.get(url=imgUrl, headers=headers, proxies=proxies)
    #     # 本地图片地址
    #     with open(path + title + '/' + str(index) + '.jpg' , 'wb')as f:
    #         f.write(img.content)


spider = Spider()
spider.start_request(url) # 调用









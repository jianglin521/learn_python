# 需要安装requests库
import requests
import os
url = 'http://bpic.588ku.com//back_origin_min_pic/19/11/27/b68eff8c0c23d0e15e0e6e87bdbb4e0a.jpg'
root = './图片/'
path = root + '001.jpg'
try:
  if not os.path.exists(root):
    os.mkdir(root)
  if not os.path.exists(path):
    r = requests.get(url)
    print(r.status_code)
    f = open(path, 'wb')
    f.write(r.content)
    f.close()
    print('文件保存成功')
  else:
    print('文件已存在！')
except:
  print('爬取失败')

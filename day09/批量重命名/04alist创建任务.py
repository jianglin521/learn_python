#觉得不错麻烦点个star谢谢

import time
import random
import re
import sys
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

# 要选择的文件地址
selectAddress = '/阿里/临时文件/航拍中国1-4季/第一季'

# 加载环境变量
load_dotenv(dotenv_path='./day09/批量重命名/.env.local', verbose=True)
# 加启动配置
chrome_options = webdriver.ChromeOptions()
# 打开chrome浏览器
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])#跟上面只能选一个
# chrome_options.add_argument('--start-maximized')#最大化
chrome_options.add_argument('--incognito')#无痕隐身模式
chrome_options.add_argument("disable-cache")#禁用缓存
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
# chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"')

try:
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        driver = webdriver.Chrome(options=chrome_options, executable_path=r'D:/driver/chromedriver.exe')
    else:
        driver = webdriver.Chrome(options=chrome_options, executable_path=r'./chromedriver')
except:
    print('报错了!请检查你的环境是否安装谷歌Chrome浏览器！或者驱动【chromedriver.exe】版本是否和Chrome浏览器版本一致！\n驱动更新链接：http://npm.taobao.org/mirrors/chromedriver/')

username = os.environ['alist_username'] # 用户名
password = os.environ['alist_password'] # 密码
address = os.environ['alist_address'] # 登陆地址：https：//xxxx：xxxx/

driver.get(f'{address}/@login')
time.sleep(1)

## 登录
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/input[1]').send_keys(f'{username}')
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/input[2]').send_keys(f'{password}')
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/button[2]').click()
time.sleep(0.3)
driver.get(address + selectAddress)
time.sleep(0.5)

## 显示复选框
driver.find_element_by_xpath('/html/body/div[4]/div/*[name()="svg"]').click()
time.sleep(0.3)
element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/*[name()="svg"][6]').click()
time.sleep(0.3)

for item in range(1, 5):
    driver.find_element_by_xpath(f'//*[@id="root"]/div[2]/div/div/div/div[{item + 1}]/a/div/label').click()
    # time.sleep(0.6)

## 选择复制路径
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/*[name()="svg"][3]').click()
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="hope-modal-cl-4--body"]/div/div/div/*[name()="svg"]').click()
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="hope-modal-cl-4--body"]/div/div/div[2]/div[2]/div/p').click()
# driver.find_element_by_xpath('//*[@id="hope-modal-cl-4"]/div[3]/button[2]').click()
# time.sleep(0.3)

# driver.get(f'{address}/@manage/tasks/copy')

# driver.close()
print('运行成功了')



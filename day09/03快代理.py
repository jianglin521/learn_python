import requests
import parsel
import time

# 检测代理ip
def check_ip(proxies_list):
  """ 检测代理ip质量 """
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
  }
  can_use = []
  for proxie in proxies_list:
    try:
      requests.get('http://www.baidu.com', headers=headers, proxies = proxie, timeout=0.1)
      can_use.append(proxie)
    except Exception as e:
      print(e)
  return can_use

# 获取到的列表
proxies_list = []
for page in range(1, 3):
  print('=========正在爬取第{}页数据========='.format(page))
  # 1.确定url,hearer
  base_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(str(page))
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
  }

  # 2.发送请求，读取数据
  response = requests.get(base_url, headers=headers)
  data = response.text
  # print(response.text)

  # 3.解析数据
  html_data = parsel.Selector(data)
  pase_list = html_data.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")

  # print(pase_list)
  for tr in pase_list:
    proxies_dict = {}
    http_type = tr.xpath("./td[4]/text()").extract_first()
    ip_num = tr.xpath("./td[1]/text()").extract_first()
    ip_port = tr.xpath("./td[2]/text()").extract_first()
    # print(http_type, ip_num, ip_port)
    # 构建代理ip的字典
    proxies_dict[http_type] = ip_num + ':' + ip_port
    # print(proxies_dict)
    proxies_list.append(proxies_dict)
  # 等待1s
  time.sleep(1)

print(proxies_list)
print('获取到代理ip的数量', len(proxies_list))

# 检测代理ip
can_use = check_ip(proxies_list)
print('能用的代理ip', can_use)
print('能用的代理ip数量', len(can_use))
with open('代理ip.txt',"w",encoding='utf-8') as f:
      f.write(str(can_use))
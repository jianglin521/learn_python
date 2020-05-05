#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import requests
from scrapy.selector import Selector
import time

connect = pymysql.connect(host='127.0.0.1', user='root', passwd='123456',
                          db='py_test', charset='utf8')


class GetIP(object):

    def judeg_ip(self, ip=None, port=None):
        proxy = {}
        if ip:
            proxy = {
                'http': "{0}:{1}".format(ip, port)  # 或者加上http://
            }
            print(proxy["http"])
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        test_http_url = "https://11maoww.com/vodtype/34-41.html"

        try:
            response = requests.get(test_http_url, headers=headers, proxies=proxy, timeout=0.2)
            print(response.status_code, '-------------------------------')
        except Exception as e:
            print("jugeg_ip exception: ", e)
            self.delete_ip(ip)
            return False
        print(">>>status_code: ", response.status_code)
        # print(">>>text: ", response.text)
        if 200 <= response.status_code < 300:
            print(str(response.status_code)+", ip可以用!\n")
            return True
        else:
            self.delete_ip(ip)  # 将此ip从数据库中删除
            return False

    def delete_ip(self, ip=None):
        if not ip:  # ip=None
            return True
        # 从数据库中删除无效的ip
        delete_sql = "delete from `ip_proxy_pool` where ip='{0}'".format(ip)
        try:
            cursor = connect.cursor()
            cursor.execute(delete_sql)
            connect.commit()
            print("已移除IP： %s ." % ip)
            return True
        except Exception as e:
            print("delete_ip exception: ", e)
            print("IP： %s 移除失败." % ip)

        cursor.close()

    def get_random_ip(self):
        print("正在获取ip，请稍后...")

        random_sql = "select ip, port from ip_proxy_pool order by rand() limit 1;"
        cursor = connect.cursor()
        results = cursor.execute(random_sql)

        if results == 0:
            print("ip获取失败：数据库为空！")
            return False

        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            if self.judeg_ip(ip, port):
                print("可用代理：", ip+':'+port)
                return ip, port
            else:
                return self.get_random_ip()

        cursor.close()


def get_ip():
    try:
        ip, port = GetIP().get_random_ip()
        print("成功获取：", ip+':'+port)
        return ip+':'+port
    except Exception as e:
        print('exception: ', e)
        print('获取失败！')
        return


proxy = {
    'http': get_ip()
}


def crawl_ips():
    # 爬取某网站的国内高匿代理IP
    url = 'https://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36',

    }

    res = requests.get(url, headers=headers, proxies=proxy)
    if not res.status_code == 200:
        print('status_code: ', res.status_code)
        return
    selector = Selector(text=res.text)
    page_number = selector.xpath('//a[last()-1]/text()').extract_first()  # 获取总页数
    page_numbers = int(selector.xpath('//a[last()-1]/text()').extract_first())

    for i in range(10, 1000):
        time.sleep(10)
        # if i == 1:
        #     response = res
        response = requests.get(url+str(i), headers=headers, proxies=proxy)

        selector = Selector(text=response.text)
        # print(response.text)

        all_trs = selector.xpath('//*[@id="ip_list"]//tr')

        ip_list = []
        for tr in all_trs[1:]:

            try:
                country = tr.xpath('td[1]/img/@alt').extract()[0]  # 国家
                server_address = tr.xpath('td[4]/a/text()').extract()[0]  # 服务器地址
            except Exception as e:
                print("crawl_ips exception 1: ", e)
                # continue
                country = server_address = None
            ip = tr.xpath('td[2]/text()').extract()[0]  # IP地址
            port = tr.xpath('td[3]/text()').extract()[0]  # 端口
            anonymity = tr.xpath('td[5]/text()').extract()[0]  # 是否匿名
            type = tr.xpath('td[6]/text()').extract()[0]  # 类型
            speed = tr.xpath('td[7]/div/@title').extract()[0]  # 速度
            connection_time = tr.xpath('td[8]/div/@title').extract()[0]  # 连接时间
            survival_time = tr.xpath('td[9]/text()').extract()[0]  # 存活时间
            verify_time = tr.xpath('td[10]/text()').extract()[0]  # 验证时间

            ip_list.append((country, ip, port, server_address, anonymity, type, speed,
                            connection_time, survival_time, verify_time))

        #存入数据库
        for ip_info in ip_list:
            import datetime

            cursor = connect.cursor()

            speed = float(ip_info[6].split('秒')[0])
            connection_time = float(ip_info[7].split('秒')[0])
            verify_time = datetime.datetime.strptime("20"+ip_info[9]+":00", "%Y-%m-%d %H:%M:%S")
            print(ip_info, '444444')

            # 注意传递值的时候字符串需要引号
            sql = "INSERT INTO `ip_proxy_pool` VALUES (null,'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, " \
                  "{7}, '{8}', '{9}');".format(ip_info[0], ip_info[1], ip_info[2], ip_info[3], ip_info[4],
                                             ip_info[5], speed, connection_time, ip_info[8], verify_time)
            print('sql', sql)

            try:
                cursor.execute(sql)

                connect.commit()
            except Exception as e:
                print('insert exception: ', e)


if __name__ == '__main__':
    # crawl_ips()
    print(get_ip(), '777')
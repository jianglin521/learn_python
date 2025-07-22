import json
import requests
from lxml import etree

def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'
    }
    url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/'
    response = requests.get(url=url, headers=headers)
    tree = etree.HTML(response.text)
    dict1 = tree.xpath('//script[@id="captain-config"]/text()')
    dict2 = json.loads(dict1[0])
    china = dict2['component'][0]['caseList']
    
    for province in china:
        if province['area'] == '北京' or province['area'] == '山西' :
            sum = 0
            sum_str = ''
            for city in province['subList']:
                if city['confirmedRelative'] != '0':
                    sum += int(city['confirmedRelative'])
                    sum_str += '{}：{} '.format(city['city'],city['confirmedRelative']) 
                    # print([province['area'] + city['city'], city['confirmedRelative']])
            print(province['area'], sum, sum_str)	
if __name__ == '__main__':
    main()
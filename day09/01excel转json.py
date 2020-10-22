import xlrd
import json
import requests

def openWorkbook():
    # 读取excel表的数据
    workbook = xlrd.open_workbook('./车辆资料2.xlsx')
    # 选取需要读取数据的那一页
    sheet = workbook.sheet_by_index(1)
    # sheet = workbook.sheet_by_name('视频86')
    # 获得行数
    rows = sheet.nrows
    # 列数列数
    cols = sheet.ncols
    # 创建一个数组用来存储excel中的数据
    excel_data = []
    #print(rows, 'rows')
    for i in range(1, rows):
        item = {}
        for j in range(0, cols):
            title = sheet.cell(0, j).value
            item[title] = sheet.cell(i, j).value
        #print(item) 
        ap = []
        for key, value in item.items():
            #print(key,value, 'kv')
            if isinstance(value, float):  # excel中的值默认是float,需要进行判断处理，通过'"%s":%d'，'"%s":"%s"'格式化数组
                ap.append('"%s":%d' % (key, value))
            else:
                ap.append('"%s":"%s"' % (key, value))
        #print(ap)
        s = '{%s}' % (','.join(ap))  # 继续格式化
        excel_data.append(s)

    t = '[%s]' % (','.join(excel_data))  # 格式化
    print(t)
    #data = json.dumps(t,ensure_ascii=False)
    #print(data.replace("\\",""))
    with open('student.json',"w",encoding='utf-8') as f:
         f.write(t)
openWorkbook()
# url="http://192.168.1.11:8090/pushdata/"
# headers={"Content-Type":"application/json"}
# data=openWorkbook()
# re=requests.get(url=url,headers=headers,data=data)
# print(re.text)
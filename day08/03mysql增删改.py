import pymysql
# import pandas as pd

# 使用pymysql连接上mysql数据库服务器，创建了一个数据库对象；
db = pymysql.connect(
  host='localhost',
  user='root',
  password='123456',
  port=3306,
  db='test',
  charset='utf8mb4'
)

# 开启mysql的游标功能，创建一个游标对象；              
cursor = db.cursor()

# 1.一次性插入一条数据
sql = 'insert into guan_test(id,title) values(%s,%s)'
try:
    cursor.execute(sql,(1,'添加测试'))
    db.commit()
    print("插入成功")
except:
    print("插入失败")
    db.rollback()
db.close()

# 2.一次性插入多条数据
# sql = 'insert into person(name,age) values(%s,%s)'
# # 注意：(('牛魔王',9000),('铁扇公主',8000),('玉皇大帝',6000))也可以
# # 小括号都可以换为中括号
# datas = [('牛魔王',9000),('铁扇公主',8000),('玉皇大帝',6000)]
# try:
#     cursor.executemany(sql,datas)
#     db.commit()
#     print("插入成功")
# except:
#     print("插入失败")
#     db.rollback()
# db.close()

# 3.更新数据
# sql = 'update person set age=%s where name=%s'
# try:
#     cursor.execute(sql,[90000,"玉皇大帝"])
#     db.commit()
#     print("更新成功")
# except:
#     print("更新失败")
#     db.rollback()
# db.close()

# 4.删除数据
# sql = 'delete from person where age=8000'
# try:
#     cursor.execute(sql)
#     db.commit()
#     print("删除成功")
# except:
#     print("删除失败")
#     db.rollback()
# db.close()
import pymysql
import pandas as pd

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
#cursor = db.cursor()

# 1.fetchone()：一次获取一条记录
# cursor.execute('select count(*) from person')
# num = cursor.fetchone() # 获取总条数
# print(num, 'num')
# # 注意这一句一定是在循环之外，不能放到循环里面。
# cursor.execute('select name,age from person')    
# for i in range(num[0]):
#     name, age = cursor.fetchone()
#     data_one = "我的名字叫{}，今年{}岁".format(name,age)
#     print(data_one, 'item')
# db.close()

# 2.fetchall()：一次获取所有记录
# cursor.execute('select name,age from person')
# data = cursor.fetchall()
# # print(aa)
# for name,age in data:
#     data_one = "我的名字叫{}，今年{}岁".format(name,age)
#     print(data_one, 'item')
# db.close()
# 还有一个fetchmany()方法，用于一次性获取指定条数的记录

# 3.使用pandas中的read_sql()方法，将提取到的数据直接转化为DataFrame
df = pd.read_sql("select * from person where id<10",db)
print(df)
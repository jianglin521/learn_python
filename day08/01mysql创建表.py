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

# 创建一个游标对象；
cursor = db.cursor()

# 建表语句；
sql = """ create table person(
        id int auto_increment primary key not null,
        name varchar(10) not null,
        age int not null) charset=utf8mb4 """

# 执行sql语句；
cursor.execute(sql)

# 断开数据库的连接；
db.close()


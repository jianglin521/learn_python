# 二进制存储
import pickle

# 写入文件
my_list = [123, '小甲鱼', '4566', 777777]
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close() # 关闭文件

# 读取文件
pickle_file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
pickle_file.close()


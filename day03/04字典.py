# 字典
dict = {}
print(type(dict))

dict1 = dict.fromkeys(range(32), '赞')
print(dict1)

for key in dict1.keys():
  print(key)

for value in dict1.values():
  print(value)

for item in dict1.items():
  print(item)

# print(dict1[31]) # 找不到的时候会报错
print(dict1.get(31))
print(dict1.get(32)) # 找不到时候为None

print(31 in dict1) # 判断key是否在dict1中

# 清除键
dict1.clear()
print(dict1)

# 拷贝
a = {1: 'one', 2: 'two', 3: 'three'}
b = a.copy()
c = a
print(id(a), id(b), id(c))

c[4] = 'four'
print(a, b, c)

# Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。
print(b.popitem(), b)

# 添加键值对
b.setdefault(5, 'five')
print(b)

e = {}
e.update(b)
print(e, b, id(e), id(b))





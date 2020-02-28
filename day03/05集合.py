# 集合
a = {}
print(type(a))

# 集合是唯一的
b = {1, 2, 3, 4, 5, 1}
print(type(b), b)
#print(b[1]) # 不支持索引

# 去除重复值
num1 = [1, 2, 3, 4, 5, 5, 0]
num1 = list(set(num1))
print(num1)

num2 = {1, 2, 3, 4, 5, 5, 0}
print(1 in num2) # 判断某个值是否存在

# 添加元素
num2.add(6)
print(num2) 

# 删除元素
num2.remove(2)
print(num2)

# 冻结集合
num3 = frozenset([1, 2, 3, 4, 5])
print(num3, type(num3))
num3.add(55)

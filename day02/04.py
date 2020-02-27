# 迭代器
a = list() # 转为list
print(a)

b = 'jianglin'
b = list(b)
print(b)

c = (1, 1, 23, 45, 78, 4, 2, 10)
c = list(c)
print(c, type(c))

d = tuple(c) # 转为元组
print(d, type(d))

print(len(b))  # 返回长度
print(max(c))  # 返回最大值
print(min(c))  # 返回最小值

e = (3.1, 2.3, 4.5)
print(sum(e)) # 求和

print(sorted(c)) # 从小到大排序
# filter
filter1 = list(filter(None, [1, 0, False, True]))
print(filter1)

# python range() 函数可创建一个整数列表，一般用在 for 循环中。
# range(start, stop[, step])
temp = range(10)
print(temp, type(temp))

# filter 个数减少
def odd(x): # 奇数
  return x % 2

show = filter(odd, range(10))
print(list(show), )

# lambda
show = filter(lambda x : x % 2, range(10))
print(list(show), 'lambda')

# map 个数不变
show = map(lambda x : x * 2, range(10))
print(list(show), 'map')

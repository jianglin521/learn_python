def myGen():
  print('生成器被执行')
  yield 1
  yield 2

myG = myGen()
# print(next(myG))
# print(next(myG))
for i in myGen():
  print(i)

def libs():
  a = 0
  b = 1
  while True:
    a, b = b, a + b
    yield a

for each in libs():
  if each > 100:
    break
  print(each, end = ' ')


a = [i for i in range(100) if not(i % 2) and i % 3]
print(a)

b = {i: i % 2 == 1 for i in range(10)}
print(b)

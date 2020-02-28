""" def factorial(n):
  result = n
  for i in range(1, n):
    result *= i
  
  return result

number = int(input('请输入一个正整数！'))
res = factorial(number)
print('%d 的阶乘是 %d' % (number, res)) """

# 递归
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)
number = int(input('请输入一个正整数！'))
res = factorial(number)
print('%d 的阶乘是 %d' % (number, res)) 

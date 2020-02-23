import random

print('--------游戏开始---------')
secret = random.randint(1, 10) # 创建随机数
guess = '' # 创建变量
index = 1  # 次数设置

# 猜数字循环
while guess != secret and index < 10:
  temp = input('不妨猜测一下小甲鱼现在心中想的是哪个数字')
  guess = int(temp)
  if guess == secret: # 猜对
    print('我草，你是小甲鱼心中的蛔虫吗？')
    print('哼，猜中了也没有奖励！')
  else: # 猜错
    print('错误次数', index )
    index += 1 # 次数
    if guess > secret: # 大了
      print('哥，大了，大了！')
    else: # 小了
      print('哥，小了，小了！')
  print('-------------------------------')
# 次数判断
if index < 4:
  print('恭喜你游戏结束，不玩啦！')
else:
  print('错误次数太多，不玩了！')




print('--------游戏测试---------')
temp = input('不妨猜测一下小甲鱼现在心中想的是哪个数字')
#print(temp, 'temp')
guess = int(temp)
if guess == 8:
  print('我草，你是小甲鱼心中的蛔虫吗？')
  print('哼，猜中了也没有奖励！')
else:
  print('猜错啦，小甲鱼现在心中想的是8！')
print('游戏结束，不玩啦！')

import time as t

class MyTimer:
  def __init__(self):
    self.unit = ['年', '月', '天', '小时', '分钟', '秒']
    self.prompt = '未开始计时！'
    self.lasted = []
    self.begin = 0
    self.end = 0

  def __str__(self):
    return self.prompt
  
  __repr__ = __str__

  # 开始计时
  def start(self):
    self.begin = t.localtime()
    print('计时开始...')

  # 停止计时
  def stop(self):
    self.end = t.localtime()
    self._calc()
    print('计时结束...')

  # 内部方法，计算运行时间
  def _calc(self):
    self.lasted = []
    self.prompt = '总共运行了'
    for index in range(6):
      self.lasted.append(self.end[index] - self.begin[index])
      # 判断self.lasted[index]存在
      if self.lasted[index]:
        self.prompt += str(self.lasted[index]) + self.unit[index]
  
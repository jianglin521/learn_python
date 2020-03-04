import time as t

class MyTimer:
  def __init__(self):
    self.unit = ['年', '月', '天', '小时', '分钟', '秒']
    self.prompt = '未开始计时！'
    self.lasted = []
    self.begin = 0
    self.end = 0

  # __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
  # 打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。
  # __repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
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
  
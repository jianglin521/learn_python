class Turtle:
  def __init__(self, x):
    self.num = x

class Fish:
  def __init__(self, x):
    self.num = x

class Pool:
  def __init__(self, x, y):
    self.turtle = Turtle(x).num
    self.fish = Fish(y).num   

  def print_num(self):
    print('水池中乌龟%d只,小鱼%d条' % (self.turtle, self.fish))

pool = Pool(10, 100)

pool.print_num()
class Wing(object):

  def __init__(self, ratio):
    self._ratio = ratio

  def fly(self):
    if self._ratio > 1:
      print('Weee!')
    elif self._ratio == 1:
      print('This is hard work, but I\'m flying')
    else:
      print('I think I\'ll just walk')


class Duck(object):

  def __init__(self):
    self._wing = Wing(1.8)

  def walk(self):
    print('Waddle, waddle')

  def swim(self):
    print('Come on it, the water\'s lovely')

  def fly(self):
    self._wing.fly()


class Penguin(object):
  
  def walk(self):
    print('Waddle, waddle, I waddle too')

  def swim(self):
    print('Come on it, but it\'s a bit chilly this far South')

  def quack(self):
    print('Are you \'avin\' a larf? I\'m a penguin!')


class Flock(object):

  def __init__(self):
    self.flock = []

  def addDuck(self, duck: Duck) -> None:
    self.flock.append(duck)

  def migrate(self):
    for duck in self.flock:
      duck.fly()


if __name__ == '__main__':
  donald = Duck()
  donald.fly()

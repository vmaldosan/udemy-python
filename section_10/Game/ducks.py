class Duck(object):

  def walk(self):
    print('Waddle, waddle')

  def swim(self):
    print('Come on it, the water\'s lovely')

  def fly(self):
    print('Woooosh')

class Penguin(object):
  
  def walk(self):
    print('Waddle, waddle, I waddle too')

  def swim(self):
    print('Come on it, but it\'s a bit chilly this far South')

  def fly(self):
    print('Are you \'avin\' a larf? I\'m a penguin!')

def testDuck(duck):
  duck.walk()
  duck.swim()
  duck.fly()

if __name__ == '__main__':
  donald = Duck()
  testDuck(donald)

  hopper = Penguin()
  testDuck(hopper)
  
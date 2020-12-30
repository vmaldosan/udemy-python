import random

class Enemy:
  
  def __init__(self, name='Enemy', hitPoints=0, lives=1):
    self._name = name
    self._hitPoints = hitPoints
    self._originalHP = hitPoints
    self._lives = lives
    self._alive = True

  def takeDamage(self, damage):
    self._hitPoints -= damage
    print('I took {} points of damage'.format(damage))
    if self._hitPoints <= 0:
      self._lives -= 1
      lostLives = 1
      self._hitPoints += self._originalHP
      while self._hitPoints <= 0:
        lostLives += 1
        self._lives -= 1
        self._hitPoints += self._originalHP
      if self._lives > 0:
        print('{0._name} lost {1} lives'.format(self, lostLives))
      else:
        print('{0._name} is dead'.format(self))
        self._alive = False
        self._hitPoints = 0

  def __str__(self):
    return 'Name: {0._name}, Lives: {0._lives}, Hit points: {0._hitPoints}'.format(self)

  def _isAlive(self):
    return self._alive

  def _setAlive(self, alive):
    self._alive = alive

  alive = property(_isAlive, _setAlive)


class Troll(Enemy):

  def __init__(self, name):
    super().__init__(name=name, lives=1, hitPoints=23)

  def grunt(self):
    print('Me {0._name}. {0._name} stomp you'.format(self))


class Vampyre(Enemy):

  def __init__(self, name):
    super().__init__(name=name, lives=3, hitPoints=12)

  def dodges(self):
    if random.randint(1, 3) == 3:
      print('***** {0._name} dodges *****'.format(self))
      return True
    else:
      return False

  def takeDamage(self, damage):
    if not self.dodges():
      super().takeDamage(damage=damage)


class VampyreKing(Vampyre):

  def __init__(self, name):
    super().__init__(name)
    self._hitPoints = 140
    self._originalHP = 140

  def takeDamage(self, damage):
    super().takeDamage(damage // 4)

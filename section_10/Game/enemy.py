class Enemy:
  
  def __init__(self, name="Enemy", hitPoints=0, lives=1):
    self.name = name
    self.hitPoints = hitPoints
    self.originalHP = hitPoints
    self.lives = lives
    self.alive = True

  def takeDamage(self, damage):
    self.hitPoints -= damage
    print('I took {} points of damage'.format(damage))
    if self.hitPoints <= 0:
      self.lives -= 1
      lostLives = 1
      self.hitPoints += self.originalHP
      while self.hitPoints <= 0:
        lostLives += 1
        self.lives -= 1
        self.hitPoints += self.originalHP
      if self.lives > 0:
        print('{0.name} lost {1} lives'.format(self, lostLives))
      else:
        print('{0.name} is dead'.format(self))
        self.alive = False

  def __str__(self):
    return 'Name: {0.name}, Lives: {0.lives}, Hit points: {0.hitPoints}'.format(self)


class Troll(Enemy):

  def __init__(self, name):
    super().__init__(name=name, lives=1, hitPoints=23)

  def grunt(self):
    print('Me {0.name}. {0.name} stomp you'.format(self))


class Vampyre(Enemy):

  def __init__(self, name):
    super().__init__(name=name, lives=3, hitPoints=12)

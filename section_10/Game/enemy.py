class Enemy:
  
  def __init__(self, name="Enemy", hitPoints=0, lives=1):
    self.name = name
    self.hitPoints = hitPoints
    self.lives = lives

  def takeDamage(self, damage):
    remainingPoints = self.hitPoints - damage
    if remainingPoints >= 0:
      self.hitPoints = remainingPoints
      print('I took {} points of damage and have {} left'.format(damage, self.hitPoints))
    else:
      self.lives -= 1

  def __str__(self):
    return 'Name: {0.name}, Lives: {0.lives}, Hit points: {0.hitPoints}'.format(self)


class Troll(Enemy):
  pass

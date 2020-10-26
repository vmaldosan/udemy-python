class Player(object):

  def __init__(self, name):
    self.name = name
    self._lives = 3
    self.level = 1
    self.score = 0

  def _getLives(self):
    return self._lives

  def _setLives(self, lives):
    if lives >= 0:
      self._lives = lives
    else:
      print('Lives cannot be negative')
      self._lives = 0

  lives = property(_getLives, _setLives)

  def __str__(self):
    return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}'.format(self)

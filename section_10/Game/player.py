class Player(object):

  def __init__(self, name):
    self.name = name
    self._lives = 3
    self._level = 1
    self.score = 0

  def _getLives(self):
    return self._lives

  def _setLives(self, lives):
    if lives >= 0:
      self._lives = lives
    else:
      print('Lives cannot be negative')
      self._lives = 0

  def _getLevel(self):
    return self._level

  def _setLevel(self, level):
    if level > 0:
      self._level = level
      self.score = level * 1000
    else:
      print('Level cannot be less than 1')
      self._level = 1
      self.score = 0

  lives = property(_getLives, _setLives)
  level = property(_getLevel, _setLevel)

  def __str__(self):
    return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}'.format(self)

from player import Player

victor = Player('Victor')

from enemy import Troll

uglyTroll = Troll()
print('Ugly troll - {}'.format(uglyTroll))

anotherTroll = Troll('Ug', 18, 1)
print ('Another troll - {}'.format(anotherTroll))

brother = Troll('Urg', 23)
print(brother)

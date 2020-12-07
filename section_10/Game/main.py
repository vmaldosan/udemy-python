from enemy import Troll, Vampyre

uglyTroll = Troll('Pug')
print('Ugly troll - {}'.format(uglyTroll))

anotherTroll = Troll('Ug')
print ('Another troll - {}'.format(anotherTroll))

brother = Troll('Urg')
print(brother)

uglyTroll.grunt()
anotherTroll.grunt()
brother.grunt()

uglyTroll.takeDamage(12)
print(uglyTroll)
uglyTroll.takeDamage(20)
print(uglyTroll)

oldVampyre = Vampyre('Drake')
print(oldVampyre)

youngVampyre = Vampyre('Lestat')
print(youngVampyre)

youngVampyre.takeDamage(25)
print(youngVampyre)

while oldVampyre.alive:
  oldVampyre.takeDamage(1)
  print(oldVampyre)

from enemy import Troll

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
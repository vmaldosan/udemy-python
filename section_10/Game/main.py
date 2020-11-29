from player import Player

victor = Player('Victor')

print(victor.name)
print(victor.lives)
victor.lives -= 1
print(victor)

victor.lives -= 1
print(victor)

victor.lives -= 1
print(victor)

victor.lives -= 1
print(victor)

victor.level = 2
print(victor)

victor.level = 0
print(victor)

victor.score = 500
print(victor)
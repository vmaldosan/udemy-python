jabber = open('sample.txt', 'r')

for line in jabber:
	if 'jab' in line.lower():
		print(line, end='')

jabber.close()

print('=' * 40)

with open('sample.txt', 'r') as jabber:
	for line in jabber:
		if 'JAB' in line.upper():
			print(line, end='')

print('=' * 40)

# cities = ['Caceres', 'Limerick', 'Dublin', 'City of Mexico']
#
# with open('cities.txt', 'w') as cityFiles:
# 	for city in cities:
# 		print(city, file=cityFiles)

cities = []
with open('cities.txt', 'r') as cityFile:
	for city in cityFile:
		cities.append(city.strip('\n'))

print(cities)

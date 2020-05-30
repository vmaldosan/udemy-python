fruit = {'orange': 'sweet, orange citrus fruit',
         'apple': 'good for cider',
         'lemon': 'sour, yellow citrus fruit'}

print(fruit['lemon'])
fruit['pear'] = 'odd shaped apple'
print(fruit)
del fruit['pear']
print(fruit)

key = 'apple' # input('Enter a key: ')

if key in fruit:
	print(fruit.get(key))
else:
	print('{} not in fruit'.format(key))

print(fruit.keys())
print(fruit.values())

sortedKeys = sorted(list(fruit.keys()))
print(sortedKeys)

fruitTuple = tuple(fruit.items())
print(fruitTuple)

print(dict(fruitTuple))

print('=' * 40)

veg = {'aparragus': 'funny to collect in spring',
       'carrots': 'yummy'}

healthy = fruit.copy()
healthy.update(veg)
print(healthy)


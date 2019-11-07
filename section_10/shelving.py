import shelve

with shelve.open('ShelfTest') as fruit:
	fruit['orange'] = 'a sweet, orange, citrus fruit'
	fruit['apple'] = 'good for making cider'
	fruit['lemon'] = 'sour, yellow citrus fruit'
	fruit['grape'] = 'small, sweet fruit, used for making wine'

	print(fruit['lemon'])
	print(fruit['grape'])

print('=' * 40)

pasta = ['pasta', 'tomato sauce', 'chorizo']
paella = ['rice', 'chicken', 'beans', 'tomato']
pancakes = ['milk', 'flour', 'sugar', 'eggs', 'raising agents']
pisto = ['garlic', 'onion', 'carrot', 'courgette', 'aubergine', 'pepper', 'eggs']

with shelve.open('recipes') as recipes:
	# recipes['pasta'] = pasta
	# recipes['paella'] = paella
	# recipes['pancakes'] = pancakes
	# recipes['pisto'] = pisto

	# First method to append elements
	# tmpList = recipes['pancakes']
	# tmpList.append('salt')
	# recipes['pancakes'] = tmpList

	for snack in recipes:
		print(snack, recipes[snack])

# Second method to append elements
with shelve.open('recipes', writeback=True) as recipes:
	recipes['paella'].append('saffron')

	for snack in recipes:
		print(snack, recipes[snack])

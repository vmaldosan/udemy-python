polymorphic = ['10', '2', 3, '7', 5]

for i in polymorphic:
	print(i)

# polymorphic.sort() # gives error
print(polymorphic)

# same with print(sorted(polymorphic))

polymorphic2 = ['10', '2', 3, '7', 5]
print(polymorphic == polymorphic2) # prints True
print(polymorphic is polymorphic2) # prints False

print('=' * 40)

even = [2, 4, 6, 8]
print(sorted(even, reverse=True))

reversed_even = even
reversed_even.sort(reverse=True)
print(even)

print('=' * 40)

backStr = 'sdrawkcab si gnirts sihT'
print(backStr[::-1])
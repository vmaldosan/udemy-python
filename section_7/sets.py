even = set(range(0, 40, 2))
print(even)
print(len(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print('=' * 40)

print(even.intersection(squares))
print(even & squares)

print('=' * 40)

print(sorted(even.difference(squares)))
print(sorted(even - squares))

print('=' * 40)

print(sorted(even.symmetric_difference(squares)))

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
if 8 in squares:
	squares.remove(8)
